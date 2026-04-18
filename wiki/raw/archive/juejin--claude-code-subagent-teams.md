---
title: "手撕Claude Code-5：Subagent 与 Agent Teams"
source: "juejin"
url: "https://juejin.cn/post/7629598396504784948"
date: "2026-04-18"
tags: ['claude-code', 'subagent', 'agent-teams', 'multi-agent', 'fork']
triage: "✅ Take"
scraped: "2026-04-18T09:28:22.156091"
---

# 手撕Claude Code-5：Subagent 与 Agent Teams

Claude Code 支持三种不同的多代理模式：**普通Subagent**（指定类型）、**Fork Subagent**（继承上下文）、**Agent Teams**（团队协作）。本文将从源码层面逐一解析这三种模式的工作原理和使用方法。

## 一、普通Subagent（指定类型）

### 1.1 什么是Subagent

Subagent是运行在独立上下文窗口中的专用AI助手。每个子代理拥有自己的系统提示、工具访问权限和权限设置。

简单来说，Subagent就是在当前会话里派出去的"分身"，每个分身有独立的上下文窗口，干完活只把结果摘要返回给主对话。主对话不会被那些大量输出塞满。

### 1.2 创建Subagent

在Claude Code中创建Subagent非常简单：

```bash
# 指定创建特定类型的Subagent
claude subagent create --type code-reviewer --name "代码审查员"
```

Subagent创建后，你可以给它分配具体的任务：

```bash
claude subagent run --name "代码审查员" --task "检查src目录下所有Python文件的代码规范"
```

### 1.3 Subagent的工作原理

从源码角度来看，Subagent的工作流程如下：

1. **创建阶段**：主Agent调用 `create_subagent` API，传入系统提示和工具配置
2. **执行阶段**：Subagent在独立的沙箱环境中运行，拥有自己的上下文窗口
3. **结果返回**：Subagent执行完毕后，将结果摘要返回给主Agent
4. **上下文隔离**：Subagent的完整对话历史不会污染主对话的上下文

### 1.4 Subagent的使用场景

- **代码审查**：创建专门的代码审查Subagent，检查代码质量和规范
- **测试生成**：为测试任务创建独立的Subagent，生成单元测试
- **文档编写**：让Subagent专注于技术文档的编写
- **数据处理**：处理大规模数据时，使用Subagent避免上下文溢出

## 二、Fork Subagent（继承上下文）

### 2.1 什么是Fork Subagent

Fork Subagent是普通Subagent的进阶版本。与普通Subagent不同，Fork Subagent会**继承主对话的上下文**，包括之前的对话历史、代码改动和项目理解。

### 2.2 Fork Subagent的工作原理

Fork操作的本质是：

1. **上下文复制**：将当前主对话的完整上下文（包括历史消息、工具调用记录、文件变更）复制到一个新的Subagent实例中
2. **并行执行**：Fork后的Subagent可以独立运行，与主对话并行处理不同任务
3. **结果整合**：Fork Subagent完成后，将其结果合并回主对话

### 2.3 Fork Subagent的使用场景

Fork Subagent特别适合以下场景：

- **多路径探索**：需要同时尝试多种解决方案时，Fork出多个Subagent并行探索
- **分支开发**：在主开发流之外，Fork出一个Subagent来处理实验性功能
- **并行调试**：同时调试多个问题，每个问题分配一个Fork Subagent

```bash
# Fork一个Subagent，继承当前所有上下文
claude subagent fork --name "调试助手" --task "帮我调试这个内存泄漏问题"
```

### 2.4 Fork vs 普通Subagent的区别

| 特性 | 普通Subagent | Fork Subagent |
|------|-------------|---------------|
| 上下文 | 独立的空白上下文 | 继承主对话的完整上下文 |
| 文件访问 | 受限的文件访问 | 完整的文件访问权限 |
| 工具集 | 可自定义的工具集 | 继承主对话的工具集 |
| 适用场景 | 独立任务 | 需要上下文延续的任务 |
| 资源消耗 | 较低 | 较高（需要复制上下文） |

## 三、Agent Teams（团队协作）

### 3.1 什么是Agent Teams

Agent Teams是Claude Code的多Agent协作机制，让多个"队友"并行处理任务。简单来说：把"一个全能选手"变成"一个项目经理+多个专业工程师"。

### 3.2 Agent Teams的工作原理

Agent Teams的核心架构：

1. **团队创建**：主Agent创建一个团队，包含多个专业Subagent
2. **任务分配**：将复杂任务分解为子任务，分配给不同的团队成员
3. **并行执行**：所有团队成员同时开始工作
4. **结果整合**：团队协调器收集所有结果，整合成最终输出
5. **冲突解决**：当多个Agent对同一文件进行修改时，协调器负责解决冲突

### 3.3 创建Agent Teams

```bash
# 创建一个多Agent团队
claude teams create --name "重构团队"

# 添加团队成员
claude teams add-member --team "重构团队" --type code-reviewer --name "审查员"
claude teams add-member --team "重构团队" --type refactoring-specialist --name "重构专家"
claude teams add-member --team "重构团队" --type test-engineer --name "测试工程师"

# 分配任务
claude teams assign-task --team "重构团队" --task "重构用户认证模块"
```

### 3.4 Agent Teams的使用场景

Agent Teams特别适合处理复杂的多阶段任务：

- **大型重构项目**：需要同时处理代码重构、测试更新、文档编写
- **多模块开发**：同时开发多个相互关联的模块
- **全面代码审查**：从安全性、性能、可读性等多个维度审查代码
- **复杂Bug修复**：需要同时分析多个相关的问题

### 3.5 Team模式的优势

1. **并行效率**：多个Agent同时工作，显著缩短任务完成时间
2. **专业分工**：每个Agent专注于自己的领域，提高工作质量
3. **上下文隔离**：不同Agent的工作互不干扰
4. **可扩展性**：可以根据任务复杂度动态调整团队规模

## 四、三种模式的选择指南

### 4.1 如何选择

| 场景 | 推荐模式 | 原因 |
|------|---------|------|
| 简单独立任务 | 普通Subagent | 轻量，上下文隔离 |
| 需要上下文的复杂任务 | Fork Subagent | 继承完整项目理解 |
| 多步骤并行任务 | Agent Teams | 多Agent协作，效率高 |
| 代码审查 | 普通Subagent | 专注单一任务 |
| 重构大型项目 | Agent Teams | 需要多专业协作 |
| 调试复杂问题 | Fork Subagent | 需要完整上下文 |

### 4.2 最佳实践

1. **从小开始**：先用普通Subagent，发现不够用时再升级到Fork或Teams
2. **合理分工**：为每个Subagent/Team定义清晰的职责范围
3. **监控资源**：Agent Teams会消耗较多资源，注意监控Token使用情况
4. **设置超时**：为长时间运行的Subagent设置合理的超时时间
5. **定期清理**：完成任务后及时清理不再需要的Subagent

## 五、总结

Claude Code的三种多代理模式各有特色：

- **普通Subagent** 是基础的多任务处理方式，适合独立、简单的任务
- **Fork Subagent** 提供了上下文继承能力，适合需要完整项目理解的任务
- **Agent Teams** 实现了真正的多Agent协作，适合复杂的并行任务

理解这三种模式的区别和适用场景，可以帮助我们更高效地使用Claude Code处理各种复杂的开发任务。

---

> 本文是"手撕Claude Code"系列的第5篇，基于Claude Code真实源码的Agent工程拆解。
> 作者：唐旺仔 | 2026-04-18
