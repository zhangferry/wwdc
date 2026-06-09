# SwiftUI

## 领域判断

声明式 UI、布局、导航、动画、Observation 与 SwiftUI 性能。本领域覆盖 166 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **SwiftUI & UI Frameworks**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何在 Reality Composer Pro 3 中使用 ScriptGraph 为你的 App 和游戏开发无代码 3D 内容。了解如何利用可视化节点来构建动画、创建互动时刻，并整合 SwiftUI 元素，为你的体验添加对话气泡和其他 UI。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 SwiftUI 的新增功能，了解这些功能如何提升你的 App。我们将介绍的内容有：一种新的 Document 协议，支持直接磁盘访问和快照差异比对，助你构建高性能 App；一系列全新 API，用于在列表、网格和分区中重新排列内容；以及工具栏增强功能，包括可见性优先级和自动最小化行为。我们还将介绍扩展的呈现 API，包括可在任意视图上实现的轻扫操作、AsyncImage 缓存改进，以及 Observable 类型的惰性状态初始化。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：跟着我们的演示一起构建一款单人纸牌游戏，探索 SwiftUI 支持的最… 来源：[WWDC26-252]、[WWDC26-269]、[WWDC26-271]、[WWDC26-272]
- **WindowGroup**：SwiftUI 在 macOS Sequoia 上终于补齐了窗口定制的三块拼图——toolbar 样式、窗口行为、窗口位置——让 SwiftUI macOS App 不再只能用千篇一律的系统默认窗口。；如果你的 visionOS 或 macOS App 需要多窗口交互——尤其是控制面板、详情面板这类辅助窗口——这场 Session 介绍的 WindowPlacement、pushWindow 和 defaultWindowPlacement 就是你要找的东西。；SwiftUI 是空间计算平台的首选 UI 框架，系统本身从控制中心到 Safari 都用它构建。三种场景类型（窗口、体积、全空间）构成了 App 的完整形态。 来源：[WWDC24-10148]、[WWDC24-10149]、[WWDC23-10109]、[WWDC23-10111]
- **Swift & UI**：StoreKit 终于有了原生的 SwiftUI 视图，几行代码就能搭建完整的内购商店界面。；两位 Maps 团队的设计师分享了他们用 SwiftUI 在设备上直接做设计的实践经验——这对设计师来说是必看的一场。；UICollectionView 的 cell prefetching 和差异更新（Diffable Data Source）在 iOS 15 中做了性能优化——但真正的性能飞跃来自正确使用 cell registration 和避免在 cellForItemAt 中做布局计算。 来源：[WWDC23-10013]、[WWDC23-10115]、[WWDC21-10252]、[WWDC21-10259]
- **Observable**：如果你之前在 SwiftUI 里用 UIViewRepresentable 包装 WKWebView，现在可以把那坨胶水代码删掉了——WebKit for SwiftUI 的原生 API 把 web 内容集成简化到了"传个 URL 就行"的程度。；UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。；SwiftUI 和 RealityKit 终于从"各干各的"变成了"双向奔赴"——Entity 现在可以当数据模型用，SwiftUI 动画可以直接驱动 RealityKit 组件变化。但双向数据流是把双刃剑，用不好就会陷入无限循环。 来源：[WWDC25-231]、[WWDC25-268]、[WWDC25-274]、[WWDC25-306]
- **ScrollView**：SwiftUI 今年给了你 Mesh Gradient、scroll transition 增强、TextRenderer 和 Metal shader 直接写 view modifier 这四把刷子——以前需要手动管理 Core Animation layer 或写大量 UIKit bridge 的视觉效果，现在全部声明式搞定。；TVMLKit 在 tvOS 18 正式被标记为 deprecated，SwiftUI 已经完全具备了构建媒体目录和流媒体 app 的能力——如果你还在维护 TVML 项目，这场 Session 就是你的迁移路线图。；SwiftUI 的 ScrollView 在 iOS 17 获得了分页对齐、容器相对布局、自定义滚动行为和滚动转场动画——终于可以替代大部分手写滚动逻辑了。 来源：[WWDC24-10151]、[WWDC24-10207]、[WWDC23-10159]、[WWDC20-10031]
- **SwiftData**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 SwiftData 的最新增强功能。我们将介绍如何使用 Codable 持久保留自定类型和第三方类型的数据，并将获取的数据分组到 SwiftUI App 的各个分区。我们还将探索如何使用 ModelResultsObserver 和 HistoryObserver 在其他各处观察数据存储的变化，以便灵活地驱动强大的状态对象、与基于委托的架构实现整合，并精准地响应模型更新。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：跟着我们为现有 App 添加持久化功能的演示，体验 SwiftData 的实际应用。我们将介绍如何定义数据模型，并将持久数据无缝整合到 SwiftUI 中。你还将了解一些基础技能，以便利用这个富有表现力的声明式 API 来管理 App 状态。；如果你的 App 需要离线同步、Widget 数据回传或增量式 UI 更新，SwiftData History 是今年最值得直接上手的新 API 之一。 来源：[WWDC26-274]、[WWDC26-275]、[WWDC24-10075]、[WWDC24-10137]
- **Task**：三行代码就能把你的 SwiftUI 视图变成一个沉浸式空间体验——ImmersiveSpace 就是这么简单。；这场 Session 是 Instruments 卡顿分析的实战教学——从人类感知阈值出发，用灯泡实验解释为什么 100ms 是"即时感"的生死线，然后用三种典型的卡顿模式演示如何在 Instruments 中定位和修复问题。；CarPlay 今年开了两个新的应用类型入口（Fueling 和 Driving Task），同时推出了 CarPlay Simulator 这个开发利器——你终于不用跑到车里去调试了。 来源：[WWDC23-10111]、[WWDC23-10248]、[WWDC22-10016]、[WWDC21-10176]

## API 演进时间线

- **WWDC26**：19 场，代表来源：[WWDC26-203]、[WWDC26-213]、[WWDC26-252]、[WWDC26-269]、[WWDC26-271]
- **WWDC25**：30 场，代表来源：[WWDC25-207]、[WWDC25-208]、[WWDC25-210]、[WWDC25-215]、[WWDC25-219]
- **WWDC24**：28 场，代表来源：[WWDC24-10073]、[WWDC24-10075]、[WWDC24-10118]、[WWDC24-10134]、[WWDC24-10136]
- **WWDC23**：25 场，代表来源：[WWDC23-10013]、[WWDC23-10028]、[WWDC23-10036]、[WWDC23-10043]、[WWDC23-10055]
- **WWDC22**：22 场，代表来源：[WWDC22-10001]、[WWDC22-10016]、[WWDC22-10049]、[WWDC22-10051]、[WWDC22-10052]
- **WWDC21**：16 场，代表来源：[WWDC21-10017]、[WWDC21-10018]、[WWDC21-10019]、[WWDC21-10022]、[WWDC21-10023]
- **WWDC20**：26 场，代表来源：[WWDC20-10026]、[WWDC20-10028]、[WWDC20-10031]、[WWDC20-10033]、[WWDC20-10037]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 立即迁移到 Locale.preferredLocales 。如果你的 app 有语言选择器，用这个 API 把用户常用语言排在最前面，参考 Translate app 的交互模式。
- 确保你的文本视图使用 TextKit2 。如果你还在用 textView.layoutManager（TextKit1），Natural Selection 会被禁用。改为 textView.textLayoutManager。
- 如果你有自定义文本引擎 ，参考 Apple 的 Language Introspector 示例代码，使用新 API 根据文本内容判断书写方向。
- 日历相关功能考虑新增的 11 个 calendar identifier ，特别是如果你的用户群覆盖印度或韩国市场。
- 用 Coding Assistant 探索不熟悉的代码库时关闭自动应用修改，先理解模型的建议再决定是否采纳。
- 在 Signing & Capabilities 编辑器中统一管理 usage description，避免手动修改 Info.plist 导致的遗漏。
- 新项目开启 Explicitly Built Modules（Xcode 26 默认启用），享受 debugger 响应速度的显著提升。

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

`SwiftUI` (39)、`Design` (10)、`UIKit` (5)、`Swift` (4)、`空间计算` (4)、`应用服务` (3)、`开发工具` (3)、`AppKit` (2)、`SwiftData` (2)、`visionOS` (2)、`Liquid Glass` (2)、`PencilKit` (1)、`Xcode` (1)、`TextKit` (1)、`PaperKit` (1)、`SwiftUI & UI Frameworks` (1)、`MapKit` (1)、`地图` (1)

## 关键 Session

- [WWDC26-203] 使用 PencilKit 解读笔触之间的奥秘：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：运用“无边记”和“备忘录”等 Apple App 背后的强大技术，为你的 App 解锁手写识别功能。了解如何在各种字母和语言中使用手写识别，并探索如何利用新功能将 PencilKit 整合到多种多样的 App 中。
- [WWDC26-213] 使用 Xcode 中的智能体翻译你的 App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 Xcode 和编码智能体如何根据 App 的情境帮助你翻译字符串目录。我们将介绍审核翻译输出和迭代本地化的策略，以便你为全球用户提供量身定制的体验。
- [WWDC26-252] 使用 Reality Composer Pro 3 设计无代码游戏：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何在 Reality Composer Pro 3 中使用 ScriptGraph 为你的 App 和游戏开发无代码 3D 内容。了解如何利用可视化节点来构建动画、创建互动时刻，并整合 SwiftUI 元素，为你的体验添加对话气泡和其他 UI。
- [WWDC26-269] SwiftUI 的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 SwiftUI 的新增功能，了解这些功能如何提升你的 App。我们将介绍的内容有：一种新的 Document 协议，支持直接磁盘访问和快照差异比对，助你构建高性能 App；一系列全新 API，用于在列表、网格和分区中重新排列内容；以及工具栏增强功能，包括可见性优先级和自动最小化行为。我们还将介绍扩展的呈现 API，包括可在任意视图上实现的轻扫操作、AsyncImage 缓存改进，以及 Observable 类型的惰性状态初始化。
- [WWDC26-271] 跟随编程：使用 SwiftUI 构建强大的拖放功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：跟着我们的演示一起构建一款单人纸牌游戏，探索 SwiftUI 支持的最新拖放功能。我们将介绍如何使用新的重新排序 API 方便用户重新排列内容，通过实现拖移容器来批量移动项目，并根据你 App 的规则定制拖放生命周期。为了充分从这个讲座中获益，建议你观看 WWDC22 视频“Transferable 简介”。
- [WWDC26-272] 将 SwiftUI 与 AppKit 和 UIKit 搭配使用：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何在现有的 AppKit 或 UIKit App 中逐步采用 SwiftUI。我们将介绍如何使用 Observation 框架自动更新视图，将 SwiftUI 组件整合到现有的视图层次结构中，并将手势识别器引入 SwiftUI。我们还将探索如何向你的 App 添加完整的 SwiftUI 场景，同时不改变整体架构。
- [WWDC26-274] SwiftData 的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 SwiftData 的最新增强功能。我们将介绍如何使用 Codable 持久保留自定类型和第三方类型的数据，并将获取的数据分组到 SwiftUI App 的各个分区。我们还将探索如何使用 ModelResultsObserver 和 HistoryObserver 在其他各处观察数据存储的变化，以便灵活地驱动强大的状态对象、与基于委托的架构实现整合，并精准地响应模型更新。
- [WWDC26-275] 跟随编程：使用 SwiftData 添加持久化功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：跟着我们为现有 App 添加持久化功能的演示，体验 SwiftData 的实际应用。我们将介绍如何定义数据模型，并将持久数据无缝整合到 SwiftUI 中。你还将了解一些基础技能，以便利用这个富有表现力的声明式 API 来管理 App 状态。
- [WWDC26-278] 升级改造你的 UIKit App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 UIKit 的最新更新。了解如何更新 iPhone App 的布局，以便在调整大小时能够呈现出色效果，让你的 App 无论是通过 iPhone 镜像功能使用还是显示在 iPad 上都相宜。探索适用于标签栏和导航栏的全新 API，并了解如何针对 Apple 智能的新功能准备好的 App。我们还将介绍一种充分利用所选编码智能体的技巧，帮助你实现代码库现代化。
- [WWDC26-286] 使用 Foveated Streaming 将沉浸式内容融入 visionOS：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 Foveated Streaming 如何以高保真质量将远程渲染的场景传输到 Apple Vision Pro。探索这个框架如何通过完全无线的方式，将 visionOS 原生功能与第三方流媒体技术相结合，并通过 OpenXR 场景和 NVIDIA CloudXR 进行演示。了解 Foveated Streaming 框架、与 NVIDIA CloudXR SDK 的集成，以及动态注视点流式传输技术如何在保护隐私的同时带来种种好处。
- [WWDC26-289] 升级改造你的 AppKit App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：根据最新的 macOS 设计惯例升级改造你的 AppKit App。深入探索如何利用控制事件和手势识别器来处理输入，告别传统的追踪循环。增强 App 中的键盘导航功能，在重启后顺畅实现状态恢复；并利用新的边角同心性 API，让你的界面与 macOS 的美学设计无缝融合。
- [WWDC26-321] 深入探索 SwiftUI 的惰性堆栈与滚动：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 SwiftUI 惰性堆栈的内部工作原理。我们将探索 LazyVStack 和 LazyHStack 如何估算大小、惰性加载子视图并预取内容，从而提供流畅的滚动浏览体验。我们还将介绍高级性能优化方式、状态管理最佳做法，以及实现精准程序化滚动的技巧。为了充分从这个讲座中获益，我们建议你先熟悉一下使用堆栈的 SwiftUI 布局。
- [WWDC26-322] 使用 SwiftUI 构建高级图形效果：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何通过创造性地组合运用 SwiftUI 布局和图形 API 来打造丰富的自定体验。我们将介绍如何分解复杂的设计，并通过创意流程将简单的构建块串联起来。了解如何使用图层着色器进行绘制、利用时间线制作动画，并通过对齐参考线锚定视图。
- [WWDC26-370] 使用 TextKit 提升 App 的文本体验：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何将内置文本视图的便利性与 TextKit 的控制优势相结合。我们将介绍如何借助新的 API，通过行号、可折叠部分等自定行为，轻松地扩展 UITextView 和 NSTextView。我们还将深入探索 TextKit 架构，并详细讲解文本附件的全新缓存和重用策略。为了充分从这个讲座中获益，我们建议你观看 WWDC21 视频“认识 TextKit 2”和 WWDC22 视频“TextKit 和文本视图的新功能”。
- [WWDC26-372] 深入探索 PaperKit：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 PaperKit 制作基于画布的应用程序。探索新的数据模型 API，以便访问、创建和修改标记元素。了解如何添加自定控件和注释，并探索将这些功能整合到 App 中的最佳做法，打造功能齐全的创意画布。
- [WWDC26-375] 使用 Image Playground 制作高质量图像：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 Image Playground 框架，为你的 App 启用高质量图像生成功能。借助基于专用云计算运行的全新生成式模型，用户可以在你的 App 中制作写实以及其他各种风格的图像。你还可以指定尺寸来扩展应用场景，并允许用户使用自然语言描述和触控来修改图像。了解如何采用 Image Playground 框架，基于描述和照片生成图像，并管理 App 内功能的可用性。
- [WWDC26-8002] SwiftUI 初学者小组实验室：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，围绕 SwiftUI 入门这一主题，提出问题、获取建议，并关注相关的精彩讨论。活动语言为英语。
- [WWDC26-8006] SwiftUI 小组实验室：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，与 Apple 工程师和设计师一起深入探索 WWDC26。在这个以 SwiftUI 为主题的活动中，你可以提出问题、获取建议，并实时关注围绕大会一周的相关重磅发布展开的精彩讨论。活动语言为英语。
