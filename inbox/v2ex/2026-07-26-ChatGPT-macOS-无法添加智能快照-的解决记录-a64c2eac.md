---
title: "ChatGPT macOS「无法添加智能快照」的解决记录"
source: v2ex
url: "https://www.v2ex.com/t/1229981"
author: "peacekang"
date: 2026-07-26
score: 0
tags: ["openai", "ChatGPT", "ai"]
---

# ChatGPT macOS「无法添加智能快照」的解决记录

最近 ChatGPT macOS 的智能快照突然不能用了。
不管截 Finder 、Edge 还是其他软件，按下快捷键后都会卡一会儿，然后提示：
无法添加智能快照
Unable to attach appshot

一开始我以为是权限问题，把“屏幕与系统音频录制”“辅助功能”“完全磁盘访问权限”都检查了一遍，ChatGPT 和 Codex Computer Use 也都有权限，但没有用。
重新启动、重新授权、换目标软件也都一样。
网上能搜到的线索很少，最后在 GitHub 找到了两个相关 Issue：

https://github.com/openai/codex/issues/25269
https://github.com/openai/codex/issues/29772

我又检查了本机日志：
~/Library/Logs/com.openai.codex/

发现每次失败都会出现：
captureNotFound
update_poll_failed
hadAxText=false
hadScreenshot=false

简单说就是：截图任务启动成功了，但 ChatGPT 随后查询结果时，却找不到刚刚创建的任务。
最后找到的原因
#25269 下面有位用户提到，他的 ~/.codex 是一个符号链接。把它改回真实目录，并清理旧的 Computer Use 注册后，智能快照就恢复了。
我检查了一下自己的电脑：
test -L "$HOME/.codex" && echo "是符号链接"
readlink "$HOME/.codex"

结果发现我的 ~/.codex 确实也被链接到了其他位置。

…(内容已截断)

## 涉及话题
- openai
- ChatGPT
- ai

[原文链接](https://www.v2ex.com/t/1229981)
