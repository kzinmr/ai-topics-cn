---
title: "写 README/技术方案时被 Ai 生成的 PlantUml/Mermaid 折腾烦了，做了个 预览小工具"
source: v2ex
url: "https://www.v2ex.com/t/1218486"
author: "lipengxs"
date: 2026-06-06
score: 3
tags: ["AI", "大模型", "ai", "Ai"]
---

# 写 README/技术方案时被 Ai 生成的 PlantUml/Mermaid 折腾烦了，做了个 预览小工具

大家好，最近我做了一个小工具 DiagramPreview：

https://diagrampreview.com

起因是我最近写 README 、技术方案和接口文档时，经常让大模型生成 Mermaid 、PlantUML 、架构图、OpenAPI 流程、SQL ER 图之类的文本。

AI 生成初稿确实很快，但有个步骤一直很烦：它通常只给代码，不帮你确认能不能渲染。很多时候复制到文档里才发现 Mermaid 报错，或者 PlantUML 图看起来不对，还要再找工具预览、修语法、导出图片。

所以我把这个中间步骤做成了一个在线工具站：

- Mermaid / PlantUML / Graphviz / D2 / Markdown 预览
- AI Diagram Generator 、Text to Mermaid 、Mermaid AI Fixer
- OpenAPI to Sequence Diagram 、SQL to ER Diagram
- JSON / YAML / JSON Schema / XML / CSV 结构可视化
- Docker Compose 、Kubernetes Manifest 、package.json 依赖图
- SVG / PNG / PDF 导出
- 不需要登录，浏览器里直接用

普通预览类工具主要在浏览器里处理。AI 生成类工具会调用后端接口，所以不要把私有代码、密钥、内部架构细节直接丢进去。

我的主要使用场景是：

1. 让 AI 先生成图表代码。
2. 粘贴到 DiagramPreview 里看是否能渲染。
3. 如果语法坏了，修一下或让 AI 修复。
4. 导出 SVG/PNG 放到 README 、PRD 、技术方案或周报里。

目前还比较早期，想听听 V2EX 上大家的建议：


…(内容已截断)

## 涉及话题
- AI
- 大模型
- ai
- Ai

[原文链接](https://www.v2ex.com/t/1218486)
