# UIKit & AppKit

## 领域判断

UIKit、AppKit、生命周期与 SwiftUI 互操作。本领域覆盖 24 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Observable**：UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。；UIHostingController 的增强、SwiftUI 视图用作 UICollectionView/UITableView cell——这场 Session 是渐进式 SwiftUI 采用的实操指南。 来源：[WWDC25-268]、[WWDC22-10072]
- **Swift & UI**：SF Symbols 3 带来了多色渲染和可变颜色——但你如果在 UIKit 中还在用 withRenderingMode(.alwaysTemplate)，你正在浪费这套图标系统的全部能力。；macOS Big Sur 的 Mac Catalyst 终于可以做到"看不出是 Catalyst App"了——原生的窗口工具栏、侧边栏、右键菜单、以及可选的 AppKit 控件，让你的 iPad App 在 Mac 上获得真正的桌面体验。 来源：[WWDC21-10251]、[WWDC20-10143]
- **SwiftUI & UI Frameworks**：UIScene 生命周期即将变成强制要求——现在不迁移以后编译都过不了。但 Apple 给的迁移路径其实很清晰：Scene 管生命周期和状态恢复，SplitView/TabBar 管布局适应，Safe Area + Layout Guide 管自适应 UI。问题在于老项目的迁移成本。；iOS 18 的 UIKit 最值得关注的是用 SwiftUI Animation 驱动 UIKit 动画——两个框架的动画系统终于打通了。 来源：[WWDC25-282]、[WWDC24-10118]
- **Accessibility**：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。 来源：[WWDC25-221]
- **Apple Silicon 过渡的技术路线**：这是 WWDC 2020 的技术版 Keynote——如果你只看一场 Session 就要了解今年所有平台的开发者新特性，选这场准没错。 来源：[WWDC20-102]
- **CollectionView Cell 中的 SwiftUI 托管技巧。**：如果你的 Mac App 已经有大量 AppKit 代码，这场 Session 以 Shortcuts 为案例，详细讲解了 SwiftUI 和 AppKit 互相嵌入、数据共享、响应链集成等实战技巧。 来源：[WWDC22-10075]
- **Configuration 与旧 API 的共存**：UIButton.Configuration 是 UIKit 对「现代按钮」的正式回答——终于不用在 setTitle、setImage、setBackgroundColor 之间反复横跳了，一个 struct 搞定所有配置。 来源：[WWDC21-10064]

## API 演进时间线

- **WWDC25**：5 场，代表来源：[WWDC25-219]、[WWDC25-221]、[WWDC25-268]、[WWDC25-282]、[WWDC25-310]
- **WWDC24**：2 场，代表来源：[WWDC24-10118]、[WWDC24-10124]
- **WWDC23**：5 场，代表来源：[WWDC23-10036]、[WWDC23-10054]、[WWDC23-10055]、[WWDC23-10057]、[WWDC23-111215]
- **WWDC22**：4 场，代表来源：[WWDC22-10068]、[WWDC22-10072]、[WWDC22-10074]、[WWDC22-10075]
- **WWDC21**：6 场，代表来源：[WWDC21-10054]、[WWDC21-10057]、[WWDC21-10059]、[WWDC21-10063]、[WWDC21-10064]
- **WWDC20**：2 场，代表来源：[WWDC20-10143]、[WWDC20-102]

## 决策启发式

- 第一步：用 Xcode 26 构建 。大部分新设计会自动生效——toolbar 浮动、sidebar 玻璃、控件新外观。这是最低成本的第一轮适配。
- 清理遗留代码 ：移除 sidebar 中的 NSVisualEffectView，移除硬编码的控件高度（改用 Auto Layout），给菜单项加 symbol icon。
- 内容延伸到边缘 ：充分利用浮动 toolbar 和 sidebar 的视觉效果，让内容（地图、照片、艺术品）延伸到这些区域下方。用 NSBackgroundExtensionView 处理没有足够负空间的艺术作品。
- Liquid Glass 用在刀刃上 ：只给最高层级的控件（浮动工具、编辑控件）用玻璃材质。不要大面积使用——玻璃的折射和反射效果在大面积使用时会造成视觉混乱。用 NSGlassEffectContainerView 分组相邻的玻璃元素。
- 已有项目 ：逐步迁移动画代码——新写的交互式动画用 UIView.animate(using:) + SwiftUI spring，旧的 UIViewPropertyAnimator 代码不需要立刻改。优先在新功能中采用 automatic trait tracking，旧的 registerForTraitChanges 可以在下次碰到相关代码时顺手删除。
- 新项目 ：Tab Bar 直接用新的 UITab 和 UITabGroup API 来描述结构，不要再用旧的 UITabBarItem 数组方式。新的 API 能自动适配 tab bar 和 sidebar 两种形态，在 Mac Catalyst 和 visionOS 上也能获得原生体验。
- 检查窗口尺寸约束 ：在 Sequoia 上跑一遍你的 app，尝试用 Window Tiling 把窗口拖到各种位置，确认最小尺寸不会导致布局崩溃。
- 用 cascadingReferenceFrame 处理新窗口定位 ：如果你手动创建窗口，用这个新属性获取已有窗口的未吸附 frame 来计算级联偏移。
- Writing Tools 零成本适配 ：对于标准 NSTextView，Writing Tools 自动生效。但如果你做了高级文本处理，需要看《Get started with Writing Tools》了解更多交互行为细节。
- Genmoji 的图片本质 ：新表情是图片而非字符，如果你的 app 有文本存储和渲染的自定义逻辑，需要确认能正确处理内联图片。

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

`SwiftUI` (4)、`UIKit` (3)、`tvOS` (1)、`Accessibility` (1)、`Liquid Glass` (1)、`iPadOS` (1)、`Observable` (1)、`HDR` (1)

## 关键 Session

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
- [WWDC22-10075] 在 AppKit 项目中使用 SwiftUI：如果你的 Mac App 已经有大量 AppKit 代码，这场 Session 以 Shortcuts 为案例，详细讲解了 SwiftUI 和 AppKit 互相嵌入、数据共享、响应链集成等实战技巧。
- [WWDC21-10054] AppKit 的新特性：AppKit 在 macOS 12 终于拿到了 Swift Concurrency 的入场券——@MainActor 标注的 NSViewController、async 版本的 panel 展示、以及改进的 SwiftUI 互操作能力，老牌 Mac app 的现代化路径越来越清晰了。
- [WWDC21-10057] 让你的 iPad app 更上一层楼：iPad app 在 iPadOS 15 获得了一大波生产力增强——多任务分屏、键盘快捷键、全系统拖拽支持——如果你的 iPad app 还只是一个放大版 iPhone app，这场 Session 给你列出了升级清单。
