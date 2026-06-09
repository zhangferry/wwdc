# Platform Services

## 领域判断

系统服务、Widget、App Intents、Live Activity、通知与系统集成。本领域覆盖 335 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **System Frameworks**：AdAttributionKit 是 SKAdNetwork 的继任者，新增了 re engagement 归因和 view through 广告支持，如果你在做广告归因相关的工作，这是必须了解的框架。；WeatherKit 今年新增了天气变化预警和历史对比两个查询，你的 app 终于可以不只是"展示数据"，而是"告诉你数据意味着什么"。；如果你的 App 有大量用户同时关注同一个 Live Activity（比如体育赛事、航班信息），iOS 18 的 Broadcast Push Notifications 能用一条推送同时更新所有设备，再也不用逐个管理 push token 了。 来源：[WWDC24-10060]、[WWDC24-10067]、[WWDC24-10069]、[WWDC24-10074]
- **System & Services**：L4S 能在拥挤网络中将视频通话的延迟降低 50%、丢包率降到接近零——如果你的 app 涉及实时通信，这个技术必须了解。；iOS 17 终于支持可恢复的上传任务了，下载和上传现在都能从中断处继续——这对大文件传输是改变游戏规则的更新。；BERT 嵌入来了，Natural Language 框架一次性支持 27 种语言，多语言文本分类从此变得简单。 来源：[WWDC23-10004]、[WWDC23-10006]、[WWDC23-10042]、[WWDC23-10054]
- **WidgetKit**：这场 Session 最值得关注的一件事是：灵动岛（Dynamic Island）终于支持横屏了，Apple 提供了一套全新的环境变量（Environment Values）让你用极少的代码搞定横屏、待机显示（StandBy）和 Apple Watch 的 UI 适配灾难。；别指望看到颠覆性的 Widget 新玩法，这是一场给新手打底、给老手查漏补缺的“规范课”，最大的干货是明确了 Tinted/Clear 模式的适配边界和刷新预算的潜规则。；小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。 来源：[WWDC26-223]、[WWDC26-277]、[WWDC25-215]、[WWDC25-217]
- **Task**：Core Spotlight 今年加入了语义搜索（semantic search），用户不再需要精确匹配关键词，用自然语言就能搜到你 app 里的内容——而且实现成本极低。；iOS 17 让你把系统的 Photos Picker 直接嵌入 App 界面，配合 continuous selection 模式实现实时选图，再也不需要自建相册浏览器。；如果你已经用了 async/await 但对任务取消、优先级传播和任务组资源管理还有疑问，这场 Session 用汤厨的比喻把这些概念讲清楚了——特别是 withTaskCancellationHandler 在 AsyncSequence 中的用法值得反复看。 来源：[WWDC24-10131]、[WWDC23-10107]、[WWDC23-10170]、[WWDC23-10185]
- **AppIntent**：Apple Intelligence 让 Siri 真正能理解自然语言了，而 Assistant Schemas 是你把应用接入这套能力的最短路径——只要一个 Macro，你的 AppIntent 就能被 Siri 的 LLM 理解和调用。；iOS 18 把 App Intents 的定位从"少数常用操作暴露给系统"变成了"你 App 做的每件事都应该是一个 Intent"——这意味着 App Intents 的设计质量直接决定了你的 App 在 Spotlight、Shortcuts、Siri、Action Button 等系统入口的表现。；Widget 终于支持动画和交互了——用 App Intents 驱动按钮和开关操作，用 SwiftUI 的动画 API 让内容切换有感知力，再加上新的 Preview API 实时预览动画效果，这让 Widget 从"静态信息卡"变成了"可以操作的迷你 App"。 来源：[WWDC24-10133]、[WWDC24-10176]、[WWDC23-10028]、[WWDC23-10102]
- **CloudKit**：TipKit 今年补齐了功能引导最缺的三块拼图：分组控制展示顺序、自定义标识符让 Tip 可复用、CloudKit 同步让跨设备状态一致——从此功能引导不再是一锤子买卖。；如果你的 App 有协作功能（文档共享、多人编辑等），这场 Session 讲解了如何通过 Messages 将协作流程与对话无缝衔接，支持 CloudKit、iCloud Drive 和自定义基础设施三种路径。；App Clips 在 iOS 16 迎来一波实用更新：体积上限提升到 15MB、新增诊断工具、支持 CloudKit 只读访问和 Keychain 迁移，如果你在做 App Clips，这些改进直接降低开发成本。 来源：[WWDC24-10070]、[WWDC22-10095]、[WWDC22-10097]、[WWDC22-10115]
- **RealityKit**：Reality Composer Pro 今年新增了 Timelines 编辑器——一个可视化的动画编排工具，让你不用写代码就能串起旋转、移动、动画播放、音频触发等动作序列，而且编排结果可以在代码中通过触发器精确控制播放时机。；RealityKit 今年把 MaterialX shader 和 blend shapes、subdivision surfaces 带到了全平台（iOS/iPadOS/macOS），加上 macOS 上 Preview 的 USD 工具链增强，3D 内容创作的工作流统一性向前迈了一大步。；USD 和 MaterialX 在 xrOS 上获得了全面支持——从 Safari 的 3D Model 元素、Freeform 的 USDZ 嵌入、Reality Composer Pro 的 Shader Graph，到 MaterialX 生成 Metal 着色器的能力，3D 内容创作和消费的完整生态已经成型。 来源：[WWDC24-10102]、[WWDC24-10106]、[WWDC23-10086]、[WWDC23-10203]

## API 演进时间线

- **WWDC26**：10 场，代表来源：[WWDC26-207]、[WWDC26-212]、[WWDC26-223]、[WWDC26-237]、[WWDC26-262]
- **WWDC25**：23 场，代表来源：[WWDC25-202]、[WWDC25-204]、[WWDC25-207]、[WWDC25-208]、[WWDC25-213]
- **WWDC24**：48 场，代表来源：[WWDC24-10060]、[WWDC24-10067]、[WWDC24-10068]、[WWDC24-10069]、[WWDC24-10070]
- **WWDC23**：75 场，代表来源：[WWDC23-10002]、[WWDC23-10004]、[WWDC23-10006]、[WWDC23-10007]、[WWDC23-10013]
- **WWDC22**：88 场，代表来源：[WWDC22-10002]、[WWDC22-10003]、[WWDC22-10005]、[WWDC22-10008]、[WWDC22-10016]
- **WWDC21**：44 场，代表来源：[WWDC21-10002]、[WWDC21-10003]、[WWDC21-10005]、[WWDC21-10015]、[WWDC21-10032]
- **WWDC20**：47 场，代表来源：[WWDC20-10006]、[WWDC20-10033]、[WWDC20-10034]、[WWDC20-10035]、[WWDC20-10036]

## 决策启发式

- 已有音视频项目 ：立刻去 Developer Portal 申请 CarPlay Video entitlement。在代码里通过 CPSessionConfiguration 判断 supportsVideo，动态在 CPTabBarTemplate 里加一个“视频”Tab。别硬编码，不然老车主看到点不动的视频 Tab 会提一堆一星差评。
- 导航项目 ：全面接入 Route Sharing。现在的车机仪表盘越来越智能，把路线数据喂给车厂，能大幅提升你的 App 在车企预装白名单里的权重。
- UI 适配 ：CarPlay 的列表现在支持横竖图比例和复杂的 Overlay。把 CPListItem 的 image 和 detailText 利用起来，特别是 CPPlaybackConfiguration，一定要在播放状态改变时实时更新，别让用户看到进度条卡死。
- 已有项目的迁移策略 ：如果你之前的实时活动只写了锁屏和灵动岛竖屏视图，现在必须加上 isDynamicIslandLimitedInWidth 和 activityFamily 的判断。不用重写整个 UI，只需要在现有的 SwiftUI 视图外层套一层条件判断，把长文本换成图标，把复杂列表换成单行状态即可。
- 新项目的采用建议 ：严格分离静态数据和动态数据。把永远不变的字段（如店铺名、订单号）放在 ActivityAttributes 里，把随时间变化的字段（如状态、倒计时）放在 ContentState 里。这不仅是 Apple 的强制要求，更能大幅减少推送更新的 payload 体积。
- 实战中容易踩的坑 ：推送更新策略的选择。如果你的 App 是赛事直播，几万人同时看一场比赛，一定要用广播频道（Channel）推送更新，而不是给每个设备单独发 Push。单播推送在并发量高时极易触发 APNs 的限流，导致部分用户的实时活动卡死在旧状态。
- 老项目迁移 ：如果你之前用 Core ML 跑自定义的分割模型或者 OCR，先评估下 Vision 的新 API 和 Foundation Models 的内置 Tool 能不能平替。端侧内置模型的功耗和内存占用通常比你自己跑的 Core ML 模型好得多。
- 新项目采用 ：做图像分析时，优先用 Foundation Models 加 Tool Calling 的组合。不要试图让 LLM 直接输出条形码内容或者精确的像素坐标，让它调用 Vision 工具去做。
- 避坑指南 ：Tap to segment 是异步且需要下载模型的，在 UI 上一定要做好 loading 状态和模型下载进度的提示，别让用户点了没反应以为 App 卡死了。可以用 downloadAssets API 提前在后台拉取模型。
- 老项目迁移 ：全局搜索你的 Widget 代码，把所有硬编码的背景色替换为 .containerBackground(for: .widget)。检查所有包含图片或复杂渐变的 View，评估是否需要加上 .widgetAccentedRenderingMode(.fullColor) 以防在 Tinted 模式下“毁容”。

## 反模式与坑

- 骑行功率区间（Cycling Power Zones）原生支持 ：和心率区间共用一套 API 结构，只要把 HKQuantityType 换成 .cyclingPower，骑行 App 开发者可以直接白嫖这套逻辑。
- 偏好区间跨设备同步 ：用户在 iPhone 健康 App 里手动微调的区间阈值，会通过 iCloud 同步到 Apple Watch，App 不需要自己做配置下发。
- 区间来源溯源 ：HKWorkoutZoneConfiguration 里的 source 枚举可以告诉你这个区间是系统自动算的、用户手改的、还是你的 App 自定义的，方便在 UI 上给用户做差异化提示。
- CarPlay Simulator 史诗级增强 ：现在可以直接在 Mac 上模拟不同车型的硬件配置（比如是否带视频支持），不用再苦等真车测试了。
- Detail Header (详细头部) ：列表顶部新增了一个大卡片 UI，适合放“正在播放的播客”或“电影简介”，下面再跟推荐列表，视觉层级终于合理了。
- 体育比分 Overlay ：列表缩略图现在原生支持叠加左右球队 Logo 和实时比分，做体育类 App 的开发者可以直接白嫖这套 UI 了。
- staleDate 的妙用 ：在 ContentState 中设置 staleDate，当超过这个时间系统还没收到新推送时，UI 会自动变灰或显示过期样式，防止用户看到错误的倒计时。
- 提前安排实时活动 ：除了前台直接启动，现在支持通过 ActivityKit 提前 schedule 一个实时活动，比如在用户买完电影票后，安排电影开场前一小时自动弹出。

## 高频主题

`SwiftUI` (9)、`系统服务` (7)、`WidgetKit` (4)、`HealthKit` (3)、`watchOS` (3)、`App Intents` (3)、`应用服务` (3)、`Health & Fitness` (3)、`Design` (3)、`CarPlay` (2)、`Live Activities` (2)、`MapKit` (2)、`隐私与安全` (2)、`HKWorkout` (1)、`Heart Rate Zones` (1)、`CarPlay framework` (1)、`MiniPlayer` (1)、`Voice Control` (1)

## 关键 Session

- [WWDC26-207] 利用 HealthKit 体能训练区间提供健身洞察：这场 Session 最值得关注的一件事是：HealthKit 终于把“计算和存储心率/功率区间”这个脏活累活彻底接管了，健身 App 开发者再也不用自己手写区间统计算法和状态机了。
- [WWDC26-212] 为你的 CarPlay 车载 App 加足马力：这场 Session 最值得关注的一件事是：CarPlay 终于把触角伸向了“停车场景”，通过新增 Video App 类别和全局 Voice Control 模板，Apple 正在把 CarPlay 从单纯的“驾驶辅助工具”变成“座舱娱乐与交互中枢”。
- [WWDC26-223] 实时活动基础知识：这场 Session 最值得关注的一件事是：灵动岛（Dynamic Island）终于支持横屏了，Apple 提供了一套全新的环境变量（Environment Values）让你用极少的代码搞定横屏、待机显示（StandBy）和 Apple Watch 的 UI 适配灾难。
- [WWDC26-237] 图像理解方面的新动向：这场 Session 最值得关注的一件事是：Apple 终于把 Vision 框架的“像素级操作”和 Foundation Models 的“语义级理解”通过 Tool Calling 彻底打通了，以后做图像分析不用再在 CV 模型和 LLM 之间手动倒腾数据了。
- [WWDC26-262] Swift 的新功能：这场 Session 最值得关注的一件事是：Swift 终于把所有权系统（Ownership System）全面铺开到非拷贝类型（Noncopyable Types），让底层性能优化从“语法实验”变成了真正能写进生产环境的利器，顺手还用 anyAppleOS 干掉了折磨大家十年的多端可用性样板代码。
- [WWDC26-277] WidgetKit 基础知识：别指望看到颠覆性的 Widget 新玩法，这是一场给新手打底、给老手查漏补缺的“规范课”，最大的干货是明确了 Tinted/Clear 模式的适配边界和刷新预算的潜规则。
- [WWDC26-345] 探索 App Intents 框架的新功能：这场 Session 最值得关注的一件事是：App Intents 终于通过 EntityCollection 和 LongRunningIntent 摘掉了“只能处理小数据的 30 秒玩具”的帽子，正式具备了接管生产环境重活的能力。
- [WWDC26-369] 通过 Bluetooth Channel Sounding 查找你的配件：这场 Session 最值得关注的一件事是：Bluetooth Channel Sounding (蓝牙信道探测) 终于让纯蓝牙配件摆脱了 RSSI (接收信号强度指示) 测距的“玄学”，但“仅限前台”的限制说明苹果在功耗和射频干扰上还没完全搞定，目前它更适合“主动寻找”而非“无感追踪”。
- [WWDC26-378] 通过 StoreKit 和后台资源解锁游戏内内容：✅ Apple 官方下场帮 Unity 开发者把 Steam 资产和 IAP 无缝搬到 Apple 平台了，这是明抢 PC 游戏开发者。
- [WWDC26-389] 探索容器机：这场 Session 最值得关注的一件事是：Mac 上的 Linux 开发终于告别了 Docker Desktop 的笨重和传统虚拟机的割裂，Container machine (容器机) 把持久化 Linux 环境做成了 macOS 的原生延伸。
- [WWDC25-202] Wallet 新特性：如果你做票务或航空 App，今年 Wallet 的更新能让你砍掉一半的推送逻辑和通行证管理代码——前提是你愿意把航班状态追踪这类核心体验交给 Apple 的系统服务。
- [WWDC25-204] 深入探索 MapKit：如果你的 app 里有任何"把别人的地点 ID 塞进 MapKit"的胶水代码，这场 Session 直接帮你删掉它。
- [WWDC25-207] MapKit 新特性：MapKit 终于从"给你一个地图，自己贴标签"进化成"你可以定义地图长什么样"，这对所有在应用里做品牌化地图体验的团队来说是质变。
- [WWDC25-208] HealthKit 新特性：HealthKitUI 的推出比新增的情绪数据类型影响更大——它宣告 Apple 认为健康数据可视化应该是系统级能力，不是每个 App 自己用 Charts 库画的活儿。
- [WWDC25-213] Foundation 新特性：如果你还在用 NSPredicate 字符串表达式做过滤，这次更新给了你一个必须迁移的理由—— Predicate 宏把运行时炸弹拆成了编译时错误。
- [WWDC25-215] 小组件新特性：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。
- [WWDC25-217] CarPlay 新特性：CarPlay 终于不再是导航和音乐播放器的独角戏了——WidgetKit 和 Live Activities 的引入，让任何有实时状态信息的应用都有机会出现在驾驶场景中，但谁先做出适配谁就能吃到红利。
- [WWDC25-218] watchOS 新特性：watchOS 26 把 Apple Watch 的应用分发逻辑从"用户找应用"翻转成了"系统替用户挑应用"——RelevanceKit 才是这场 Session 里真正改变游戏规则的东西。
