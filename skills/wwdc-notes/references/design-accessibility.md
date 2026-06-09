# Design & Accessibility

## 领域判断

设计原则、无障碍、国际化与包容性体验。本领域覆盖 166 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Accessibility**：✅ 这场 Session 最值得关注的一件事是：Apple 终于把多段落离散文本的 VoiceOver 焦点连贯性问题解决了，并且让自定义渲染的文本（如扫描图或 Canvas 绘制的字）能通过实现 UITextInput 获得原生级别的逐词朗读和选择体验。；自定义控件的辅助功能终于不再是“加个 Label 糊弄过去”，Apple 用 Direct Touch API 和 Custom Actions 给出了 2D 空间和复杂手势的官方标准解法。；tvOS 终于补齐了 Dynamic Type (动态字体) 这块无障碍短板，但这场 Session 真正的价值在于教你如何用 AnyLayout 和 containerRelativeFrame 优雅地重构客厅大屏的响应式布局。 来源：[WWDC26-219]、[WWDC26-220]、[WWDC26-221]、[WWDC26-230]
- **Design**：Liquid Glass 不是换个背景色就完事的——它改变了 UIKit 组件的行为逻辑：Tab Bar 浮起来了、导航栏变透明了、搜索栏可以塞进工具栏了、按钮要分组共享玻璃背景了。好消息是重新编译就有大部分效果，坏消息是你之前做的一切 UI 自定义都得重新审视。；如果你的 App 已经支持了 iPhone Live Activities，watchOS 11 会自动把它带到 Apple Watch 上——但要做好，你需要理解 Smart Stack 的交互模型和 Watch 端独有的设计约束。；SF Symbols 6 新增 Wiggle、Rotate、Breathe 三种动画预设，升级 Replace 为 Magic Replace，改进 Variable Color 的循环播放，让你的图标动起来这件事变得前所未有地简单。 来源：[WWDC25-284]、[WWDC24-10098]、[WWDC24-10188]、[WWDC23-10138]
- **空间计算**：visionOS 上的 Widget 终于不再是 iPad 的"兼容模式移植"了——它有了自己的设计语言：持久锚定、物理尺寸、环境感知，这三个特性让 Widget 从"信息卡片"变成了"房间里的实物"。；如果你熟悉 SwiftUI 的 2D 布局（VStack/HStack/alignment），现在可以直接用同样的心智模型构建 visionOS 的 3D 体验——每个视图多了 depth 和 Z position，alignment 多了深度维度，新增的 rotation3DLayout 和 SpatialContainer 解决了 2D modifier 在 3D 空间中的失效问题。；SwiftUI 和 RealityKit 终于从"各干各的"变成了"双向奔赴"——Entity 现在可以当数据模型用，SwiftUI 动画可以直接驱动 RealityKit 组件变化。但双向数据流是把双刃剑，用不好就会陷入无限循环。 来源：[WWDC25-255]、[WWDC25-273]、[WWDC25-274]、[WWDC25-290]
- **RealityKit**：这场 Session 最值得关注的一件事是：Reality Composer Pro 3 的 ScriptGraph 配合即将推出的 Vision Pro 实机 Live Preview，彻底把 visionOS 空间交互的“调参权”从程序员手里抢走，交给了设计师。；✅ Apple 终于用纯 Swift 重写了 USD 绑定（USDKit），让 3D 场景组装从“啃 C++ 头文件”变成了“写 SwiftUI 一样的日常”。；visionOS 上最好的 App 不是把 iPad 版搬过来，而是找到了"只有空间计算才能做到"的那个瞬间——Session 通过 JigSpace、Loona、Lowe's 等实际案例给出了三条可复用的设计策略。 来源：[WWDC26-252]、[WWDC26-285]、[WWDC24-10086]、[WWDC24-10102]
- **ScrollView**：tvOS 终于补齐了 Dynamic Type (动态字体) 这块无障碍短板，但这场 Session 真正的价值在于教你如何用 AnyLayout 和 containerRelativeFrame 优雅地重构客厅大屏的响应式布局。；可发现性（Discoverability）是区分"好用"和"难用"的关键因素 —— 用户不会阅读你的使用说明，所以每个功能都必须有被"偶然发现"的路径，这集 Session 给出了系统性的设计方法。；这不是一堂形而上的「政治正确」课，而是用真实案例告诉你：不做包容性设计 = 放弃用户 = 放弃收入。 来源：[WWDC26-221]、[WWDC21-10126]、[WWDC21-10275]、[WWDC20-10175]
- **WidgetKit**：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。；watchOS 10 的智能叠放让 Widget 回到 Apple Watch 中心——六种标准布局、动态背景色、相关性排序，10 秒内传达核心信息。；Widget 不是迷你 app——这是这场 Session 最核心的观点。如果你的 Widget 试图做太多事情，大概率会既不好用又不好看。 来源：[WWDC25-215]、[WWDC23-10309]、[WWDC21-10048]、[WWDC20-10086]
- **AppIntent**：Snippet 从"系统替你弹一个结果卡片"变成了"你的 App 可以在系统层做轻量级交互"——按钮、数据更新、确认流程全支持。设计指南的核心矛盾是：既要信息密度够高，又要一眼就能扫完。；iOS 18 把 App Intents 的定位从"少数常用操作暴露给系统"变成了"你 App 做的每件事都应该是一个 Intent"——这意味着 App Intents 的设计质量直接决定了你的 App 在 Spotlight、Shortcuts、Siri、Action Button 等系统入口的表现。；Widget 终于支持动画和交互了——用 App Intents 驱动按钮和开关操作，用 SwiftUI 的动画 API 让内容切换有感知力，再加上新的 Preview API 实时预览动画效果，这让 Widget 从"静态信息卡"变成了"可以操作的迷你 App"。 来源：[WWDC25-281]、[WWDC24-10176]、[WWDC23-10028]、[WWDC22-10170]

## API 演进时间线

- **WWDC26**：13 场，代表来源：[WWDC26-219]、[WWDC26-220]、[WWDC26-221]、[WWDC26-230]、[WWDC26-250]
- **WWDC25**：31 场，代表来源：[WWDC25-111]、[WWDC25-206]、[WWDC25-214]、[WWDC25-215]、[WWDC25-221]
- **WWDC24**：11 场，代表来源：[WWDC24-10073]、[WWDC24-10074]、[WWDC24-10085]、[WWDC24-10086]、[WWDC24-10096]
- **WWDC23**：24 场，代表来源：[WWDC23-10028]、[WWDC23-10032]、[WWDC23-10035]、[WWDC23-10036]、[WWDC23-10037]
- **WWDC22**：25 场，代表来源：[WWDC22-10001]、[WWDC22-10009]、[WWDC22-10015]、[WWDC22-10034]、[WWDC22-10059]
- **WWDC21**：32 场，代表来源：[WWDC21-10023]、[WWDC21-10029]、[WWDC21-10048]、[WWDC21-10053]、[WWDC21-10056]
- **WWDC20**：30 场，代表来源：[WWDC20-10005]、[WWDC20-10019]、[WWDC20-10020]、[WWDC20-10022]、[WWDC20-10060]

## 决策启发式

- 已有项目的迁移策略 ：先排查现有 App 里的长文本页面。如果是多个 TextView 拼的，立刻加上 accessibilityLinkedGroup 或配置 Next/Previous 指针。如果是自绘文本，评估是否有必要上 UITextInput；如果只是为了让盲人“听”内容，先考虑 accessibilityLabel 结合 UIAccessibilityReadingContent，成本更低。
- 新项目的采用建议 ：排版允许的话，无脑用 TextEditor 或单个大 UITextView。必须拆分 UI 时，优先使用 SwiftUI 的 Linked Group，把脏活累活交给框架。
- 实战避坑 ：如果你给文本选择添加了自定义操作（比如“高亮”、“保存”），在构建 UIAccessibilityCustomAction 时，一定要设置 category = .editCategory。如果不设置，这个操作只会出现在通用的 Actions 菜单里，而不会出现在 VoiceOver 文本编辑专属的转子 (Rotor) 中，用户根本找不到。
- 已有项目的迁移策略 ：先排查项目里那些“为了好看而手搓的 UI”。如果是单轴的（如音量、进度），直接补上 .adjustable 和 accessibilityAdjustableAction；如果是多轴或画板类的，把隐藏的辅助按钮删掉，换成 accessibilityAction。
- 新项目的采用建议 ：在设计自定义控件的第一天，就把 Accessibility 语义写进 API 设计里。不要等 UI 画完了再想怎么“加”无障碍，而是让控件本身就“是”无障碍的。比如设计一个 2D 摇杆，它的 Value 就应该返回极坐标或 XY 值，而不是只返回一个状态。
- 实战避坑 ：播报 (Announcement) 绝对不能滥用。像视频里提到的 0.3 秒防抖阈值是个很好的基准线。如果用户滑动很快，一秒钟播报 10 次“50%、51%、52%”会让 VoiceOver 用户直接关掉 App。
- 全局清洗硬编码 ：在已有项目中，用正则搜索 .system(size: 和 UIFont.systemFont(ofSize:，全部替换为 .font(.body) 或 UIFont.preferredFont(forTextStyle: .body)。同时搜索固定的 .frame(width: 300)，改为 .frame(maxWidth: .infinity) 让内容自己撑开。
- 焦点测试是灵魂 ：tvOS 适配大字体后，一定要用 Siri Remote 实际按一按。布局切换时如果焦点跳到了屏幕边缘或者消失，说明你的视图层级在切换时被销毁了，老老实实换回 AnyLayout。
- 跑马灯兜底 ：如果某些电影标题实在太长，大字体下无论怎么调布局都会截断，别硬塞。Apple 建议实现自定义的 Marquee (跑马灯) 效果，让文字在焦点停留时滚动显示。
- 已有项目的迁移策略 ：赶紧删掉你项目里那些用 CGEventTap 拦截键盘鼠标、用隐藏窗口遮挡 Dock 的“祖传代码”。把这些逻辑全部替换成 AEAssessmentConfiguration。自己造的轮子不仅容易在 macOS 大版本更新时崩溃，还会被系统判定为恶意行为。

## 反模式与坑

- 无障碍阅读器 (Accessibility Reader) ：iOS 26 新增的系统级工具，只要你的文本无障碍属性配置规范，用户可以在控制中心一键唤起，系统会提取内容并重新排版为极简阅读模式。
- 编辑转子 (Editor Rotor) 增强 ：现在可以把业务逻辑（如“加入生词本”）无缝塞进 VoiceOver 的文本编辑上下文菜单中，极大提升了视力障碍用户的操作效率。
- 自动翻页 Trait ：.causesPageTurn 配合 accessibilityScroll，让“朗读屏幕”体验直接追平专业的有声书 App，不用再手动干预翻页逻辑。
- 动态激活点 (Dynamic Activation Point) ：accessibilityActivationPoint 可以绑定状态，让穿透手势的起点永远跟随当前控件的实际物理位置，这个细节极其提升体验。
- 转子 (Rotor) 的无缝集成 ：Custom Actions 会自动注册到 VoiceOver 的转子菜单中，不需要开发者手动去写复杂的 UIAccessibilityCustomRotor 代码了。
- Direct Touch 的按需激活 ：[.requiresActivation] 参数是灵魂，它防止了用户只是想滑过这个区域时误触发复杂的控件手势。
- Accessibility Nutrition Labels (无障碍营养标签) ：现在可以在 App Store Connect 里勾选支持大字体，这会让你的 App 在无障碍筛选搜索中获得更高权重。
- 语义化样式的红利 ：使用 .caption 或 .headline 等 Semantic text styles (语义文本样式)，系统不仅会帮你缩放大小，还会自动调整字重和行高，比手动算比例省心得多。

## 高频主题

`SwiftUI` (22)、`Design` (22)、`Accessibility` (10)、`空间计算` (6)、`基础` (4)、`无障碍` (4)、`Liquid Glass` (3)、`VoiceOver` (2)、`Dynamic Type` (2)、`UIKit` (2)、`SF Symbols` (2)、`RealityKit` (2)、`开发工具` (2)、`机器学习` (2)、`UITextInput` (1)、`TextEditor` (1)、`DirectTouch` (1)、`CustomControls` (1)

## 关键 Session

- [WWDC26-219] 提升阅读 App 的辅助功能体验：✅ 这场 Session 最值得关注的一件事是：Apple 终于把多段落离散文本的 VoiceOver 焦点连贯性问题解决了，并且让自定义渲染的文本（如扫描图或 Canvas 绘制的字）能通过实现 UITextInput 获得原生级别的逐词朗读和选择体验。
- [WWDC26-220] 优化自定控件的辅助功能体验：自定义控件的辅助功能终于不再是“加个 Label 糊弄过去”，Apple 用 Direct Touch API 和 Custom Actions 给出了 2D 空间和复杂手势的官方标准解法。
- [WWDC26-221] 针对动态字体准备好你的 Apple tvOS App：tvOS 终于补齐了 Dynamic Type (动态字体) 这块无障碍短板，但这场 Session 真正的价值在于教你如何用 AnyLayout 和 containerRelativeFrame 优雅地重构客厅大屏的响应式布局。
- [WWDC26-230] macOS 评估体验的新动向：✅ macOS 的考试模式（Assessment Mode）终于从“粗暴锁死全屏”进化到了“系统级精细化管控”，教育类 App 不用再自己写脆弱的防作弊拦截代码了。
- [WWDC26-250] 出色设计的原则：这场 Session 最值得关注的一件事是：Apple 在 AI 时代对“责任（Responsibility）”划了硬红线——如果你的 AI 功能存在造成实质伤害的风险（比如给过敏用户推荐致命食材），直接砍掉这个功能，而不是甩锅给一句“AI 可能会出错”的免责声明。
- [WWDC26-251] 在 iOS 上彰显品牌风格：iOS 26 的 Liquid Glass（液态玻璃）彻底终结了"魔改导航栏"的时代，Apple 明确划定界限：UI 层老老实实用系统组件，品牌个性全部塞进内容层。
- [WWDC26-252] 使用 Reality Composer Pro 3 设计无代码游戏：这场 Session 最值得关注的一件事是：Reality Composer Pro 3 的 ScriptGraph 配合即将推出的 Vision Pro 实机 Live Preview，彻底把 visionOS 空间交互的“调参权”从程序员手里抢走，交给了设计师。
- [WWDC26-256] 探索生成式字幕和字幕样式：✅ 视频播放器的脏活累活被 Apple 底层接管了：设备端 AI 字幕生成和实时样式预览现在对标准播放器“零代码”默认生效。
- [WWDC26-285] 探索 USDKit 以及 OpenUSD 的新进展：✅ Apple 终于用纯 Swift 重写了 USD 绑定（USDKit），让 3D 场景组装从“啃 C++ 头文件”变成了“写 SwiftUI 一样的日常”。
- [WWDC26-290] 为 App 中的功能和标签构思一目了然的名称：这场 Session 最值得关注的一件事是，Apple 终于把“起名字”从文案玄学变成了可量化的工程标准，明确告诉你为什么 Apple Cash 叫 "Balance"（余额）而不叫 "Spending Power"（消费能力）。
- [WWDC26-292] 设计直观的搜索体验：✅ iOS 搜索框官方终于“妥协”推荐放底部工具栏了，配合全新的 Liquid Glass（液态玻璃）材质，大屏手机的单手搜索体验迎来史诗级救赎。
- [WWDC26-314] 了解 CSS Grid Lanes：原生 CSS 终于干掉了瀑布流 JS 库，还顺手用 flow tolerance (流容差) 解决了键盘焦点乱跳的无障碍大坑。
- [WWDC26-315] 重新探索 HTML select 元素：✅ 前端开发者终于可以把那些臃肿的第三方 Select JS 库扔进垃圾桶，用纯 CSS 搞定带图标的下拉菜单，且完全不牺牲屏幕阅读器的体验。
- [WWDC25-111] Keynote (ASL)：这是 Keynote 的 ASL（美国手语）版本，内容与 Session 101 完全一致，适合需要手语辅助理解的开发者观看。
- [WWDC25-206] 设计新动态：如果你只做一件事：升级 SDK，让系统控件自动获得 Liquid Glass 效果，其他的适配可以慢慢来。
- [WWDC25-214] 本地化新特性：如果你还在用 .strings 文件做本地化，今年是迁移 String Catalog 的最后窗口——增量翻译检测和内置机器翻译已经让旧方案显得原始。
- [WWDC25-215] 小组件新特性：小组件终于能打字了——这个变化比听起来重要得多，它意味着主屏幕上的那块小方格第一次有了"做事"的能力，而不只是"展示"。
- [WWDC25-221] 辅助功能新特性：Accessibility Nutrition Labels 让辅助功能从"良心活"变成了"竞争力指标"——用户下载前就能看到你做了没有，这比任何技术 API 都更有杀伤力。
