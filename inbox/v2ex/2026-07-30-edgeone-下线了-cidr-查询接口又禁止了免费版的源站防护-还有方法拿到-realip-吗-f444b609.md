---
title: "edgeone 下线了 cidr 查询接口又禁止了免费版的源站防护，还有方法拿到 realip 吗？"
source: v2ex
url: "https://www.v2ex.com/t/1231018"
author: "lonelyhentai"
date: 2026-07-30
score: 8
tags: ["ai"]
---

# edgeone 下线了 cidr 查询接口又禁止了免费版的源站防护，还有方法拿到 realip 吗？

第一步：2025 年先下线源站防护，公告 https://cloud.tencent.com/announce/detail/2153
这样没有办法通过查到自己站点的 cdn ip cidr ，一般用户都会想到查询整个 edgeone ip 段，比如 https://api.edgeone.ai/ips?version=v4
第二步：2026 年下线 ip range 查询接口，这下彻底拿不到 ip range 了
# [DEPRECATION NOTICE] This interface stopped serving on 2026-07-31 and will be officially offline on 2026-08-31. Please migrate in time.
# [下线公告] 本接口已于 2026-07-31 停止服务，2026-08-31 正式下线，请及时迁移。

通常来说有反向代理情况下，最通用的方法都是通过 xff 递归判断 ip 是否符合代理 ip 然后找到第一个不认识的 ip 作为 real-ip 。
edgeone 连这个都限制后，就只能靠 EO-Connecting-IP 之类的头，一旦你有多 cdn （比如同时在用 cf ）或者多级 cdn ，那很容易被伪造。逼着你要不只用 edgeone 一家，要不付钱，要不不允许防御？还有其它方法吗？

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1231018)
