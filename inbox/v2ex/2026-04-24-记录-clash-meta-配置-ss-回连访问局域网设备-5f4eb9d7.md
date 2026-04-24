---
title: "记录： clash-meta 配置 ss 回连访问局域网设备"
source: v2ex
url: "https://www.v2ex.com/t/1208311"
author: "evemoo"
date: 2026-04-24
score: 2
tags: ["ai", "AI"]
---

# 记录： clash-meta 配置 ss 回连访问局域网设备

两个注意点：

clash-meta 取消勾选“网络->绕过私有地址”，不然配置了 dns 和 tun 都会被直接过滤掉，连 debug 日志都不显示 192.168.0.0/16 的访问流量；
dns -> proxy-server-nameserver 要加，不然解析不到回连的 ddns 域名

配置如下：
mixed-port: 7890

# Linux 和 macOS 的 redir 代理端口
redir-port: 7892

# 允许局域网的连接
allow-lan: true

# 规则模式：Rule （规则） / Global （全局代理）/ Direct （全局直连）
mode: rule

# 设置日志输出级别 (默认级别：silent ，即不输出任何内容，以避免因日志内容过大而导致程序内存溢出）。
# 5 个级别：silent / warning / error / info / debug 。级别越高日志输出量越大，越倾向于调试，若需要请自行开启。
log-level: info

# Clash 的 RESTful API
external-controller: '127.0.0.1:9091'

# RESTful API 的口令
secret: ''

tun:
  enable: true
  stack: mixed
  dns-hijack:
    - "any:53"
    - "tcp://any:53"
  auto-route: true
  auto-redirect: true
  auto-detect-interface: true

dns:
  enable: true
  ipv6: false
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16

…(内容已截断)

## 涉及话题
- ai
- AI

[原文链接](https://www.v2ex.com/t/1208311)
