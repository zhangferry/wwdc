# UIKit & AppKit

## 领域判断

UIKit、AppKit、生命周期与 SwiftUI 互操作。本领域覆盖 28 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Observable**：这场 Session 最值得关注的一件事是：AppKit 和 UIKit 的原生视图（NSView/UIView）终于能直接“白嫖” @Observable 的自动刷新机制了，老项目混编最恶心的手动状态同步彻底成为历史。；UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。；UIHostingController 的增强、SwiftUI 视图用作 UICollectionView/UITableView cell——这场 Session 是渐进式 SwiftUI 采用的实操指南。 来源：[WWDC26-272]、[WWDC25-268]、[WWDC22-10072]
- **Liquid Glass**：✅ AppKit 彻底抛弃 mouseDown: 转向手势识别器（Gesture Recognizers），并用全新的“边角同心性（Concentricity）”API 终结了 macOS 嵌套圆角对不齐的强迫症。；UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。 来源：[WWDC26-289]、[WWDC25-268]
- **MainActor**：这场 Session 最值得关注的一件事是：AppKit 和 UIKit 的原生视图（NSView/UIView）终于能直接“白嫖” @Observable 的自动刷新机制了，老项目混编最恶心的手动状态同步彻底成为历史。；AppKit 在 macOS 12 终于拿到了 Swift Concurrency 的入场券——@MainActor 标注的 NSViewController、async 版本的 panel 展示、以及改进的 SwiftUI 互操作能力，老牌 Mac app 的现代化路径越来越清晰了。 来源：[WWDC26-272]、[WWDC21-10054]
- **Swift & UI**：SF Symbols 3 带来了多色渲染和可变颜色——但你如果在 UIKit 中还在用 withRenderingMode(.alwaysTemplate)，你正在浪费这套图标系统的全部能力。；macOS Big Sur 的 Mac Catalyst 终于可以做到"看不出是 Catalyst App"了——原生的窗口工具栏、侧边栏、右键菜单、以及可选的 AppKit 控件，让你的 iPad App 在 Mac 上获得真正的桌面体验。 来源：[WWDC21-10251]、[WWDC20-10143]
- **SwiftUI & UI Frameworks**：UIScene 生命周期即将变成强制要求——现在不迁移以后编译都过不了。但 Apple 给的迁移路径其实很清晰：Scene 管生命周期和状态恢复，SplitView/TabBar 管布局适应，Safe Area + Layout Guide 管自适应 UI。问题在于老项目的迁移成本。；iOS 18 的 UIKit 最值得关注的是用 SwiftUI Animation 驱动 UIKit 动画——两个框架的动画系统终于打通了。 来源：[WWDC25-282]、[WWDC24-10118]
- **Accessibility**：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。 来源：[WWDC25-221]
- **Adaptivity**：iPhone App 在 Mac (iPhone Mirroring) 和 iPad 上变成了“完全可自由拉伸的窗口”，这直接宣判了 UIScreen.main 和硬编码设备类型的死刑，逼迫所有 UIKit 老项目必须彻底拥抱 Size Classes (尺寸类别)。 来源：[WWDC26-278]

## API 演进时间线

- **WWDC26**：4 场，代表来源：[WWDC26-272]、[WWDC26-278]、[WWDC26-289]、[WWDC26-372]
- **WWDC25**：5 场，代表来源：[WWDC25-219]、[WWDC25-221]、[WWDC25-268]、[WWDC25-282]、[WWDC25-310]
- **WWDC24**：2 场，代表来源：[WWDC24-10118]、[WWDC24-10124]
- **WWDC23**：5 场，代表来源：[WWDC23-10036]、[WWDC23-10054]、[WWDC23-10055]、[WWDC23-10057]、[WWDC23-111215]
- **WWDC22**：4 场，代表来源：[WWDC22-10068]、[WWDC22-10072]、[WWDC22-10074]、[WWDC22-10075]
- **WWDC21**：6 场，代表来源：[WWDC21-10054]、[WWDC21-10057]、[WWDC21-10059]、[WWDC21-10063]、[WWDC21-10064]
- **WWDC20**：2 场，代表来源：[WWDC20-10143]、[WWDC20-102]

## 决策启发式

- 已有项目的迁移策略 ：别想着“一把梭”重写。最稳妥的起手式是把核心数据模型加上 @Observable 宏，让现有的 NSView/UIView 享受自动刷新；遇到需要大改 UI 或新增复杂交互的独立模块（比如新的设置面板、复杂的图表），直接用 SwiftUI 写，通过 NSHostingView 嵌进去；边缘 Scene（如菜单栏扩展）则可以通过 NSHostingSceneRepresentation 无缝替换。
- 新项目的采用建议 ：直接上纯 SwiftUI。除非你要做极度依赖底层事件循环的复杂自定义控件（比如 DAW 软件的钢琴卷帘），否则不要主动引入 AppKit/UIKit 混编，徒增心智负担。
- 实战中容易踩的坑 ：Info.plist 里的 NSObservationTrackingEnabled 开关。如果你要支持 macOS 15 / iOS 18，必须手动加这个 key 才能开启自动追踪，而在 macOS 26 / iOS 26 上它是默认开启的。漏了这个 key 会导致老系统上视图死活不刷新，排查起来极其痛苦。
- 第一步：用 Xcode 26 构建 。大部分新设计会自动生效——toolbar 浮动、sidebar 玻璃、控件新外观。这是最低成本的第一轮适配。
- 清理遗留代码 ：移除 sidebar 中的 NSVisualEffectView，移除硬编码的控件高度（改用 Auto Layout），给菜单项加 symbol icon。
- 内容延伸到边缘 ：充分利用浮动 toolbar 和 sidebar 的视觉效果，让内容（地图、照片、艺术品）延伸到这些区域下方。用 NSBackgroundExtensionView 处理没有足够负空间的艺术作品。
- Liquid Glass 用在刀刃上 ：只给最高层级的控件（浮动工具、编辑控件）用玻璃材质。不要大面积使用——玻璃的折射和反射效果在大面积使用时会造成视觉混乱。用 NSGlassEffectContainerView 分组相邻的玻璃元素。
- 已有项目 ：逐步迁移动画代码——新写的交互式动画用 UIView.animate(using:) + SwiftUI spring，旧的 UIViewPropertyAnimator 代码不需要立刻改。优先在新功能中采用 automatic trait tracking，旧的 registerForTraitChanges 可以在下次碰到相关代码时顺手删除。
- 新项目 ：Tab Bar 直接用新的 UITab 和 UITabGroup API 来描述结构，不要再用旧的 UITabBarItem 数组方式。新的 API 能自动适配 tab bar 和 sidebar 两种形态，在 Mac Catalyst 和 visionOS 上也能获得原生体验。
- 检查窗口尺寸约束 ：在 Sequoia 上跑一遍你的 app，尝试用 Window Tiling 把窗口拖到各种位置，确认最小尺寸不会导致布局崩溃。

## 反模式与坑

- NSHostingMenu ：可以直接用 SwiftUI 的 View（包含 Button、Picker 等）构建菜单，然后包装成 NSMenu 塞进 AppKit 的主菜单栏，连键盘快捷键都能完美映射。
- Canvas 与 CoreGraphics 互通 ：在 SwiftUI 的 Canvas 里可以通过 withCGContext 直接拿到 CGContext，以前写在 drawRect 里的老 CoreGraphics 绘制代码可以一行不改地搬到 SwiftUI 里。
- Liquid Glass 的底层实现 ：Apple 透露 AppKit 里的 NSSlider、NSSwitch 等基础控件，底层已经大量使用 SwiftUI 来渲染新的 Liquid Glass 效果，这意味着你即使不写 SwiftUI，也在享受它的渲染红利。
- Menu 图片可见性控制 ：在 iPadOS 和 macOS 的菜单栏中，Menu element (菜单元素) 的图片默认可能不显示，需要用 preferredImageVisibility 强制覆盖。
- Siri 与 Drag & Drop 整合 ：如果你的 App 支持拖拽，Siri 可以直接读取你 Drag handler (拖拽处理器) 里的资源，但切记别在 sessionWillBegin 里弹 Modal UI，因为现在的拖拽可以由 Siri 无手势触发。
- Navigation Bar 滚动隐藏 ：导航栏现在支持在滚动时自动滑走 (barMinimizationBehavior)，以前用 .soft 覆盖默认样式的 App 需要重新评估设计，因为 .automatic 的默认视觉效果已经大改了。
- NSTextSelectionManager ：让非 NSTextView 的自定义视图也能白嫖原生的双向文本选择、拖拽和切换行为。
- Liquid Glass 自动演进 ：macOS 27 会自动给侧边栏选中项加半粗体，给工具栏加玻璃材质，老 App 重新编译就能获得视觉升级。

## 高频主题

`UIKit` (6)、`SwiftUI` (5)、`AppKit` (2)、`Liquid Glass` (2)、`Observation` (1)、`NSHostingView` (1)、`Size Classes` (1)、`Trait Collections` (1)、`UIScene` (1)、`Adaptivity` (1)、`Gesture Recognizers` (1)、`macOS 27` (1)、`State Restoration` (1)、`PaperKit` (1)、`PencilKit` (1)、`Canvas` (1)、`Adornments` (1)、`tvOS` (1)

## 关键 Session

- [WWDC26-272] 将 SwiftUI 与 AppKit 和 UIKit 搭配使用：这场 Session 最值得关注的一件事是：AppKit 和 UIKit 的原生视图（NSView/UIView）终于能直接“白嫖” @Observable 的自动刷新机制了，老项目混编最恶心的手动状态同步彻底成为历史。
- [WWDC26-278] 升级改造你的 UIKit App：iPhone App 在 Mac (iPhone Mirroring) 和 iPad 上变成了“完全可自由拉伸的窗口”，这直接宣判了 UIScreen.main 和硬编码设备类型的死刑，逼迫所有 UIKit 老项目必须彻底拥抱 Size Classes (尺寸类别)。
- [WWDC26-289] 升级改造你的 AppKit App：✅ AppKit 彻底抛弃 mouseDown: 转向手势识别器（Gesture Recognizers），并用全新的“边角同心性（Concentricity）”API 终结了 macOS 嵌套圆角对不齐的强迫症。
- [WWDC26-372] 深入探索 PaperKit：✅ Apple 终于把 Notes 和 Freeform 的底裤（PaperKit）扒下来给开发者穿了，这意味着你可以用几行代码手搓一个带 Apple Pencil 原生支持和无限画布的白板应用。
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
