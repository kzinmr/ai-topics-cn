---
title: "Claude Code 生态全景：使用技巧、Skills、Subagent、Token 管理与竞品分析"
created: 2026-04-18
updated: 2026-04-18
tags: [claude-code, ai-agents, coding-agents, skills, subagent, token-management, kimi, openclaw, tooling]
aliases: ["Claude Code 生态", "Claude Code 综合指南"]
source_lang: zh-CN
---

# Claude Code 生态全景

Claude Code 是 Anthropic 开发的终端型 AI 编码智能体，与传统 IDE 插件型 AI 工具（GitHub Copilot、Cursor 等）不同，它以 Agent 的方式在终端中运行，具备文件读写、命令执行、Git 操作等自主能力。截至 2026 年 4 月，Claude Code 在中国开发者社区已成为讨论热度最高的 AI 工具，围绕其形成了涵盖 Skills、MCP、Subagent、Token 监控等多个维度的完整生态。

> 本文综合了 36kr、掘金、V2EX 等来源的 15+ 篇中文技术文章与讨论，从七个维度梳理 Claude Code 的生态全貌。

---

## 一、使用技巧与工作流

### 1.1 必会的终端命令

| 命令 | 作用 | 使用场景 |
|------|------|---------|
| `/clear` | 清空对话但保留代码改动 | **长任务必备**——上下文过长时重置，保留已有代码成果 |
| `/compact` | 将上下文压缩为摘要 | 比 `/clear` 更温和，保留关键信息同时节省 Token |
| `/rewind` / `Esc+Esc` | 撤销最近的代码修改 | 回退不满意的改动 |
| `/init` | 新项目一键生成 CLAUDE.md | 初始化项目规范文件 |
| `/memory` | 编辑长期记忆 | 存储项目的"祖传规范"，跨会话持久化 |
| `/add-dir` | 将其他目录加入上下文 | **Monorepo 场景**神器 |
| `/context` | 可视化查看 Token 占用 | 彩色格子一目了然，监控上下文大小 |
| `/model` | 切换模型 | 复杂任务用 Opus，简单任务用 Sonnet 节省成本 |
| `/cost` | 查看当前会话账单 | 长对话必看，避免超额 |
| `/usage` | 检查速率限制和剩余额度 | 配额管理 |

> **血泪教训**：长任务做到一半记得定期 `/compact`，别等上下文爆了才后悔。

### 1.2 Plan Mode —— 先思考，后行动

Plan Mode（规划模式）是 Claude Code 的**只读模式**，让 AI 在不修改任何代码的情况下先分析问题、制定详细计划，等待批准后再执行。创始人 Boris Cherny 也强调这是"唯一必学的功能"。

**进入方式：**

| 方式 | 操作 | 适用场景 |
|------|------|---------|
| 快捷键 | `Shift + Tab` 按两次，看到 `⏸ plan mode on` | 最常用，随时切换 |
| 命令行 | `claude --permission-mode plan` | 启动时直接进入 |
| 单次查询 | `claude --permission-mode plan -p "你的问题"` | 只问不聊，快速分析 |

**最佳工作流（来自社区实践）：**

1. 进入 Plan Mode，让 Claude 分析需求并输出计划
2. 选择 **"Type here to tell Claude what to change"**（选项 4），让 Claude 先把计划保存到 `plan.md`
3. 审查计划，调整后再选择 **"Yes, auto-accept edits"**（选项 2）执行
4. 一旦发现进展跑偏（go sideways），**立刻切回 Plan Mode 重新规划**，不要硬推

**三大高频场景：**
- **接手新项目** —— 让 Claude 出架构图 + 入口分析，比手动啃代码快得多
- **大型功能开发** —— 先规划模块拆分和接口设计，后期返工少一半
- **重构/优化** —— 先分析现有代码问题，确认方案再执行

### 1.3 高级 Prompt 技巧

来自 Claude Code 团队内部的使用心得：

🧪 **角色反转** —— 让 Claude 考你：
> "针对这些改动向我提问，在我通过你的测试之前不要提交 PR"

🔍 **要求自证**：
> "证明这套方案行得通，对比 main 分支和 feature 分支的差异"

💡 **推倒重来**：
> "基于你现在掌握的信息，推翻刚才的方案，换一个更优雅的实现"

📝 **先写 Spec 再动手**：
交付任务前先让 Claude 写详细规格说明。需求写得越具体，输出越靠谱。模糊的需求 = 模糊的代码。

### 1.4 Hooks（钩子系统）

Hooks 是 Claude Code 工作流生命周期中的深度集成能力，允许在各阶段注入自定义逻辑。掘金用户 GeraldChen 在 4 个月实战后表示"Hooks 从根本上改变了自己的工作流"。典型用法包括：

- 代码提交前自动运行 lint
- 文件修改后自动触发测试
- 会话结束时生成变更摘要

### 1.5 Routines（定时任务）

2026 年 4 月 Anthropic 正式发布 Routines 功能，Claude Code 可基于以下触发器自动执行任务：

- **定时触发**：类 cron 的周期任务
- **API 触发**：外部服务调用
- **GitHub 触发**：PR 创建、Issue 登记等事件驱动

中国媒体将其称为"云端员工"，标志着 Claude Code 从交互式工具进化为 24/7 自律型开发智能体。

---

## 二、Skills 系统与自定义

### 2.1 什么是 Skill

Skill 是 Claude Code 中**封装了特定领域知识、最佳实践和工具组合的"技能包"**。类比人类的职业资格证书——一个医生有"看病技能"，一个程序员有"写代码技能"。

一个 Skill 通常包含：
- 领域专用的提示词模板
- 一组相关的工具函数
- 特定的工作流逻辑

**Skill 与 Function Call 的区别：**

| 维度 | Function Call | Skill |
|------|--------------|-------|
| 本质 | 单一能力 | 能力集合 + 领域知识 |
| 粒度 | 原子操作 | 业务模块 |
| 是否包含知识 | 不包含 | 包含领域知识和最佳实践 |
| 类比 | 单个螺丝刀 | 电工工具箱 + 电工手册 |
| 关系 | 底层能力 | `Function Call + 领域知识 + 最佳实践 = Skill` |

### 2.2 社区实战：32 个 Skills + 8 个 MCP

掘金一篇题为"别再裸用 Claude Code 了！32 个亲测Skills + 8 个 MCP，开发效率直接拉满！"的文章获得了 463 赞和 1152 收藏，是掘金 AI 开发工具类文章中罕见的爆款。

这反映了中国开发者社区的一个趋势：Claude Code 正在从"开箱即用"的简单工具，演变为需要**深度配置和定制**的开发者平台。

### 2.3 如何编写自己的 Skill

编写 Skill 的核心原则：
1. **写一次，永久生效**——将常用工作流固化为 Skill
2. **领域专精**——每个 Skill 聚焦一个明确的职责范围
3. **最小知识集**——只加载完成任务所需的最小上下文，提高精度和安全性
4. **组合复用**——好的 Skill 可以跨项目复用，就像代码库中的工具包

### 2.4 MCP（Model Context Protocol）

MCP 是 Anthropic 提出的标准化工具调用协议，让 AI 模型可以像 USB 设备一样动态发现和调用工具。

- **MCP 解决"怎么连"**——标准化工具调用协议
- **Skill 解决"连什么"**——封装专业知识和工具集合

典型架构：Agent 通过 MCP 调用各种 Skill 暴露的工具，底层工具变化时 Agent 无需修改代码，只需通过 MCP 动态发现。

---

## 三、Subagent 与 Agent Teams 架构

Claude Code 支持三种不同的多代理模式，每种模式有独立的使用场景和资源特性。

### 3.1 普通 Subagent（独立上下文）

普通 Subagent 运行在**独立上下文窗口**中，拥有自己的系统提示、工具访问权限和权限设置。

```bash
# 创建特定类型的 Subagent
claude subagent create --type code-reviewer --name "代码审查员"

# 给 Subagent 分配任务
claude subagent run --name "代码审查员" --task "检查src目录下所有Python文件的代码规范"
```

**工作原理：**
1. **创建阶段**：主 Agent 调用 `create_subagent` API，传入系统提示和工具配置
2. **执行阶段**：Subagent 在独立沙箱环境中运行，拥有自己的上下文窗口
3. **结果返回**：执行完毕后将**结果摘要**返回主 Agent
4. **上下文隔离**：完整对话历史不会污染主对话

**使用场景：**
- 代码审查
- 测试生成
- 文档编写
- 大规模数据处理（避免主上下文溢出）

### 3.2 Fork Subagent（继承上下文）

Fork Subagent 是普通 Subagent 的进阶版本，会**继承主对话的完整上下文**，包括对话历史、代码改动和项目理解。

```bash
# Fork 一个 Subagent，继承当前所有上下文
claude subagent fork --name "调试助手" --task "帮我调试这个内存泄漏问题"
```

**Fork vs 普通 Subagent：**

| 特性 | 普通 Subagent | Fork Subagent |
|------|-------------|---------------|
| 上下文 | 独立的空白上下文 | 继承主对话的完整上下文 |
| 文件访问 | 受限 | 完整访问权限 |
| 工具集 | 可自定义 | 继承主对话工具集 |
| 适用场景 | 独立任务 | 需要上下文延续的任务 |
| 资源消耗 | 较低 | 较高（需要复制上下文） |

**使用场景：**
- 多路径探索：同时尝试多种解决方案
- 分支开发：在主开发流之外处理实验性功能
- 并行调试：同时调试多个问题

### 3.3 Agent Teams（团队协作）

Agent Teams 将"一个全能选手"变成"一个项目经理 + 多个专业工程师"，实现真正的多 Agent 协作。

```bash
# 创建多 Agent 团队
claude teams create --name "重构团队"

# 添加团队成员
claude teams add-member --team "重构团队" --type code-reviewer --name "审查员"
claude teams add-member --team "重构团队" --type refactoring-specialist --name "重构专家"
claude teams add-member --team "重构团队" --type test-engineer --name "测试工程师"

# 分配任务
claude teams assign-task --team "重构团队" --task "重构用户认证模块"
```

**团队工作流程：**
1. 主 Agent 创建团队，包含多个专业 Subagent
2. 复杂任务被分解为子任务，分配给不同成员
3. 所有团队成员**并行执行**
4. 团队协调器收集并整合结果
5. 当多个 Agent 修改同一文件时，协调器负责冲突解决

### 3.4 三种模式选择指南

| 场景 | 推荐模式 | 原因 |
|------|---------|------|
| 简单独立任务 | 普通 Subagent | 轻量，上下文隔离 |
| 需要上下文的复杂任务 | Fork Subagent | 继承完整项目理解 |
| 多步骤并行任务 | Agent Teams | 多 Agent 协作，效率高 |
| 代码审查 | 普通 Subagent | 专注单一任务 |
| 重构大型项目 | Agent Teams | 需要多专业协作 |
| 调试复杂问题 | Fork Subagent | 需要完整上下文 |

### 3.5 技术实现细节

从源码层面分析，Claude Code 的多代理架构具有以下技术特性：

- **Async Generator**：Subagent 以 `async function*` 实现，可通过 `for await...of` 实时监控进度
- **AsyncLocalStorage 隔离**：每个 Subagent 拥有独立的 agentId、Todo 列表和工具权限
- **字节级 Prompt 缓存**：Fork Subagent 通过字节级复制系统提示，避免重建成本，缓存效率剧增
- **omitClaudeMd 设计**：Explore/Plan 等只读 Agent 省略 CLAUDE.md，每次 spawn 节省 5-15 Gtok
- **permissionMode: 'bubble'**：权限要求向上传播到父 Agent

**Agent 定义的 6 层优先级体系：**
```
built-in → plugin → userSettings → projectSettings → flagSettings → policySettings
```
policySettings（托管 Agent）拥有最高优先级，可覆盖所有自定义 Agent。

### 3.6 最佳实践

1. **从小开始**：先用普通 Subagent，不够用时再升级到 Fork 或 Teams
2. **合理分工**：为每个 Subagent/Team 定义清晰的职责范围
3. **监控资源**：Agent Teams 消耗较多 Token，注意监控
4. **设置超时**：为长时间运行的 Subagent 设置合理的超时
5. **定期清理**：完成任务后及时释放不再需要的 Subagent

---

## 四、Token 成本管理

### 4.1 官方成本控制

Claude Code 提供 `/cost` 和 `/usage` 命令来监控当前会话的 Token 消耗。但社区反馈这些工具**只能看当前会话，没有项目维度的聚合**。

### 4.2 社区方案：cc-monitor

V2EX 用户开发了 **cc-monitor**——一个 Claude Code 实时 Token 消耗监控器，解决了官方工具的不足：

**核心功能：**
- **按项目聚合**：同时监控多个项目的 Token 消耗和费用
- **实时 TUI**：终端界面每 2 秒刷新，操作记录自动轮播
- **双数据源**：JSONL 日志（精确）+ PostToolUse Hook（实时时序）
- **费用估算**：按 Sonnet / Opus / Haiku 模型定价自动计算
- **Compact 检测**：自动识别上下文压缩，显示节省了多少 Token

**安装使用：**
```bash
git clone https://github.com/SagesAi/claude-cost-monitor.git
cd claude-cost-monitor
python -m pip install -e .
cc-monitor-install    # 一键安装 hook
cc-monitor &          # 后台启动
cc-monitor-tui        # 启动终端 UI
```

### 4.3 省钱策略

1. **模型分级使用**：写注释、格式化等简单活切 Sonnet 或 Haiku，别用 Opus 烧钱
2. **定期 /compact**：防止上下文无限膨胀
3. **合理使用 Subagent**：大规模数据处理时使用独立 Subagent 避免主上下文溢出
4. **Fork Subagent 的缓存优势**：字节级相同的前缀消息使 Prompt Cache 效率显著提升

### 4.4  Anthropic 定价变动与影响

2026 年 Anthropic 对 Enterprise 定价做了重大调整：

- **从 $200/月固定费用** → **$20 基础费 + 按使用量计费**
- 部分团队支出**翻了 3 倍**
- 原因：模型推理成本同比增长 3 倍
- 同时对 OpenClaw 等高消耗 Agent 工具开始了调用限制

### 4.5 阿里云 CodingPlan 替代方案

阿里云推出了 CodingPlan 服务，整合 Qwen-3.5、Kimi-K2.5 和 GLM-4.7 等国内模型，采用**按请求次数计费**而非按 Token 计费，解决了传统 Token 计费的高成本问题。这为国内开发者提供了一条"算力自由"的路径。

---

## 五、安全沙箱分析

### 5.1 Claude Code 的沙箱机制

Claude Code 的 Subagent 运行在**独立沙箱环境**中：

- 每个 Subagent 拥有独立的上下文窗口和权限集
- 主 Agent 仅接收 Subagent 的**结果摘要**，完整对话历史不污染主上下文
- Fork Subagent 虽然继承上下文，但仍在隔离环境中执行
- Agent Teams 的团队成员之间通过 mailbox 通信，权限独立同步

### 5.2 Prompt Injection 风险

2026 年 4 月 LangChain-core 发布紧急安全补丁 **CVE-2026-4539**：

- **漏洞根源**：`PromptTemplate.str.format_map` 导致用户输入被二次模板解析
- **影响范围**：所有使用 LangChain 的 Agent 都可能遭受 Prompt Injection 攻击
- **"越狱"风险**：恶意提示词可使 Agent 执行原本被禁止的操作

使用 Claude Code + LangChain 工具链的开发者需要特别注意此安全问题。

### 5.3 安全最佳实践

1. **权限最小化**：为每个 Subagent 分配完成其任务所需的最小权限
2. **Skill 隔离**：不同 Agent 加载不同 Skill，实现权限隔离（前端 Agent 不能调用后端数据库工具）
3. **高风险动作拦截**：对写操作、删除操作等高风险动作设置严格的确认机制
4. **人工兜底**：关键决策点保留人工审核出口
5. **日志追踪**：细化失败链路的日志记录，方便回放和复盘

> 来自 OpenClaw 电商后台实践的教训："AI 系统一旦接入真实业务，最忌讳的就是'所有问题都长得像模型问题'。"——环境复杂度、链路异常、资源超时等非模型问题往往比 Prompt 错误更难定位。

---

## 六、CLI vs IDE 对比

### 6.1 Claude Code（CLI）的优势

- **并行处理能力**：2026 年 Claude Code 重构了内部架构支持并行化，被评价为"可能终结 IDE 时代"
- **1M 上下文窗口**：可将整个代码库作为上下文分析，远超 IDE 插件的能力
- **完整系统访问**：可直接执行命令、操作文件系统、管理 Git
- **Agent 自主性**：从"补全工具"升级为"编程智能体"，可独立完成任务
- **Subagent 生态**：多代理协作能力是 IDE 插件无法实现的

### 6.2 Claude Code 桌面版的问题

36kr 报道了社区对 Claude Code 桌面版的尖锐批评。开发者 Theo 在 1 小时试用中发现了 **40+ 个 Bug**：

- iOS 版键盘频繁冻结、输入框消失
- Windows 版频繁崩溃和冻结
- 聊天窗口闪烁、按钮位置错误
- Routines 无法连接数据库
- 分屏模式下终端显示在错误窗口
- 语音模式下所有输入框同时接收输入

### 6.3 "100% AI 编码"的幻灭

Anthropic 曾多次宣称 Claude Code 是"100% AI 编写"的，但社区审计发现其代码质量堪忧：

| 文件 | 问题 |
|------|------|
| `print.ts` | 单个函数 **3,167 行**，486 个分支判断，嵌套深度 12 层 |
| `QueryEngine.ts` | 46,000 行 |
| `Tool.ts` | 接近 30,000 行 |
| `commands.ts` | 25,000 行 |
| `main.tsx` | 单文件 785KB |
| 情感识别 | 使用正则 `\b(wtf|shit|fuck|horrible|awful|terrible)\b/i` |

> 36kr 评论："AI 只会放大原本的东西。如果原本有工程纪律，会得到更好的结果；如果原本没有纪律，就会以机器的速度放大技术债务。"

### 6.4 IDE vs CLI 适用场景

| 场景 | 推荐工具 | 原因 |
|------|---------|------|
| 快速补全/小修改 | IDE 插件（Copilot、Cursor） | 轻量、即时反馈 |
| 大型重构 | Claude Code CLI | 并行处理、全局上下文 |
| 代码审查 | Claude Code CLI + Subagent | 独立上下文、批量处理 |
| 学习新代码库 | Claude Code CLI（Plan Mode） | 可生成 ASCII 架构图、HTML 演示文稿 |
| 日常开发 | Cursor（60%）+ Claude Code（40%）| 社区主流搭配 |

> **V2EX 开发者反馈**："没有编辑器，CLI 纯聊天写代码的方式有点儿难适应。看不到代码，心里感觉虚得很。提供上下文给 AI 时，没办法精确关联到文件第几行。"——这反映了部分开发者对 CLI 模式的适应门槛。

---

## 七、与其他工具对比

### 7.1 Kimi K2.5

**背景**：月之暗面（Moonshot）开发的国产大模型，在 OpenRouter 周排行榜和 OpenClaw 调用请求量榜单上长期**霸榜第一**，大幅领先 Gemini 3。

**为什么选择 Kimi K2.5 替代 Claude：**
- 避免 Anthropic 身份认证问题（中国大陆用户访问受限）
- 国内 API 访问稳定，无超时烦恼
- 性价比高，按请求计费更可控
- 日常开发效率不输 Claude 官方模型

**接入方式：**
```bash
export ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
export ANTHROPIC_AUTH_TOKEN=你的API_KEY
export ANTHROPIC_MODEL=kimi-k2.5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=kimi-k2.5
export ANTHROPIC_DEFAULT_SONNET_MODEL=kimi-k2.5
export ANTHROPIC_DEFAULT_OPUS_MODEL=kimi-k2.5
```

**社区评价**："Claude Code 换成了 Kimi K2.5 后，我再也回不去了"——掘金文章获得 225 赞，反映了相当一部分中国开发者已经完成了模型迁移。

### 7.2 OpenClaw

**OpenClaw** 是一个新兴的 Agent 工具链/平台，与 Claude Code 在多个维度形成对比：

| 维度 | Claude Code | OpenClaw |
|------|-------------|----------|
| 定位 | 编码智能体 | 通用 Agent 工具链 |
| 商业模式 | 按 Token 计费 | 按请求/订阅计费 |
| 调用限制 | 已开始对高消耗 Agent 限制调用 | 更灵活的调用策略 |
| 生态系统 | Skills + MCP 成熟生态 | 正在建设中 |
| 中国可用性 | 受身份认证影响 | 无此限制 |

**OpenClaw 电商后台实践教训**（来自掘金 Jooolin）：
- "半对半错"比"完全不会"更危险——AI 在复杂业务系统中给出部分正确的答案极具误导性
- 真正有价值的不一定是"无所不能"的 Agent，而是知道**自己什么时候该停、什么时候该交还人工**的 Agent
- 工程化问题（环境、链路、资源、成本）比 Agent 逻辑更难解决
- 按量计费模式下，试错成本会迅速累积

### 7.3 GLM-4.7（智谱）

GLM-4.7 是智谱 AI 开发的国产大模型，也可通过兼容接口接入 Claude Code：

```bash
export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
export ANTHROPIC_AUTH_TOKEN=你的API_KEY
export ANTHROPIC_MODEL=GLM-4.7
export ANTHROPIC_DEFAULT_HAIKU_MODEL=GLM-4.7
export ANTHROPIC_DEFAULT_SONNET_MODEL=GLM-4.7
export ANTHROPIC_DEFAULT_OPUS_MODEL=GLM-4.7
```

配合 [claude-code-router](https://github.com/musistudio/claude-code-router) 工具可实现一条命令快速切换模型：
```bash
ccr use kimi    # 切换到 Kimi
ccr use glm     # 切换到 GLM
ccr use claude  # 切回 Claude 官方
```

### 7.4 Cursor

Cursor 是 IDE 集成型 AI 编码工具的标杆。社区普遍的工作流是 **Cursor（60%）+ Claude Code（40%）**：

- Cursor 适合日常编码、即时补全、小范围修改
- Claude Code 适合大型任务、代码审查、并行处理、全局重构
- 两者互补而非替代

### 7.5 模型性价比总览（2026年4月）

V2EX 社区讨论的模型选择现状：

| 模型/方案 | 优势 | 劣势 | 适用场景 |
|-----------|------|------|---------|
| Claude Sonnet 4.6 | 平衡性好 | Token 成本高 | 中等复杂度任务 |
| Claude Opus 4.6 | 最强推理 | 最贵，响应慢 | 复杂架构/重构 |
| Kimi K2.5 | 性价比高，国内稳定 | 某些场景略逊于 Opus | 日常开发主力 |
| GLM-4.7 | 国产可用，价格合理 | 生态不如 Claude | 国内合规场景 |
| GPT-5.4 | OpenAI 生态 | 订阅受限 | Codex 用户 |
| Qwen-3.5 | 阿里云 CodingPlan 按次计费 | 需要接入配置 | 成本敏感项目 |

> **省钱原则**："写注释、格式化这种简单活，切 Sonnet 或 Haiku 就够了，别用 Opus 烧钱。"

---

## 附录：概念速查

| 概念 | 一句话定义 | 核心作用 |
|------|-----------|---------|
| **Prompt** | 给 AI 的指令 | 告诉 AI 要做什么 |
| **Function Call** | 让 AI 能调用外部工具 | 赋予 AI 行动能力 |
| **Agent** | 能自主决策的智能系统 | 完成复杂任务的闭环 |
| **Skill** | 封装专业知识的技能包 | 固化领域知识和最佳实践 |
| **MCP** | 统一工具调用的标准协议 | 让所有 AI 用同一接口 |
| **Subagent** | 独立上下文窗口的专用 AI 助手 | 并行任务处理，避免上下文污染 |
| **Fork Subagent** | 继承主对话上下文的 Subagent | 需要完整项目理解的并行任务 |
| **Agent Teams** | 多 Agent 协作机制 | 复杂并行任务的团队化处理 |
| **Plan Mode** | 只读规划模式 | 先思考后行动，减少返工 |
| **Hooks** | 生命周期钩子 | 工作流深度定制 |
| **Routines** | 定时/事件触发任务 | 24/7 自律型开发智能体 |

---

## 参考来源

| 来源 | 文章 | 类型 | 层级 |
|------|------|------|------|
| 掘金（宅小年） | Claude Code 换成了 Kimi K2.5 后，我再也回不去了 | 技术博客 | T2 |
| 掘金（唐旺仔） | 手撕 Claude Code-5：Subagent 与 Agent Teams | 技术博客 | T2 |
| 掘金（sakana） | 如何写一个自己的 skill | 技术博客 | T2 |
| 掘金（蝎子莱莱） | 别再裸用 Claude Code 了！32 个亲测 Skills + 8 个 MCP | 技术博客 | T2 |
| 掘金 | Prompt/Agent/Function Call/Skill/MCP 概念梳理 | 技术博客 | T2 |
| 掘金（Jooolin） | 把 OpenClaw 接进电商后台之后，我对 AI 落地这件事的理解变了 | 技术博客 | T2 |
| 掘金 | Claude Code 重构，并行化或终结 IDE 时代 | 技术博客 | T2 |
| 掘金 | Claude Code 源码深度解析 - 前言 | 技术博客 | T2 |
| 36kr（极客邦） | Claude Code 桌面版烂爆了，Anthropic 终于把 "100% AI 编码"演砸了 | 新闻 | T1 |
| 36kr（量子位） | Claude 降智实锤了，还变相涨价，Opus 跌下神坛 | 新闻 | T1 |
| V2EX（SIFT2009） | 写了一个 Claude Code 实时 token 消耗监控器，按项目聚合 | 论坛 | T1 |
| V2EX（jedeft） | 没有编辑器，CLI 纯聊天写代码的方式有点儿难适应 | 论坛 | T1 |
| V2EX（fan88） | 现在到底是什么模型强？性价比高？ | 论坛 | T1 |
| 掘金（AI袋鼠帝） | 阿里出手了！终于不怕 OpenClaw 烧 token 啦，直接算力自由 | 技术博客 | T2 |
