---
title: "Tailscale 中，如何在分享节点的同时，使用 DERP/peer-relay 加速国内访问？"
source: v2ex
url: "https://www.v2ex.com/t/1210371"
author: "aur3l14no"
date: 2026-05-05
score: 4
tags: ["ai"]
---

# Tailscale 中，如何在分享节点的同时，使用 DERP/peer-relay 加速国内访问？

我有一个无法直连的 Tailscale 节点想要分享给朋友使用。但我发现 Shared Node 在 Tailscale 中会和 Custom DERP 以及 Peer Relay 这两个用于改善连接的中继发生冲突。
具体是这样的：如果我使用了 Custom DERP ，而我朋友的 Tailscale 没有绑定这个 DERP ，那么他就完全无法访问我的节点了。因为我的那个节点会记住这个 DERP ，同时抢占、挤掉原本的那些 Official DERP Server ，使它们无法生效，最终导致朋友也无法访问。
至于 Peer Relay ，它也是依赖 DERP Server 去做 negotiate 的，而由于 Official DERP Server 在国内有的时候会受到干扰，那这个时候 Peer Relay 也会有时不灵。
还有两个备选方案：frp 和 headscale ，但是我觉得这两个也比较麻烦：

FRP 中，如果我想有很多个端口要去分享的话，我每次都得去手动添加，比较麻烦。当然，如果实在不行的话，这就是我的 fallback 计划了。
Headscale ，我觉得它的维护成本有点高，有点麻烦，所以我也在尽力试图避免。

另外我发现其实还有一个办法，就是我发现如果让朋友也在他的 Tailscale 里面加入和我一样的 Custom DERP Server 的话，那么他就能够通过 Custom DERP Server 来连接了。但是这样的话会有一个缺点：

首先，我需要让所有人都在他们的 Tailscale 中加入这个配置，这是个麻烦事。
此外，他们正常在自己的 Tailscale 中做 relayed connection ，都会耗我的 DERP Server 流量。

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1210371)
