# Hermes 中国語圏 AI Topics — Migration Runbook

別の exe.dev VM（または同等環境）への完全移行手順書。

> **前提**: 新マシンは Ubuntu 24.04 相当の exe.dev VM を想定。

---

## 1. 現行環境の全体像

### サービス構成

| サービス | systemd unit | タイプ | ポート | 役割 |
|----------|-------------|--------|--------|------|
| Go Web Dashboard | `srv.service` | simple (常駐) | 8000 | Web ダッシュボード |
| Shelley Agent | `shelley.service` | exec (常駐) | — | exe.dev コーディングエージェント |

### スケジュールジョブ（systemd timer）

| タイマー | スケジュール | 役割 |
|----------|-------------|------|
| `crawl-cn-ai.timer` | 6時間ごと (00,06,12,18:00) | 中国語圏ソースクローリング |
| `shelley-triage.timer` | 12時間ごと (03,15:00) | Hermes Agent によるトリアージ |
| `shelley-trending-topics.timer` | 毎日 10:00 UTC | トレンドトピック検出 |
| `shelley-active-crawl.timer` | 毎日 11:00 UTC | 能動的知識クローリング |
| `shelley-wiki-health.timer` | 毎週月曜 09:00 UTC | Wiki ヘルスチェック |

### ディレクトリ構成

```
/home/exedev/
├── ai-topics-cn/                 # メインリポジトリ (GitHub: kzinmr/ai-topics-cn)
│   ├── wiki/                     # LLM Wiki 知識ベース (日本語)
│   │   ├── entities/             # 人物・企業・モデル
│   │   ├── concepts/             # 技術・手法
│   │   ├── comparisons/          # 比較分析
│   │   ├── raw/articles/         # キュレート済み原文
│   │   ├── index.md              # Wikiインデックス
│   │   ├── log.md                # 操作ログ
│   │   └── SCHEMA.md             # Wikiスキーマ定義
│   ├── inbox/                    # クロール結果
│   │   ├── v2ex/
│   │   ├── juejin/
│   │   ├── 36kr/
│   │   ├── zhihu/
│   │   └── wechat-media/
│   ├── config/
│   │   ├── feeds/                # x-accounts.yaml
│   │   ├── hermes/               # SOUL.md, skills/
│   │   └── hot-topics.yaml       # アクティブクローリング対象
│   ├── scripts/                  # クローラー・分析ツール
│   ├── systemd/                  # systemd unit ファイル (参考)
│   ├── docs/                     # ドキュメント
│   ├── srv/                      # Go Web ダッシュボード
│   └── bin/                      # ビルド済みバイナリ
│
├── .hermes/
│   ├── hermes-agent/             # Hermes Agent ソース
│   │   └── venv/                 # Python 仮想環境
│   └── node/                     # Node.js
│
├── wiki → ai-topics-cn/wiki/     # シンボリックリンク
├── x-accounts.yaml → ai-topics-cn/config/feeds/x-accounts.yaml
└── .config/shelley/              # Shelley エージェント設定
```

### 依存ソフトウェア

| ソフトウェア | 用途 |
|-------------|------|
| Python 3.12+ | クローラー・分析スクリプト |
| Go | Web ダッシュボード |
| httpx, beautifulsoup4, curl_cffi | Python HTTP/スクレイピング |
| Shelley | exe.dev エージェント |

---

## 2. 新マシンのセットアップ

### 2.1 基本パッケージ

```bash
sudo apt-get update
sudo apt-get install -y git python3 python3-pip python3-venv curl wget jq
```

### 2.2 Python 依存

```bash
pip install httpx beautifulsoup4 readability-lxml pyyaml curl_cffi
```

---

## 3. リポジトリのクローン

```bash
cd ~
git clone https://github.com/kzinmr/ai-topics-cn.git
cd ai-topics-cn
git config user.name "Hermes Agent"
git config user.email "hermes@hermes-china-digest.exe.xyz"
```

### 3.1 GitHub 認証の設定（HTTPS push 用）

リポジトリをクローン後、**Classic PAT（Personal Access Token）**を作成して認証を通す。

```bash
# GitHub で Classic PAT を取得
# Settings → Developer settings → Personal access tokens → Tokens (classic)
# Scope: ☑ repo (Full control of private repositories)

# ~/.netrc に認証情報を保存（git push時に自動使用）
cat >> ~/.netrc << 'EOF'
machine github.com login <GitHubユーザー名> password <Classic PAT>
EOF
chmod 600 ~/.netrc

# 動作確認
cd ~/ai-topics-cn && git push origin main
```

> **注意**: Fine-grained PAT（`github_pat_`で始まるtoken）はリポジトリ単位の許可が必要で、HTTPS pushには使用できない。Classic PATを使用すること。

---

## 4. シンボリックリンクの作成

```bash
# Wiki
ln -sf ~/ai-topics-cn/wiki ~/wiki

# X accounts
ln -sf ~/ai-topics-cn/config/feeds/x-accounts.yaml ~/x-accounts.yaml
```

---

## 5. systemd サービスの設定

### 5.1 Go Web Dashboard

```bash
sudo cp ~/ai-topics-cn/systemd/srv.service /etc/systemd/system/srv.service
sudo systemctl daemon-reload
sudo systemctl enable --now srv.service
```

### 5.2 Crawl Timer (6時間ごと)

```bash
sudo cp ~/ai-topics-cn/systemd/crawl-cn-ai.service /etc/systemd/system/
sudo cp ~/ai-topics-cn/systemd/crawl-cn-ai.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now crawl-cn-ai.timer
```

### 5.3 Triage Timer (12時間ごと)

```bash
sudo cp ~/ai-topics-cn/systemd/shelley-triage.service /etc/systemd/system/
sudo cp ~/ai-topics-cn/systemd/shelley-triage.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now shelley-triage.timer
```

### 5.4 Trending Topics Timer (毎日)

```bash
sudo cp ~/ai-topics-cn/systemd/shelley-trending-topics.service /etc/systemd/system/
sudo cp ~/ai-topics-cn/systemd/shelley-trending-topics.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now shelley-trending-topics.timer
```

### 5.5 Active Crawl Timer (毎日)

```bash
sudo cp ~/ai-topics-cn/systemd/shelley-active-crawl.service /etc/systemd/system/
sudo cp ~/ai-topics-cn/systemd/shelley-active-crawl.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now shelley-active-crawl.timer
```

### 5.6 Wiki Health Timer (毎週)

```bash
sudo cp ~/ai-topics-cn/systemd/shelley-wiki-health.service /etc/systemd/system/
sudo cp ~/ai-topics-cn/systemd/shelley-wiki-health.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now shelley-wiki-health.timer
```

---

## 6. 動作確認チェックリスト

### 基本

- [ ] `python3 --version` → 3.12+
- [ ] `python3 -c 'import httpx, bs4, yaml'` → エラーなし

### リポジトリ

- [ ] `cd ~/ai-topics-cn && git status` → クリーン
- [ ] `git push origin main` → 成功（HTTPS認証確認）
- [ ] `ls ~/wiki/SCHEMA.md` → 存在

### シンボリックリンク

- [ ] `ls -la ~/wiki` → `~/ai-topics-cn/wiki`
- [ ] `ls -la ~/x-accounts.yaml` → `~/ai-topics-cn/config/feeds/x-accounts.yaml`

### クローラー

- [ ] `python3 scripts/crawl_all.py --dry-run` → 正常出力
- [ ] `python3 scripts/trending_topics.py --days 3` → レポート出力
- [ ] `python3 scripts/wiki_health.py` → ヘルスレポート出力
- [ ] `python3 scripts/build_x_wiki.py --dry-run` → X アカウント確認

### systemd

- [ ] `systemctl status srv` → active (running)
- [ ] `systemctl list-timers --no-pager` → 全タイマー表示
- [ ] `curl -s http://localhost:8000/` → HTML

### Web アクセス

- [ ] `https://hermes-china-digest.exe.xyz:8000/` → ダッシュボード表示

---

## 7. トラブルシューティング

### クローラーエラー

```bash
journalctl -u crawl-cn-ai -n 50 --no-pager
# よくある原因:
# - httpx/curl_cffi がインストールされていない
# - 中国サイトのレート制限 (429)
# - ネットワーク接続の問題
```

### トリアージが発火しない

```bash
systemctl list-timers --all --no-pager
journalctl -u shelley-triage -n 20 --no-pager
# 手動トリガー:
sudo systemctl start shelley-triage.service
```

### CSDNコンテンツの混入

CSDNは絶対に使用禁止。混入した場合:
```bash
grep -rl 'csdn.net' wiki/ inbox/
# 該当ファイルを削除
```

---

## 8. 付録: ファイル一覧

### git に含まれるもの（クローンで自動復元）

- `wiki/` — 全 wiki ページ
- `inbox/` — クロール結果
- `config/` — feeds, hermes skills, hot-topics.yaml, SOUL.md
- `scripts/` — クローラー・分析スクリプト
- `systemd/` — systemd unit ファイル
- `docs/` — ドキュメント
- `srv/`, `cmd/`, `bin/` — Go web ダッシュボード

### ポート使用

| ポート | サービス | 公開 |
|--------|---------|------|
| 8000 | Go Web Dashboard | `https://hermes-china-digest.exe.xyz:8000/` |

---

## 変更履歴

| 日付 | 内容 |
|------|------|
| 2026-04-17 | 初版作成 |
