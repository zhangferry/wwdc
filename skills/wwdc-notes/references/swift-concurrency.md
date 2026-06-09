# Swift Concurrency

## 领域判断

Swift 语言演进、async/await、Actor、Sendable 与线程安全。本领域覆盖 44 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Task**：如果你已经用了 async/await 但对任务取消、优先级传播和任务组资源管理还有疑问，这场 Session 用汤厨的比喻把这些概念讲清楚了——特别是 withTaskCancellationHandler 在 AsyncSequence 中的用法值得反复看。；CoreLocation 终于有了基于 Swift Concurrency 的定位 API——CLLocationUpdate.liveUpdates() 一行代码就能开始接收定位，配合 AsyncSequence 的全部能力，这是多年来定位 API 最大的使用体验升级。；这场 Session 是 Instruments 卡顿分析的实战教学——从人类感知阈值出发，用灯泡实验解释为什么 100ms 是"即时感"的生死线，然后用三种典型的卡顿模式演示如何在 Instruments 中定位和修复问题。 来源：[WWDC23-10170]、[WWDC23-10180]、[WWDC23-10248]、[WWDC22-110351]
- **Actor**：Distributed Actors 把 Swift 的并发安全模型从单进程扩展到了多进程——Actor 隔离 + 位置透明性，让分布式系统的代码和本地代码一样安全。；Swift 5.5 最大的变化是 async/await 和 Actor 的引入，这是 Swift 并发模型的一次彻底重构，影响范围远超语言本身。；这场 Session 用一个真实的照片浏览 App，手把手演示了从 completion handler 地狱到 async/await 的完整迁移过程——比看十篇博客都管用。 来源：[WWDC22-110356]、[WWDC21-10192]、[WWDC21-10194]、[WWDC21-10254]
- **MainActor**：SwiftUI 的并发模型可以用一句话概括：@MainActor 是编译期默认，Sendable 是后台优化的信号灯。SwiftUI 的注解表达的是运行时语义——View 默认主线程、Shape/visualEffect/Layout 可能后台调用。理解了这一点，你就不需要害怕并发。；如果你的 Swift App 还没开 Swift 6 模式，现在是时候了——编译器会告诉你所有潜在的数据竞争问题，而且迁移过程可以按模块逐步推进。；Core Data 终于正式拥抱 Swift Concurrency——@MainActor 标注的 View Context 和 NSManagedObjectContext 的 perform 方法现在可以用 async/await 写了，不用再嵌套回调地狱。 来源：[WWDC25-266]、[WWDC24-10169]、[WWDC21-10017]、[WWDC21-10192]
- **Sendable**：Swift 6.2 的核心主题是"并发退一步、性能进一步"——默认单线程、按需并发的策略让 data race safety 不再是初学者的噩梦。；如果你的 Swift App 还没开 Swift 6 模式，现在是时候了——编译器会告诉你所有潜在的数据竞争问题，而且迁移过程可以按模块逐步推进。；Doug Gregor 用航海比喻系统性地讲解了 Swift 并发模型如何通过隔离（Isolation）和 Sendable 协议在编译期防止数据竞争——这是理解 Swift 6 严格并发检查的基础。 来源：[WWDC25-245]、[WWDC24-10169]、[WWDC22-110351]、[WWDC21-10133]
- **Developer Tools**：这是一场信息密度极高的全景扫描——Swift 并发、Xcode Cloud、StoreKit 2、SharePlay 四大主题构成了 2021 年 Apple 开发者生态的骨架。；周一就是 Keynote + Platforms State of the Union 的消化日——大方向已经定了，接下来四天都在讲细节。；周二是 Session 密集轰炸的第一天——Xcode Cloud 三连讲、SF Symbols 3、MusicKit 是今天的技术干货。 来源：[WWDC21-102]、[WWDC21-10321]、[WWDC21-10322]
- **开发工具**：Swift 6.2 的核心主题是"并发退一步、性能进一步"——默认单线程、按需并发的策略让 data race safety 不再是初学者的噩梦。；这是一场循序渐进的 Swift 并发实战教程——从单线程贴纸 app 出发，通过 Instruments 发现 hang，逐步引入 async/await、@concurrent、async let 和 TaskGroup，同时处理了两个真实的数据竞争场景。如果你对 Swift 6 的数据竞争安全检查还比较陌生，这场的错误信息分析过程比最终代码更有价值。；Apple 用 Swift 写了一个 Linux 容器框架，每个容器跑在独立的轻量级 VM 里，sub second 启动，没有 Docker Desktop 也能在 Mac 上跑容器了。 来源：[WWDC25-245]、[WWDC25-270]、[WWDC25-346]
- **AppIntents**：WWDC 2024 Keynote 的核心叙事只有一个：Apple Intelligence——从系统级 AI 能力到开发者工具链，Apple 在全面铺设自己的 AI 基础设施。；Platforms State of the Union 是开发者视角的 WWDC 重头戏——Apple Intelligence 的端侧模型架构（Adapter 机制 + 4 bit 量化 + Neural Engine 优化）、Private Cloud Compute 的安全设计、Swift 6 的并发安全迁移、以及 Xcode 16 的预测代码补全，这些都会直接影响你接下来的开发工作。 来源：[WWDC24-111]、[WWDC24-112]

## API 演进时间线

- **WWDC26**：1 场，代表来源：[WWDC26-262]
- **WWDC25**：8 场，代表来源：[WWDC25-102]、[WWDC25-230]、[WWDC25-245]、[WWDC25-250]、[WWDC25-266]
- **WWDC24**：4 场，代表来源：[WWDC24-10169]、[WWDC24-10212]、[WWDC24-111]、[WWDC24-112]
- **WWDC23**：4 场，代表来源：[WWDC23-10147]、[WWDC23-10170]、[WWDC23-10180]、[WWDC23-10248]
- **WWDC22**：6 场，代表来源：[WWDC22-110350]、[WWDC22-110351]、[WWDC22-110355]、[WWDC22-110356]、[WWDC22-110379]
- **WWDC21**：17 场，代表来源：[WWDC21-10017]、[WWDC21-10019]、[WWDC21-10058]、[WWDC21-10095]、[WWDC21-10132]
- **WWDC20**：4 场，代表来源：[WWDC20-10151]、[WWDC20-10163]、[WWDC20-10170]、[WWDC20-10188]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- Liquid Glass adoption 不要一步到位 。先 recompile 看效果，再用 toolbar spacer、tint 等 API 微调，最后处理自定义控件。很多自定义背景和边框现在可以删掉了。
- Foundation Models 用 playground 宏做 prompt engineering 。在 Xcode 中用 playground 快速迭代不同 prompt，找到最佳结果后再集成到 app。
- SwiftData 在今年获得了 model subclassing 和 entity inheritance 。如果你之前因为数据模型灵活性不够而犹豫，现在可以重新评估。
- Metal 4 的 neural rendering 是游戏图形的下一个范式 。在 shader 中直接跑推理网络计算光照和材质，这对光线追踪的性能优化意义重大。
- 对于服务端 Swift 开发者 ，立即试试 Containerization 框架。它提供了在 Mac 上创建、下载、运行 Linux 容器的完整工具链。
- 新项目在 Xcode build settings 中开启 @MainActor 默认推断模式，大幅减少并发标注噪音。
- 对 CPU 密集型的 async 函数显式添加 @concurrent，让意图清晰、性能可预期。

## 反模式与坑

- App Intents 在 macOS Tahoe 的 Spotlight 中全面可用 ，用户可以直接从 Spotlight 调用你的 app actions 并填写参数。
- visionOS 26 的 enterprise APIs 更加开放：UVC 视频和 Neural Engine 不再需要企业许可证。
- SwiftCharts 3D 基于 RealityKit ，在 visionOS 上可以放在空间环境中交互。
- GameSave 框架 让游戏轻松实现跨设备云存档。
- WebKit 引入 Swift ，使用新的 opt in strict memory safety 特性确保与 C API 的安全交互。
- Liquid Glass 的 adoption 路径分三层
- Foundation Models 的 @Generable + tool calling 组合拳
- Swift 6.2 的 concurrency 路线在纠偏

## 高频主题

`Swift` (5)、`开发工具` (3)、`基础` (2)、`Span` (1)、`InlineArray` (1)、`并发` (1)、`标准库` (1)、`系统服务` (1)、`SwiftUI` (1)

## 关键 Session

- [WWDC26-262] Swift 的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：与我们一起了解 Swift 的最新更新。探索语言方面的最新进展，包括提升日常开发体验的更新、改进的并发性，以及更安全的高性能代码。了解工作流程和语言互操作性的改进，以及嵌入式 Swift 的更新。
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
- [WWDC23-10147] 认识 Core Location Monitor：Core Location 团队终于把位置监听从 delegate 回调地狱中解救出来了——CLMonitor 是一个 Swift Actor，用三行代码就能实现地理围栏和 Beacon 监听，再也不用手动管理 CLLocationManager 的各种回调状态。
- [WWDC23-10170] 深入结构化并发：取消、优先级与任务组：如果你已经用了 async/await 但对任务取消、优先级传播和任务组资源管理还有疑问，这场 Session 用汤厨的比喻把这些概念讲清楚了——特别是 withTaskCancellationHandler 在 AsyncSequence 中的用法值得反复看。
- [WWDC23-10180] 探索简化的定位更新 API：CoreLocation 终于有了基于 Swift Concurrency 的定位 API——CLLocationUpdate.liveUpdates() 一行代码就能开始接收定位，配合 AsyncSequence 的全部能力，这是多年来定位 API 最大的使用体验升级。
- [WWDC23-10248] 用 Instruments 分析应用卡顿：这场 Session 是 Instruments 卡顿分析的实战教学——从人类感知阈值出发，用灯泡实验解释为什么 100ms 是"即时感"的生死线，然后用三种典型的卡顿模式演示如何在 Instruments 中定位和修复问题。
- [WWDC22-110350] 可视化与优化 Swift 并发：Instruments 终于有了专门的 Swift Concurrency 模板——你可以直观地看到 actor 阻塞、线程池耗尽、continuation 泄露这些以前只能靠猜的并发问题。
