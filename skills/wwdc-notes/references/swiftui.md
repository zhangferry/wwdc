# SwiftUI

## 领域判断

声明式 UI、布局、导航、动画、Observation 与 SwiftUI 性能。本领域覆盖 173 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **SwiftUI & UI Frameworks**：Widget 终于能从服务端推送更新了——不再需要 App 主动轮询或者依赖 Timeline 调度；visionOS 和 CarPlay 的加入让 Widget 的覆盖面又扩大了一圈；watchOS 的 Relevance Widget 则是直接解决了"不相关 Widget 堵 Smart Stack"的老问题。；UIScene 生命周期即将变成强制要求——现在不迁移以后编译都过不了。但 Apple 给的迁移路径其实很清晰：Scene 管生命周期和状态恢复，SplitView/TabBar 管布局适应，Safe Area + Layout Guide 管自适应 UI。问题在于老项目的迁移成本。；SwiftUI 的无障碍不是"事后补丁"而是"设计输出"——你的 View 代码同时在生成视觉界面和无障碍元素树，理解这个机制才能写出真正好用的 App。 来源：[WWDC25-278]、[WWDC25-282]、[WWDC24-10073]、[WWDC24-10118]
- **WindowGroup**：SwiftUI 在 macOS Sequoia 上终于补齐了窗口定制的三块拼图——toolbar 样式、窗口行为、窗口位置——让 SwiftUI macOS App 不再只能用千篇一律的系统默认窗口。；如果你的 visionOS 或 macOS App 需要多窗口交互——尤其是控制面板、详情面板这类辅助窗口——这场 Session 介绍的 WindowPlacement、pushWindow 和 defaultWindowPlacement 就是你要找的东西。；SwiftUI 是空间计算平台的首选 UI 框架，系统本身从控制中心到 Safari 都用它构建。三种场景类型（窗口、体积、全空间）构成了 App 的完整形态。 来源：[WWDC24-10148]、[WWDC24-10149]、[WWDC23-10109]、[WWDC23-10111]
- **ScrollView**：这场 Session 最值得关注的一件事是：Apple 终于承认 AI 直接生成的 UI 通常是垃圾，并手把手教你如何用“多变体对比”和“实时调试面板”把 Xcode Agent 从盲盒玩具驯化成可控的设计工具。；这场 Session 最值得关注的一件事是：Apple 终于把 Lazy Stack（惰性堆栈）的“黑盒”估算机制和预取行为扒光了给你看，明确告诉你为什么长列表滚动会掉帧，以及为什么在 onAppear 里干活是性能杀手。；SwiftUI 今年给了你 Mesh Gradient、scroll transition 增强、TextRenderer 和 Metal shader 直接写 view modifier 这四把刷子——以前需要手动管理 Core Animation layer 或写大量 UIKit bridge 的视觉效果，现在全部声明式搞定。 来源：[WWDC26-227]、[WWDC26-321]、[WWDC24-10151]、[WWDC24-10207]
- **Swift & UI**：StoreKit 终于有了原生的 SwiftUI 视图，几行代码就能搭建完整的内购商店界面。；两位 Maps 团队的设计师分享了他们用 SwiftUI 在设备上直接做设计的实践经验——这对设计师来说是必看的一场。；UICollectionView 的 cell prefetching 和差异更新（Diffable Data Source）在 iOS 15 中做了性能优化——但真正的性能飞跃来自正确使用 cell registration 和避免在 cellForItemAt 中做布局计算。 来源：[WWDC23-10013]、[WWDC23-10115]、[WWDC21-10252]、[WWDC21-10259]
- **Observable**：这场 Session 最值得关注的一件事是：AppKit 和 UIKit 的原生视图（NSView/UIView）终于能直接“白嫖” @Observable 的自动刷新机制了，老项目混编最恶心的手动状态同步彻底成为历史。；如果你之前在 SwiftUI 里用 UIViewRepresentable 包装 WKWebView，现在可以把那坨胶水代码删掉了——WebKit for SwiftUI 的原生 API 把 web 内容集成简化到了"传个 URL 就行"的程度。；UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。 来源：[WWDC26-272]、[WWDC25-231]、[WWDC25-268]、[WWDC25-274]
- **Liquid Glass**：这场 Session 最值得关注的一件事是：@State 属性包装器（Property Wrapper）被重构成了 Macro（宏），实现了对象引用的惰性初始化（Lazy Initialization），并且苹果把这个性能红利直接向下兼容到了 iOS 17 和 macOS 14。；✅ AppKit 彻底抛弃 mouseDown: 转向手势识别器（Gesture Recognizers），并用全新的“边角同心性（Concentricity）”API 终结了 macOS 嵌套圆角对不齐的强迫症。；✅ iOS 搜索框官方终于“妥协”推荐放底部工具栏了，配合全新的 Liquid Glass（液态玻璃）材质，大屏手机的单手搜索体验迎来史诗级救赎。 来源：[WWDC26-269]、[WWDC26-289]、[WWDC26-292]、[WWDC25-267]
- **MainActor**：这场 Session 最值得关注的一件事是：AppKit 和 UIKit 的原生视图（NSView/UIView）终于能直接“白嫖” @Observable 的自动刷新机制了，老项目混编最恶心的手动状态同步彻底成为历史。；SwiftUI 的并发模型可以用一句话概括：@MainActor 是编译期默认，Sendable 是后台优化的信号灯。SwiftUI 的注解表达的是运行时语义——View 默认主线程、Shape/visualEffect/Layout 可能后台调用。理解了这一点，你就不需要害怕并发。；Swift 6 语言模式带来了编译期的 data race 安全检查——如果你写并发代码，这是今年最重要的更新，但迁移策略一定要"渐进式"而不是"一步到位"。 来源：[WWDC26-272]、[WWDC25-266]、[WWDC24-10136]、[WWDC24-10169]

## API 演进时间线

- **WWDC26**：26 场，代表来源：[WWDC26-102]、[WWDC26-112]、[WWDC26-203]、[WWDC26-213]、[WWDC26-227]
- **WWDC25**：30 场，代表来源：[WWDC25-207]、[WWDC25-208]、[WWDC25-210]、[WWDC25-215]、[WWDC25-219]
- **WWDC24**：28 场，代表来源：[WWDC24-10073]、[WWDC24-10075]、[WWDC24-10118]、[WWDC24-10134]、[WWDC24-10136]
- **WWDC23**：25 场，代表来源：[WWDC23-10013]、[WWDC23-10028]、[WWDC23-10036]、[WWDC23-10043]、[WWDC23-10055]
- **WWDC22**：22 场，代表来源：[WWDC22-10001]、[WWDC22-10016]、[WWDC22-10049]、[WWDC22-10051]、[WWDC22-10052]
- **WWDC21**：16 场，代表来源：[WWDC21-10017]、[WWDC21-10018]、[WWDC21-10019]、[WWDC21-10022]、[WWDC21-10023]
- **WWDC20**：26 场，代表来源：[WWDC20-10026]、[WWDC20-10028]、[WWDC20-10031]、[WWDC20-10033]、[WWDC20-10037]

## 决策启发式

- 老项目迁移 ：如果你之前在用 Vision 框架的 VNRecognizeTextRequest 做手写识别，建议直接替换为 PKStrokeRecognizer。Vision 对印刷体很强，但对连笔手写的理解远不如 PencilKit 的原生引擎。
- 新项目采用 ：把 PencilKit 当作数据层和识别层，UI 层可以根据需求选择 PKCanvasView 或自定义渲染。利用 PKStroke 新增的稳定 Identifiable (UUID) 来管理你的业务逻辑状态，这样在执行 Undo/Redo 时，你能精准追踪到具体是哪一笔发生了变化。
- 性能避坑 ：在复杂绘图（几千个 Stroke）中使用 Stroke Slicing (笔画切割) 时，计算开销会呈指数级上升。尽量在用户停止绘制后的后台线程进行切割计算，或者限制单次切割的 Stroke 数量。另外，Simulator 目前只支持拉丁语系的识别，测试中日韩语言必须用真机。
- 新项目采用建议 ：把 ScriptGraph 当作“胶水”和“原型工具”。用它来处理手势反馈、简单的物理碰撞、动画状态机和 UI 触发时机。一旦涉及网络请求、复杂数据解析或 ECS 系统级查询，立刻切回 Swift 代码。
- 已有项目迁移 ：不需要把现有的 RealityKit 逻辑推翻重写。你可以把 ScriptGraph 生成的逻辑封装成独立的 Scripting Component，与现有的自定义 Component 和 System 共存。
- 实战避坑 ：在 ScriptGraph 里大量使用 Prototyped Subgraph（原型子图）来封装常用逻辑（比如“检测变量是否改变”）。如果不做封装，你的节点图在两周内就会变成无法维护的蜘蛛网。
- 已有项目的迁移策略 ：别一上来就让智能体重构核心逻辑。先让它跑一遍 Explore 流程，生成项目的架构文档。人工 Review 这些文档，修正 AI 理解错的地方，把这份文档作为后续 AI 协作的“基准线”。
- 新项目的采用建议 ：把智能体当成一个记忆力很好但缺乏业务常识的 Junior 开发。使用 Plan mode (计划模式) 让它先出方案，你通过 Queued messages (排队消息) 实时纠偏，确认架构没问题了再让它动手写代码。
- 实战避坑 ：千万别在聊天框里发几百字的长篇大论。把需求拆碎，利用 Xcode 的 Preview 和 Test 工具做闭环验证。AI 改完一步，立刻跑一次测试，别等它改完十个文件再跑，那时候报错你都找不到是哪一步引入的。
- 已有项目的迁移策略 ：别想着“一把梭”重写。最稳妥的起手式是把核心数据模型加上 @Observable 宏，让现有的 NSView/UIView 享受自动刷新；遇到需要大改 UI 或新增复杂交互的独立模块（比如新的设置面板、复杂的图表），直接用 SwiftUI 写，通过 NSHostingView 嵌进去；边缘 Scene（如菜单栏扩展）则可以通过 NSHostingSceneRepresentation 无缝替换。

## 反模式与坑

- Agentic coding (智能体编程) ：Xcode 里的 AI 助手现在能自己跑测试和修 Bug 了，写样板代码的效率大幅提升。
- Flexible UI layout (灵活 UI 布局) ：SwiftUI 新增了更细粒度的布局控制 API，终于不用为了一个奇葩的 UI 需求去桥接 UIKit 了。
- Liquid Glass 设计语言 ：去年的设计主题今年继续深化，系统控件的毛玻璃质感和光影效果有了更多可定制的参数。
- Liquid Glass 设计语言 ：UI 层面引入了类似 visionOS 的玻璃材质渲染，SwiftUI 新增了 .glassBackground() 修饰符，做毛玻璃效果终于不用自己手搓 Shader 了。
- Agentic Coding 增强 ：Xcode 里的 AI 代码补全现在能理解整个 Workspace 的上下文，甚至能帮你自动写 XCTest 单元测试，省去了写 boilerplate 的时间。
- SwiftUI 布局灵活性 ：新增了 AdaptiveStack，能优雅地处理 iPad 和 iPhone 之间横竖屏切换时的复杂嵌套布局，不用再写一堆 if horizontalSizeClass == .regular 了。
- 稳定的 Stroke ID ：PKStroke 终于遵循了 Identifiable，Undo/Redo 或跨设备同步时，再也不用靠坐标和颜色去猜是不是同一笔了。
- Wet ink 渲染控制 ：现在可以手动调整 renderGroupID，控制哪些笔画在渲染时被视为“墨水未干”的状态，方便做特殊的混合效果。

## 高频主题

`SwiftUI` (45)、`Design` (10)、`UIKit` (6)、`Liquid Glass` (5)、`Swift` (4)、`空间计算` (4)、`App Intents` (3)、`visionOS` (3)、`Observation` (3)、`应用服务` (3)、`开发工具` (3)、`Apple Intelligence` (2)、`Foundation Models` (2)、`Private Cloud Compute` (2)、`PencilKit` (2)、`Xcode Agents` (2)、`RealityKit` (2)、`AppKit` (2)

## 关键 Session

- [WWDC26-102] Platforms State of the Union：Apple 终于把大模型 API 开放给云端了，而且小开发者能免费使用 Private Cloud Compute (私有云计算) 额度，这是今年最实在的福利。
- [WWDC26-112] Platforms State of the Union (ASL)：Apple 终于向现实低头，Foundation Models 框架原生支持了云端大模型路由，还倒贴钱给中小开发者用 Private Cloud Compute。
- [WWDC26-203] 使用 PencilKit 解读笔触之间的奥秘：这场 Session 最值得关注的一件事是：Apple 终于把“备忘录”和“无边记”里那套极其好用的设备端手写识别引擎（PKStrokeRecognizer）开放给第三方了，而且直接做成了 Swift Actor。
- [WWDC26-213] 使用 Xcode 中的智能体翻译你的 App：Xcode 终于把 AI 翻译做成了原生工作流，靠 String Catalogs（字符串目录）攒了三年的工程上下文，这次大模型翻译不再是“人工智障”了。
- [WWDC26-227] 使用 Xcode 中的智能体创建 UI 原型：这场 Session 最值得关注的一件事是：Apple 终于承认 AI 直接生成的 UI 通常是垃圾，并手把手教你如何用“多变体对比”和“实时调试面板”把 Xcode Agent 从盲盒玩具驯化成可控的设计工具。
- [WWDC26-252] 使用 Reality Composer Pro 3 设计无代码游戏：这场 Session 最值得关注的一件事是：Reality Composer Pro 3 的 ScriptGraph 配合即将推出的 Vision Pro 实机 Live Preview，彻底把 visionOS 空间交互的“调参权”从程序员手里抢走，交给了设计师。
- [WWDC26-253] 了解 Music Understanding 框架：这场 Session 最值得关注的一件事是：苹果终于把 Final Cut Pro 里那套极其好用的音频节拍和结构分析能力，剥离出来做成了系统级的 MusicUnderstanding 框架，第三方 App 终于不用自己手搓 FFT（快速傅里叶变换）或买昂贵的第三方 SDK 来做音乐卡点了。
- [WWDC26-254] 将 MusicKit 整合到你的 App 中：✅ MusicKit 终于把授权、选歌、播放和订阅转化打磨成了一套极其顺滑的 SwiftUI 原生体验，非音乐类 App 接入 Apple Music 的门槛降到了历史最低。
- [WWDC26-259] 在 Xcode 中与智能体协作开发：Xcode 27 的编码智能体 (Coding agents) 终于从“只会补全代码的打字员”变成了“能读懂祖传代码并自己拆包分发的包工头”。
- [WWDC26-269] SwiftUI 的新功能：这场 Session 最值得关注的一件事是：@State 属性包装器（Property Wrapper）被重构成了 Macro（宏），实现了对象引用的惰性初始化（Lazy Initialization），并且苹果把这个性能红利直接向下兼容到了 iOS 17 和 macOS 14。
- [WWDC26-271] 跟随编程：使用 SwiftUI 构建强大的拖放功能：SwiftUI 的拖放终于从“玩具级”进化到了“生产力级”，reorderContainer 让跨列/跨容器的复杂重排（比如看板、纸牌游戏）不再需要求助于 UIKit。
- [WWDC26-272] 将 SwiftUI 与 AppKit 和 UIKit 搭配使用：这场 Session 最值得关注的一件事是：AppKit 和 UIKit 的原生视图（NSView/UIView）终于能直接“白嫖” @Observable 的自动刷新机制了，老项目混编最恶心的手动状态同步彻底成为历史。
- [WWDC26-274] SwiftData 的新功能：这场 Session 最值得关注的一件事是：SwiftData 终于把数据监听能力从 SwiftUI 视图里剥离出来了，ModelResultsObserver 让你能在纯 ViewModel 或后台服务里优雅地响应数据库变化，不用再写恶心的 workaround。
- [WWDC26-275] 跟随编程：使用 SwiftData 添加持久化功能：这场 Session 最值得关注的一件事是：SwiftData 迁移绝不是无脑加 @Model 宏，它强迫你重构底层数据结构（比如把 Enum 拍平成 Class 继承），并且苹果终于用全新的 withContinuousObservation API 解决了 @Model 里 didSet 失效的痛点。
- [WWDC26-277] WidgetKit 基础知识：别指望看到颠覆性的 Widget 新玩法，这是一场给新手打底、给老手查漏补缺的“规范课”，最大的干货是明确了 Tinted/Clear 模式的适配边界和刷新预算的潜规则。
- [WWDC26-278] 升级改造你的 UIKit App：iPhone App 在 Mac (iPhone Mirroring) 和 iPad 上变成了“完全可自由拉伸的窗口”，这直接宣判了 UIScreen.main 和硬编码设备类型的死刑，逼迫所有 UIKit 老项目必须彻底拥抱 Size Classes (尺寸类别)。
- [WWDC26-286] 使用 Foveated Streaming 将沉浸式内容融入 visionOS：这场 Session 最值得关注的一件事是：Apple 终于官方下场做“串流”了，FoveatedStreaming 框架让 visionOS 能直接当 PC 的“高级显示器”，把跑不动的重度 OpenXR 应用通过眼动追踪优化带宽后无线串流过来，而且还能和原生 3D 物体无缝缝合。
- [WWDC26-289] 升级改造你的 AppKit App：✅ AppKit 彻底抛弃 mouseDown: 转向手势识别器（Gesture Recognizers），并用全新的“边角同心性（Concentricity）”API 终结了 macOS 嵌套圆角对不齐的强迫症。
