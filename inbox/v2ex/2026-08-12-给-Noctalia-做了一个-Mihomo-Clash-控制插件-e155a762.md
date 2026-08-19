---
title: "给 Noctalia 做了一个 Mihomo / Clash 控制插件"
source: v2ex
url: "https://www.v2ex.com/t/1233875"
author: "MarMDJtin"
date: 2026-08-12
score: 0
tags: ["ai"]
---

# 给 Noctalia 做了一个 Mihomo / Clash 控制插件

最近给 Noctalia 写了一个 Mihomo Control 插件，希望使用 Noctalia + Clash/Mihomo 的朋友可以少开一个管理页面。

它不是新的代理内核，也不会接管或修改 Mihomo 配置。Mihomo 继续负责代理、规则和订阅，插件只通过 External Controller API 提供常用操作。

目前支持：

- 状态栏显示连接状态、代理模式和实时上下行流量
- 查看连接数量、流量统计和内存占用
- 切换 Rule / Global / Direct 模式
- 查看所有代理组及当前节点
- 展开代理组并直接切换节点
- 显示节点延迟
- 单独测试某个代理组，或一键测试全部
- 重启 Mihomo
- Control Center 快捷开关
- 支持本机或远程 Controller
- 支持 HTTP 、HTTPS 以及自签名证书

使用前需要确保 Mihomo 已开启 External Controller ，例如：

```yaml
external-controller: 127.0.0.1:9090
secret: your-secret
```

然后在插件设置中填写 Host 、Port 和 Secret ，启用 `service`，再把组件添加到 Noctalia 状态栏即可。

如果 Controller 暴露到局域网或公网，建议务必配置 Secret ，并通过 HTTPS 或反向代理访问。

目前插件本体的 PR 还在 review 。合并后可以直接从 Noctalia Community Plugins 安装。拖拽排序会在前一个 PR 合并后单独提交。

项目地址：

https://github.com/noctalia-dev/community-plugins/tree/main/mihomo-control

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1233875)
