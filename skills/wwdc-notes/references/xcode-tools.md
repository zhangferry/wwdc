# Xcode & Developer Tools

## 领域判断

Xcode、调试、测试、Instruments、性能与开发工具。本领域覆盖 152 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Developer Tools**：Xcode 16 在编辑、构建、调试、测试四个环节都有实质改进，其中 Explicit Modules 和 Swift 6 渐进式迁移是最值得开发者立刻上手的两件事。；不管你是 Xcode 新手还是老用户，这个 session 里的导航、搜索和 Git 技巧至少有三个是你不知道的——尤其是 Find Navigator 的高级搜索和 tab 管理的隐藏行为。；Xcode Cloud 新增了手动触发工作流、自定义别名（Custom Aliases）和 ci scripts 自定义脚本三大能力，让你的 CI 从"代码推送就跑"进化到"按需触发、版本统一、环境可控"。 来源：[WWDC24-10135]、[WWDC24-10181]、[WWDC24-10200]、[WWDC23-10140]
- **Swift & UI**：Swift 5.9 宏的完整指南——从创建你的第一个宏到处理错误诊断，这节课把该讲的都讲了。；SwiftUI 在 iOS 15 中补上了样式系统这块拼图——ButtonRole、controlSize、listStyle 等新 API 让你不用写自定义修饰符就能获得平台一致的视觉效果。；ARC 不是垃圾回收，理解 retain/release 的插入时机是写出高性能 Swift 代码的前提——特别是 async/await 场景下 ARC 优化器的行为发生了变化。 来源：[WWDC23-10166]、[WWDC21-10196]、[WWDC21-10216]、[WWDC20-10093]
- **System Frameworks**：WorkoutKit 终于在 watchOS 11 支持自定义游泳训练了，包括全新的"距离+时间"复合目标类型，这是游泳开发者等了整整一年的核心功能。；iOS 18 为文档类 App 提供了一套全新的可定制启动界面，从系统文档浏览器变成了带有品牌装饰、模板选择和自定义背景的沉浸式首页——重新编译就能获得。；如果你的 App 有任何非英语用户（基本上就是所有 App），这场 Session 提供的几个"一行代码修 bug"方案值得立刻加进你的代码库。 来源：[WWDC24-10084]、[WWDC24-10132]、[WWDC24-10185]、[WWDC20-10111]
- **开发工具**：Xcode 26 的 String Catalog 自动注释生成和符号生成功能，让本地化从"维护负担"变成了"开发工作流的自然延伸" 你写代码，Xcode 帮你准备翻译上下文。；Xcode 26 最大的卖点是 LLM 驱动的 Coding Assistant 正式落地，但更实在的进步是 build 加速、debugger 改善、以及 UI testing 的代码生成革命。；SwiftUI 今年的更新覆盖了从视觉到性能到生态的全链路——Liquid Glass 设计语言让你重新编译就焕然一新，列表性能提升 16 倍，WebView 和富文本终于官方支持，visionOS 三维布局正式成型。 来源：[WWDC25-225]、[WWDC25-247]、[WWDC25-256]、[WWDC25-306]
- **System & Services**：iOS 17 终于支持可恢复的上传任务了，下载和上传现在都能从中断处继续——这对大文件传输是改变游戏规则的更新。；Accelerate 框架在 iOS 15 中新增了加密归档（Encrypted Archive）支持——用 Apple 独有的加密算法压缩和保护数据，性能比 CommonCrypto 好得多。；iOS 14 新增的"大致位置"选项让用户可以选择只给 App 一个模糊的位置精度，如果你的企业 App 需要精确定位（比如室内导航、资产管理），你需要引导用户授予精确定位权限。 来源：[WWDC23-10006]、[WWDC21-10233]、[WWDC20-10140]、[WWDC20-10142]
- **SwiftData**：这是一场手把手教学——用闪卡应用做实例，演示如何用 @Model、@Query、ModelContainer 三板斧在 SwiftUI 中集成 SwiftData，从零到完整持久化只需要改几行代码。；这是 WWDC 2023 的技术方向总览——从 Swift Macros 到 SwiftUI 新特性，从 SwiftData 到 visionOS SDK，一场 Session 勾勒出 Apple 全平台的年度技术演进蓝图。；这场 Platforms State of the Union 覆盖面很广——Swift Macros、Swift C++ 互操作、SwiftUI 新控件、SwiftData 框架、visionOS 技术栈、Xcode 15 全面升级——适合快速了解今年开发者生态的全貌。 来源：[WWDC23-10154]、[WWDC23-102]、[WWDC23-112]
- **Task**：visionOS 上性能优化的首要目标不是省电，而是避免热压降频——系统始终在渲染每一帧（即使用户没操作），多个 App 同时运行，你的 App 如果占用资源过多会导致整体体验下降。；从开发阶段到发布后，Apple 提供了一整套卡顿（Hang）检测工具链——Xcode 中的 Hangs Instrument、TestFlight 阶段的设备端检测、以及 App Store Connect 中的聚合报告。；Hang（挂起）是比崩溃更糟糕的用户体验——App 没崩溃但卡住不动了。Xcode 13 的新 Hang Report 让你终于能看到用户遇到了多少次挂起以及每次挂起的堆栈。 来源：[WWDC23-10100]、[WWDC22-10082]、[WWDC21-10258]

## API 演进时间线

- **WWDC25**：10 场，代表来源：[WWDC25-225]、[WWDC25-247]、[WWDC25-256]、[WWDC25-257]、[WWDC25-306]
- **WWDC24**：13 场，代表来源：[WWDC24-10066]、[WWDC24-10084]、[WWDC24-10113]、[WWDC24-10132]、[WWDC24-10135]
- **WWDC23**：25 场，代表来源：[WWDC23-10006]、[WWDC23-10016]、[WWDC23-10023]、[WWDC23-10029]、[WWDC23-10056]
- **WWDC22**：22 场，代表来源：[WWDC22-10027]、[WWDC22-10039]、[WWDC22-10070]、[WWDC22-10082]、[WWDC22-10103]
- **WWDC21**：37 场，代表来源：[WWDC21-10009]、[WWDC21-10013]、[WWDC21-10015]、[WWDC21-10031]、[WWDC21-10062]
- **WWDC20**：45 场，代表来源：[WWDC20-10021]、[WWDC20-10033]、[WWDC20-10039]、[WWDC20-10042]、[WWDC20-10048]

## 决策启发式

- 开启自动注释生成 。Xcode Settings Editing "automatically generate string catalog comments"。这会让翻译人员获得足够上下文，减少来回沟通。
- 早期项目用字符串提取，成熟项目切符号生成 。两者之间的 Refactor 菜单可以一键转换，不必一开始就做决定。
- 使用 plural form 处理数量相关字符串 。不要用简单的 "item(s)" 占位，让系统根据语言规则选择正确形式。
- 给翻译人员导出时选择性导出语言 。Product Export Localizations 只选需要的语言，减少翻译文件体积。
- 大型项目的字符串按功能模块分 table 。比如 "Settings"、"Discover"、"Profile" 各一个 String Catalog，避免单个文件过大。
- 用 Coding Assistant 探索不熟悉的代码库时关闭自动应用修改，先理解模型的建议再决定是否采纳。
- 在 Signing & Capabilities 编辑器中统一管理 usage description，避免手动修改 Info.plist 导致的遗漏。
- 新项目开启 Explicitly Built Modules（Xcode 26 默认启用），享受 debugger 响应速度的显著提升。
- 用 UI 测试录制快速生成初始测试骨架，然后重构为 page object 模式以降低维护成本。
- 对有显著攻击面的 app（社交、消息、浏览器）启用 Enhanced Security capability。

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

`开发工具` (7)、`Swift` (5)、`SwiftUI` (3)、`应用服务` (1)、`Design` (1)、`基础` (1)、`空间计算` (1)、`Xcode` (1)、`AI` (1)、`调试` (1)、`性能` (1)、`Icon Composer` (1)、`图形与游戏` (1)、`机器学习` (1)

## 关键 Session

- [WWDC25-225] Code-along: Explore localization with Xcode：Xcode 26 的 String Catalog 自动注释生成和符号生成功能，让本地化从"维护负担"变成了"开发工作流的自然延伸" 你写代码，Xcode 帮你准备翻译上下文。
- [WWDC25-247] Xcode 26 新特性详解：Xcode 26 最大的卖点是 LLM 驱动的 Coding Assistant 正式落地，但更实在的进步是 build 加速、debugger 改善、以及 UI testing 的代码生成革命。
- [WWDC25-256] SwiftUI 年度更新：Liquid Glass、性能飞跃与三维布局：SwiftUI 今年的更新覆盖了从视觉到性能到生态的全链路——Liquid Glass 设计语言让你重新编译就焕然一新，列表性能提升 16 倍，WebView 和富文本终于官方支持，visionOS 三维布局正式成型。
- [WWDC25-257] Xcode 新特性：Xcode 26 把 Apple Intelligence 直接嵌入了 IDE 工具链——真正改变日常开发节奏的不是 AI 本身，而是 playground 宏让代码验证从"事件"变成了"习惯"。
- [WWDC25-306] 用 Instruments 优化 SwiftUI 性能：SwiftUI 的性能问题有两大根源：body 太慢和更新太多——新的 SwiftUI Instrument 能同时定位两者，特别是那个 Cause & Effect Graph，第一次把"为什么这个 View 会更新"这件事可视化了。
- [WWDC25-307] 探索 Swift 与 Java 互操作：Swift 要走出 Apple 生态了——SwiftJava 让 Swift 和 Java 在同一个项目里共存，双向互调，用 Gradle/SwiftPM 集成构建，而且是开源的。这对服务端 Swift 和企业级迁移意义重大。
- [WWDC25-308] 用 Instruments 优化 CPU 性能：一个二分查找函数从 Collection 换到 Span 就快了 4 倍，手动特化泛型再快 1.7 倍，无分支化再快 2 倍，Eytzinger 布局再快 2 倍——总共 25 倍加速，靠的不是灵感，是 Instruments 的三层工具链。
- [WWDC25-312] 改善 Swift 的内存使用和性能：从 700 倍性能差距到丝滑——用 Instruments 定位性能瓶颈，然后用 InlineArray、Span、OutputSpan 把 retain/release 和内存分配统统干掉。
- [WWDC25-344] Record, replay, and review: UI automation with Xcode：Xcode 的 UI 自动化工作流终于形成闭环了 Record 录制交互生成代码，Test Plan 配置多语言/多设备回放，Xcode Cloud 云端执行，Test Report 带视频回放和故障点定位。关键是 accessibility 做好了，UI 自动化自然就好用了。
- [WWDC25-346] 认识 Containerization：Apple 用 Swift 写了一个 Linux 容器框架，每个容器跑在独立的轻量级 VM 里，sub second 启动，没有 Docker Desktop 也能在 Mac 上跑容器了。
- [WWDC24-10066] 用 WebXR 构建沉浸式网页体验：Apple Vision Pro 上的 Safari 终于支持 WebXR，这意味着你的网站现在可以直接启动全沉浸式 VR 体验，无需安装任何 App。
- [WWDC24-10084] 用 WorkoutKit 构建自定义游泳训练：WorkoutKit 终于在 watchOS 11 支持自定义游泳训练了，包括全新的"距离+时间"复合目标类型，这是游泳开发者等了整整一年的核心功能。
- [WWDC24-10113] 探索 AVFoundation 中的媒体性能指标：iOS 18 的 AVMetrics API 让你能以事件流的方式精确追踪 HLS 播放的每一个环节——从 playlist 请求到 content key 获取到 stall 发生——终于可以在客户端层面系统性地诊断播放质量问题了。
- [WWDC24-10132] 升级你的文档启动体验：iOS 18 为文档类 App 提供了一套全新的可定制启动界面，从系统文档浏览器变成了带有品牌装饰、模板选择和自定义背景的沉浸式首页——重新编译就能获得。
- [WWDC24-10135] Xcode 16 新特性一览：Xcode 16 在编辑、构建、调试、测试四个环节都有实质改进，其中 Explicit Modules 和 Swift 6 渐进式迁移是最值得开发者立刻上手的两件事。
- [WWDC24-10172] 深入 RealityKit 调试器：Xcode 今年新增了 RealityKit Debugger——一个类似 View Debugger 的 3D 场景检查器，能让你看到 Entity Hierarchy、每个 Entity 的 Transform 和 Component 属性、还有 3D 视口里直接选中元素检查，从此 debug "为什么我的 3D 内容显示不正常"不再是猜谜游戏。
- [WWDC24-10179] 认识 Swift Testing：全新的 Swift 测试框架：Swift Testing 是一个开源的全新 Swift 测试框架，用 @Test、 expect、Trait、Suite 四个构建块替代 XCTest 的传统模式，写法更 Swifty、失败信息更有用、组织方式更灵活，而且可以和 XCTest 混用。
- [WWDC24-10181] Xcode 高效开发必备技巧：不管你是 Xcode 新手还是老用户，这个 session 里的导航、搜索和 Git 技巧至少有三个是你不知道的——尤其是 Find Navigator 的高级搜索和 tab 管理的隐藏行为。
