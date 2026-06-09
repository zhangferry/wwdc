# Swift Concurrency

## 领域判断

Swift 语言演进、async/await、Actor、Sendable 与线程安全。本领域覆盖 49 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Task**：如果你已经用了 async/await 但对任务取消、优先级传播和任务组资源管理还有疑问，这场 Session 用汤厨的比喻把这些概念讲清楚了——特别是 withTaskCancellationHandler 在 AsyncSequence 中的用法值得反复看。；CoreLocation 终于有了基于 Swift Concurrency 的定位 API——CLLocationUpdate.liveUpdates() 一行代码就能开始接收定位，配合 AsyncSequence 的全部能力，这是多年来定位 API 最大的使用体验升级。；这场 Session 是 Instruments 卡顿分析的实战教学——从人类感知阈值出发，用灯泡实验解释为什么 100ms 是"即时感"的生死线，然后用三种典型的卡顿模式演示如何在 Instruments 中定位和修复问题。 来源：[WWDC23-10170]、[WWDC23-10180]、[WWDC23-10248]、[WWDC22-110351]
- **Actor**：Distributed Actors 把 Swift 的并发安全模型从单进程扩展到了多进程——Actor 隔离 + 位置透明性，让分布式系统的代码和本地代码一样安全。；Swift 5.5 最大的变化是 async/await 和 Actor 的引入，这是 Swift 并发模型的一次彻底重构，影响范围远超语言本身。；这场 Session 用一个真实的照片浏览 App，手把手演示了从 completion handler 地狱到 async/await 的完整迁移过程——比看十篇博客都管用。 来源：[WWDC22-110356]、[WWDC21-10192]、[WWDC21-10194]、[WWDC21-10254]
- **MainActor**：SwiftUI 的并发模型可以用一句话概括：@MainActor 是编译期默认，Sendable 是后台优化的信号灯。SwiftUI 的注解表达的是运行时语义——View 默认主线程、Shape/visualEffect/Layout 可能后台调用。理解了这一点，你就不需要害怕并发。；如果你的 Swift App 还没开 Swift 6 模式，现在是时候了——编译器会告诉你所有潜在的数据竞争问题，而且迁移过程可以按模块逐步推进。；Core Data 终于正式拥抱 Swift Concurrency——@MainActor 标注的 View Context 和 NSManagedObjectContext 的 perform 方法现在可以用 async/await 写了，不用再嵌套回调地狱。 来源：[WWDC25-266]、[WWDC24-10169]、[WWDC21-10017]、[WWDC21-10192]
- **Sendable**：Swift 6.2 的核心主题是"并发退一步、性能进一步"——默认单线程、按需并发的策略让 data race safety 不再是初学者的噩梦。；如果你的 Swift App 还没开 Swift 6 模式，现在是时候了——编译器会告诉你所有潜在的数据竞争问题，而且迁移过程可以按模块逐步推进。；Doug Gregor 用航海比喻系统性地讲解了 Swift 并发模型如何通过隔离（Isolation）和 Sendable 协议在编译期防止数据竞争——这是理解 Swift 6 严格并发检查的基础。 来源：[WWDC25-245]、[WWDC24-10169]、[WWDC22-110351]、[WWDC21-10133]
- **Developer Tools**：这是一场信息密度极高的全景扫描——Swift 并发、Xcode Cloud、StoreKit 2、SharePlay 四大主题构成了 2021 年 Apple 开发者生态的骨架。；周一就是 Keynote + Platforms State of the Union 的消化日——大方向已经定了，接下来四天都在讲细节。；周二是 Session 密集轰炸的第一天——Xcode Cloud 三连讲、SF Symbols 3、MusicKit 是今天的技术干货。 来源：[WWDC21-102]、[WWDC21-10321]、[WWDC21-10322]
- **开发工具**：Swift 6.2 的核心主题是"并发退一步、性能进一步"——默认单线程、按需并发的策略让 data race safety 不再是初学者的噩梦。；这是一场循序渐进的 Swift 并发实战教程——从单线程贴纸 app 出发，通过 Instruments 发现 hang，逐步引入 async/await、@concurrent、async let 和 TaskGroup，同时处理了两个真实的数据竞争场景。如果你对 Swift 6 的数据竞争安全检查还比较陌生，这场的错误信息分析过程比最终代码更有价值。；Apple 用 Swift 写了一个 Linux 容器框架，每个容器跑在独立的轻量级 VM 里，sub second 启动，没有 Docker Desktop 也能在 Mac 上跑容器了。 来源：[WWDC25-245]、[WWDC25-270]、[WWDC25-346]
- **AppIntents**：WWDC 2024 Keynote 的核心叙事只有一个：Apple Intelligence——从系统级 AI 能力到开发者工具链，Apple 在全面铺设自己的 AI 基础设施。；Platforms State of the Union 是开发者视角的 WWDC 重头戏——Apple Intelligence 的端侧模型架构（Adapter 机制 + 4 bit 量化 + Neural Engine 优化）、Private Cloud Compute 的安全设计、Swift 6 的并发安全迁移、以及 Xcode 16 的预测代码补全，这些都会直接影响你接下来的开发工作。 来源：[WWDC24-111]、[WWDC24-112]

## API 演进时间线

- **WWDC26**：6 场，代表来源：[WWDC26-203]、[WWDC26-226]、[WWDC26-262]、[WWDC26-265]、[WWDC26-267]
- **WWDC25**：8 场，代表来源：[WWDC25-102]、[WWDC25-230]、[WWDC25-245]、[WWDC25-250]、[WWDC25-266]
- **WWDC24**：4 场，代表来源：[WWDC24-10169]、[WWDC24-10212]、[WWDC24-111]、[WWDC24-112]
- **WWDC23**：4 场，代表来源：[WWDC23-10147]、[WWDC23-10170]、[WWDC23-10180]、[WWDC23-10248]
- **WWDC22**：6 场，代表来源：[WWDC22-110350]、[WWDC22-110351]、[WWDC22-110355]、[WWDC22-110356]、[WWDC22-110379]
- **WWDC21**：17 场，代表来源：[WWDC21-10017]、[WWDC21-10019]、[WWDC21-10058]、[WWDC21-10095]、[WWDC21-10132]
- **WWDC20**：4 场，代表来源：[WWDC20-10151]、[WWDC20-10163]、[WWDC20-10170]、[WWDC20-10188]

## 决策启发式

- 老项目迁移 ：如果你之前在用 Vision 框架的 VNRecognizeTextRequest 做手写识别，建议直接替换为 PKStrokeRecognizer。Vision 对印刷体很强，但对连笔手写的理解远不如 PencilKit 的原生引擎。
- 新项目采用 ：把 PencilKit 当作数据层和识别层，UI 层可以根据需求选择 PKCanvasView 或自定义渲染。利用 PKStroke 新增的稳定 Identifiable (UUID) 来管理你的业务逻辑状态，这样在执行 Undo/Redo 时，你能精准追踪到具体是哪一笔发生了变化。
- 性能避坑 ：在复杂绘图（几千个 Stroke）中使用 Stroke Slicing (笔画切割) 时，计算开销会呈指数级上升。尽量在用户停止绘制后的后台线程进行切割计算，或者限制单次切割的 Stroke 数量。另外，Simulator 目前只支持拉丁语系的识别，测试中日韩语言必须用真机。
- 已有项目的迁移策略
- 新项目的采用建议
- 实战中容易踩的坑
- 已有项目的迁移策略 ：先别急着改代码。用 Instruments 27 跑一遍 Time Profiler，盯住 CPU 使用率。如果卡顿时 CPU 飙高，用新的 Top Functions 视图找最耗时的函数去优化算法；如果卡顿时 CPU 闲置，切到 System Trace 查 I/O 和锁。
- 新项目的采用建议 ：全面拥抱 OSSignpost。把网络请求、数据库查询、复杂 UI 渲染等关键路径全部用 beginInterval 和 endInterval 包起来。这会让你的 Instruments Trace 从一团乱麻变成清晰的业务时间线。
- 实战中容易踩的坑 ：永远不要用 Debug 构建包去跑 Profiling。Debug 模式下的 Swift 编译器会关闭优化并插入大量运行时检查，导致测出来的性能数据毫无参考价值，甚至会把原本不卡的代码测出卡顿。
- Liquid Glass adoption 不要一步到位 。先 recompile 看效果，再用 toolbar spacer、tint 等 API 微调，最后处理自定义控件。很多自定义背景和边框现在可以删掉了。

## 反模式与坑

- 稳定的 Stroke ID ：PKStroke 终于遵循了 Identifiable，Undo/Redo 或跨设备同步时，再也不用靠坐标和颜色去猜是不是同一笔了。
- Wet ink 渲染控制 ：现在可以手动调整 renderGroupID，控制哪些笔画在渲染时被视为“墨水未干”的状态，方便做特殊的混合效果。
- 选区变化代理 ：新增 canvasViewSelectionDidChange 方法，终于能精准捕获用户在画布上框选内容的变化，不用再靠 KVO 去 hack 内部属性了。
- 原生通话记录集成 ：只要配置 includesConversationInRecents: true，你的 App 通话记录会自动混入系统自带的“电话”App 历史记录中，点击还能直接回拨。
- 群组通话的合并与拆分 ：通过 .merging 能力，系统原生支持将两个独立的 1v1 通话合并成一个多人会议，底层信令的复杂度被系统 UI 接管了一大半。
- 灵动岛多任务无缝切换 ：通话切到后台时，系统会自动在灵动岛生成 Live Activity，用户可以在不打开 App 的情况下进行静音、挂断等操作，且动画完全由系统接管。
- Subprocess 1.0 正式发布 ：做服务端或命令行工具的开发者有福了，新的 API 支持逐行流式输出（line by line output streaming），不用再自己封装难用的 Pipe 了。
- Swift Testing 增强 ：支持了动态取消测试和 Flaky test（不稳定测试）自动重试，终于不用为了偶发的网络超时去写恶心的 XCTWaiter 重试逻辑了。

## 高频主题

`Swift` (4)、`开发工具` (3)、`Swift Concurrency` (2)、`基础` (2)、`PencilKit` (1)、`PKStrokeRecognizer` (1)、`Handwriting Recognition` (1)、`Swift Actor` (1)、`Bezier Path` (1)、`LiveCommunicationKit` (1)、`PushKit` (1)、`CallKit` (1)、`VoIP` (1)、`Dynamic Island` (1)、`Swift 6.4` (1)、`Noncopyable Types` (1)、`anyAppleOS` (1)、`Module Selectors` (1)

## 关键 Session

- [WWDC26-203] 使用 PencilKit 解读笔触之间的奥秘：这场 Session 最值得关注的一件事是：Apple 终于把“备忘录”和“无边记”里那套极其好用的设备端手写识别引擎（PKStrokeRecognizer）开放给第三方了，而且直接做成了 Swift Actor。
- [WWDC26-226] 打造实时沟通体验：✅ CallKit 终于迎来了现代重构，LiveCommunicationKit 用统一的 Action 机制彻底解决了 VoIP 应用系统 UI 与 App 内 UI 状态撕裂的顽疾。
- [WWDC26-262] Swift 的新功能：这场 Session 最值得关注的一件事是：Swift 终于把所有权系统（Ownership System）全面铺开到非拷贝类型（Noncopyable Types），让底层性能优化从“语法实验”变成了真正能写进生产环境的利器，顺手还用 anyAppleOS 干掉了折磨大家十年的多端可用性样板代码。
- [WWDC26-265] 使用 gRPC 和 Swift 构建实时 App 及服务：gRPC Swift 终于补齐了现代 Swift 并发（Swift Concurrency）的最后一块拼图，全栈 Swift 开发者现在可以用一套 .proto 文件无缝搞定 iOS 和后端的双向实时流，不用再捏着鼻子手写 WebSocket 状态机了。
- [WWDC26-267] 迁移到 Swift Testing：✅ Swift Testing 终于不用“推倒重来”了，官方提供的互操作性（Interoperability）让你能在同一个文件里无缝混写 XCTest 和 Swift Testing，老项目的迁移成本直接降维。
- [WWDC26-268] 性能分析、修复和验证：利用 Instruments 提升 App 响应性：Instruments 27 终于把“找卡顿”从玄学变成了填空题，新增的 Top Functions 视图和 Swift Executors 工具让新手也能一眼看穿 Main Actor 阻塞和同步 I/O 的锅。
- [WWDC25-102] Platforms State of the Union：如果说 Keynote 是面向用户的发布会，PSOTU 就是面向开发者的施工图 Liquid Glass 的 API 落地细节、Foundation Models 的 tool calling 和 guided generation、Swift 6.2 的并发简化、Metal 4 的 neural rendering，全部在这里展开。
- [WWDC25-230] Swift 新特性：如果你还在用 UnsafeBufferPointer 处理高性能数据，这场 Session 会给你一个终于可以扔掉它的理由。
- [WWDC25-245] Swift 6.2 新特性全览：Swift 6.2 的核心主题是"并发退一步、性能进一步"——默认单线程、按需并发的策略让 data race safety 不再是初学者的噩梦。
- [WWDC25-250] Network framework 的结构化并发实践：Network framework 终于有了 Swift native 的声明式 API——NetworkConnection、NetworkListener、NetworkBrowser 三个类型把底层网络编程的门槛拉低到了 SwiftUI 的水平。
- [WWDC25-266] SwiftUI 中的并发探索：@MainActor 默认、后台优化与数据竞争防护：SwiftUI 的并发模型可以用一句话概括：@MainActor 是编译期默认，Sendable 是后台优化的信号灯。SwiftUI 的注解表达的是运行时语义——View 默认主线程、Shape/visualEffect/Layout 可能后台调用。理解了这一点，你就不需要害怕并发。
- [WWDC25-270] 实战：用 Swift 并发优化 app——从单线程到并行的数据竞争处理：这是一场循序渐进的 Swift 并发实战教程——从单线程贴纸 app 出发，通过 Instruments 发现 hang，逐步引入 async/await、@concurrent、async let 和 TaskGroup，同时处理了两个真实的数据竞争场景。如果你对 Swift 6 的数据竞争安全检查还比较陌生，这场的错误信息分析过程比最终代码更有价值。
- [WWDC25-346] 认识 Containerization：Apple 用 Swift 写了一个 Linux 容器框架，每个容器跑在独立的轻量级 VM 里，sub second 启动，没有 Docker Desktop 也能在 Mac 上跑容器了。
- [WWDC25-367] WWDC25 Platforms State of the Union Recap：10 分钟看完 WWDC25 全部重点 Liquid Glass、Foundation Models、Xcode 26、Swift 6.2、SwiftUI 富文本和性能、Metal 4、visionOS 沉浸式媒体。适合团队分享或快速复习，不适合用来学技术细节。
- [WWDC24-10169] 将你的 App 迁移到 Swift 6：如果你的 Swift App 还没开 Swift 6 模式，现在是时候了——编译器会告诉你所有潜在的数据竞争问题，而且迁移过程可以按模块逐步推进。
- [WWDC24-10212] Core Location 授权新范式：CLServiceSession 声明式授权：CLServiceSession 把 Core Location 授权从"你在什么时机调用什么方法"变成了"声明你需要什么等级的定位"，系统自动处理弹窗时机和状态恢复——复杂场景下代码量能减少 80%。
- [WWDC24-111] WWDC 2024 主题演讲：WWDC 2024 Keynote 的核心叙事只有一个：Apple Intelligence——从系统级 AI 能力到开发者工具链，Apple 在全面铺设自己的 AI 基础设施。
- [WWDC24-112] 平台技术全景：Apple Intelligence 架构、Swift 6 与工具链更新：Platforms State of the Union 是开发者视角的 WWDC 重头戏——Apple Intelligence 的端侧模型架构（Adapter 机制 + 4 bit 量化 + Neural Engine 优化）、Private Cloud Compute 的安全设计、Swift 6 的并发安全迁移、以及 Xcode 16 的预测代码补全，这些都会直接影响你接下来的开发工作。
