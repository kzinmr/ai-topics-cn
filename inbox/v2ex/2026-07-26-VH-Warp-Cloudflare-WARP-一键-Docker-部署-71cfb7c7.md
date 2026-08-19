---
title: "🥝 VH-Warp： Cloudflare WARP 一键 Docker 部署"
source: v2ex
url: "https://www.v2ex.com/t/1229903"
author: "uxiaohan"
date: 2026-07-26
score: 0
tags: ["ai"]
---

# 🥝 VH-Warp： Cloudflare WARP 一键 Docker 部署

🥝 轻量级 Docker 镜像封装 Cloudflare WARP ，快速搭建局域网可访问的代理服务，极简部署、极致性能、极其稳定。
🔗 GitHub 仓库：github.com/uxiaohan/vh-warp

一条命令部署：docker compose up -d，零配置上手
局域网代理：Mixed 模式（ SOCKS5 + HTTP ），单端口 1111 ，全屋设备直连
多账号支持：WARP Free （ MASQUE ）/ WARP+ / Zero Trust Teams ，菜单切换
断线自愈：四级渐进恢复，自动软重连 → 完整重置，无需人工干预
多架构：amd64 + arm64 ，NAS 、软路由、树莓派通吃

快速开始
🐳 直接拉取（推荐）
# 下载 docker-compose.yml
wget https://raw.githubusercontent.com/uxiaohan/vh-warp/main/docker-compose.yml
# 启动
docker compose up -d


局域网设备配置代理地址即可(支持 socks5 及 http) ：
SOCKS5:  192.168.x.x:1111
HTTP:    192.168.x.x:1111

端口 1111 为 Mixed 模式，同一端口同时支持 HTTP 和 SOCKS5 ，客户端无需区分协议类型。

仅供学习与技术研究使用。

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1229903)
