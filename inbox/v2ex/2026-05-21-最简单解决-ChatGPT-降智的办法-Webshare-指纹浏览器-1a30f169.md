---
title: "最简单解决 ChatGPT 降智的办法（Webshare+指纹浏览器）"
source: v2ex
url: "https://www.v2ex.com/t/1214447"
author: "EvaElfie"
date: 2026-05-21
score: 2
tags: ["OpenAI", "ChatGPT"]
---

# 最简单解决 ChatGPT 降智的办法（Webshare+指纹浏览器）

抛砖引玉，尽量不说的太复杂，很多一搜其实都有，这只是一个整理
背景：
1 ，OpenAI 会探测浏览器指纹。包括不限于字体，时区，系统语言，因此只全局代理没有用的。被发现指纹和你 IP 不一样，必降智。这就是为何很多人 web 降智，但是 app 不降智的原因。用 https://www.browserscan.net/ 可以自己测试
2 ，OpenAI 对于 IP 纯净度没那么高的要求，主要不能频繁换号和换 IP 。即一个 IP 尽量只与少量账号关联。因此没必要斥巨资买真家宽，但是机场那种万人骑节点肯定也是不行的。用 http://ping0.cc/ 可以简单自测。
解决方法：
1 ，注册 webshare 家宽，8.4 刀一年。https://www.webshare.io/?referral_code=l8pbcdgt108a
Static Residential ，Private ，PROXY NUMBER CUSTOM 选 1 ，Bandwidth 选 250 ，Choose Location of Proxies 选美，Manual Replacementsi 选 20 ，右边 pay year 打开是 8.4 刀
2 ，设置好链式代理。webshare 的 socks5 在大陆不能直连，香港可以。
3 ，指纹浏览器，用 Roxy 免费版足够了。https://roxybrowser.cn?code=09143UXA
新建窗口后，https://www.browserscan.net/ 测试确保是 100%即可
可以设置 IP 变动，国家地区变动时不打开浏览器，防止你误操作被风控

## 涉及话题
- OpenAI
- ChatGPT

[原文链接](https://www.v2ex.com/t/1214447)
