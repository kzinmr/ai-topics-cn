---
title: "安卓手机 sing-box 和 tailscale 共存配置参考"
source: v2ex
url: "https://www.v2ex.com/t/1207255"
author: "evemoo"
date: 2026-04-20
score: 5
tags: ["ai"]
---

# 安卓手机 sing-box 和 tailscale 共存配置参考

一开始折腾 Clash-Meta 和 tailscaled-socks5-android 浪费了很多时间，指定 Userspace networking mode 的 socks5 代理出口一直报错：
dial tail-socks match IPCIDR/100.64.0.0/10 --> error: context deadline exceeded
172.19.0.1:41221 -> 100.170.x.x:9801 io/timeout




测试版本：Android 15 + SFA 1.14.0-alpha.15 、Windows-amd64 + SFA 1.13.9
基础配置来源：OkProxyConf Sing-Box Generator，修改 outbounds 和 endpoint 的配置
重点：

sing-box inbounds 的 tun 不能加 route_exclude_address，加了的话 100.64.0.0/10 会走直连不经过 tun （和 Windows 上的 Clash 配置有区别，被坑了）
要访问自己的子网设备，route -> rules 的 IPCIDR 要加上自己的内网网段（ 192.168.x.x/16)，不然规则往下匹配会走直连




配置参考：
{
  "$schema": "https://raw.githubusercontent.com/xmdhs/sing-box-generate-schema/refs/heads/master/schema.generated.json",
  "log": {
    "disabled": false,
    "level": "error",
    "timestamp": true
  },
  "dns": {

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1207255)
