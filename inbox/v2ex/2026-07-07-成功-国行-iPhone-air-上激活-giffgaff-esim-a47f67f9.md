---
title: "成功：国行 iPhone air 上激活 giffgaff esim"
source: v2ex
url: "https://www.v2ex.com/t/1225621"
author: "zjzs"
date: 2026-07-07
score: 0
tags: ["ai"]
---

# 成功：国行 iPhone air 上激活 giffgaff esim

参考了几个文章：
1.使用 mumu 模拟器，模拟安卓手机，申请 esim ，会下发下个激活串

2.使用 https://qrcode.show/ ，将文字串转换为二维码（要在码头加上 LPA:）

3.参考 https://github.com/Yu9191/wloc ，修改定位，激活 esim ，全程顺利
我的系统是 IOS26.5.2 模拟定位用的以下步骤
0.按 wloc 要求，配置 shadowrocket ，并将节点切到英国（与 esim 卡申请时填的国家一致）
1.https://wloc-pages.pages.dev/ 在选点页面选好需要修改的定位并储存到设备
2.开飞行模式 → 关闭定位服务 → 重启设备
3.关闭飞行模式（ WiFi 也要关）→ 连接代理工具（确认 VPN 图标出现）→ 打开定位服务
4.打开地图验证
5.添加 esim ，扫二维码成功

马上测试了 whats app 接码，都很顺利。

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1225621)
