package srv

import (
	"database/sql"
	"fmt"
	"html/template"
	"log/slog"
	"net/http"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strings"
	"time"

	"srv.exe.dev/db"
)

type Server struct {
	DB           *sql.DB
	Hostname     string
	TemplatesDir string
	StaticDir    string
	WikiDir      string
	InboxDir     string
}

type dashboardData struct {
	Hostname    string
	Now         string
	Sources     []sourceInfo
	RecentItems []inboxItem
	Trending    string
}

type sourceInfo struct {
	Name       string
	Count      int
	LastCrawl  string
	Description string
}

type inboxItem struct {
	Title  string
	Source string
	Date   string
	URL    string
	Tags   string
}

func New(dbPath, hostname string) (*Server, error) {
	_, thisFile, _, _ := runtime.Caller(0)
	baseDir := filepath.Dir(thisFile)
	repoDir := filepath.Dir(baseDir)
	srv := &Server{
		Hostname:     hostname,
		TemplatesDir: filepath.Join(baseDir, "templates"),
		StaticDir:    filepath.Join(baseDir, "static"),
		WikiDir:      filepath.Join(repoDir, "wiki"),
		InboxDir:     filepath.Join(repoDir, "inbox"),
	}
	if err := srv.setUpDatabase(dbPath); err != nil {
		return nil, err
	}
	return srv, nil
}

func (s *Server) HandleDashboard(w http.ResponseWriter, r *http.Request) {
	now := time.Now()

	sources := []sourceInfo{
		{Name: "V2EX", Description: "HN相当 — シニアエンジニア議論"},
		{Name: "Juejin", Description: "掘金 — Dev.to相当、実践的コード"},
		{Name: "36kr", Description: "36氪 — テック業界ニュース"},
		{Name: "Zhihu", Description: "知乎 — 専門家回答"},
		{Name: "WeChat Media", Description: "微信公众号 — 深層メディア"},
	}

	// Count files in each inbox
	for i, src := range sources {
		dirName := strings.ToLower(strings.ReplaceAll(src.Name, " ", "-"))
		dir := filepath.Join(s.InboxDir, dirName)
		entries, err := os.ReadDir(dir)
		if err == nil {
			count := 0
			var latest time.Time
			for _, e := range entries {
				if strings.HasSuffix(e.Name(), ".md") {
					count++
					if info, err := e.Info(); err == nil && info.ModTime().After(latest) {
						latest = info.ModTime()
					}
				}
			}
			sources[i].Count = count
			if !latest.IsZero() {
				sources[i].LastCrawl = latest.Format("2006-01-02 15:04")
			} else {
				sources[i].LastCrawl = "未実行"
			}
		} else {
			sources[i].LastCrawl = "未実行"
		}
	}

	// Gather recent items from all inboxes
	recentItems := s.getRecentItems(30)

	data := dashboardData{
		Hostname:    s.Hostname,
		Now:         now.Format("2006-01-02 15:04:05"),
		Sources:     sources,
		RecentItems: recentItems,
	}

	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	if err := s.renderTemplate(w, "dashboard.html", data); err != nil {
		slog.Warn("render template", "error", err)
		http.Error(w, "Internal Server Error", 500)
	}
}

func (s *Server) HandleWikiPage(w http.ResponseWriter, r *http.Request) {
	page := r.PathValue("page")
	if page == "" {
		page = "index.md"
	}
	// Security: prevent path traversal
	page = filepath.Clean(page)
	if strings.Contains(page, "..") {
		http.Error(w, "Forbidden", 403)
		return
	}

	path := filepath.Join(s.WikiDir, page)
	content, err := os.ReadFile(path)
	if err != nil {
		http.Error(w, "Page not found", 404)
		return
	}

	w.Header().Set("Content-Type", "text/plain; charset=utf-8")
	w.Write(content)
}

func (s *Server) HandleInboxList(w http.ResponseWriter, r *http.Request) {
	source := r.PathValue("source")
	if source == "" {
		http.Error(w, "Source required", 400)
		return
	}

	dir := filepath.Join(s.InboxDir, source)
	entries, err := os.ReadDir(dir)
	if err != nil {
		http.Error(w, "Source not found", 404)
		return
	}

	var files []string
	for _, e := range entries {
		if strings.HasSuffix(e.Name(), ".md") {
			files = append(files, e.Name())
		}
	}
	sort.Sort(sort.Reverse(sort.StringSlice(files)))

	w.Header().Set("Content-Type", "text/plain; charset=utf-8")
	for _, f := range files {
		fmt.Fprintln(w, f)
	}
}

func (s *Server) HandleInboxItem(w http.ResponseWriter, r *http.Request) {
	source := r.PathValue("source")
	item := r.PathValue("item")
	if source == "" || item == "" {
		http.Error(w, "Bad request", 400)
		return
	}

	// Security
	source = filepath.Clean(source)
	item = filepath.Clean(item)
	if strings.Contains(source, "..") || strings.Contains(item, "..") {
		http.Error(w, "Forbidden", 403)
		return
	}

	path := filepath.Join(s.InboxDir, source, item)
	content, err := os.ReadFile(path)
	if err != nil {
		http.Error(w, "Not found", 404)
		return
	}

	w.Header().Set("Content-Type", "text/plain; charset=utf-8")
	w.Write(content)
}

func (s *Server) getRecentItems(limit int) []inboxItem {
	var items []inboxItem

	sourceDirs := []string{"v2ex", "juejin", "36kr", "zhihu", "wechat-media"}

	type fileEntry struct {
		source  string
		name    string
		modTime time.Time
	}

	var allFiles []fileEntry

	for _, src := range sourceDirs {
		dir := filepath.Join(s.InboxDir, src)
		entries, err := os.ReadDir(dir)
		if err != nil {
			continue
		}
		for _, e := range entries {
			if !strings.HasSuffix(e.Name(), ".md") {
				continue
			}
			info, err := e.Info()
			if err != nil {
				continue
			}
			allFiles = append(allFiles, fileEntry{source: src, name: e.Name(), modTime: info.ModTime()})
		}
	}

	// Sort by mod time descending
	sort.Slice(allFiles, func(i, j int) bool {
		return allFiles[i].modTime.After(allFiles[j].modTime)
	})

	if len(allFiles) > limit {
		allFiles = allFiles[:limit]
	}

	for _, f := range allFiles {
		// Extract title from frontmatter
		path := filepath.Join(s.InboxDir, f.source, f.name)
		content, err := os.ReadFile(path)
		if err != nil {
			continue
		}

		title, url, tags := parseFrontmatter(string(content))
		if title == "" {
			title = f.name
		}

		// Extract date from filename (YYYY-MM-DD prefix)
		date := ""
		if len(f.name) >= 10 {
			date = f.name[:10]
		}

		items = append(items, inboxItem{
			Title:  title,
			Source: f.source,
			Date:   date,
			URL:    url,
			Tags:   tags,
		})
	}

	return items
}

func parseFrontmatter(content string) (title, url, tags string) {
	lines := strings.Split(content, "\n")
	inFront := false
	for _, line := range lines {
		if strings.TrimSpace(line) == "---" {
			if !inFront {
				inFront = true
				continue
			} else {
				break
			}
		}
		if inFront {
			if strings.HasPrefix(line, "title:") {
				title = strings.Trim(strings.TrimPrefix(line, "title:"), " \"")
			} else if strings.HasPrefix(line, "url:") {
				url = strings.Trim(strings.TrimPrefix(line, "url:"), " \"")
			} else if strings.HasPrefix(line, "tags:") {
				tags = strings.TrimPrefix(line, "tags: ")
			}
		}
	}
	return
}

func (s *Server) renderTemplate(w http.ResponseWriter, name string, data any) error {
	path := filepath.Join(s.TemplatesDir, name)
	tmpl, err := template.ParseFiles(path)
	if err != nil {
		return fmt.Errorf("parse template %q: %w", name, err)
	}
	return tmpl.Execute(w, data)
}

func (s *Server) setUpDatabase(dbPath string) error {
	wdb, err := db.Open(dbPath)
	if err != nil {
		return fmt.Errorf("failed to open db: %w", err)
	}
	s.DB = wdb
	if err := db.RunMigrations(wdb); err != nil {
		return fmt.Errorf("failed to run migrations: %w", err)
	}
	return nil
}

func (s *Server) Serve(addr string) error {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /{$}", s.HandleDashboard)
	mux.HandleFunc("GET /wiki/{page...}", s.HandleWikiPage)
	mux.HandleFunc("GET /inbox/{source}", s.HandleInboxList)
	mux.HandleFunc("GET /inbox/{source}/{item}", s.HandleInboxItem)
	mux.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir(s.StaticDir))))
	slog.Info("starting server", "addr", addr)
	return http.ListenAndServe(addr, mux)
}
