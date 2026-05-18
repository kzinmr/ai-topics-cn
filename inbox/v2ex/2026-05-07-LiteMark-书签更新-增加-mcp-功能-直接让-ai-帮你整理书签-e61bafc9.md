---
title: "LiteMark 书签更新-增加 mcp 功能 直接让 ai 帮你整理书签"
source: v2ex
url: "https://www.v2ex.com/t/1210890"
author: "topqaz"
date: 2026-05-07
score: 1
tags: ["MCP", "mcp", "ai", "AI"]
---

# LiteMark 书签更新-增加 mcp 功能 直接让 ai 帮你整理书签

LiteMark：轻量自部署书签导航系统
LiteMark 是一个基于 Vue 3 + FastAPI 的轻量书签导航系统，适合部署在自己的服务器上，用来统一管理常用网站、工具入口、技术资料和收藏链接。
项目地址：
https://github.com/topqaz/LiteMark
预览地址：
http://oracle.mn00.net:8081 ，默认账号 admin / admin123      
主要功能

书签添加、编辑、删除、隐藏、排序
分类管理和分类排序
响应式页面，支持手机和电脑访问
后台管理面板
JSON / CSV / HTML 导入导出
WebDAV 定时备份
AI 辅助获取网页信息、生成摘要和标签
内置 Streamable HTTP MCP Server ，可让支持 MCP 的 AI 客户端管理书签

Docker 部署
docker run -d \
  --name litemark \
  -p 8080:80 \
  -v litemark-data:/app/data \
  -e JWT_SECRET=change-this-to-a-secure-random-string \
  -e DEFAULT_ADMIN_USERNAME=admin \
  -e DEFAULT_ADMIN_PASSWORD=admin123 \
  topqaz/litemark:amd64

MCP 使用
后台进入：
系统设置 -> MCP 设置

生成 Token 、开启 MCP 后，可在支持 MCP 的客户端中配置：
{
  "servers": {
    "litemark": {
      "type": "http",
      "url": "https://your-domain.com/mcp/",

…(内容已截断)

## 涉及话题
- MCP
- mcp
- ai
- AI

[原文链接](https://www.v2ex.com/t/1210890)
