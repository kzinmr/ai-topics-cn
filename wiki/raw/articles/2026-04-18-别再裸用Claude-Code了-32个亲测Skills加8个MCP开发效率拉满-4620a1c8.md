# 别再裸用 Claude Code 了！32 个亲测Skills + 8 个 MCP，开发效率直接拉满！

**Source:** juejin.cn
**Author:** 蝎子莱莱爱打怪
**URL:** https://juejin.cn/post/7620060655607857178
**Date:** 2026-03-23
**Engagement:** 464 likes, 39,172 views, 37 min read
**Tags:** [MCP, Claude, Skills, Claude Code, AI Engineer, 开发效率]

## 核心要点

SkillsとMCPの違い:
- **Skills**: 提示詞/標準化ワークフローをカプセル化。Claudeを特定分野の「専門職」に変える。本質はAIを「より賢く」する。
- **MCPサーバー**: ローカルで動作するツール/APIサービス。Claudeにローカルファイル、ブラウザ、外部APIへのアクセスを可能にする。本質はAIを「より行動力のある」にする。

### 推奨インストールコマンド
```bash
npx skills find <キーワード>
npx skills add <owner/repo@skill> -y -g
npx skills list -g
```

### 32個のスキルカテゴリ
- フロントエンド開発: frontend-design, web-artifacts-builder, canvas-design, theme-factory, vercel-react-best-practices, web-design-guidelines
- バックエンド開発: backend-architecture, system-design, code-review, api-design
- DevOps: docker-deploy, ci-cd-setup, monitoring-setup
- AIエンジニアリング: prompt-engineering, rag-builder, agent-orchestrator

## 分析

掘金の記事はClaude CodeのSkillsエコシステムとMCPサーバーの統合を深く解説している。V2EXの開発者層からも同様の議論（Hermes-Agent + Kimi Coding Planの連携）が出ており、中国の開発者コミュニティ全体で「AIコーディングツールの最適化」がホットトピックになっている。
