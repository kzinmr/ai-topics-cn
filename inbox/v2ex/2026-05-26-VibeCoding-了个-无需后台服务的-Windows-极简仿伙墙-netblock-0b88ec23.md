---
title: "VibeCoding 了个 无需后台服务的 Windows 极简仿伙墙 netblock"
source: v2ex
url: "https://www.v2ex.com/t/1215645"
author: "ghking6"
date: 2026-05-26
score: 0
tags: ["AI"]
---

# VibeCoding 了个 无需后台服务的 Windows 极简仿伙墙 netblock

开源地址：github 点 com/ghking1/netblock 求 star
特性介绍

AI 友好的命令行接口
直接使用 Windows 底层接口，无需后台服务
不依赖 windows 仿伙墙，即使仿伙墙是关的也能生效

使用方法
C:\Windows\System32>netblock.exe -h
netblock <command> [options]

Commands:
  add    Add a blocking/filtering rule
  del    Delete rule(s)
  list   List all rules managed by netblock

Options for 'add':
  -n <name>         Rule name (for later management; default: auto-generated UUID)
  -p <path>         Program absolute path (include .exe; default: all programs)
  -a <ip/cidr>      Remote IP address (IPv4/IPv6, e.g. 192.168.1.1 or 2001:db8::/32)
  -l <port|range>   Local port (e.g. 80; 8000-9000; 81,82,83; 81,82-85; default: all)
  -r <port|range>   Remote port (same format as -l; default: all)
  -e <block|allow>  Action (default: block)

…(内容已截断)

## 涉及话题
- AI

[原文链接](https://www.v2ex.com/t/1215645)
