---
title: "rzsz： Rust 重写的 lrzsz"
source: v2ex
url: "https://www.v2ex.com/t/1206595"
author: "ob"
date: 2026-04-17
score: 1
tags: ["ai", "AI"]
---

# rzsz： Rust 重写的 lrzsz

rzsz：Rust 重写的 lrzsz
起因是，在使用 rz 传文件的过程中，时不时会遇到控制台满屏乱码的情况，有时候传的日志文件比较大，直接就刷个不停，按 Ctrl+C 都结束不了。
然后就想着基于自己的使用习惯，给自己搞个简单好用的（主要是有 AI 帮忙），主要解决三个问题：

难以接受的乱码问题
每次用命令的时候，老得停顿思考一下是用 rz 还是 sz ，而且这俩组合按键按的有点别扭
统一改用 zz ，自动判断是发送还是接收文件，旧的 rz 和 sz 依然可用

安装
一键脚本（自动检测架构、装到 /usr/local/bin、建好所有符号链接）：
curl -fsSL https://raw.githubusercontent.com/kookob/rzsz/main/install.sh | bash

cargo：
cargo install rzsz

旧的 lrzsz 怎么办？
一键脚本会检测到系统已有的 lrzsz 可选择替换或保留。想自己手动清理直接：
sudo apt purge -y lrzsz       # Debian/Ubuntu
sudo yum remove -y lrzsz      # CentOS/RHEL
hash -r                       # 清 shell 命令缓存，否则 rz 可能还指向旧路径

不想完全替代也行，装完后老的 rz sz 保留，日常用新的 zz 即可。回滚用 bash install.sh --uninstall。
用法
和 lrzsz 完全一样，直接替代。最常用的两条：
# 接收文件（在服务器执行，终端弹选择框让你选本地文件）
zz

# 发送文件（把服务器上的文件下载到本地）
zz file.tar.gz
zz *.log                # 多文件

重名文件处理

…(内容已截断)

## 涉及话题
- ai
- AI

[原文链接](https://www.v2ex.com/t/1206595)
