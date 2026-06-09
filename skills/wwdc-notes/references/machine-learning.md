# Machine Learning & AI

## 领域判断

Core ML、Core AI、MLX、Foundation Models、端侧推理、模型优化与 Apple Intelligence。本领域覆盖 112 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **App Intents**：Apple 终于把大模型 API 开放给云端了，而且小开发者能免费使用 Private Cloud Compute (私有云计算) 额度，这是今年最实在的福利。；Apple 终于向现实低头，Foundation Models 框架原生支持了云端大模型路由，还倒贴钱给中小开发者用 Private Cloud Compute。；这场 Session 最值得关注的一件事是：Apple 终于给 Siri 做了独立 App 并支持对话历史，这标志着 Siri 从“系统级语音助手”正式向“独立对话 AI 产品”转型。不过别被骗了，这根本不是一个技术 Session，而是一个时长 0 秒、充满电影旁白和音效的纯营销 Hype Video（宣传视频）。 来源：[WWDC26-102]、[WWDC26-112]、[WWDC26-121]、[WWDC26-240]
- **Apple Intelligence**：Apple 终于把大模型 API 开放给云端了，而且小开发者能免费使用 Private Cloud Compute (私有云计算) 额度，这是今年最实在的福利。；Apple 终于向现实低头，Foundation Models 框架原生支持了云端大模型路由，还倒贴钱给中小开发者用 Private Cloud Compute。；这场 Session 最值得关注的一件事是：Siri 终于长出了“眼睛”，通过 .appEntityIdentifier 视图修饰符，Siri 现在能直接理解屏幕上的 UI 元素并执行跨 App 操作，这彻底改变了人机交互的范式。 来源：[WWDC26-102]、[WWDC26-112]、[WWDC26-240]、[WWDC26-246]
- **Foundation Models**：Apple 终于把大模型 API 开放给云端了，而且小开发者能免费使用 Private Cloud Compute (私有云计算) 额度，这是今年最实在的福利。；Apple 终于向现实低头，Foundation Models 框架原生支持了云端大模型路由，还倒贴钱给中小开发者用 Private Cloud Compute。；这场 Session 最值得关注的一件事是 Xcode 27 彻底拥抱 Agentic Coding（智能体编程），AI 终于从“代码补全器”进化成了能直接操作 Device Hub（设备中心）跑 UI 自动化测试的“初级工程师”。 来源：[WWDC26-102]、[WWDC26-112]、[WWDC26-122]、[WWDC26-237]
- **机器学习**：App Intents 已经从"可选的 Shortcuts 集成"变成了 Apple Intelligence 时代 app 的必修课——如果你还没接入，现在是认真考虑的时候了。；如果你想给 app 加端侧 AI 功能但不知道从哪里开始，这场 Session 是手把手级别的教程——从 prompt 工程到 tool calling 到流式输出到性能优化，完整走了一遍构建旅行规划 app 的全过程。；Shortcuts 今年最大的变化是 Use Model action——用户可以在快捷指令中直接调用 Apple Intelligence 模型，而你的 App Entity 会被序列化成 JSON 传给模型推理。这意味着你的实体定义不仅决定了 UI 展示，还决定了模型能"看到"什么信息。 来源：[WWDC25-244]、[WWDC25-259]、[WWDC25-260]、[WWDC25-272]
- **AppIntents**：Apple 终于把大模型 API 开放给云端了，而且小开发者能免费使用 Private Cloud Compute (私有云计算) 额度，这是今年最实在的福利。；Apple 终于向现实低头，Foundation Models 框架原生支持了云端大模型路由，还倒贴钱给中小开发者用 Private Cloud Compute。；这场 Session 最值得关注的一件事是：Apple 终于给 Siri 做了独立 App 并支持对话历史，这标志着 Siri 从“系统级语音助手”正式向“独立对话 AI 产品”转型。不过别被骗了，这根本不是一个技术 Session，而是一个时长 0 秒、充满电影旁白和音效的纯营销 Hype Video（宣传视频）。 来源：[WWDC26-102]、[WWDC26-112]、[WWDC26-121]、[WWDC26-295]
- **CoreML**：这场 Session 最值得关注的一件事是：Apple 终于把 Core ML 模型塞进了 RAW 解码管线（Pipeline），用神经网络接管了去马赛克（Demosaic）和降噪（Denoise），这意味着第三方修图 App 终于能拿到和系统相册一样“作弊”级别的 RAW 解析画质了。；从找到开源模型到实机运行——这场 Session 是一份完整的端到端 ML 应用开发流程演示，特别适合第一次把 ML 模型集成到 iOS 应用的开发者。；Core ML 模型的性能调优不只是换小模型——compute unit 选择、模型量化（Quantization）和批量预测优化这三个维度同时调才能榨干最后一滴性能。 来源：[WWDC26-305]、[WWDC22-10017]、[WWDC21-10038]、[WWDC21-10039]
- **AppIntent**：App Intents 已经从"可选的 Shortcuts 集成"变成了 Apple Intelligence 时代 app 的必修课——如果你还没接入，现在是认真考虑的时候了。；App Intents 终于从"系统替你展示一个静态结果"进化到了"用户可以直接在 Snippet 里交互"——按钮、Toggle、多选项、撤销手势全部打通，而且 App Intent 的代码可以完全不做修改就用在 Snippet 里。；Snippet 从"系统替你弹一个结果卡片"变成了"你的 App 可以在系统层做轻量级交互"——按钮、数据更新、确认流程全支持。设计指南的核心矛盾是：既要信息密度够高，又要一眼就能扫完。 来源：[WWDC25-244]、[WWDC25-275]、[WWDC25-281]、[WWDC24-101]

## API 演进时间线

- **WWDC26**：37 场，代表来源：[WWDC26-102]、[WWDC26-112]、[WWDC26-121]、[WWDC26-122]、[WWDC26-204]
- **WWDC25**：26 场，代表来源：[WWDC25-101]、[WWDC25-102]、[WWDC25-111]、[WWDC25-112]、[WWDC25-204]
- **WWDC24**：13 场，代表来源：[WWDC24-10075]、[WWDC24-101]、[WWDC24-10159]、[WWDC24-10160]、[WWDC24-10161]
- **WWDC23**：8 场，代表来源：[WWDC23-10042]、[WWDC23-10044]、[WWDC23-10047]、[WWDC23-10049]、[WWDC23-10050]
- **WWDC22**：8 场，代表来源：[WWDC22-10017]、[WWDC22-10019]、[WWDC22-10020]、[WWDC22-10027]、[WWDC22-10063]
- **WWDC21**：9 场，代表来源：[WWDC21-10036]、[WWDC21-10037]、[WWDC21-10038]、[WWDC21-10039]、[WWDC21-10040]
- **WWDC20**：11 场，代表来源：[WWDC20-10043]、[WWDC20-10099]、[WWDC20-10152]、[WWDC20-10153]、[WWDC20-10156]

## 决策启发式

- 已有项目的迁移策略 ：立刻审查你现有的 App Intents。Siri 变成独立 App 后，用户会在一个沉浸式界面里和你的 App 交互。如果你的 Intent 返回的只是简单的文本或基础 Snippet（代码片段），体验会非常割裂。赶紧用 AppEntity 和自定义的 IntentView 把 UI 丰富起来。
- 新项目的采用建议 ：把 Siri 当作一个真正的 Agent（智能体）来设计。不要只暴露“打开某个页面”的 Intent，要暴露“查询状态”、“执行多步操作”的细粒度 Intent，让 Siri 能够自己组合调用。
- 实战中容易踩的坑 ：不要假设 Siri 的上下文是永久的。系统会因为内存压力随时清理对话历史，你的 App 必须自己维护关键状态，不能依赖 Siri 帮你记住上一步操作。
- Xcode 27 迁移与 CI 调整 ：Xcode 27 是 Apple Silicon only（仅限苹果芯片）。如果你的 CI/CD 机器还是 Intel 的 Mac mini，赶紧换掉。同时 Device Hub 取代了传统的 Simulator，自动化测试脚本里的 xcrun simctl 命令需要全面排查和更新。
- 把 Accessibility 当作 AI 的基石 ：既然 Xcode Agent 和 Siri 都通过 View Annotations API 和 a11y 标签来理解你的 App，现在写 UI 必须把无障碍标签写全。这不只是为了视障用户，更是为了让 AI 能正确操作你的界面。
- 端云模型路由的降级策略 ：使用 Foundation Models 时，务必为云端模型调用加上超时和重试机制。端侧处理失败 fallback 到云端时，记得在 UI 上给用户明确的 loading 状态。
- 已有项目的迁移策略 ：如果你的 macOS 应用目前依赖云端 LLM API 做文本处理或代码补全，现在可以无缝切换到本地。只需在代码里把 baseURL 替换为 http://127.0.0.1:8080/v1，并在应用首次启动时引导用户通过 pip 或内嵌 Python 环境拉起 mlx lm.server。这能帮你省下巨额的 API 账单，同时彻底解决隐私合规问题。
- 新项目的采用建议 ：做本地 IDE 插件或开发者工具时，直接基于 MLX LM Server 构建。不要自己去写 Metal 渲染或 Core ML 转换，MLX 生态已经处理了量化、KV Cache 管理和 Continuous batching (连续批处理)。把精力放在设计更好的 Agent Prompt 和工具链上。
- 实战中容易踩的坑 ：Agent 循环会产生极长的上下文。如果你发现本地 Agent 越跑越慢，甚至 OOM (内存溢出)，不要盲目换大模型。去检查你的 Agent 框架有没有做上下文截断或摘要，并在启动 mlx lm.server 时合理设置 max tokens 和上下文窗口限制。
- 已有项目的迁移 ：如果你之前用单台 Mac 跑 mlx lm.lora 微调，现在只需要把 batch size 乘以机器数量，然后用 mlx.launch 包装你的启动命令。代码一行不用改，MLX 会自动处理梯度的 All Reduce 和平均。

## 反模式与坑

- Agentic coding (智能体编程) ：Xcode 里的 AI 助手现在能自己跑测试和修 Bug 了，写样板代码的效率大幅提升。
- Flexible UI layout (灵活 UI 布局) ：SwiftUI 新增了更细粒度的布局控制 API，终于不用为了一个奇葩的 UI 需求去桥接 UIKit 了。
- Liquid Glass 设计语言 ：去年的设计主题今年继续深化，系统控件的毛玻璃质感和光影效果有了更多可定制的参数。
- Liquid Glass 设计语言 ：UI 层面引入了类似 visionOS 的玻璃材质渲染，SwiftUI 新增了 .glassBackground() 修饰符，做毛玻璃效果终于不用自己手搓 Shader 了。
- Agentic Coding 增强 ：Xcode 里的 AI 代码补全现在能理解整个 Workspace 的上下文，甚至能帮你自动写 XCTest 单元测试，省去了写 boilerplate 的时间。
- SwiftUI 布局灵活性 ：新增了 AdaptiveStack，能优雅地处理 iPad 和 iPhone 之间横竖屏切换时的复杂嵌套布局，不用再写一堆 if horizontalSizeClass == .regular 了。
- Safari Notify Me ：Safari 终于原生支持网页状态变更通知，不用自己写 Push Notification（推送通知）后端了。
- 密码一键修复 ：系统级的 compromised passwords（泄露密码）自动更新，开发者需要确保自己的账号设置页面支持 AutoFill（自动填充）的密码更新流程。

## 高频主题

`机器学习` (17)、`Foundation Models` (14)、`Apple Intelligence` (10)、`App Intents` (10)、`基础` (7)、`Private Cloud Compute` (6)、`Core AI` (5)、`Siri` (5)、`SwiftUI` (4)、`Swift` (4)、`MLX` (3)、`Agent` (3)、`Evaluations` (3)、`LLM` (3)、`Metal 4` (3)、`MetalFX` (3)、`iOS 27` (2)、`Agentic Coding` (2)

## 关键 Session

- [WWDC26-102] Platforms State of the Union：Apple 终于把大模型 API 开放给云端了，而且小开发者能免费使用 Private Cloud Compute (私有云计算) 额度，这是今年最实在的福利。
- [WWDC26-112] Platforms State of the Union (ASL)：Apple 终于向现实低头，Foundation Models 框架原生支持了云端大模型路由，还倒贴钱给中小开发者用 Private Cloud Compute。
- [WWDC26-121] Announcing Apple’s next big step for Siri and iPhone：这场 Session 最值得关注的一件事是：Apple 终于给 Siri 做了独立 App 并支持对话历史，这标志着 Siri 从“系统级语音助手”正式向“独立对话 AI 产品”转型。不过别被骗了，这根本不是一个技术 Session，而是一个时长 0 秒、充满电影旁白和音效的纯营销 Hype Video（宣传视频）。
- [WWDC26-122] WWDC26 Platforms State of the Union 精彩回顾：这场 Session 最值得关注的一件事是 Xcode 27 彻底拥抱 Agentic Coding（智能体编程），AI 终于从“代码补全器”进化成了能直接操作 Device Hub（设备中心）跑 UI 自动化测试的“初级工程师”。
- [WWDC26-204] 面向 Safari 浏览器 27 的 WebKit 新功能：Safari 终于原生支持 <select 深度定制和 <model 3D 渲染，Web 开发者不用再捏着鼻子写一堆 div 模拟表单和引入沉重的 Three.js 了。
- [WWDC26-213] 使用 Xcode 中的智能体翻译你的 App：Xcode 终于把 AI 翻译做成了原生工作流，靠 String Catalogs（字符串目录）攒了三年的工程上下文，这次大模型翻译不再是“人工智障”了。
- [WWDC26-215] HTML 模型元素入门：✅ Web 端 3D 展示终于从“引入几十 KB 的 JS 库”变成了“写一个 <model 标签”。
- [WWDC26-232] 使用 MLX 在 Mac 上本地运行 AI 智能体：这场 Session 最值得关注的一件事是：Apple 把 Mac 变成了完全离线、零 API 费用的 Agentic AI (智能体) 运行时，M5 芯片的 Neural Accelerator (神经网络加速器) 让本地处理几十万 Token 的 Prompt 速度直接翻了 4 倍。
- [WWDC26-233] 使用 MLX 探索分布式推理和训练：Mac 终于能名正言顺地当“穷人版” AI 算力集群了，这场 Session 最值得关注的是 Apple 用 Thunderbolt 5 上的 RDMA (Remote Direct Memory Access) 配合全新的 JACCL 通信库，把几台 Mac 物理缝合成了一个低延迟的巨型统一内存池。
- [WWDC26-237] 图像理解方面的新动向：这场 Session 最值得关注的一件事是：Apple 终于把 Vision 框架的“像素级操作”和 Foundation Models 的“语义级理解”通过 Tool Calling 彻底打通了，以后做图像分析不用再在 CV 模型和 LLM 之间手动倒腾数据了。
- [WWDC26-240] 使用 App Schemas 打造智能 Siri 体验：这场 Session 最值得关注的一件事是：Siri 终于长出了“眼睛”，通过 .appEntityIdentifier 视图修饰符，Siri 现在能直接理解屏幕上的 UI 元素并执行跨 App 操作，这彻底改变了人机交互的范式。
- [WWDC26-241] Foundation Models 框架的新功能：这场 Session 最值得关注的一件事是：Foundation Models 终于从“调参玩具”变成了“工程基建”，Dynamic Profiles 让 Agent 状态机原生支持，而 LanguageModel 协议让苹果设备端模型、PCC（Private Cloud Compute，私有云计算）和第三方模型实现了真正的无缝热切换。
- [WWDC26-242] 使用 Foundation Models 框架构建智能体 App 体验：Foundation Models 终于从“套壳对话框”进化到了“真正的多 Agent 编排框架”，DynamicProfile 是今年做 AI App 必须拿下的 API。
- [WWDC26-243] 使用 Instruments 调试和分析智能体 App 体验：这场 Session 最值得关注的一件事是：Foundation Models Instrument 终于把 LLM 智能体（Agentic App）里最让人抓狂的“工具调用死循环”和“静默失败”变成了时间轴上肉眼可见的色块。
- [WWDC26-246] 使用 Core Spotlight 进行 LLM 搜索：✅ Core Spotlight 正式成为 Apple Intelligence 端侧 RAG（检索增强生成）的官方数据库，开发者只需喂数据，不用再手写向量检索和 Prompt 拼装。
- [WWDC26-256] 探索生成式字幕和字幕样式：✅ 视频播放器的脏活累活被 Apple 底层接管了：设备端 AI 字幕生成和实时样式预览现在对标准播放器“零代码”默认生效。
- [WWDC26-295] 使用 AppIntentsTesting 验证你的 App Intents 采用情况：这场 Session 最值得关注的一件事是：Apple 终于把 App Intents（应用意图）的测试从“玄学 UI 自动化”变成了“确定性的跨进程集成测试”，你不再需要对着 Siri 喊破喉咙或者写脆弱的 UI 脚本来验证 Shortcuts（快捷指令）和 Spotlight（聚焦搜索）了。
- [WWDC26-298] 了解 Evaluations 框架：✅ 单元测试在 AI 时代正式破产，Evaluations 框架把“调 Prompt”从玄学变成了可量化的 CI/CD 工程。
