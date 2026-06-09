# Platform Services

## 领域判断

系统服务、Widget、App Intents、Live Activity、通知与系统集成。本领域覆盖 337 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **System Frameworks**：AdAttributionKit 是 SKAdNetwork 的继任者，新增了 re engagement 归因和 view through 广告支持，如果你在做广告归因相关的工作，这是必须了解的框架。；WeatherKit 今年新增了天气变化预警和历史对比两个查询，你的 app 终于可以不只是"展示数据"，而是"告诉你数据意味着什么"。；如果你的 App 有大量用户同时关注同一个 Live Activity（比如体育赛事、航班信息），iOS 18 的 Broadcast Push Notifications 能用一条推送同时更新所有设备，再也不用逐个管理 push token 了。 来源：[WWDC24-10060]、[WWDC24-10067]、[WWDC24-10069]、[WWDC24-10074]
- **System & Services**：L4S 能在拥挤网络中将视频通话的延迟降低 50%、丢包率降到接近零——如果你的 app 涉及实时通信，这个技术必须了解。；iOS 17 终于支持可恢复的上传任务了，下载和上传现在都能从中断处继续——这对大文件传输是改变游戏规则的更新。；BERT 嵌入来了，Natural Language 框架一次性支持 27 种语言，多语言文本分类从此变得简单。 来源：[WWDC23-10004]、[WWDC23-10006]、[WWDC23-10042]、[WWDC23-10054]
- **WidgetKit**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：小组件可在系统各处突出显示你 App 中最重要的内容，让用户有更多机会与你的 App 交互。探索不同类型的小组件，以及令人印象深刻的小组件需要具备的特质。了解如何创建小组件、让小组件保持最新状态，并利用 App Intents 和动态样式为用户提供自定义小组件的选项。；小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。；CarPlay 终于不再是导航和音乐播放器的独角戏了——WidgetKit 和 Live Activities 的引入，让任何有实时状态信息的应用都有机会出现在驾驶场景中，但谁先做出适配谁就能吃到红利。 来源：[WWDC26-277]、[WWDC25-215]、[WWDC25-217]、[WWDC25-218]
- **Task**：Core Spotlight 今年加入了语义搜索（semantic search），用户不再需要精确匹配关键词，用自然语言就能搜到你 app 里的内容——而且实现成本极低。；iOS 17 让你把系统的 Photos Picker 直接嵌入 App 界面，配合 continuous selection 模式实现实时选图，再也不需要自建相册浏览器。；如果你已经用了 async/await 但对任务取消、优先级传播和任务组资源管理还有疑问，这场 Session 用汤厨的比喻把这些概念讲清楚了——特别是 withTaskCancellationHandler 在 AsyncSequence 中的用法值得反复看。 来源：[WWDC24-10131]、[WWDC23-10107]、[WWDC23-10170]、[WWDC23-10185]
- **AppIntent**：Apple Intelligence 让 Siri 真正能理解自然语言了，而 Assistant Schemas 是你把应用接入这套能力的最短路径——只要一个 Macro，你的 AppIntent 就能被 Siri 的 LLM 理解和调用。；iOS 18 把 App Intents 的定位从"少数常用操作暴露给系统"变成了"你 App 做的每件事都应该是一个 Intent"——这意味着 App Intents 的设计质量直接决定了你的 App 在 Spotlight、Shortcuts、Siri、Action Button 等系统入口的表现。；Widget 终于支持动画和交互了——用 App Intents 驱动按钮和开关操作，用 SwiftUI 的动画 API 让内容切换有感知力，再加上新的 Preview API 实时预览动画效果，这让 Widget 从"静态信息卡"变成了"可以操作的迷你 App"。 来源：[WWDC24-10133]、[WWDC24-10176]、[WWDC23-10028]、[WWDC23-10102]
- **CloudKit**：TipKit 今年补齐了功能引导最缺的三块拼图：分组控制展示顺序、自定义标识符让 Tip 可复用、CloudKit 同步让跨设备状态一致——从此功能引导不再是一锤子买卖。；如果你的 App 有协作功能（文档共享、多人编辑等），这场 Session 讲解了如何通过 Messages 将协作流程与对话无缝衔接，支持 CloudKit、iCloud Drive 和自定义基础设施三种路径。；App Clips 在 iOS 16 迎来一波实用更新：体积上限提升到 15MB、新增诊断工具、支持 CloudKit 只读访问和 Keychain 迁移，如果你在做 App Clips，这些改进直接降低开发成本。 来源：[WWDC24-10070]、[WWDC22-10095]、[WWDC22-10097]、[WWDC22-10115]
- **RealityKit**：Reality Composer Pro 今年新增了 Timelines 编辑器——一个可视化的动画编排工具，让你不用写代码就能串起旋转、移动、动画播放、音频触发等动作序列，而且编排结果可以在代码中通过触发器精确控制播放时机。；RealityKit 今年把 MaterialX shader 和 blend shapes、subdivision surfaces 带到了全平台（iOS/iPadOS/macOS），加上 macOS 上 Preview 的 USD 工具链增强，3D 内容创作的工作流统一性向前迈了一大步。；USD 和 MaterialX 在 xrOS 上获得了全面支持——从 Safari 的 3D Model 元素、Freeform 的 USDZ 嵌入、Reality Composer Pro 的 Shader Graph，到 MaterialX 生成 Metal 着色器的能力，3D 内容创作和消费的完整生态已经成型。 来源：[WWDC24-10102]、[WWDC24-10106]、[WWDC23-10086]、[WWDC23-10203]

## API 演进时间线

- **WWDC26**：12 场，代表来源：[WWDC26-207]、[WWDC26-210]、[WWDC26-212]、[WWDC26-223]、[WWDC26-262]
- **WWDC25**：23 场，代表来源：[WWDC25-202]、[WWDC25-204]、[WWDC25-207]、[WWDC25-208]、[WWDC25-213]
- **WWDC24**：48 场，代表来源：[WWDC24-10060]、[WWDC24-10067]、[WWDC24-10068]、[WWDC24-10069]、[WWDC24-10070]
- **WWDC23**：75 场，代表来源：[WWDC23-10002]、[WWDC23-10004]、[WWDC23-10006]、[WWDC23-10007]、[WWDC23-10013]
- **WWDC22**：88 场，代表来源：[WWDC22-10002]、[WWDC22-10003]、[WWDC22-10005]、[WWDC22-10008]、[WWDC22-10016]
- **WWDC21**：44 场，代表来源：[WWDC21-10002]、[WWDC21-10003]、[WWDC21-10005]、[WWDC21-10015]、[WWDC21-10032]
- **WWDC20**：47 场，代表来源：[WWDC20-10006]、[WWDC20-10033]、[WWDC20-10034]、[WWDC20-10035]、[WWDC20-10036]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 现在就跑一次 Power Profiler trace 。连上设备，Profile 你的 app，看看有没有意外的 CPU/GPU 尖峰。这是成本最低的功耗审计。
- 启用设备端 Performance Trace 做真实场景测试 。让 QA 或 beta 用户在不同使用场景下采集 trace，特别是导航、长时间后台、弱网等环境。
- 所有列表/网格默认使用 Lazy 容器 。除非你确定数据量很小（< 20 项），否则没有理由用 VStack/HStack 代替 LazyVStack/LazyHStack。
- 避免在频繁调用的回调中做文件 I/O 或 JSON 解析 。位置更新、timer 回调、通知处理等高频触发点应该只做增量计算，重活缓存或预计算。
- 建立功耗基线 。用 Power Profiler 记录当前版本的功耗数据，每次修改后对比，防止"优化一个功能，引入另一个耗电问题"。
- 为每个后台任务选择正确的 API 。用户发起的长任务 BGContinuedProcessingTask。静默预取 BGAppRefreshTask。服务器推送更新 Background Push。离线批处理 BGProcessingTask。短时间收尾 beginBackgroundTask。
- 任务必须报告进度 。使用 Progress 对象并持续更新 completedUnitCount，否则系统会认为任务卡死并 expire 它。

## 反模式与坑

- Live Activity 支持通过信息分享航班状态，这对出行场景是社交属性的补完，但实现上依赖 Widget Extension，项目配置别忘了。
- 登机牌现在集成了 Maps 机场导航和 Find My 行李追踪，虽然不是开发者直接控制的功能，但如果你的登机牌语义标签够完整，这些系统能力会自动解锁。
- upcomingPassInformation 中的日期必须按时间顺序排列，否则 Wallet 界面会乱序展示——这个没有校验提示，出了 bug 很难排查。
- GeoToolbox 是个新框架，目前公开的能力主要服务于 PlaceDescriptor 和地理编码，但它的定位是"跨平台地理工具箱"，后续大概率会扩展更多地理数据处理能力。
- Look Around 街景登陆 MapKit JS，意味着房产、旅游类 Web 应用终于能嵌入 Apple 街景了，之前这块是 Google 的地盘。
- MKAddressRepresentations 支持按语言环境自定义地址格式，做国际化的团队可以用它干掉一大段手动拼接地址的工具代码。
- MapCamera 动画不要在短时间内连续触发，否则会导致动画堆叠和卡顿，需要自己做节流。
- MapItemDetail 需要设备有地图数据，模拟器上的功能可能受限，真机测试是必须的。

## 高频主题

`SwiftUI` (8)、`系统服务` (7)、`Design` (4)、`HealthKit` (3)、`CarPlay` (3)、`System Services` (3)、`Swift` (3)、`WidgetKit` (3)、`应用服务` (3)、`Health & Fitness` (3)、`StoreKit` (2)、`App Intents` (2)、`MapKit` (2)、`隐私与安全` (2)、`Xcode` (1)、`Wallet` (1)、`PassKit` (1)、`Apple Pay` (1)

## 关键 Session

- [WWDC26-207] 利用 HealthKit 体能训练区间提供健身洞察：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 HealthKit，你可以更轻松地在自己的 App 中提供健身洞察，比如心率区间和骑行功率区间。了解如何利用内置的个性化区间，或创建自定区间。探索如何利用当前区间以及处于每个区间内的时长，在锻炼过程中和锻炼后提供有针对性的实用指导。
- [WWDC26-210] Apple App 内购买项目的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 12 个月承诺期的月度订阅，为用户提供更实惠的订阅支付方式，同时巩固长期订阅关系。探索如何使用 App Store Connect、StoreKit API、Xcode 测试以及其他工具，配置并测试这一全新的支付选项。你还将了解优惠代码兑换 API 的改进，以及 App 审核内容提交体验的提升。
- [WWDC26-212] 为你的 CarPlay 车载 App 加足马力：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 CarPlay 车载音频、导航、语音对话类 App 等方面的新功能。探索如何打造 CarPlay 车载视频 App，让用户在停车休息时能够直接在兼容车型上浏览并观看喜爱的视频。了解如何将缩略图、媒体信息和语音控制统统整合到你的 CarPlay 车载 App 中。
- [WWDC26-223] 实时活动基础知识：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：为你的 App 提升实时活动体验。探索展示实时活动的多个位置，包括迎来新样式的灵动岛，能在横屏使用 iPhone 时提供更多信息。了解如何为每个空间量身定制实时活动、合理安排内容和数据，并利用 ActivityKit 和推送通知实现全程实时更新。
- [WWDC26-262] Swift 的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：与我们一起了解 Swift 的最新更新。探索语言方面的最新进展，包括提升日常开发体验的更新、改进的并发性，以及更安全的高性能代码。了解工作流程和语言互操作性的改进，以及嵌入式 Swift 的更新。
- [WWDC26-277] WidgetKit 基础知识：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：小组件可在系统各处突出显示你 App 中最重要的内容，让用户有更多机会与你的 App 交互。探索不同类型的小组件，以及令人印象深刻的小组件需要具备的特质。了解如何创建小组件、让小组件保持最新状态，并利用 App Intents 和动态样式为用户提供自定义小组件的选项。
- [WWDC26-312] 了解 NowPlaying 框架：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：抢先了解 NowPlaying——利用这个 Swift 框架，将你 App 的媒体播放搬上锁定屏幕、控制中心、灵动岛和 CarPlay 车载等系统界面。了解如何使用其中的可观察 API 发布播放状态并响应命令。探索远程播放会话，这项新功能可让你的 App 在外部设备上呈现媒体播放，并将完整的播放控件带到同样的系统界面。
- [WWDC26-345] 探索 App Intents 框架的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：利用高级功能提升 App Intents 的应用效果，从而打造更快速、更灵活、更相关的使用体验。了解如何使用 ValueRepresentation 和 RelevantEntities 让你的内容更易于发现并呈现在不同的 App 中，如何利用 EntityCollection 提升性能，以及如何借助 SyncableEntity 实现跨设备扩展。探索更丰富的参数类型，包括联合值以及能够顺畅处理取消事件的长时间运行意图。
- [WWDC26-369] 通过 Bluetooth Channel Sounding 查找你的配件：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：开始使用 Channel Sounding，为你的蓝牙配件带来距离和方向感知功能。深入探索全新的 Nearby Interaction 和 Core Bluetooth API，并详细了解你需要进行哪些配件端更改。在优化功耗的同时，确保顺畅灵敏的体验。
- [WWDC26-378] 通过 StoreKit 和后台资源解锁游戏内内容：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 Steam Asset Converter 和新的 Unity 插件，简化你的跨平台开发，并为 App 内购买项目提供更好的支持。了解如何通过特定于语言的资源包，精准地分发恰如所需的内容，从而让你的游戏更精简，并为玩家带来更出色的体验。
- [WWDC26-389] 探索容器机：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解容器机，这是开源项目 Container 中新增的一款工具，可为 Mac 提供持久的轻量级 Linux 环境。探索容器机的工作原理，以及容器化设计如何在 macOS 上的 Linux 开发流程中提供顺畅丝滑的高性能体验。
- [WWDC26-8014] watchOS 小组实验室：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，与 Apple 工程师和设计师一起深入探索 WWDC26。在这个以 watchOS 为主题的活动中，你可以提出问题、获取建议，并实时关注围绕大会一周的相关重磅发布展开的精彩讨论。活动语言为英语。
- [WWDC25-202] Wallet 新特性：如果你做票务或航空 App，今年 Wallet 的更新能让你砍掉一半的推送逻辑和通行证管理代码——前提是你愿意把航班状态追踪这类核心体验交给 Apple 的系统服务。
- [WWDC25-204] 深入探索 MapKit：如果你的 app 里有任何"把别人的地点 ID 塞进 MapKit"的胶水代码，这场 Session 直接帮你删掉它。
- [WWDC25-207] MapKit 新特性：MapKit 终于从"给你一个地图，自己贴标签"进化成"你可以定义地图长什么样"，这对所有在应用里做品牌化地图体验的团队来说是质变。
- [WWDC25-208] HealthKit 新特性：HealthKitUI 的推出比新增的情绪数据类型影响更大——它宣告 Apple 认为健康数据可视化应该是系统级能力，不是每个 App 自己用 Charts 库画的活儿。
- [WWDC25-213] Foundation 新特性：如果你还在用 NSPredicate 字符串表达式做过滤，这次更新给了你一个必须迁移的理由—— Predicate 宏把运行时炸弹拆成了编译时错误。
- [WWDC25-215] 小组件新特性：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。
