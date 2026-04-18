---
title: "GoMCP — Go言語MCP Serverフレームワーク"
created: 2026-04-18
updated: 2026-04-18
tags: [ai-agents, mcp, framework, open-source-ai, tooling]
aliases: ["Go MCP Server", "GoMCPフレームワーク", "Gin MCP アダプター"]
source_lang: zh-CN
---

# GoMCP — Go言語MCP Serverフレームワーク

Goエコシステム向けの軽量MCP（Model Context Protocol）Serverフレームワーク。既存のGin APIを1行のコードでMCP Toolとして公開できる。

## 概要

開発者: zhangpanda  
GitHub: [zhangpanda/gomcp](https://github.com/zhangpanda/gomcp)

既存のGo MCPライブラリ（mcp-go、公式SDK）はSDKレベルで、Tool定義に多くの定型コードが必要。GoMCPはこれを框架レベルで解決する。

## 核心機能

### 1. struct tag 自動JSON Schema生成

手動でJSON Schemaを書く必要なし。Goのstruct tagから自動生成。

### 2. GinルートのMCP Toolインポート

既存のGinプロジェクトを1行でMCP化:

```go
adapter.ImportGin(s, ginRouter, adapter.ImportOptions{
    IncludePaths: []string{"/api/v1/"},
})
```

これにより、指定パス配下の全Ginルートが自動的にMCP Toolとして公開される。

### 3. 框架レベル機能

- ミドルウェアサポート
- ルートグループ管理
- 認証メカニズム統合

## ユースケース

既存のGoバックエンドサービスにAI Agentからの呼び出し機能を追加。例えば、在庫管理API・ユーザー情報API・決済APIなどをMCP Tool化し、Claude DesktopやCursorから直接呼び出せるようにする。

## 関連プロジェクト

- [[mcp]] — Model Context Protocol
- [[claude-code]] — MCPサポートの開発ツール
- [[function-calling]] — LLMと外部APIの接続メカニズム

## 出典

- [V2EX: 做了个 Go 的 MCP Server 框架，一行代码把 Gin API 接入 AI](https://www.v2ex.com/t/1206602) — zhangpanda (2026-04-17)
- [GitHub: zhangpanda/gomcp](https://github.com/zhangpanda/gomcp)
