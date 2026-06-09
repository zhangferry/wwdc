# Xcode & Developer Tools

## 领域判断

Xcode、调试、测试、Instruments、性能与开发工具。本领域覆盖 175 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Developer Tools**：Xcode 16 在编辑、构建、调试、测试四个环节都有实质改进，其中 Explicit Modules 和 Swift 6 渐进式迁移是最值得开发者立刻上手的两件事。；不管你是 Xcode 新手还是老用户，这个 session 里的导航、搜索和 Git 技巧至少有三个是你不知道的——尤其是 Find Navigator 的高级搜索和 tab 管理的隐藏行为。；Xcode Cloud 新增了手动触发工作流、自定义别名（Custom Aliases）和 ci scripts 自定义脚本三大能力，让你的 CI 从"代码推送就跑"进化到"按需触发、版本统一、环境可控"。 来源：[WWDC24-10135]、[WWDC24-10181]、[WWDC24-10200]、[WWDC23-10140]
- **Xcode**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 12 个月承诺期的月度订阅，为用户提供更实惠的订阅支付方式，同时巩固长期订阅关系。探索如何使用 App Store Connect、StoreKit API、Xcode 测试以及其他工具，配置并测试这一全新的支付选项。你还将了解优惠代码兑换 API 的改进，以及 App 审核内容提交体验的提升。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 Xcode 和编码智能体如何根据 App 的情境帮助你翻译字符串目录。我们将介绍审核翻译输出和迭代本地化的策略，以便你为全球用户提供量身定制的体验。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：从零开始构建并测试 Safari 浏览器网页扩展，放心迈出入门第一步，而且全程无需使用 Xcode。探索内容拦截、页面修改、原生通信和权限模式如何协同工作，跨平台打造强大且保护隐私的浏览体验。 来源：[WWDC26-210]、[WWDC26-213]、[WWDC26-216]、[WWDC26-227]
- **Swift & UI**：Swift 5.9 宏的完整指南——从创建你的第一个宏到处理错误诊断，这节课把该讲的都讲了。；SwiftUI 在 iOS 15 中补上了样式系统这块拼图——ButtonRole、controlSize、listStyle 等新 API 让你不用写自定义修饰符就能获得平台一致的视觉效果。；ARC 不是垃圾回收，理解 retain/release 的插入时机是写出高性能 Swift 代码的前提——特别是 async/await 场景下 ARC 优化器的行为发生了变化。 来源：[WWDC23-10166]、[WWDC21-10196]、[WWDC21-10216]、[WWDC20-10093]
- **System Frameworks**：WorkoutKit 终于在 watchOS 11 支持自定义游泳训练了，包括全新的"距离+时间"复合目标类型，这是游泳开发者等了整整一年的核心功能。；iOS 18 为文档类 App 提供了一套全新的可定制启动界面，从系统文档浏览器变成了带有品牌装饰、模板选择和自定义背景的沉浸式首页——重新编译就能获得。；如果你的 App 有任何非英语用户（基本上就是所有 App），这场 Session 提供的几个"一行代码修 bug"方案值得立刻加进你的代码库。 来源：[WWDC24-10084]、[WWDC24-10132]、[WWDC24-10185]、[WWDC20-10111]
- **开发工具**：Xcode 26 的 String Catalog 自动注释生成和符号生成功能，让本地化从"维护负担"变成了"开发工作流的自然延伸" 你写代码，Xcode 帮你准备翻译上下文。；Xcode 26 最大的卖点是 LLM 驱动的 Coding Assistant 正式落地，但更实在的进步是 build 加速、debugger 改善、以及 UI testing 的代码生成革命。；SwiftUI 今年的更新覆盖了从视觉到性能到生态的全链路——Liquid Glass 设计语言让你重新编译就焕然一新，列表性能提升 16 倍，WebView 和富文本终于官方支持，visionOS 三维布局正式成型。 来源：[WWDC25-225]、[WWDC25-247]、[WWDC25-256]、[WWDC25-306]
- **Swift & Data**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：与我们一起了解 Swift 的最新更新。探索语言方面的最新进展，包括提升日常开发体验的更新、改进的并发性，以及更安全的高性能代码。了解工作流程和语言互操作性的改进，以及嵌入式 Swift 的更新。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 gRPC 在你的 Swift App 中及后端打造引人入胜的实时体验。gRPC 是一个开源的 RPC 框架，专为高性能、双向流式 API 设计。探索 gRPC Swift 软件包如何借助 Swift 并发提供现代且安全的运行时环境。了解整合的诸多工具如何简化你的工作流程，并帮助你轻松打造实时功能。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何借助测试框架之间的互操作性，在使用 XCTest 的同时放心地采用 Swift Testing。探索逐步引入高级测试功能的最佳做法和模式，以便加快开发速度并扩大测试覆盖面。 来源：[WWDC26-262]、[WWDC26-265]、[WWDC26-267]、[WWDC26-298]
- **System & Services**：iOS 17 终于支持可恢复的上传任务了，下载和上传现在都能从中断处继续——这对大文件传输是改变游戏规则的更新。；Accelerate 框架在 iOS 15 中新增了加密归档（Encrypted Archive）支持——用 Apple 独有的加密算法压缩和保护数据，性能比 CommonCrypto 好得多。；iOS 14 新增的"大致位置"选项让用户可以选择只给 App 一个模糊的位置精度，如果你的企业 App 需要精确定位（比如室内导航、资产管理），你需要引导用户授予精确定位权限。 来源：[WWDC23-10006]、[WWDC21-10233]、[WWDC20-10140]、[WWDC20-10142]

## API 演进时间线

- **WWDC26**：23 场，代表来源：[WWDC26-210]、[WWDC26-213]、[WWDC26-216]、[WWDC26-222]、[WWDC26-227]
- **WWDC25**：10 场，代表来源：[WWDC25-225]、[WWDC25-247]、[WWDC25-256]、[WWDC25-257]、[WWDC25-306]
- **WWDC24**：13 场，代表来源：[WWDC24-10066]、[WWDC24-10084]、[WWDC24-10113]、[WWDC24-10132]、[WWDC24-10135]
- **WWDC23**：25 场，代表来源：[WWDC23-10006]、[WWDC23-10016]、[WWDC23-10023]、[WWDC23-10029]、[WWDC23-10056]
- **WWDC22**：22 场，代表来源：[WWDC22-10027]、[WWDC22-10039]、[WWDC22-10070]、[WWDC22-10082]、[WWDC22-10103]
- **WWDC21**：37 场，代表来源：[WWDC21-10009]、[WWDC21-10013]、[WWDC21-10015]、[WWDC21-10031]、[WWDC21-10062]
- **WWDC20**：45 场，代表来源：[WWDC20-10021]、[WWDC20-10033]、[WWDC20-10039]、[WWDC20-10042]、[WWDC20-10048]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 开启自动注释生成 。Xcode Settings Editing "automatically generate string catalog comments"。这会让翻译人员获得足够上下文，减少来回沟通。
- 早期项目用字符串提取，成熟项目切符号生成 。两者之间的 Refactor 菜单可以一键转换，不必一开始就做决定。
- 使用 plural form 处理数量相关字符串 。不要用简单的 "item(s)" 占位，让系统根据语言规则选择正确形式。
- 给翻译人员导出时选择性导出语言 。Product Export Localizations 只选需要的语言，减少翻译文件体积。
- 大型项目的字符串按功能模块分 table 。比如 "Settings"、"Discover"、"Profile" 各一个 String Catalog，避免单个文件过大。
- 用 Coding Assistant 探索不熟悉的代码库时关闭自动应用修改，先理解模型的建议再决定是否采纳。
- 在 Signing & Capabilities 编辑器中统一管理 usage description，避免手动修改 Info.plist 导致的遗漏。

## 反模式与坑

- Session 222（多语言体验增强）提供了 Locale.preferredLocales 和 Natural Selection 的 API 更新，与本地化工作流直接相关。
- String Catalog 支持 Usage Description Comments 自动生成，提供翻译所需的上下文信息。
- 如果你的 app 支持多语言，优先处理长字符串语言（如德语）和 RTL 语言（如阿拉伯语、希伯来语）的布局适配。
- 两种工作流各有优势
- bundle 宏是小而美的改进
- 自动注释生成使用的是端侧模型
- Swift Build 已开源并在 GitHub 上接受社区贡献，正在被集成到 SwiftPM 中以统一 Xcode 和开源工具链的 build 引擎。
- String Catalog 现在能用 on device model 自动生成 localized string 的上下文注释，对翻译团队非常有价值。

## 高频主题

`Xcode` (12)、`Swift` (9)、`开发工具` (7)、`Instruments` (3)、`SwiftUI` (3)、`Xcode & Developer Tools` (2)、`Siri` (2)、`Other` (2)、`Design` (2)、`StoreKit` (1)、`Safari` (1)、`App Intents` (1)、`Swift & Data` (1)、`Metal` (1)、`应用服务` (1)、`基础` (1)、`空间计算` (1)、`AI` (1)

## 关键 Session

- [WWDC26-210] Apple App 内购买项目的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 12 个月承诺期的月度订阅，为用户提供更实惠的订阅支付方式，同时巩固长期订阅关系。探索如何使用 App Store Connect、StoreKit API、Xcode 测试以及其他工具，配置并测试这一全新的支付选项。你还将了解优惠代码兑换 API 的改进，以及 App 审核内容提交体验的提升。
- [WWDC26-213] 使用 Xcode 中的智能体翻译你的 App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 Xcode 和编码智能体如何根据 App 的情境帮助你翻译字符串目录。我们将介绍审核翻译输出和迭代本地化的策略，以便你为全球用户提供量身定制的体验。
- [WWDC26-216] 创建 Safari 浏览器的网页扩展：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：从零开始构建并测试 Safari 浏览器网页扩展，放心迈出入门第一步，而且全程无需使用 Xcode。探索内容拦截、页面修改、原生通信和权限模式如何协同工作，跨平台打造强大且保护隐私的浏览体验。
- [WWDC26-222] 了解全新的 MetricKit：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助新工具，比以往更快地发现和修复性能问题。与我们一起探索 MetricKit 如何为你提供关键的性能指标和实用的诊断信息，助你精准发现你的 App 在哪些方面仍有改进空间。我们还将介绍如何使用 StateReporting 框架按 App 状态对 App 的指标和诊断信息进行交叉分析，借此全面掌握相关情况，以便进一步排查并优化你 App 的体验。
- [WWDC26-227] 使用 Xcode 中的智能体创建 UI 原型：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何使用 Xcode 中的智能体构建 App 原型。探索相关技巧，看看如何借助 AI 进行互动原型设计、布局迭代，并创造性地解决设计难题。你还将了解如何用辩证的眼光评估想法，并将想法提炼成以用户为中心的高质量 App 体验。
- [WWDC26-240] 使用 App Schemas 打造智能 Siri 体验：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：利用 App Intents，将你 App 的内容和操作带到 Siri。通过 App Entities 对数据进行建模，使用 App Schemas 实现强大的系统操作，并为依托 Apple 智能的自然语言交互提供支持。探索如何启用语义搜索、跨 App 执行操作，以及利用屏幕感知和内容传输功能打造贴合情境的用户体验。了解一些最佳做法和测试工具，助你构建快速、可靠的 Siri 体验。
- [WWDC26-243] 使用 Instruments 调试和分析智能体 App 体验：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Xcode 中增强的 Foundation Models Instrument，以便检查相关行为表现，并优化智能体流程的性能。了解如何在涉及多个 LanguageModelSession 和配置的高级用例中，检查提示词、分析延迟并追踪控制流。
- [WWDC26-258] Xcode 27 的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Xcode 27 中最新的效率增强功能。通过自定、编码智能体和 Device Hub 加速你的开发流程。探索本地化、性能和测试工具方面的更新，以便进一步优化你的 App。
- [WWDC26-259] 在 Xcode 中与智能体协作开发：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何在开发过程中使用 Xcode 中的编码智能体。我们将探索与智能体协作的多种方式，并分享从创建初始原型到打磨完善 App 的实用技巧。了解 Xcode 的编码助手如何适应你的需求，帮助你持续投入那些让编程充满乐趣的创意工作——无论你是独自开发 App，还是与团队协作开发。
- [WWDC26-260] 充分利用 Device Hub：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 Device Hub 如何加速你的开发流程。我们将介绍 Device Hub 的具体功能，还将演示如何借助设备和模拟器快速诊断并复现问题。
- [WWDC26-261] 使用 Xcode Cloud 构建、交付并实现自动化：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Xcode Cloud 的最新更新，助你更快地开始构建和交付 App。了解 Xcode Cloud 的核心概念，通过连接你的源代码库来轻松设置云端构建和测试，并在准备好发布时配置 App 分发。了解 Web 挂钩和管理工具如何扩展 Xcode Cloud 的功能，为你的高级工作流程提供支持。
- [WWDC26-262] Swift 的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：与我们一起了解 Swift 的最新更新。探索语言方面的最新进展，包括提升日常开发体验的更新、改进的并发性，以及更安全的高性能代码。了解工作流程和语言互操作性的改进，以及嵌入式 Swift 的更新。
- [WWDC26-265] 使用 gRPC 和 Swift 构建实时 App 及服务：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 gRPC 在你的 Swift App 中及后端打造引人入胜的实时体验。gRPC 是一个开源的 RPC 框架，专为高性能、双向流式 API 设计。探索 gRPC Swift 软件包如何借助 Swift 并发提供现代且安全的运行时环境。了解整合的诸多工具如何简化你的工作流程，并帮助你轻松打造实时功能。
- [WWDC26-267] 迁移到 Swift Testing：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何借助测试框架之间的互操作性，在使用 XCTest 的同时放心地采用 Swift Testing。探索逐步引入高级测试功能的最佳做法和模式，以便加快开发速度并扩大测试覆盖面。
- [WWDC26-268] 性能分析、修复和验证：利用 Instruments 提升 App 响应性：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：通过明确的工作流程处理 App 响应性问题。探索 Swift 并发 Instrument、Time Profiler 和 System Trace，以便定位性能瓶颈。了解如何使用热点函数并进行对比，以衡量你的性能改进并验证修复效果。同时探索 Instruments 中的其他增强功能，让每次迭代变得更快，从而帮助你在更短时间内为用户打造更流畅的体验。
- [WWDC26-281] 使用 Xcode 扩展 Reality Composer Pro 3 的功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Reality Composer Pro 3 如何助你构建规模更大、更具雄心的空间项目。了解如何创建项目专属插件，以便编辑自定组件、运行自定系统，并构建自己的 ScriptGraph 节点，从而全面掌控你的空间创作工作流程。
- [WWDC26-298] 了解 Evaluations 框架：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何使用 Evaluations 框架来评估模型驱动的体验。在概率世界中，仅靠单元测试是不够的。探索如何定义指标、自动评估输出质量并汇总统计数据，以便确保由 AI 支持的功能在各个 Apple 平台上都能稳定可靠地运行。
- [WWDC26-335] 通过爬山法评估优化你的提示词：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解比较评估的实用技巧，从而引导你完善提示工程，并为你的 App 选择最合适的模型。探索如何为性能建立基准、扩展评估策略，并将结果转换为 JSON 格式以便与其他工具集成。了解不同提示策略的适用场景，以及如何迭代优化提示词以获得最佳结果。
