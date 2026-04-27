---
title: "搞个云端 claude code 防止 封号"
source: v2ex
url: "https://www.v2ex.com/t/1206141"
author: "stevenrao"
date: 2026-04-15
score: 3
tags: ["claude"]
---

# 搞个云端 claude code 防止 封号

被封了几个号后，发现问题出在很容易忘记切换 全局代理。更换设备这些操作导致 ip 漂移；
于是突发奇想，如果把 claude code  cli 所有操作行为锁死在一台 vps ； 就弄了个云端 web terminal 这小工具； 
自己用了 2 天，写了 1 个 小项目，感觉还不错，意外收获是可以用手机直接打开网页，也可以躺在床上 编程了
但是手机输入不方便，于是就加了个 语音转 文字输入功能；
说来搞笑，我这个工具全程都使用 claude code 开发出来，用魔法打败魔法啊。我问他这个方案有没有违法 claude code 规则，他说 没有使用第三方工具使用订阅 token ，还是使用原生的  claude code  cli ；在允许范围之内；看起来这条路目前比较安全。

有同样需求的同学可以试用一下，不过前提是你需要一台海外 vps 。我用的腾讯云 轻量 vps 99 元一年那种；之前用它来搭梯子。
https://github.com/mageg-x/ccwt

## 涉及话题
- claude

[原文链接](https://www.v2ex.com/t/1206141)
