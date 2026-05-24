---
title: "Graphiti — LLM用リアルタイム知識グラフ"
created: 2026-04-21
updated: 2026-04-21
tags: [knowledge-graph, llm-memory, rag, ai-agents, open-source]
aliases: ["Graphiti", "知識グラフ", "LLM記憶"]
source_lang: zh-CN
source: juejin
url: "https://juejin.cn/post/7630450023371276315"
---

# Graphiti — LLM用リアルタイム知識グラフ

> **トレンド順位**: NEW（2026-04-20 Juejin）
> **ソース**: Juejin
> **作者**: 弋痕
> **スコア**: 👍0 ⭐0（04-20時点）
> **関連**: [[rag]], [[ai-agent]]

## 概要

**Graphiti**は、大規模言語モデルのための構造化記憶能力を提供する知識グラフ構築フレームワークである。LLMアプリケーションに時間軸を考慮した動的な知識グラフを構築し、エンティティ間の関係と時系列情報を効率的に管理できる。

## 核心機能

### 時間軸知識グラフ

Graphitiの特点是支持时间维度的事实追踪：

```python
# エンティティ作成（時間情報付き）
graph.add_entity(
    name="Claude Code",
    entity_type="AI_Tool",
    attributes={"company": "Anthropic"},
    timestamp=datetime.now()
)

# リレーション作成
graph.add_relation(
    source="Claude Code",
    target="MCP",
    relation_type="supports",
    timestamp=datetime.now()
)
```

### 検索能力

| 検索方式 | 説明 |
|---------|------|
| 時刻範囲検索 | 特定期間の情報抽出 |
| エンティティ近傍 | 特定ノードの隣接関係取得 |
| パス検索 | 2つのエンティティ間の経路探索 |

## 類似技術との比較

GraphitiはRAGの进化形として位置づけられる：

| 観点 | 传统RAG | Graphiti |
|------|---------|----------|
| 知識表現 | ベクトル（暗黙的） | グラフ（明示的） |
| 関係抽出 | 類似度ベース | 構造化関係 |
| 時系列対応 | 限定的 | フルサポート |
| 推論能力 | 限定的 | パスベース推論可能 |

## 主要信息来源

- [Graphiti 掘金実践ノート](https://juejin.cn/post/7630450023371276315)