---
title: "分享一个 tailscale peer relay 相比自建 derp 的优势"
source: v2ex
url: "https://www.v2ex.com/t/1212280"
author: "haukuen"
date: 2026-05-12
score: 1
tags: ["ai"]
---

# 分享一个 tailscale peer relay 相比自建 derp 的优势

这件事有个背景故事：我以前一直是自建的 derp 来中继，体验一直很好，有次朋友的一台 nas 分享到我的 tailnet ，控制面板一切正常但当时就是访问不了。过了好几天排查出来是因为我自建 derp 后就关闭了官方的中继节点，朋友分享的设备不会走我自建中继，又打不了洞所以一直连不上，最后开启官方中继后解决此问题。

今天搞了个 peer relay 玩，无意中发现朋友的那台 nas 竟然会走我 tailnet 里的这台 peer relay 节点，然后手动测试了一下。
 
上图是 ping 朋友的设备，可以看到只会走官方的海外中继，然后再走 peer relay （如果此时没有 peer relay 就会一直走海外节点，不会走自建 derp ），下图是我自己的设备，会走自建 derp 。
 
不敢确定是不是 100%这样，如有高手欢迎斧正。

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1212280)
