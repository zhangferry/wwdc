# UIKit & AppKit

## 领域判断

UIKit、AppKit、生命周期与 SwiftUI 互操作。本领域覆盖 27 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **SwiftUI & UI Frameworks**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何在现有的 AppKit 或 UIKit App 中逐步采用 SwiftUI。我们将介绍如何使用 Observation 框架自动更新视图，将 SwiftUI 组件整合到现有的视图层次结构中，并将手势识别器引入 SwiftUI。我们还将探索如何向你的 App 添加完整的 SwiftUI 场景，同时不改变整体架构。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 UIKit 的最新更新。了解如何更新 iPhone App 的布局，以便在调整大小时能够呈现出色效果，让你的 App 无论是通过 iPhone 镜像功能使用还是显示在 iPad 上都相宜。探索适用于标签栏和导航栏的全新 API，并了解如何针对 Apple 智能的新功能准备好的 App。我们还将介绍一种充分利用所选编码智能体的技巧，帮助你实现代码库现代化。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：根据最新的 macOS 设计惯例升级改造你的 AppKit App。深入探索… 来源：[WWDC26-272]、[WWDC26-278]、[WWDC26-289]、[WWDC25-282]
- **Observable**：UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。；UIHostingController 的增强、SwiftUI 视图用作 UICollectionView/UITableView cell——这场 Session 是渐进式 SwiftUI 采用的实操指南。 来源：[WWDC25-268]、[WWDC22-10072]
- **Swift & UI**：SF Symbols 3 带来了多色渲染和可变颜色——但你如果在 UIKit 中还在用 withRenderingMode(.alwaysTemplate)，你正在浪费这套图标系统的全部能力。；macOS Big Sur 的 Mac Catalyst 终于可以做到"看不出是 Catalyst App"了——原生的窗口工具栏、侧边栏、右键菜单、以及可选的 AppKit 控件，让你的 iPad App 在 Mac 上获得真正的桌面体验。 来源：[WWDC21-10251]、[WWDC20-10143]
- **Accessibility**：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。 来源：[WWDC25-221]
- **Apple Silicon 过渡的技术路线**：这是 WWDC 2020 的技术版 Keynote——如果你只看一场 Session 就要了解今年所有平台的开发者新特性，选这场准没错。 来源：[WWDC20-102]
- **CollectionView Cell 中的 SwiftUI 托管技巧。**：如果你的 Mac App 已经有大量 AppKit 代码，这场 Session 以 Shortcuts 为案例，详细讲解了 SwiftUI 和 AppKit 互相嵌入、数据共享、响应链集成等实战技巧。 来源：[WWDC22-10075]
- **Configuration 与旧 API 的共存**：UIButton.Configuration 是 UIKit 对「现代按钮」的正式回答——终于不用在 setTitle、setImage、setBackgroundColor 之间反复横跳了，一个 struct 搞定所有配置。 来源：[WWDC21-10064]

## API 演进时间线

- **WWDC26**：3 场，代表来源：[WWDC26-272]、[WWDC26-278]、[WWDC26-289]
- **WWDC25**：5 场，代表来源：[WWDC25-219]、[WWDC25-221]、[WWDC25-268]、[WWDC25-282]、[WWDC25-310]
- **WWDC24**：2 场，代表来源：[WWDC24-10118]、[WWDC24-10124]
- **WWDC23**：5 场，代表来源：[WWDC23-10036]、[WWDC23-10054]、[WWDC23-10055]、[WWDC23-10057]、[WWDC23-111215]
- **WWDC22**：4 场，代表来源：[WWDC22-10068]、[WWDC22-10072]、[WWDC22-10074]、[WWDC22-10075]
- **WWDC21**：6 场，代表来源：[WWDC21-10054]、[WWDC21-10057]、[WWDC21-10059]、[WWDC21-10063]、[WWDC21-10064]
- **WWDC20**：2 场，代表来源：[WWDC20-10143]、[WWDC20-102]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 第一步：用 Xcode 26 构建 。大部分新设计会自动生效——toolbar 浮动、sidebar 玻璃、控件新外观。这是最低成本的第一轮适配。
- 清理遗留代码 ：移除 sidebar 中的 NSVisualEffectView，移除硬编码的控件高度（改用 Auto Layout），给菜单项加 symbol icon。
- 内容延伸到边缘 ：充分利用浮动 toolbar 和 sidebar 的视觉效果，让内容（地图、照片、艺术品）延伸到这些区域下方。用 NSBackgroundExtensionView 处理没有足够负空间的艺术作品。
- Liquid Glass 用在刀刃上 ：只给最高层级的控件（浮动工具、编辑控件）用玻璃材质。不要大面积使用——玻璃的折射和反射效果在大面积使用时会造成视觉混乱。用 NSGlassEffectContainerView 分组相邻的玻璃元素。
- 已有项目 ：逐步迁移动画代码——新写的交互式动画用 UIView.animate(using:) + SwiftUI spring，旧的 UIViewPropertyAnimator 代码不需要立刻改。优先在新功能中采用 automatic trait tracking，旧的 registerForTraitChanges 可以在下次碰到相关代码时顺手删除。
- 新项目 ：Tab Bar 直接用新的 UITab 和 UITabGroup API 来描述结构，不要再用旧的 UITabBarItem 数组方式。新的 API 能自动适配 tab bar 和 sidebar 两种形态，在 Mac Catalyst 和 visionOS 上也能获得原生体验。
- 检查窗口尺寸约束 ：在 Sequoia 上跑一遍你的 app，尝试用 Window Tiling 把窗口拖到各种位置，确认最小尺寸不会导致布局崩溃。

## 反模式与坑

- SharePlay 的多人同步改进支持更灵活的交互延迟容错，适合派对游戏和多人观影场景，但 Session 里没有给具体 API 变化。
- SwiftUI 的 LazyVGrid 在 tvOS 上的性能有明显提升，大列表滚动不再掉帧了，这对内容浏览类 app 是直接的体验改善。
- 自定义视频播放叠加层现在支持章节导航 UI，可以不离开播放界面就切换章节，对长视频内容（课程、纪录片）体验提升明显。
- 包容性债务（Inclusion Debt） ：苹果正式把这个概念提出来了，意思是累积未解决的辅助功能缺陷应该像技术债务一样被追踪和偿还。
- Liquid Glass 的 Reduced Motion 适配 ：新的玻璃动效在"减少动效"模式下需要降级为静态效果，自定义动画需要额外处理。
- Assistive Access 自定义场景定义 ：开发者现在可以为特定使用场景定义专用的简化界面，而不仅仅是全局开关。
- UIBarButtonItem 新增 badge 属性，一行代码就能给导航栏按钮加未读数角标，如果你之前是自定义角标视图，现在可以换掉了。
- HDR 颜色选取器原生支持和 UITraitHDRHeadroomUsageLimit trait 的组合，让 HDR 内容在失去焦点时自动降级功耗，对展示 HDR 照片的应用很有意义。

## 高频主题

`SwiftUI` (5)、`UIKit` (5)、`AppKit` (2)、`tvOS` (1)、`Accessibility` (1)、`Liquid Glass` (1)、`iPadOS` (1)、`Observable` (1)、`HDR` (1)

## 关键 Session

- [WWDC26-272] 将 SwiftUI 与 AppKit 和 UIKit 搭配使用：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何在现有的 AppKit 或 UIKit App 中逐步采用 SwiftUI。我们将介绍如何使用 Observation 框架自动更新视图，将 SwiftUI 组件整合到现有的视图层次结构中，并将手势识别器引入 SwiftUI。我们还将探索如何向你的 App 添加完整的 SwiftUI 场景，同时不改变整体架构。
- [WWDC26-278] 升级改造你的 UIKit App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 UIKit 的最新更新。了解如何更新 iPhone App 的布局，以便在调整大小时能够呈现出色效果，让你的 App 无论是通过 iPhone 镜像功能使用还是显示在 iPad 上都相宜。探索适用于标签栏和导航栏的全新 API，并了解如何针对 Apple 智能的新功能准备好的 App。我们还将介绍一种充分利用所选编码智能体的技巧，帮助你实现代码库现代化。
- [WWDC26-289] 升级改造你的 AppKit App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：根据最新的 macOS 设计惯例升级改造你的 AppKit App。深入探索如何利用控制事件和手势识别器来处理输入，告别传统的追踪循环。增强 App 中的键盘导航功能，在重启后顺畅实现状态恢复；并利用新的边角同心性 API，让你的界面与 macOS 的美学设计无缝融合。
- [WWDC25-219] tvOS 新特性：如果你只做一件事：把你的 tvOS 应用的焦点管理从 UIKit 迁到 SwiftUI 的新 @FocusState 体系，这是回报最高的投入。
- [WWDC25-221] 辅助功能新特性：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。
- [WWDC25-268] UIKit 新特性：UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。
- [WWDC25-282] 让 UIKit 应用更灵活：UIScene 生命周期即将变成强制要求——现在不迁移以后编译都过不了。但 Apple 给的迁移路径其实很清晰：Scene 管生命周期和状态恢复，SplitView/TabBar 管布局适应，Safe Area + Layout Guide 管自适应 UI。问题在于老项目的迁移成本。
- [WWDC25-310] 用新设计构建 AppKit 应用：macOS Tahoe 的 Liquid Glass 来了——AppKit 里 toolbar、sidebar、controls 全变了，好消息是大部分自动生效，坏消息是你得清理掉那些 VisualEffectView 和硬编码高度。
- [WWDC24-10118] UIKit 的新变化：iOS 18 的 UIKit 最值得关注的是用 SwiftUI Animation 驱动 UIKit 动画——两个框架的动画系统终于打通了。
- [WWDC24-10124] AppKit 的新功能：macOS Sequoia 的 AppKit 更新是近几年来最实在的一批：Window Tiling、SwiftUI Menu 和 Animation 集成、Writing Tools 自动适配，每一个都是 Mac 开发者日常会用到的功能，值得逐条过一遍。
- [WWDC23-10036] 用 SwiftUI 和 UIKit 构建无障碍应用：如果你的 App 还没认真做过无障碍适配，这场 Session 提供的 API 足够让你低成本地迈出一大步——特别是 isToggle trait 和 AccessibilityNotification 这两个新增能力。
- [WWDC23-10054] AppKit 的新变化：macOS Sonoma 给 AppKit 带来了全新菜单系统、Inspector 面板和大量控件更新，值得每一位 Mac 开发者关注。
- [WWDC23-10055] UIKit 新特性：预览、Trait 系统、动画符号与空状态：UIKit 在 iOS 17 迎来几项重量级更新：Xcode 预览支持、viewIsAppearing 回调、自定义 Trait、动画符号、空状态 API——每一项都直击日常开发的痛点。
- [WWDC23-10057] 释放 UIKit Trait System 的全部潜力：iOS 17 的 Trait System 迎来大升级：自定义 Trait、新式覆写 API、SwiftUI 桥接，让数据在视图层级中的传递有了全新的范式。
- [WWDC23-111215] UIKit 遇见空间计算：适配、材质与交互：把 UIKit App 带到空间计算平台，核心工作是替换硬编码颜色、使用语义字体、适配不可用 API，其余系统帮你搞定。
- [WWDC22-10068] UIKit 新特性：如果你还在用 UIMenuController 和老式的 cell 高度计算方式，iOS 16 是时候动手迁移了——这版 UIKit 把过去几年积压的 API 债务清理了不少。
- [WWDC22-10072] 在 UIKit 中使用 SwiftUI：UIHostingController 的增强、SwiftUI 视图用作 UICollectionView/UITableView cell——这场 Session 是渐进式 SwiftUI 采用的实操指南。
- [WWDC22-10074] AppKit 新特性：macOS Ventura 的 AppKit 更新不算激进，但 Stage Manager 适配和 NSTableView 的性能改进是每个 Mac 开发者都需要关注的变化。
