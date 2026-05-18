---
title: "Arch Linux 中虚拟机运行 Windows,分辨率和屏幕不适配"
source: v2ex
url: "https://www.v2ex.com/t/1212814"
author: "richiewu"
date: 2026-05-14
score: 0
tags: ["ai"]
---

# Arch Linux 中虚拟机运行 Windows,分辨率和屏幕不适配

用的 kvm ，OpenGL 和 3D 加速都设置了
<video>
  <model type="virtio" vram="524288" heads="1" primary="yes">
    <acceleration accel3d="yes"/>
  </model>
  <alias name="video0"/>
  <address type="pci" domain="0x0000" bus="0x00" slot="0x01" function="0x0"/>
</video>

<graphics type="spice">
  <listen type="none"/>
  <image compression="off"/>
  <gl enable="yes" rendernode="/dev/dri/by-path/pci-0000:00:02.0-render"/>
</graphics>

virtio-win 也安装了，spice-guest-tools 也安装了
虚拟机里屏幕分辨率死活不能适配屏幕，折腾老半天了

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1212814)
