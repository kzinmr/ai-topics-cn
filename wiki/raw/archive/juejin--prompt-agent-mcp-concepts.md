---
title: "Prompt/Agent/Function Call/Skill/MCP概念梳理"
source: "juejin"
url: "https://juejin.cn/post/7614205951297732654"
date: "2026-04-18"
tags: ['prompt', 'agent', 'mcp', 'skill', 'education']
triage: "✅ Take"
scraped: "2026-04-18T09:28:22.156218"
---

# Prompt、Agent、Function Call、Skill、MCP，傻傻分不清楚？

## 前言

最近AI越来越火了。

我发现里面有很多概念有些小伙伴有点分不清楚，比如：Prompt、Agent、Function Call、Skill、MCP等。

今天这篇文章专门跟大家一起聊聊这个话题，希望对你会有所帮助。

## 核心概念关系图

先上干货，这张图让你从整体上理解这五个概念是如何分层递进的：

**一句话概括：**
- **Prompt** 是你跟AI说的"人话"
- **Function Call** 让AI能"动手干活"
- **Agent** 让AI会"思考规划"
- **Skill** 是AI的"职业技能证书"
- **MCP** 是AI世界的"USB接口"

下面我们一层一层拆开揉碎了讲，每层都有Java代码示例。

## 第一层：Prompt——和AI对话的"普通话"

### 1.1 什么是Prompt？

**Prompt（提示词）** 就是你输入给AI的文本指令。

它就像你去餐厅点菜时说的"来一份宫保鸡丁"，AI就是那个服务员，听懂你的话然后给你上菜。

在Java里，调用AI模型的第一步就是构造Prompt。

我用最简单的Spring AI示例来演示：

```java
import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.SystemPrompt;
import org.springframework.ai.chat.prompt.UserPrompt;

@Service
public class AIService {
    
    private final ChatClient chatClient;
    
    public AIService(ChatClient chatClient) {
        this.chatClient = chatClient;
    }
    
    public String askAI(String question) {
        // 构造Prompt：可以包含系统消息和用户消息
        Prompt prompt = new Prompt(
            new SystemPrompt("你是一个Java架构师，擅长用通俗的语言解释技术概念。"),
            new UserPrompt(question)
        );
        
        // 调用AI并返回结果
        return chatClient.call(prompt).getResult().getOutput().getContent();
    }
}
```

这里的 `SystemPrompt` 和 `UserPrompt` 就是最基础的Prompt形式。它们决定了AI的身份和你要问的问题。

### 1.2 Prompt的高级玩法

光有基础Prompt还不够，在实际应用中我们经常需要**提示词工程**来引导AI做出更好的回答。比如：

```java
public String generateJavaCode(String requirement) {
    String promptTemplate = """
        你是一个资深的Java开发工程师。
        请根据以下需求生成Java代码，代码要包含必要的注释，并考虑异常处理：
        
        需求：%s
        
        请输出完整的Java类代码。
        """;
    
    String prompt = String.format(promptTemplate, requirement);
    return chatClient.call(new Prompt(prompt)).getResult().getOutput().getContent();
}
```

**Prompt的本质：**它是人类意图与AI能力之间的"翻译官"。Prompt写得好，AI才能干得好。

## 第二层：Function Calling——让AI从"说话"到"动手"

Prompt只能让AI"说话"，但AI想干点实事（比如查数据库、发邮件、调用第三方API）时，就无能为力了。

**Function Calling（函数调用）** 就是来解决这个问题的。

### 2.1 什么是Function Calling？

Function Calling允许开发者在调用大模型时，注册一系列函数（工具），模型在生成回复时如果判断需要调用外部工具，就会返回一个结构化的请求，由开发者执行真实的函数，再把结果返回给模型生成最终答案。

### 2.2 Java实现Function Calling

我用LangChain4j来演示，因为它对Java开发者很友好。首先定义工具函数：

```java
import dev.langchain4j.agent.tool.Tool;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class WeatherTool {
    
    @Tool("获取指定城市的实时天气")
    public String getWeather(String city) {
        // 这里应该是真实的API调用，为了演示我们模拟数据
        if ("北京".equals(city)) {
            return "北京当前天气：晴，温度25℃，湿度40%";
        } else if ("上海".equals(city)) {
            return "上海当前天气：小雨，温度22℃，湿度80%";
        } else {
            return "抱歉，暂不支持该城市天气查询";
        }
    }
    
    @Tool("获取当前时间")
    public String getCurrentTime() {
        return LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
    }
}
```

然后创建AI服务并绑定工具：

```java
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openai.OpenAiChatModel;
import dev.langchain4j.service.AiServices;

public class WeatherAssistant {
    
    interface Assistant {
        String chat(String userMessage);
    }
    
    public static void main(String[] args) {
        ChatLanguageModel model = OpenAiChatModel.builder()
            .apiKey(System.getenv("OPENAI_API_KEY"))
            .modelName("gpt-4")
            .build();
        
        Assistant assistant = AiServices.builder(Assistant.class)
            .chatLanguageModel(model)
            .tools(new WeatherTool()) // 注册工具
            .build();
        
        // 用户提问
        String response = assistant.chat("北京现在天气怎么样？");
        System.out.println(response);
        
        response = assistant.chat("现在几点了？");
        System.out.println(response);
    }
}
```

当用户问天气时，模型会判断需要调用 `getWeather` 函数，LangChain4j自动处理了函数调用的整个流程，最后把结果整合成自然语言返回。

### 2.3 Function Calling的核心价值

**让AI从"静态知识"变成"动态能力"。** 没有Function Calling，AI只能回答训练数据里的内容；有了它，AI可以实时获取最新信息，甚至可以操作你的系统。

## 第三层：Agent——会思考、会规划的"智能体"

Function Calling让AI能调用工具，但它还是被动的一问一答。

如果遇到复杂任务，比如"帮我规划一次杭州三日游"，需要查天气、查景点、查酒店、算预算……这时候就需要**Agent（智能体）** 出场了。

### 3.1 什么是Agent？

**Agent是一个能够感知环境、做出决策并执行动作的自主系统。** 它不像Function Calling那样只是"单次工具调用"，而是具备完整的"思考-行动-观察"闭环能力。

通俗说，Function Calling是"会用手"，Agent是"有大脑"。

### 3.2 ReAct：Agent的核心决策模式

目前主流Agent都采用 **ReAct（Reasoning + Acting）框架**。

它的工作流程是：
1. **思考（Thought）**：分析当前状态，决定下一步要做什么
2. **行动（Action）**：调用某个工具
3. **观察（Observation）**：获取工具返回的结果
4. **循环**：直到任务完成

### 3.3 Java实现一个简单的ReAct Agent

我们用LangChain4j的 `AiServices` 结合工具来实现Agent。

首先定义多个工具：

```java
import dev.langchain4j.agent.tool.Tool;

public class TravelTools {
    
    @Tool("查询某城市未来一周的天气")
    public String queryWeather(String city) {
        return city + "未来一周天气：前三天晴，后四天多云，气温20-28℃";
    }
    
    @Tool("查询某城市的知名景点")
    public String queryAttractions(String city) {
        if ("杭州".equals(city)) {
            return "杭州知名景点：西湖、灵隐寺、西溪湿地、宋城";
        } else if ("上海".equals(city)) {
            return "上海知名景点：外滩、东方明珠、迪士尼乐园";
        }
        return "暂无该城市景点信息";
    }
    
    @Tool("计算预算")
    public String calculateBudget(String city, int days) {
        int base = 500;
        int total = base * days;
        return city + days + "天游预算约为：" + total + "元（不含大交通）";
    }
}
```

然后创建Agent：

```java
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openai.OpenAiChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.memory.chat.MessageWindowChatMemory;

public class TravelAgent {
    
    interface TravelPlanner {
        String planTrip(String request);
    }
    
    public static void main(String[] args) {
        ChatLanguageModel model = OpenAiChatModel.builder()
            .apiKey(System.getenv("OPENAI_API_KEY"))
            .modelName("gpt-4")
            .build();
        
        TravelPlanner agent = AiServices.builder(TravelPlanner.class)
            .chatLanguageModel(model)
            .tools(new TravelTools())
            .chatMemory(MessageWindowChatMemory.withMaxMessages(20)) // 记忆
            .build();
        
        String result = agent.planTrip("帮我规划一个3天的杭州游，包括天气、景点和预算");
        System.out.println(result);
    }
}
```

这个Agent会自己决定先查天气、再查景点、再算预算，然后把所有信息整合成一份完整的旅行计划。整个过程是自主的，不需要我们写死流程。

### 3.4 Agent与Function Calling的关系

Function Calling是Agent的"手"，Agent是拥有"大脑"的完整系统。Agent通过Function Calling调用工具，但Agent多了"规划"和"记忆"能力，能处理更复杂的任务。

## 第四层：Skill——封装专业知识的"技能包"

当Agent需要处理不同领域的任务时，如果让一个Agent掌握所有知识和工具，会变得臃肿且容易出错。这时候就需要**Skill（技能）** 的概念。

### 4.1 什么是Skill？

Skill是一套封装了特定领域知识、最佳实践和工具组合的"技能包"。它就像我们人类的职业资格证书——一个医生有"看病技能"，一个程序员有"写代码技能"。

Anthropic最早提出Skill概念，一个Skill通常包含：
- 领域专用的提示词模板
- 一组相关的工具函数
- 特定的工作流逻辑

### 4.2 Java中如何组织Skill？

我们可以把Skill定义为一个独立的模块，包含自己的工具类和提示模板。例如，一个"前端开发Skill"：

```java
// 前端技能专属工具
public class FrontendTools {
    @Tool("生成React组件代码")
    public String generateReactComponent(String componentName, String props) {
        // React组件生成逻辑
    }
    @Tool("检查CSS命名规范")
    public String checkCssNaming(String cssCode) {
        // CSS检查逻辑
    }
}

// 前端技能的提示词模板
public class FrontendPrompts {
    public static final String SYSTEM_PROMPT = """
        你是一个资深前端开发工程师，精通React、Vue、CSS等前端技术。
        请严格按照前端最佳实践生成代码，确保代码可维护。
        """;
}
```

### 4.3 Skill与Agent的关系

在大型系统中，我们通常会有多个Agent，每个Agent加载不同的Skill：
- **前端Agent**：加载 ReactSkill、CSSSkill
- **后端Agent**：加载 SpringSkill、DatabaseSkill
- **运维Agent**：加载 K8sSkill、MonitoringSkill

每个Agent只拥有完成自己领域任务所需的最小知识集，既提高了精准度，又保障了安全。

### 4.4 Function Call和Skill有什么区别？

**一句话说清本质：**
- **Function Call** 是一种能力：让AI能够调用外部函数（工具）
- **Skill** 是一个模块：封装了特定领域的知识、最佳实践和一组相关的Function Call

**比喻：**
- Function Call 像锤子、螺丝刀、扳手这些具体工具
- Skill 像木工工具箱：里面有锤子、锯子、尺子，还附带一本《木工操作手册》

**核心区别对比表：**

| 维度 | Function Call | Skill |
|------|--------------|-------|
| 本质 | 单一能力 | 能力集合 + 知识 |
| 粒度 | 原子操作 | 业务模块 |
| 是否包含工具 | 本身就是工具 | 包含多个工具 |
| 是否包含知识 | 不包含 | 包含领域知识和最佳实践 |
| 类比 | 单个螺丝刀 | 电工工具箱 + 电工手册 |
| 应用场景 | 查天气、发邮件等单次操作 | 前端开发、运维管理、财务分析等专业领域 |
| 代码形式 | 单个 @Tool 方法 | 多个 @Tool 方法 + 系统提示词 |

**为什么需要区分这两个概念？**
1. **设计层面的解耦**：Function Call是底层能力，Skill是业务封装。底层能力稳定，上层业务可以灵活组合。
2. **复用性**：好的Skill可以跨项目复用，就像代码库里的工具包。
3. **安全性**：可以给不同的Agent分配不同的Skill，实现权限隔离（前端Agent不能调用后端数据库）。

**总结：**
- Function Call：AI的"手"，能干活
- Skill：AI的"职业培训证书"，让AI知道怎么干好某个领域的事
- `Function Call + 领域知识 + 最佳实践 = Skill`

## 第五层：MCP——统一工具调用的"世界语"

随着Agent越来越多，每个Agent都要接入不同的工具，每个AI模型（OpenAI、Claude、文心一言）的Function Calling格式还不一样。这就导致开发者要针对每个模型写一套工具适配代码，非常痛苦。

**MCP（Model Context Protocol，模型上下文协议）** 就是来解决这个问题的。

### 5.1 什么是MCP？

MCP是Anthropic提出的一个标准化协议，它定义了一套统一的接口，让AI模型可以像USB设备一样动态发现和调用工具。

**核心思想：**
- 工具以Server的形式暴露（MCP Server）
- AI应用作为Client（MCP Client）连接Server
- Server提供工具清单和调用接口
- Client统一格式调用，无需关心底层工具具体实现

### 5.2 MCP的工作流程

### 5.3 Java中使用MCP

Spring AI 2.0已经原生支持MCP，可以非常方便地构建MCP客户端和服务器。

定义MCP Server（工具提供方）：

```java
import org.springframework.ai.mcp.server.McpServer;
import org.springframework.ai.mcp.server.McpServerFeatures;
import org.springframework.ai.mcp.server.McpServerRegistrar;
import org.springframework.ai.mcp.spec.McpSchema;

@Component
public class WeatherMcpServer {
    
    @Bean
    public McpServerRegistrar weatherServer() {
        // 定义工具
        McpSchema.Tool weatherTool = new McpSchema.Tool(
            "getWeather",
            "获取城市天气",
            new McpSchema.JsonSchema(Map.of(
                "type", "object",
                "properties", Map.of(
                    "city", Map.of("type", "string", "description", "城市名称")
                ),
                "required", List.of("city")
            ))
        );
        
        // 创建Server
        McpServerFeatures.AsyncServerSpec serverSpec = McpServerFeatures.async()
            .tool(weatherTool, (request) -> {
                String city = request.arguments().get("city").asText();
                // 执行真实逻辑
                String weather = "北京当前天气：晴，25℃";
                return CompletableFuture.completedFuture(
                    new McpSchema.CallToolResult(List.of(
                        new McpSchema.TextContent(weather)
                    ), false)
                );
            });
        
        return McpServerRegistrar.builder()
            .name("weather-server")
            .server(serverSpec)
            .build();
    }
}
```

MCP Client调用：

```java
import org.springframework.ai.mcp.client.McpClient;
import org.springframework.ai.mcp.client.McpClientFeatures;

@Service
public class AIServiceWithMCP {
    
    private final ChatClient chatClient;
    private final McpClient mcpClient;
    
    public AIServiceWithMCP(ChatClient chatClient) {
        this.chatClient = chatClient;
        // 连接到MCP Server
        this.mcpClient = McpClientFeatures.async()
            .connect("weather-server", "http://localhost:8080/mcp");
    }
    
    public String askWeather(String city) {
        // 通过MCP调用工具
        McpSchema.CallToolResult result = mcpClient.callTool("getWeather", 
            Map.of("city", city)).join();
        
        String weather = result.content().get(0).text();
        
        // 也可以让AI自动决定是否调用工具
        Prompt prompt = new Prompt("查询" + city + "天气");
        return chatClient.call(prompt).getResult().getOutput().getContent();
    }
}
```

### 5.4 MCP与Skill的关系

MCP和Skill是互补的：
- **MCP** 解决"怎么连"的问题——标准化工具调用协议
- **Skill** 解决"连什么"的问题——封装专业知识和工具集合

一个典型的架构是：Agent通过MCP调用各种Skill暴露的工具。这样，无论底层工具如何变化，Agent都不需要修改代码，只需要通过MCP动态发现即可。

## 一张表彻底分清五个概念

| 概念 | 一句话定义 | 核心作用 | Java生态代表 |
|------|-----------|---------|-------------|
| Prompt | 给AI的指令 | 告诉AI要做什么 | Spring AI的Prompt类 |
| Function Call | 让AI能调用外部工具 | 赋予AI行动能力 | LangChain4j的 @Tool 注解 |
| Agent | 能自主决策的智能系统 | 完成复杂任务的闭环 | LangChain4j的 AiServices + 记忆 |
| Skill | 封装专业知识的技能包 | 固化领域知识和最佳实践 | 模块化的工具集合+提示模板 |
| MCP | 统一工具调用的标准协议 | 让所有AI用同一套接口 | Spring AI的MCP支持 |

这五个概念构成了AI应用开发的完整分层：
- **Prompt** 是地基，没有它AI听不懂人话
- **Function Call** 是第一层楼，让AI能动手
- **Agent** 是第二层，让AI会思考
- **Skill** 是装修，让AI更专业
- **MCP** 是连接各层的管道，让整个系统灵活可扩展

## 总结

有些小伙伴可能会问："我现在应该先学哪个？"

我的建议是：**从Prompt开始**，这是所有AI应用的基础。理解了Prompt，再逐步接触Function Call，然后尝试搭建简单的Agent。至于Skill和MCP，可以先了解概念，等你的应用复杂到需要多个Agent协作时，再深入学习也不迟。

Prompt、Function Call、Agent、Skill、MCP，正是AI应用开发的"五层楼"，每一层都让我们离业务更近，离底层细节更远。

**开源地址：**
- Spring AI：[github.com/spring-projects/spring-ai](https://github.com/spring-projects/spring-ai)
- LangChain4j：[github.com/langchain4j/langchain4j](https://github.com/langchain4j/langchain4j)
- MCP规范：[github.com/modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification)
