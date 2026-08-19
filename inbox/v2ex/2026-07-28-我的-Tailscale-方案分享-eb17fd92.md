---
title: "我的 Tailscale 方案分享"
source: v2ex
url: "https://www.v2ex.com/t/1230557"
author: "dcsuibian"
date: 2026-07-28
score: 2
tags: ["AI", "ai"]
---

# 我的 Tailscale 方案分享

上篇：自建 NetBird 稳定吗？
前情回顾：WireGuard 不够方便，于是我自建了 NetBird 。
WireGuard 的问题：

公钥得手动分发
DDNS 支持不够好（只在建立连接时解析一次域名，后续 IP 更新感知不到）

NetBird 整体给我的感觉都不错（到现在也是），但是目前还是发现两个问题：

一个是 NetBird 的手机客户端好像没跟上版本，很古老
一个是自建 NetBird 中招了 Next.js 的漏洞，而自建 BUG 修复没有官方那么及时

因此，后续在跟 AI 迭代几轮后，我还是选择了 Tailscale 。
选 Tailscale 的原因：

我家网络状况还可以，至少从速度上看是打洞成功的
不想再自建服务器了，简单省钱
了解到了 Tailnet Lock 的存在

以下是我家设备网络的物理拓扑图。

左边是我目前工作地方租的房，右边是老家（放 NAS ）的地方。我其实需求就是想在工作的地方访问老家的 NAS ，也可以 RDP 到我的二奶机。在外的话，手机和笔记本也能访问家里的局域网。同时我还想尽量少装客户端。
多的我就不说了，直接放图（做完以后就是这样的）：

说点我觉得干货的内容吧：


我使用了 Tailscale 官方的Tailnet Lock功能。简单说就是这个在很大程度上避免了（万一） Tailscale 官方恶意地将节点插入到我们的网络里。
仍然存在 TOFU （ Trust On First Use ） 问题。
Tailscale 官方的客户端是部分开源。



我的两台 Windows Server 是签名节点，同时也负责流量的转发。这个有几个细节要讲：

…(内容已截断)

## 涉及话题
- AI
- ai

[原文链接](https://www.v2ex.com/t/1230557)
