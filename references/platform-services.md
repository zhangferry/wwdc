# Platform Services

## 领域判断

系统服务、Widget、App Intents、Live Activity、通知与系统集成。本领域覆盖 325 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **System Frameworks**：AdAttributionKit 是 SKAdNetwork 的继任者，新增了 re engagement 归因和 view through 广告支持，如果你在做广告归因相关的工作，这是必须了解的框架。；WeatherKit 今年新增了天气变化预警和历史对比两个查询，你的 app 终于可以不只是"展示数据"，而是"告诉你数据意味着什么"。；如果你的 App 有大量用户同时关注同一个 Live Activity（比如体育赛事、航班信息），iOS 18 的 Broadcast Push Notifications 能用一条推送同时更新所有设备，再也不用逐个管理 push token 了。 来源：[WWDC24-10060]、[WWDC24-10067]、[WWDC24-10069]、[WWDC24-10074]
- **System & Services**：L4S 能在拥挤网络中将视频通话的延迟降低 50%、丢包率降到接近零——如果你的 app 涉及实时通信，这个技术必须了解。；iOS 17 终于支持可恢复的上传任务了，下载和上传现在都能从中断处继续——这对大文件传输是改变游戏规则的更新。；BERT 嵌入来了，Natural Language 框架一次性支持 27 种语言，多语言文本分类从此变得简单。 来源：[WWDC23-10004]、[WWDC23-10006]、[WWDC23-10042]、[WWDC23-10054]
- **WidgetKit**：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。；CarPlay 终于不再是导航和音乐播放器的独角戏了——WidgetKit 和 Live Activities 的引入，让任何有实时状态信息的应用都有机会出现在驾驶场景中，但谁先做出适配谁就能吃到红利。；watchOS 26 把 Apple Watch 的应用分发逻辑从"用户找应用"翻转成了"系统替用户挑应用"——RelevanceKit 才是这场 Session 里真正改变游戏规则的东西。 来源：[WWDC25-215]、[WWDC25-217]、[WWDC25-218]、[WWDC24-111]
- **Task**：Core Spotlight 今年加入了语义搜索（semantic search），用户不再需要精确匹配关键词，用自然语言就能搜到你 app 里的内容——而且实现成本极低。；iOS 17 让你把系统的 Photos Picker 直接嵌入 App 界面，配合 continuous selection 模式实现实时选图，再也不需要自建相册浏览器。；如果你已经用了 async/await 但对任务取消、优先级传播和任务组资源管理还有疑问，这场 Session 用汤厨的比喻把这些概念讲清楚了——特别是 withTaskCancellationHandler 在 AsyncSequence 中的用法值得反复看。 来源：[WWDC24-10131]、[WWDC23-10107]、[WWDC23-10170]、[WWDC23-10185]
- **AppIntent**：Apple Intelligence 让 Siri 真正能理解自然语言了，而 Assistant Schemas 是你把应用接入这套能力的最短路径——只要一个 Macro，你的 AppIntent 就能被 Siri 的 LLM 理解和调用。；iOS 18 把 App Intents 的定位从"少数常用操作暴露给系统"变成了"你 App 做的每件事都应该是一个 Intent"——这意味着 App Intents 的设计质量直接决定了你的 App 在 Spotlight、Shortcuts、Siri、Action Button 等系统入口的表现。；Widget 终于支持动画和交互了——用 App Intents 驱动按钮和开关操作，用 SwiftUI 的动画 API 让内容切换有感知力，再加上新的 Preview API 实时预览动画效果，这让 Widget 从"静态信息卡"变成了"可以操作的迷你 App"。 来源：[WWDC24-10133]、[WWDC24-10176]、[WWDC23-10028]、[WWDC23-10102]
- **CloudKit**：TipKit 今年补齐了功能引导最缺的三块拼图：分组控制展示顺序、自定义标识符让 Tip 可复用、CloudKit 同步让跨设备状态一致——从此功能引导不再是一锤子买卖。；如果你的 App 有协作功能（文档共享、多人编辑等），这场 Session 讲解了如何通过 Messages 将协作流程与对话无缝衔接，支持 CloudKit、iCloud Drive 和自定义基础设施三种路径。；App Clips 在 iOS 16 迎来一波实用更新：体积上限提升到 15MB、新增诊断工具、支持 CloudKit 只读访问和 Keychain 迁移，如果你在做 App Clips，这些改进直接降低开发成本。 来源：[WWDC24-10070]、[WWDC22-10095]、[WWDC22-10097]、[WWDC22-10115]
- **RealityKit**：Reality Composer Pro 今年新增了 Timelines 编辑器——一个可视化的动画编排工具，让你不用写代码就能串起旋转、移动、动画播放、音频触发等动作序列，而且编排结果可以在代码中通过触发器精确控制播放时机。；RealityKit 今年把 MaterialX shader 和 blend shapes、subdivision surfaces 带到了全平台（iOS/iPadOS/macOS），加上 macOS 上 Preview 的 USD 工具链增强，3D 内容创作的工作流统一性向前迈了一大步。；USD 和 MaterialX 在 xrOS 上获得了全面支持——从 Safari 的 3D Model 元素、Freeform 的 USDZ 嵌入、Reality Composer Pro 的 Shader Graph，到 MaterialX 生成 Metal 着色器的能力，3D 内容创作和消费的完整生态已经成型。 来源：[WWDC24-10102]、[WWDC24-10106]、[WWDC23-10086]、[WWDC23-10203]

## API 演进时间线

- **WWDC25**：23 场，代表来源：[WWDC25-202]、[WWDC25-204]、[WWDC25-207]、[WWDC25-208]、[WWDC25-213]
- **WWDC24**：48 场，代表来源：[WWDC24-10060]、[WWDC24-10067]、[WWDC24-10068]、[WWDC24-10069]、[WWDC24-10070]
- **WWDC23**：75 场，代表来源：[WWDC23-10002]、[WWDC23-10004]、[WWDC23-10006]、[WWDC23-10007]、[WWDC23-10013]
- **WWDC22**：88 场，代表来源：[WWDC22-10002]、[WWDC22-10003]、[WWDC22-10005]、[WWDC22-10008]、[WWDC22-10016]
- **WWDC21**：44 场，代表来源：[WWDC21-10002]、[WWDC21-10003]、[WWDC21-10005]、[WWDC21-10015]、[WWDC21-10032]
- **WWDC20**：47 场，代表来源：[WWDC20-10006]、[WWDC20-10033]、[WWDC20-10034]、[WWDC20-10035]、[WWDC20-10036]

## 决策启发式

- 现在就跑一次 Power Profiler trace 。连上设备，Profile 你的 app，看看有没有意外的 CPU/GPU 尖峰。这是成本最低的功耗审计。
- 启用设备端 Performance Trace 做真实场景测试 。让 QA 或 beta 用户在不同使用场景下采集 trace，特别是导航、长时间后台、弱网等环境。
- 所有列表/网格默认使用 Lazy 容器 。除非你确定数据量很小（< 20 项），否则没有理由用 VStack/HStack 代替 LazyVStack/LazyHStack。
- 避免在频繁调用的回调中做文件 I/O 或 JSON 解析 。位置更新、timer 回调、通知处理等高频触发点应该只做增量计算，重活缓存或预计算。
- 建立功耗基线 。用 Power Profiler 记录当前版本的功耗数据，每次修改后对比，防止"优化一个功能，引入另一个耗电问题"。
- 为每个后台任务选择正确的 API 。用户发起的长任务 BGContinuedProcessingTask。静默预取 BGAppRefreshTask。服务器推送更新 Background Push。离线批处理 BGProcessingTask。短时间收尾 beginBackgroundTask。
- 任务必须报告进度 。使用 Progress 对象并持续更新 completedUnitCount，否则系统会认为任务卡死并 expire 它。
- 处理 expiration 优雅退出 。在 expirationHandler 中设置取消标志，让任务循环检查并尽快退出。调用 setTaskCompleted 告诉系统你已完成。
- 不要用 BGContinuedProcessingTask 做自动任务 。如果任务不是由用户显式操作触发的，用户可能不理解进度 UI 的含义并取消它。这种场景用 BGProcessingTask 或 BGAppRefreshTask。
- 检查 supportedResources 。如果你的任务需要 GPU，先查询 scheduler.supportedResources 确认设备支持，再设置 requirements。

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

`SwiftUI` (8)、`系统服务` (7)、`应用服务` (3)、`Health & Fitness` (3)、`Design` (3)、`MapKit` (2)、`HealthKit` (2)、`WidgetKit` (2)、`隐私与安全` (2)、`Wallet` (1)、`PassKit` (1)、`Apple Pay` (1)、`Live Activity` (1)、`GeoToolbox` (1)、`PlaceDescriptor` (1)、`Geocoding` (1)、`地图` (1)、`导航` (1)

## 关键 Session

- [WWDC25-202] Wallet 新特性：如果你做票务或航空 App，今年 Wallet 的更新能让你砍掉一半的推送逻辑和通行证管理代码——前提是你愿意把航班状态追踪这类核心体验交给 Apple 的系统服务。
- [WWDC25-204] 深入探索 MapKit：如果你的 app 里有任何"把别人的地点 ID 塞进 MapKit"的胶水代码，这场 Session 直接帮你删掉它。
- [WWDC25-207] MapKit 新特性：MapKit 终于从"给你一个地图，自己贴标签"进化成"你可以定义地图长什么样"，这对所有在应用里做品牌化地图体验的团队来说是质变。
- [WWDC25-208] HealthKit 新特性：HealthKitUI 的推出比新增的情绪数据类型影响更大——它宣告 Apple 认为健康数据可视化应该是系统级能力，不是每个 App 自己用 Charts 库画的活儿。
- [WWDC25-213] Foundation 新特性：如果你还在用 NSPredicate 字符串表达式做过滤，这次更新给了你一个必须迁移的理由—— Predicate 宏把运行时炸弹拆成了编译时错误。
- [WWDC25-215] 小组件新特性：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。
- [WWDC25-217] CarPlay 新特性：CarPlay 终于不再是导航和音乐播放器的独角戏了——WidgetKit 和 Live Activities 的引入，让任何有实时状态信息的应用都有机会出现在驾驶场景中，但谁先做出适配谁就能吃到红利。
- [WWDC25-218] watchOS 新特性：watchOS 26 把 Apple Watch 的应用分发逻辑从"用户找应用"翻转成了"系统替用户挑应用"——RelevanceKit 才是这场 Session 里真正改变游戏规则的东西。
- [WWDC25-226] Profile and optimize power usage in your app：Power Profiler 终于可以在设备上独立采集了 不用连 Xcode，让 QA 在真实场景下跑几小时 trace，回来在 Instruments 里分析 CPU/GPU/网络的功耗影响，这才是发现"办公室里复现不了的耗电问题"的正确姿势。
- [WWDC25-227] Finish tasks in the background：BGContinuedProcessingTask 是 iOS 26 最值得关注的后台 API 用户点了"导出视频"然后切到后台，系统接管任务并显示进度 UI，用户随时可以取消。这解决了"用户发起的长任务切后台就挂掉"的老问题。
- [WWDC25-234] 用 NetworkExtension 过滤和隧道化网络流量：iOS 26 终于允许你根据完整 URL 而不只是 host 来做内容过滤了——但代价是你永远碰不到 URL 本身，系统用 Bloom filter + 同态加密 + Privacy Pass 做了一个隐私优先的方案。
- [WWDC25-250] Network framework 的结构化并发实践：Network framework 终于有了 Swift native 的声明式 API——NetworkConnection、NetworkListener、NetworkBrowser 三个类型把底层网络编程的门槛拉低到了 SwiftUI 的水平。
- [WWDC25-278] Widget 新特性：Widget 终于能从服务端推送更新了——不再需要 App 主动轮询或者依赖 Timeline 调度；visionOS 和 CarPlay 的加入让 Widget 的覆盖面又扩大了一圈；watchOS 的 Relevance Widget 则是直接解决了"不相关 Widget 堵 Smart Stack"的老问题。
- [WWDC25-299] 在 App 中提供适龄体验：如果你的 App 有用户年龄分级的需求——社交、游戏、内容平台——Declared Age Range API 就是 Apple 给出的官方答案，别再自己做生日输入框了。
- [WWDC25-314] 提前应对量子安全加密：量子计算还没来，但"先收集后解密"攻击已经在发生——iOS 26 默认开启量子安全 TLS，CryptoKit 新增后量子加密 API，你没借口再拖了。
- [WWDC25-321] 认识 HealthKit 药物 API：HealthKit 终于开放药物数据读取了——HKUserAnnotatedMedication 和 HKMedicationDoseEvent 让你可以构建用药提醒、副作用追踪、用药依从性分析等功能。
- [WWDC25-322] 在 iOS 和 iPadOS 上用 HealthKit 追踪锻炼：HealthKit 的 Workout API 终于完整支持 iPhone 和 iPad 了——和 Apple Watch 几乎一样的代码，加上锁屏 Live Activity 和 Siri 控制，甚至还有 crash recovery。
- [WWDC25-325] 探索 Apple 托管的 Background Assets：On Demand Resources 要退役了，Background Assets 的 Managed 模式接管——Apple 帮你托管 200GB 的资源包，系统自动下载、更新、压缩，你甚至不需要写 downloader extension。
