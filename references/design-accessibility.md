# Design & Accessibility

## 领域判断

设计原则、无障碍、国际化与包容性体验。本领域覆盖 153 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Design**：Liquid Glass 不是换个背景色就完事的——它改变了 UIKit 组件的行为逻辑：Tab Bar 浮起来了、导航栏变透明了、搜索栏可以塞进工具栏了、按钮要分组共享玻璃背景了。好消息是重新编译就有大部分效果，坏消息是你之前做的一切 UI 自定义都得重新审视。；如果你的 App 已经支持了 iPhone Live Activities，watchOS 11 会自动把它带到 Apple Watch 上——但要做好，你需要理解 Smart Stack 的交互模型和 Watch 端独有的设计约束。；SF Symbols 6 新增 Wiggle、Rotate、Breathe 三种动画预设，升级 Replace 为 Magic Replace，改进 Variable Color 的循环播放，让你的图标动起来这件事变得前所未有地简单。 来源：[WWDC25-284]、[WWDC24-10098]、[WWDC24-10188]、[WWDC23-10138]
- **Accessibility**：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。；如果你在做无障碍测试，Xcode 13 新增的 UI 自动化 API 让你能在测试中模拟数字表冠旋转、触控板手势和 iPad 指针操作——终于不用手动测了。；watchOS 8 的新无障碍 API 让你的 Apple Watch App 能服务于更多用户——双指捏合手势、改进的 VoiceOver 和 AssistiveTouch 都是免费获得的特性，前提是你正确使用了 SwiftUI。 来源：[WWDC25-221]、[WWDC21-10208]、[WWDC21-10223]、[WWDC21-10260]
- **空间计算**：visionOS 上的 Widget 终于不再是 iPad 的"兼容模式移植"了——它有了自己的设计语言：持久锚定、物理尺寸、环境感知，这三个特性让 Widget 从"信息卡片"变成了"房间里的实物"。；如果你熟悉 SwiftUI 的 2D 布局（VStack/HStack/alignment），现在可以直接用同样的心智模型构建 visionOS 的 3D 体验——每个视图多了 depth 和 Z position，alignment 多了深度维度，新增的 rotation3DLayout 和 SpatialContainer 解决了 2D modifier 在 3D 空间中的失效问题。；SwiftUI 和 RealityKit 终于从"各干各的"变成了"双向奔赴"——Entity 现在可以当数据模型用，SwiftUI 动画可以直接驱动 RealityKit 组件变化。但双向数据流是把双刃剑，用不好就会陷入无限循环。 来源：[WWDC25-255]、[WWDC25-273]、[WWDC25-274]、[WWDC25-290]
- **WidgetKit**：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。；watchOS 10 的智能叠放让 Widget 回到 Apple Watch 中心——六种标准布局、动态背景色、相关性排序，10 秒内传达核心信息。；Widget 不是迷你 app——这是这场 Session 最核心的观点。如果你的 Widget 试图做太多事情，大概率会既不好用又不好看。 来源：[WWDC25-215]、[WWDC23-10309]、[WWDC21-10048]、[WWDC20-10086]
- **AppIntent**：Snippet 从"系统替你弹一个结果卡片"变成了"你的 App 可以在系统层做轻量级交互"——按钮、数据更新、确认流程全支持。设计指南的核心矛盾是：既要信息密度够高，又要一眼就能扫完。；iOS 18 把 App Intents 的定位从"少数常用操作暴露给系统"变成了"你 App 做的每件事都应该是一个 Intent"——这意味着 App Intents 的设计质量直接决定了你的 App 在 Spotlight、Shortcuts、Siri、Action Button 等系统入口的表现。；Widget 终于支持动画和交互了——用 App Intents 驱动按钮和开关操作，用 SwiftUI 的动画 API 让内容切换有感知力，再加上新的 Preview API 实时预览动画效果，这让 Widget 从"静态信息卡"变成了"可以操作的迷你 App"。 来源：[WWDC25-281]、[WWDC24-10176]、[WWDC23-10028]、[WWDC22-10170]
- **ScrollView**：可发现性（Discoverability）是区分"好用"和"难用"的关键因素 —— 用户不会阅读你的使用说明，所以每个功能都必须有被"偶然发现"的路径，这集 Session 给出了系统性的设计方法。；这不是一堂形而上的「政治正确」课，而是用真实案例告诉你：不做包容性设计 = 放弃用户 = 放弃收入。；排版不只是"选个字体然后调大小"——这场 Session 用大量实际案例告诉你，好的 UI 排版是像素级的精雕细琢，而 Apple 的文本系统提供了你可能从没用过的精细控制能力。 来源：[WWDC21-10126]、[WWDC21-10275]、[WWDC20-10175]、[WWDC20-10640]
- **Swift & UI**：SectorMark 让饼图和甜甜圈图成为 Swift Charts 的一等公民，加上选择和滚动交互，数据可视化又上了一层楼。；两位 Maps 团队的设计师分享了他们用 SwiftUI 在设备上直接做设计的实践经验——这对设计师来说是必看的一场。；iPadOS 13.4 引入了触控板和鼠标支持，但很多 App 还没有适配指针交互。这个 Session 教你如何利用 UIPointerInteraction 让你的 App 在连接外设时有原生级的指针体验。 来源：[WWDC23-10037]、[WWDC23-10115]、[WWDC20-10093]、[WWDC20-10104]

## API 演进时间线

- **WWDC25**：31 场，代表来源：[WWDC25-111]、[WWDC25-206]、[WWDC25-214]、[WWDC25-215]、[WWDC25-221]
- **WWDC24**：11 场，代表来源：[WWDC24-10073]、[WWDC24-10074]、[WWDC24-10085]、[WWDC24-10086]、[WWDC24-10096]
- **WWDC23**：24 场，代表来源：[WWDC23-10028]、[WWDC23-10032]、[WWDC23-10035]、[WWDC23-10036]、[WWDC23-10037]
- **WWDC22**：25 场，代表来源：[WWDC22-10001]、[WWDC22-10009]、[WWDC22-10015]、[WWDC22-10034]、[WWDC22-10059]
- **WWDC21**：32 场，代表来源：[WWDC21-10023]、[WWDC21-10029]、[WWDC21-10048]、[WWDC21-10053]、[WWDC21-10056]
- **WWDC20**：30 场，代表来源：[WWDC20-10005]、[WWDC20-10019]、[WWDC20-10020]、[WWDC20-10022]、[WWDC20-10060]

## 决策启发式

- 如果你的团队有听力障碍成员 ，推荐观看 ASL 版本而非纯字幕版本，手语传达的语气和重点比文字更丰富。
- Accessibility 应该从设计阶段开始考虑 ，而不是开发完成后再补。Keynote 中 Lisa（视力障碍设计师）的参与就是 "Nothing about us without us" 理念的实践。
- 立即定义你的 app 的公共任务列表 。这是标注 Accessibility Nutrition Labels 的第一步，也是评估 app 无障碍水平的基础。
- 与残障社区的用户合作测试 。如果你的团队没有残障成员，通过用户研究招募测试者。内部测试无法替代真实用户的反馈。
- 不要标注你的 app 不支持的特性 。准确性比覆盖面更重要。如果一个特性与你的 app 无关（如没有视频内容就不标字幕），不标注是正确的选择。
- 在设计阶段就考虑无障碍 ，而不是开发完成后修补。高对比度配色、不依赖颜色传达信息、支持减少动态效果 这些在设计稿阶段就应该确认。
- VoiceOver 和 Voice Control 共享相同的 accessibility API 。做好了 VoiceControl 支持，VoiceOver 也基本可用，反之亦然。
- 开启自动注释生成 。Xcode Settings Editing "automatically generate string catalog comments"。这会让翻译人员获得足够上下文，减少来回沟通。
- 早期项目用字符串提取，成熟项目切符号生成 。两者之间的 Refactor 菜单可以一键转换，不必一开始就做决定。
- 使用 plural form 处理数量相关字符串 。不要用简单的 "item(s)" 占位，让系统根据语言规则选择正确形式。

## 反模式与坑

- Apple 在开发者工具和平台层面持续提升无障碍体验：Xcode 26 的 Voice Control 改进、Accessibility Nutrition Labels 等都表明这是一个持续投入的方向。
- 如果你在做国际化相关工作，Session 222（多语言体验增强）是必看的补充内容。
- Apple 提供 Keynote 的 ASL 版本本身就是一个信号
- 所有 Keynote 中展示的 accessibility 更新值得单独关注
- SF Symbols 7 的符号库又扩充了一批，如果你之前用自定义图标替代系统符号，值得重新检查一遍是否有现成的了。
- Icon Composer 现在内置于 Xcode，设计师可以直接在开发环境里预览图标在不同模式下的效果，省掉了来回导图的沟通成本。
- Design System Framework 统一了色彩、排版、间距的 API 命名，第三方应用接入系统视觉一致性变得更容易，但这也意味着"故意不一样"的设计选择会更显眼。
- 简繁体变体管理升级：zh Hans、zh Hant TW、zh Hant HK 现在是独立变体，终于不用一套繁体打天下了。

## 高频主题

`Design` (21)、`SwiftUI` (16)、`空间计算` (6)、`基础` (4)、`无障碍` (4)、`开发工具` (2)、`机器学习` (2)、`Liquid Glass` (1)、`SF Symbols` (1)、`UI` (1)、`本地化` (1)、`国际化` (1)、`String Catalog` (1)、`翻译` (1)、`WidgetKit` (1)、`小组件` (1)、`Live Activities` (1)、`交互式` (1)

## 关键 Session

- [WWDC25-111] Keynote (ASL)：这是 Keynote 的 ASL（美国手语）版本，内容与 Session 101 完全一致，适合需要手语辅助理解的开发者观看。
- [WWDC25-206] 设计新动态：如果你只做一件事：升级 SDK，让系统控件自动获得 Liquid Glass 效果，其他的适配可以慢慢来。
- [WWDC25-214] 本地化新特性：如果你还在用 .strings 文件做本地化，今年是迁移 String Catalog 的最后窗口——增量翻译检测和内置机器翻译已经让旧方案显得原始。
- [WWDC25-215] 小组件新特性：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。
- [WWDC25-221] 辅助功能新特性：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。
- [WWDC25-224] Evaluate your app for Accessibility Nutrition Labels：Accessibility Nutrition Labels 让你在 App Store 产品页面上展示 app 支持的无障碍特性 这不是营销装饰，而是需要你用"公共任务"逐项验证后才能标注的功能声明。
- [WWDC25-225] Code-along: Explore localization with Xcode：Xcode 26 的 String Catalog 自动注释生成和符号生成功能，让本地化从"维护负担"变成了"开发工作流的自然延伸" 你写代码，Xcode 帮你准备翻译上下文。
- [WWDC25-229] 让你的 Mac 应用对每个人都更易用：如果你的 Mac 应用只做了基础的 accessibility 标签而没有优化容器结构和键盘导航，VoiceOver 用户可能需要按几十次键盘才能到达他们想去的地方——这场 Session 教你怎么用几个 modifier 把这个数字砍掉一半。
- [WWDC25-238] 为 Assistive Access 定制你的应用：iOS 26 给了你一个正式的 AssistiveAccess SwiftUI scene 类型——在此之前你的应用在 Assistive Access 模式下只能显示缩小版的完整界面，现在你可以为认知障碍用户构建一个完全独立的精简体验。
- [WWDC25-247] Xcode 26 新特性详解：Xcode 26 最大的卖点是 LLM 驱动的 Coding Assistant 正式落地，但更实在的进步是 build 加速、debugger 改善、以及 UI testing 的代码生成革命。
- [WWDC25-248] 端侧大模型的 Prompt 设计与安全策略：如果你打算用 Foundation Models framework 做任何用户可输入的功能，这场 Session 里关于安全分层防御的部分比 prompt 技巧本身重要十倍。
- [WWDC25-255] 为 visionOS 设计 Widget：从屏幕到空间：visionOS 上的 Widget 终于不再是 iPad 的"兼容模式移植"了——它有了自己的设计语言：持久锚定、物理尺寸、环境感知，这三个特性让 Widget 从"信息卡片"变成了"房间里的实物"。
- [WWDC25-273] SwiftUI 空间布局入门：用 2D 思维构建 3D 体验：如果你熟悉 SwiftUI 的 2D 布局（VStack/HStack/alignment），现在可以直接用同样的心智模型构建 visionOS 的 3D 体验——每个视图多了 depth 和 Z position，alignment 多了深度维度，新增的 rotation3DLayout 和 SpatialContainer 解决了 2D modifier 在 3D 空间中的失效问题。
- [WWDC25-274] SwiftUI 与 RealityKit 的合体之路：SwiftUI 和 RealityKit 终于从"各干各的"变成了"双向奔赴"——Entity 现在可以当数据模型用，SwiftUI 动画可以直接驱动 RealityKit 组件变化。但双向数据流是把双刃剑，用不好就会陷入无限循环。
- [WWDC25-281] 设计交互式 Snippet：Snippet 从"系统替你弹一个结果卡片"变成了"你的 App 可以在系统层做轻量级交互"——按钮、数据更新、确认流程全支持。设计指南的核心矛盾是：既要信息密度够高，又要一眼就能扫完。
- [WWDC25-284] 用 UIKit 构建新设计系统应用：Liquid Glass 不是换个背景色就完事的——它改变了 UIKit 组件的行为逻辑：Tab Bar 浮起来了、导航栏变透明了、搜索栏可以塞进工具栏了、按钮要分组共享玻璃背景了。好消息是重新编译就有大部分效果，坏消息是你之前做的一切 UI 自定义都得重新审视。
- [WWDC25-290] Set the scene with SwiftUI in visionOS：visionOS 26 的 SwiftUI scene 系统做了一轮全面升级：窗口可以锁房间、Volume 可以吸墙面和桌面、immersive space 支持 Mac 远程渲染、UIKit 也能桥接 Volume 了。如果你在做 visionOS app，这篇是必读。
- [WWDC25-303] 设计 visionOS 悬停交互：visionOS 的 hover 效果不是简单的 hover 态 CSS——它是隐私保护下的状态机动画、眼动驱动的滚动、以及媒体控件的持久化显示，这三个机制合在一起才是完整的交互模型。
