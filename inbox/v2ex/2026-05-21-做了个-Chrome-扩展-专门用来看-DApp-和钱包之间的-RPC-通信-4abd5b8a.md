---
title: "做了个 Chrome 扩展，专门用来看 DApp 和钱包之间的 RPC 通信"
source: v2ex
url: "https://www.v2ex.com/t/1214546"
author: "beilun"
date: 2026-05-21
score: 0
tags: ["ai"]
---

# 做了个 Chrome 扩展，专门用来看 DApp 和钱包之间的 RPC 通信

平时调 dapp 的时候经常遇到这种事：网页那边一点按钮，钱包就跳出来要签名，但页面
没说清楚到底签的是啥、传了哪些参数、返回了什么。自己写的 dapp 还好，加几行
console.log
就完事；要是想看别人家合约的调用流程、或者复现一个用户反馈的奇怪报错，就得跑去
MetaMask 设置里翻 activity log ，还看不全 —— 只能看自己钱包发出去的，看不到
dapp 那一侧的时序、参数、错误。
以前一直靠在 window.ethereum
上猴补丁打日志，每次都要写一遍，挺烦的。索性做成了一个 Chrome 扩展。装上之后
F12 里会多一个面板叫 DApp Inspector，当前 tab 所有
window.ethereum.request 的调用都按时间顺序列出来：

方法名（eth_sendTransaction / eth_signTypedData_v4 / personal_sign
…），自动分类成 read / write / sign / subscribe
完整的入参、返回值、错误对象
时延分解：dapp 发起 → 扩展排队 → throttle → 钱包审批 → RPC 往返 → 回到
dapp ，每一段单独算
当前 chainId 、来源 origin
合约调用会自动 decode calldata —— 内置 ERC-20/721/1155/Permit2
选择器，识别不到再去 Sourcify 、4byte 拉，拉到的 ABI 本地缓存 7 天

顺手加了几个调试用的规则引擎：

Block —— 按方法名/origin 匹配，拒掉某些请求，自定义错误码和消息，看 dapp
的错误分支处理得对不对
Throttle —— 给匹配的请求加延迟，验证慢网络 / loading state / 超时分支

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1214546)
