# SwiftUI

## 领域判断

声明式 UI、布局、导航、动画、Observation 与 SwiftUI 性能。本领域覆盖 147 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **SwiftUI & UI Frameworks**：Widget 终于能从服务端推送更新了——不再需要 App 主动轮询或者依赖 Timeline 调度；visionOS 和 CarPlay 的加入让 Widget 的覆盖面又扩大了一圈；watchOS 的 Relevance Widget 则是直接解决了"不相关 Widget 堵 Smart Stack"的老问题。；UIScene 生命周期即将变成强制要求——现在不迁移以后编译都过不了。但 Apple 给的迁移路径其实很清晰：Scene 管生命周期和状态恢复，SplitView/TabBar 管布局适应，Safe Area + Layout Guide 管自适应 UI。问题在于老项目的迁移成本。；SwiftUI 的无障碍不是"事后补丁"而是"设计输出"——你的 View 代码同时在生成视觉界面和无障碍元素树，理解这个机制才能写出真正好用的 App。 来源：[WWDC25-278]、[WWDC25-282]、[WWDC24-10073]、[WWDC24-10118]
- **WindowGroup**：SwiftUI 在 macOS Sequoia 上终于补齐了窗口定制的三块拼图——toolbar 样式、窗口行为、窗口位置——让 SwiftUI macOS App 不再只能用千篇一律的系统默认窗口。；如果你的 visionOS 或 macOS App 需要多窗口交互——尤其是控制面板、详情面板这类辅助窗口——这场 Session 介绍的 WindowPlacement、pushWindow 和 defaultWindowPlacement 就是你要找的东西。；SwiftUI 是空间计算平台的首选 UI 框架，系统本身从控制中心到 Safari 都用它构建。三种场景类型（窗口、体积、全空间）构成了 App 的完整形态。 来源：[WWDC24-10148]、[WWDC24-10149]、[WWDC23-10109]、[WWDC23-10111]
- **Swift & UI**：StoreKit 终于有了原生的 SwiftUI 视图，几行代码就能搭建完整的内购商店界面。；两位 Maps 团队的设计师分享了他们用 SwiftUI 在设备上直接做设计的实践经验——这对设计师来说是必看的一场。；UICollectionView 的 cell prefetching 和差异更新（Diffable Data Source）在 iOS 15 中做了性能优化——但真正的性能飞跃来自正确使用 cell registration 和避免在 cellForItemAt 中做布局计算。 来源：[WWDC23-10013]、[WWDC23-10115]、[WWDC21-10252]、[WWDC21-10259]
- **Observable**：如果你之前在 SwiftUI 里用 UIViewRepresentable 包装 WKWebView，现在可以把那坨胶水代码删掉了——WebKit for SwiftUI 的原生 API 把 web 内容集成简化到了"传个 URL 就行"的程度。；UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。；SwiftUI 和 RealityKit 终于从"各干各的"变成了"双向奔赴"——Entity 现在可以当数据模型用，SwiftUI 动画可以直接驱动 RealityKit 组件变化。但双向数据流是把双刃剑，用不好就会陷入无限循环。 来源：[WWDC25-231]、[WWDC25-268]、[WWDC25-274]、[WWDC25-306]
- **ScrollView**：SwiftUI 今年给了你 Mesh Gradient、scroll transition 增强、TextRenderer 和 Metal shader 直接写 view modifier 这四把刷子——以前需要手动管理 Core Animation layer 或写大量 UIKit bridge 的视觉效果，现在全部声明式搞定。；TVMLKit 在 tvOS 18 正式被标记为 deprecated，SwiftUI 已经完全具备了构建媒体目录和流媒体 app 的能力——如果你还在维护 TVML 项目，这场 Session 就是你的迁移路线图。；SwiftUI 的 ScrollView 在 iOS 17 获得了分页对齐、容器相对布局、自定义滚动行为和滚动转场动画——终于可以替代大部分手写滚动逻辑了。 来源：[WWDC24-10151]、[WWDC24-10207]、[WWDC23-10159]、[WWDC20-10031]
- **Task**：三行代码就能把你的 SwiftUI 视图变成一个沉浸式空间体验——ImmersiveSpace 就是这么简单。；这场 Session 是 Instruments 卡顿分析的实战教学——从人类感知阈值出发，用灯泡实验解释为什么 100ms 是"即时感"的生死线，然后用三种典型的卡顿模式演示如何在 Instruments 中定位和修复问题。；CarPlay 今年开了两个新的应用类型入口（Fueling 和 Driving Task），同时推出了 CarPlay Simulator 这个开发利器——你终于不用跑到车里去调试了。 来源：[WWDC23-10111]、[WWDC23-10248]、[WWDC22-10016]、[WWDC21-10176]
- **AppIntent**：iOS 18 把 App Intents 的定位从"少数常用操作暴露给系统"变成了"你 App 做的每件事都应该是一个 Intent"——这意味着 App Intents 的设计质量直接决定了你的 App 在 Spotlight、Shortcuts、Siri、Action Button 等系统入口的表现。；App Intents 不是某一个功能，而是 Siri、Spotlight、Shortcuts、Widgets、Control Center 等全系系统体验的统一底座——写一次 Intent，你的应用功能就能渗透到设备的每个角落。；Widget 终于支持动画和交互了——用 App Intents 驱动按钮和开关操作，用 SwiftUI 的动画 API 让内容切换有感知力，再加上新的 Preview API 实时预览动画效果，这让 Widget 从"静态信息卡"变成了"可以操作的迷你 App"。 来源：[WWDC24-10176]、[WWDC24-10210]、[WWDC23-10028]、[WWDC22-10170]

## API 演进时间线

- **WWDC25**：30 场，代表来源：[WWDC25-207]、[WWDC25-208]、[WWDC25-210]、[WWDC25-215]、[WWDC25-219]
- **WWDC24**：28 场，代表来源：[WWDC24-10073]、[WWDC24-10075]、[WWDC24-10118]、[WWDC24-10134]、[WWDC24-10136]
- **WWDC23**：25 场，代表来源：[WWDC23-10013]、[WWDC23-10028]、[WWDC23-10036]、[WWDC23-10043]、[WWDC23-10055]
- **WWDC22**：22 场，代表来源：[WWDC22-10001]、[WWDC22-10016]、[WWDC22-10049]、[WWDC22-10051]、[WWDC22-10052]
- **WWDC21**：16 场，代表来源：[WWDC21-10017]、[WWDC21-10018]、[WWDC21-10019]、[WWDC21-10022]、[WWDC21-10023]
- **WWDC20**：26 场，代表来源：[WWDC20-10026]、[WWDC20-10028]、[WWDC20-10031]、[WWDC20-10033]、[WWDC20-10037]

## 决策启发式

- 立即迁移到 Locale.preferredLocales 。如果你的 app 有语言选择器，用这个 API 把用户常用语言排在最前面，参考 Translate app 的交互模式。
- 确保你的文本视图使用 TextKit2 。如果你还在用 textView.layoutManager（TextKit1），Natural Selection 会被禁用。改为 textView.textLayoutManager。
- 如果你有自定义文本引擎 ，参考 Apple 的 Language Introspector 示例代码，使用新 API 根据文本内容判断书写方向。
- 日历相关功能考虑新增的 11 个 calendar identifier ，特别是如果你的用户群覆盖印度或韩国市场。
- 用 Coding Assistant 探索不熟悉的代码库时关闭自动应用修改，先理解模型的建议再决定是否采纳。
- 在 Signing & Capabilities 编辑器中统一管理 usage description，避免手动修改 Info.plist 导致的遗漏。
- 新项目开启 Explicitly Built Modules（Xcode 26 默认启用），享受 debugger 响应速度的显著提升。
- 用 UI 测试录制快速生成初始测试骨架，然后重构为 page object 模式以降低维护成本。
- 对有显著攻击面的 app（社交、消息、浏览器）启用 Enhanced Security capability。
- 使用 Xcode Organizer 的 Metric Recommendations 对照同类 app 评估自己的 launch time 等关键指标。

## 反模式与坑

- MapCamera 动画不要在短时间内连续触发，否则会导致动画堆叠和卡顿，需要自己做节流。
- MapItemDetail 需要设备有地图数据，模拟器上的功能可能受限，真机测试是必须的。
- 自定义样式的 JSON 放在 Bundle 里按环境区分（开发/生产），别把调试用的夸张配色带到线上。
- 运动恢复指数（Recovery Index）是配合 Apple Watch 新传感器的数据类型，适合健身 App 从"记录训练"升级到"指导恢复"，但数据源目前主要依赖 Apple Watch。
- HKAuthorizationRequest 新增了按时间段授权的能力，用户可以只授权最近三个月的数据而不是全部历史，这对隐私敏感型用户是个大加分。
- HealthKitUI 仅在 iOS 19+ 可用，没有向下兼容方案，如果你的 min deployment target 还在 iOS 17，这个框架暂时用不了。
- PHPicker 主题自定义 ：选择器现在支持自定义外观，终于能和你的 App 视觉风格保持一致了，不用再忍受那个突兀的系统默认样式。
- 细粒度变更观察 ：PHPhotoLibraryChangeObservation 可以按特定相册或资产类型监听变更，替换掉旧的全量观察者能显著降低后台资源消耗。

## 高频主题

`SwiftUI` (28)、`Design` (10)、`Swift` (4)、`空间计算` (4)、`UIKit` (3)、`应用服务` (3)、`开发工具` (3)、`Liquid Glass` (2)、`MapKit` (1)、`地图` (1)、`导航` (1)、`定位` (1)、`HealthKit` (1)、`健康` (1)、`隐私` (1)、`数据共享` (1)、`Photos` (1)、`PHPicker` (1)

## 关键 Session

- [WWDC25-207] MapKit 新特性：MapKit 终于从"给你一个地图，自己贴标签"进化成"你可以定义地图长什么样"，这对所有在应用里做品牌化地图体验的团队来说是质变。
- [WWDC25-208] HealthKit 新特性：HealthKitUI 的推出比新增的情绪数据类型影响更大——它宣告 Apple 认为健康数据可视化应该是系统级能力，不是每个 App 自己用 Charts 库画的活儿。
- [WWDC25-210] Photos 新特性：Apple 终于把照片库的"理解能力"交给了第三方——PhotoAnalysis API 是今年 Photos 框架里真正改变游戏规则的东西，PHPicker 智能筛选和编辑管线反而是锦上添花。
- [WWDC25-215] 小组件新特性：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。
- [WWDC25-219] tvOS 新特性：如果你只做一件事：把你的 tvOS 应用的焦点管理从 UIKit 迁到 SwiftUI 的新 @FocusState 体系，这是回报最高的投入。
- [WWDC25-221] 辅助功能新特性：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。
- [WWDC25-222] Enhance your app's multilingual experience：Locale.preferredLanguages 返回的 String 数组终于要被 Locale.preferredLocales 取代了，双向文本的 Natural Selection 从 macOS 扩展到了 iOS 如果你的 app 做国际化，这两个 API 变化直接影响你的代码。
- [WWDC25-231] 认识 WebKit for SwiftUI：如果你之前在 SwiftUI 里用 UIViewRepresentable 包装 WKWebView，现在可以把那坨胶水代码删掉了——WebKit for SwiftUI 的原生 API 把 web 内容集成简化到了"传个 URL 就行"的程度。
- [WWDC25-247] Xcode 26 新特性详解：Xcode 26 最大的卖点是 LLM 驱动的 Coding Assistant 正式落地，但更实在的进步是 build 加速、debugger 改善、以及 UI testing 的代码生成革命。
- [WWDC25-256] SwiftUI 年度更新：Liquid Glass、性能飞跃与三维布局：SwiftUI 今年的更新覆盖了从视觉到性能到生态的全链路——Liquid Glass 设计语言让你重新编译就焕然一新，列表性能提升 16 倍，WebView 和富文本终于官方支持，visionOS 三维布局正式成型。
- [WWDC25-266] SwiftUI 中的并发探索：@MainActor 默认、后台优化与数据竞争防护：SwiftUI 的并发模型可以用一句话概括：@MainActor 是编译期默认，Sendable 是后台优化的信号灯。SwiftUI 的注解表达的是运行时语义——View 默认主线程、Shape/visualEffect/Layout 可能后台调用。理解了这一点，你就不需要害怕并发。
- [WWDC25-267] SwiftUI 新特性：SwiftUI 这次最值得关注的不是 Liquid Glass 的视觉变化，而是 TextEditor 终于支持了 AttributedString——用纯 SwiftUI 构建富文本编辑器第一次成为现实。
- [WWDC25-268] UIKit 新特性：UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。
- [WWDC25-273] SwiftUI 空间布局入门：用 2D 思维构建 3D 体验：如果你熟悉 SwiftUI 的 2D 布局（VStack/HStack/alignment），现在可以直接用同样的心智模型构建 visionOS 的 3D 体验——每个视图多了 depth 和 Z position，alignment 多了深度维度，新增的 rotation3DLayout 和 SpatialContainer 解决了 2D modifier 在 3D 空间中的失效问题。
- [WWDC25-274] SwiftUI 与 RealityKit 的合体之路：SwiftUI 和 RealityKit 终于从"各干各的"变成了"双向奔赴"——Entity 现在可以当数据模型用，SwiftUI 动画可以直接驱动 RealityKit 组件变化。但双向数据流是把双刃剑，用不好就会陷入无限循环。
- [WWDC25-278] Widget 新特性：Widget 终于能从服务端推送更新了——不再需要 App 主动轮询或者依赖 Timeline 调度；visionOS 和 CarPlay 的加入让 Widget 的覆盖面又扩大了一圈；watchOS 的 Relevance Widget 则是直接解决了"不相关 Widget 堵 Smart Stack"的老问题。
- [WWDC25-280] 实战：用 AttributedString 在 SwiftUI 中构建富文本编辑：TextEditor 的类型从 String 换成 AttributedString 就能解锁富文本编辑——但这只是起点，真正的问题在于 AttributedString 的 Index 失效机制和 RangeSet 的双向文本语义，不了解这些就会在"修改文本后光标跳到末尾"的坑里出不来。
- [WWDC25-282] 让 UIKit 应用更灵活：UIScene 生命周期即将变成强制要求——现在不迁移以后编译都过不了。但 Apple 给的迁移路径其实很清晰：Scene 管生命周期和状态恢复，SplitView/TabBar 管布局适应，Safe Area + Layout Guide 管自适应 UI。问题在于老项目的迁移成本。
