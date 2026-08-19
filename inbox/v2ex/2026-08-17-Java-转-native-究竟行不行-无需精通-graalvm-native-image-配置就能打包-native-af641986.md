---
title: "Java 转 native 究竟行不行？无需精通 graalvm native-image 配置就能打包 native exe 方法分享。"
source: v2ex
url: "https://www.v2ex.com/t/1235141"
author: "ko1haha"
date: 2026-08-17
score: 5
tags: ["人工智能"]
---

# Java 转 native 究竟行不行？无需精通 graalvm native-image 配置就能打包 native exe 方法分享。

编译了一天一夜！
总算把我的老 javafx 项目编译成正宗的 exe 了。
花费这么长时间，也有我设备的问题。
8G 上网本（主力机跑别的），空闲内存只有一半。 
配置点虚拟内存、换成 opencode web 版本，腾出点内存，继续搞。
没错，agent 时代，谁还一个人苦哈哈地编译啊。  
当然是让人工智能给我打工。
方法就是：先准备一份可以运行的 java 版本，让 opencode 调用 java.exe 启动主类。
然后，让它把十几个 jar 用 native-image 编译成 exe ，成功后 opencode 自动调起并分析错误，不断迭代。
这很厉害，我都不知道哪里去找 log, 手动把 exe 拖进 cmd 也没有日志。
终于，javafx 的窗口跑出来了，里面 webview (webkit) 能显示，但一操作就闪退崩溃。
紧接着发现，opencode 竟然在分析汇编指令……
继续，自动迭代……
编译一次半小时，必须交给没有感情的机器人！
继续跑了一两个小时，终于修好了，操作 webview 内容不再崩溃（但是内存浮动明显，比 java8 还糙，简单操作竟然在 300mb-900mb 间浮动！）。
仍有很多功能缺失：打不开系统的文件选择器（ awt/jna 又出问题？）、没有正确启动 web 服务(开着纯血 java 版陪跑！)。
还是得放弃 javafx 了，没啥优势。
如果舍不得生态的话，就做成 web 服务。
明天再试，机器太烫了。

## 涉及话题
- 人工智能

[原文链接](https://www.v2ex.com/t/1235141)
