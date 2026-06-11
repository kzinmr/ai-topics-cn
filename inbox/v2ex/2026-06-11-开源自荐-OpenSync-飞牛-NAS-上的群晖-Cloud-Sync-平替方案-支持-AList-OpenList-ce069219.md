---
title: "[开源自荐] OpenSync：飞牛 NAS 上的群晖 Cloud Sync 平替方案，支持 AList / OpenList 自动同步"
source: v2ex
url: "https://www.v2ex.com/t/1219676"
author: "v0rtix"
date: 2026-06-11
score: 0
tags: ["ai"]
---

# [开源自荐] OpenSync：飞牛 NAS 上的群晖 Cloud Sync 平替方案，支持 AList / OpenList 自动同步

大家好，最近做了一个 nas 上的小工具，叫 OpenSync ，主要是给飞牛 fnOS / 飞牛 NAS 用户准备的。
如果你以前用过群晖的 Cloud Sync ，应该会很熟悉这种需求场景：
本地 NAS 的文件，想定时同步备份到网盘、对象存储、WebDAV ，或者另一台存储设备上。飞牛目前的备份功能不太好用，我自己也想要一个类似 Cloud Sync 的工具，于是就做了这个开源项目。
项目地址：
https://github.com/chenbin3625/OpenSync
主要场景：
1.飞牛 NAS 本地目录定时备份到网盘
2.多个网盘 / 对象存储之间同步或迁移
3.替代群晖 Cloud Sync 的基础同步能力
4.想通过网页界面管理同步任务，而不是写脚本
主要技术栈：Go+React+antd 单二进制文件可运行，支持 x86/arm 结构，同步发布 docker 镜像。
界面预览
任务总览

实时任务

历史任务

任务详情

引擎管理

通知配置

系统设置

快速部署
推荐使用 Docker Compose 部署：
docker-compose.yml
services:
  opensync:
    image: chenbin3625/opensync:latest
    container_name: opensync
    restart: unless-stopped
    ports:
      - "8023:8023"
    volumes:
      - ./data:/app/data
    environment:
      OPENSYNC_PORT: 8023
      GIN_MODE: release

启动后访问：
http://你的设备 IP:8023/


…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1219676)
