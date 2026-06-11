---
title: "『ArchLinux』简明安装指南(Laptop+Nvidia+Cachyos Kernel +xfs+KDE)"
source: v2ex
url: "https://www.v2ex.com/t/1218319"
author: "MilesClem"
date: 2026-06-05
score: 0
tags: ["ai", "AI", "GPT", "gpt"]
---

# 『ArchLinux』简明安装指南(Laptop+Nvidia+Cachyos Kernel +xfs+KDE)

原创性声明：
本文转载自本人在 Nodeseek原创的ArchLinux 安装帖，这份教程是我在初步学习 Linux 并积极开荒后得到的经验,在此向大家分享。


笔者在入门学习 linux 时选择了 ArchLinux开始传教,翻阅了很多教程,踩了很多新手的坑。零零散散 Obsidian 中存下很多自己需要注意的事项。遂写成一篇针对性的安装方案，以供大家参考。
有纰漏或者勘误的地方还请大家多多指点。
安装时遇到报错请首先在ArchWiki上寻找解决方案。

参考网页：
ArchWiki Install guide(官方) 请首先参考官方安装文档
arch_icekylin 的博客(常见教程，基于 btrfs)
archlinuxstudio.github.io （国内不可达）
unixchad 全盘加密安装 Archlinux_bilibili
笔记本配置如下：

机械革命 耀世 15pro i7-14650HX/RTX4060 32G/4T 网卡 AX211

采用系统配置如下：

systemd-boot 作为 bootloader
BIOS (UEFI): N.1.07MRO11 (5.27)
Bootmgr: UEFI OS - BOOTX64.EFI
Init System: systemd 260.2-2-arch



xfs 文件系统（采用 home 单独分区，单系统共三个分区）——不采用加密
Archlinux 做主体但采用 linux-cachyos 作为内核
nvidia-open-dkms 驱动（ cachyos 仓库版本  610.43.02-3 ）
KDE 桌面环境（ plasma-6.6.5 ）


安装详细过程
安装前准备
ArchLinux 官方 iso 源
中科大镜像源(ustc)

…(内容已截断)

## 涉及话题
- ai
- AI
- GPT
- gpt

[原文链接](https://www.v2ex.com/t/1218319)
