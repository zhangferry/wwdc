# Graphics & Media

## 领域判断

Metal、图形、游戏、音视频、照片、相机与 WebKit。本领域覆盖 206 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Audio & Video**：iOS 26 的音频录制能力有了质的飞跃——AirPods 高质量录音、空间音频捕获、Audio Mix 后期处理，三者组合起来可以做出接近专业录音笔的移动端体验。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；如果你做 180/360/广角视频相关的产品，APMP 是你必须理解的格式规范。它定义了非矩形投影视频如何在 QuickTime/MP4 文件中被正确标记和传输——从投影类型到镜头畸变参数，从帧封装到 HLS 流媒体，一套规范覆盖全流程。 来源：[WWDC25-251]、[WWDC25-296]、[WWDC25-297]、[WWDC25-300]
- **AVFoundation**：如果你还在用 UIViewRepresentable 包相机预览，这场 Session 能让你删掉一半的胶水代码——但仅限 iOS 19+。；多路音视频同步播放——体育赛事多机位、演唱会多视角、手语流——以前要自己管状态同步和 AirPlay 路由，现在 AVFoundation 和 AVRouting 给了一套完整方案。；iOS 18 的 AVMetrics API 让你能以事件流的方式精确追踪 HLS 播放的每一个环节——从 playlist 请求到 content key 获取到 stall 发生——终于可以在客户端层面系统性地诊断播放质量问题了。 来源：[WWDC25-211]、[WWDC25-302]、[WWDC24-10113]、[WWDC24-10166]
- **Graphics, Games & Media**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：将 macOS 27 强大的新功能融入你的虚拟化 App。了解如何通过在首次启动时设置用户账户来自动配置 macOS 客户机。我们将一起探索一些高级工作流程，看看如何实现 USB 配件直通虚拟机，以及自定网络拓扑和端口转发。你还将了解能够丰富 App 虚拟机体验的最新改进。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Music Understanding 这个新框架，让你的 App 能在设备端从六个维度分析音频：调性、节奏、结构、速度、乐器活动和响度。你还将利用“Music Understanding Lab”示例 App 直观地查看各个结果。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：深入了解视觉智能如何改变你 App 中的内容发现体验。探索如何定义实体、处理图像，并高效管理多种结果类型。了解优化速度和相关性的最佳做法，并探索意图如何实现一键打开或播放内容等直接操作。 来源：[WWDC26-224]、[WWDC26-253]、[WWDC26-297]、[WWDC26-303]
- **RealityKit**：SceneKit 正式 soft deprecated 了。现有 app 不会挂，但别指望新功能。如果你手上还有 SceneKit 项目，这是 Apple 给你的官方迁移指南——从资产转换到后处理 bloom，手把手把一个完整游戏搬到 RealityKit。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；如果你有一个基于 Metal 渲染的 iOS/iPadOS 游戏，这场 Session 提供了一套从"兼容模式运行"到"原生立体渲染"的渐进式升级路径，不需要一步到位重写整个游戏。 来源：[WWDC25-288]、[WWDC25-296]、[WWDC24-10093]、[WWDC24-111801]
- **图形与游戏**：Metal 4 的核心变化是"编码统一、资源规模化、管线预编译"——如果你的游戏引擎还在用 Metal 3 的 encoder 体系，这次升级的 ROI 非常高。；Metal 4 把 ML 正式纳入了 GPU 渲染管线——MTLTensor 解决了多维数据的资源管理，ML Command Encoder 让整网推理和渲染/计算命令在同一时间线上同步执行，而 Shader ML 允许你在 fragment shader 内部直接跑神经网络。这套组合拳瞄准的是实时渲染中 ML 最密集的三个场景：超分、材质压缩和光照计算。；RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。 来源：[WWDC25-254]、[WWDC25-262]、[WWDC25-287]、[WWDC25-288]
- **空间计算**：iOS 26 的音频录制能力有了质的飞跃——AirPods 高质量录音、空间音频捕获、Audio Mix 后期处理，三者组合起来可以做出接近专业录音笔的移动端体验。；Metal immersive 渲染今年加了四样东西：hover effects 让交互对象有视觉反馈、动态渲染质量按场景复杂度调分辨率、progressive immersion 用 stencil 裁剪门户外的像素、Mac 可以直接渲染 immersive content 流式投射到 Vision Pro。最后一个是最大的玩法变化。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。 来源：[WWDC25-251]、[WWDC25-294]、[WWDC25-296]、[WWDC25-304]
- **Graphics & Games**：统一游戏平台意味着你的游戏要同时适配 Mac、iPad、iPhone 三种形态——这篇 Session 给出了从首次启动到手柄适配的全套设计指南，核心原则是：让玩家零等待进入游戏，让 UI 适应设备而不是反过来。；Game Porting Toolkit 让你在几分钟内看到 Windows 游戏在 Mac 上的潜力，这是游戏移植的起点而非终点。；Metal 3 的新编译管线让着色器（Shader）编译从运行时提前到构建时——应用启动不再卡在 shader 编译上，帧率更稳定。 来源：[WWDC24-10085]、[WWDC23-10123]、[WWDC21-10229]、[WWDC20-10089]

## API 演进时间线

- **WWDC26**：19 场，代表来源：[WWDC26-204]、[WWDC26-216]、[WWDC26-224]、[WWDC26-252]、[WWDC26-253]
- **WWDC25**：35 场，代表来源：[WWDC25-101]、[WWDC25-102]、[WWDC25-201]、[WWDC25-205]、[WWDC25-209]
- **WWDC24**：14 场，代表来源：[WWDC24-10066]、[WWDC24-10085]、[WWDC24-10088]、[WWDC24-10089]、[WWDC24-10092]
- **WWDC23**：21 场，代表来源：[WWDC23-10071]、[WWDC23-10083]、[WWDC23-10088]、[WWDC23-10089]、[WWDC23-10105]
- **WWDC22**：28 场，代表来源：[WWDC22-10018]、[WWDC22-10022]、[WWDC22-10023]、[WWDC22-10048]、[WWDC22-10049]
- **WWDC21**：43 场，代表来源：[WWDC21-10021]、[WWDC21-10027]、[WWDC21-10030]、[WWDC21-10044]、[WWDC21-10045]
- **WWDC20**：46 场，代表来源：[WWDC20-10008]、[WWDC20-10009]、[WWDC20-10010]、[WWDC20-10011]、[WWDC20-10012]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 立即 recompile 你的 app 看 Liquid Glass 效果 。标准控件自动更新，不需要改代码。然后逐步审计自定义组件，优先替换为框架原生视图。
- Foundation Models 适合做内容生成、摘要、分类等"日常智能"任务 。不适合需要最新知识或超长上下文的场景。用 tool calling 补齐信息缺口。
- Xcode coding assistant 的对话历史功能是安全网 。大胆探索不同实现方案，随时回滚到任意历史节点。
- Swift 6.2 迁移建议 ：先在模块级别开启 MainActor by default，确认没有误杀并发代码后再逐步清理 warning。
- App 图标现在要过四关 ：全彩、tint、clear、macOS 圆角矩形。用 Icon Composer 从一开始就设计多层结构。
- Liquid Glass adoption 不要一步到位 。先 recompile 看效果，再用 toolbar spacer、tint 等 API 微调，最后处理自定义控件。很多自定义背景和边框现在可以删掉了。
- Foundation Models 用 playground 宏做 prompt engineering 。在 Xcode 中用 playground 快速迭代不同 prompt，找到最佳结果后再集成到 app。

## 反模式与坑

- 搭配 "Gain insights into your Metal app with Xcode 12" 一起看，可以掌握完整的 Metal 调试工具链
- App Intents + Visual Intelligence ：你的 app 可以注册 Visual Search schema，让用户通过相机识别直接跳转到你的 app。
- Background Tasks API 更新 ：支持后台长时间任务（如视频导出），CarPlay 支持 Live Activities。
- Terminal 更新 ：24 bit 色彩、Liquid Glass 主题、Powerline 字体支持。
- PermissionKit 框架 ：为儿童通信提供家长监督机制。
- Declared Age Range API ：在不侵犯隐私的前提下适龄调整 app 体验。
- Liquid Glass 不只是视觉改版
- Foundation Models 的 @Generable 是杀手级 API

## 高频主题

`空间计算` (11)、`Audio & Video` (10)、`图形与游戏` (10)、`Graphics, Games & Media` (8)、`SwiftUI` (6)、`Safari与Web` (6)、`Metal` (5)、`应用服务` (5)、`Photos & Camera` (5)、`Safari` (4)、`基础` (4)、`Design` (3)、`WebKit` (2)、`GPU` (2)、`MetalFX` (2)、`机器学习` (2)、`Xcode` (1)、`Core Image` (1)

## 关键 Session

- [WWDC26-204] 面向 Safari 浏览器 27 的 WebKit 新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 WebKit 的新功能：从 Grid Lanes 和可自定选择，到 HTML 模型和沉浸式环境，再到最新的网页扩展，种种创新为你再添助力。你还将走进上千项浏览器引擎改进的幕后，了解这些让网页更可靠的改进是如何实现的。
- [WWDC26-216] 创建 Safari 浏览器的网页扩展：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：从零开始构建并测试 Safari 浏览器网页扩展，放心迈出入门第一步，而且全程无需使用 Xcode。探索内容拦截、页面修改、原生通信和权限模式如何协同工作，跨平台打造强大且保护隐私的浏览体验。
- [WWDC26-224] 扩展虚拟化 App 的功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：将 macOS 27 强大的新功能融入你的虚拟化 App。了解如何通过在首次启动时设置用户账户来自动配置 macOS 客户机。我们将一起探索一些高级工作流程，看看如何实现 USB 配件直通虚拟机，以及自定网络拓扑和端口转发。你还将了解能够丰富 App 虚拟机体验的最新改进。
- [WWDC26-252] 使用 Reality Composer Pro 3 设计无代码游戏：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何在 Reality Composer Pro 3 中使用 ScriptGraph 为你的 App 和游戏开发无代码 3D 内容。了解如何利用可视化节点来构建动画、创建互动时刻，并整合 SwiftUI 元素，为你的体验添加对话气泡和其他 UI。
- [WWDC26-253] 了解 Music Understanding 框架：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Music Understanding 这个新框架，让你的 App 能在设备端从六个维度分析音频：调性、节奏、结构、速度、乐器活动和响度。你还将利用“Music Understanding Lab”示例 App 直观地查看各个结果。
- [WWDC26-297] 将视觉智能整合到 App 中的最佳做法：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：深入了解视觉智能如何改变你 App 中的内容发现体验。探索如何定义实体、处理图像，并高效管理多种结果类型。了解优化速度和相关性的最佳做法，并探索意图如何实现一键打开或播放内容等直接操作。
- [WWDC26-303] 构建灵敏还秒开的相机 App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何打造一款能够瞬间启动的相机 App，帮助用户捕捉每个精彩瞬间。探索如何优化从 App 启动到首帧预览的整个相机启动流程。了解可加快启动速度的全新 API，以及实现流畅预览渲染和持续稳定性能的最佳做法，从而确保你的 App 为用户带来精妙的相机体验。
- [WWDC26-304] 实现高分辨率照片拍摄：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 AVFoundation，使用你的 App 拍摄超高分辨率照片。了解三种不同的拍照选项：RAW、分段曝光和完全处理，以及各个选项的适用场景。详细探索如何配置主摄像头、长焦摄像头以及超广角摄像头，实现 2400 万像素和 4800 万像素照片拍摄。此外，了解延迟照片处理如何让你的 App 在拍摄更多照片时也能保持响应灵敏。
- [WWDC26-305] 使用 Core Image 增强 RAW 图像处理：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：运用 Core Image RAW 处理 API 版本 9 的强大功能，大幅提升你 App 的图像质量、增强锐度和色彩表现，同时利用 Apple 神经网络引擎来实现最优性能。借助 CIRAWFilter API，让用户能够通过更改曝光、降噪、锐度和对比度等参数来编辑 RAW 照片。探索全新的 CIImageProcessor API，通过对图块大小和缓冲区管理的精细控制进一步优化性能。
- [WWDC26-322] 使用 SwiftUI 构建高级图形效果：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何通过创造性地组合运用 SwiftUI 布局和图形 API 来打造丰富的自定体验。我们将介绍如何分解复杂的设计，并通过创意流程将简单的构建块串联起来。了解如何使用图层着色器进行绘制、利用时间线制作动画，并通过对齐参考线锚定视图。
- [WWDC26-341] 让你的 iOS App 支持 Center Stage 前置摄像头：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 AVCapture API，利用 iPhone 17、iPhone 17 Pro 和 iPhone Air 配备的 Center Stage 前置摄像头，为你的 iOS 相机 App 注入强劲动力。探索这些 API 如何实现缩放和旋转选项，从而更灵活地调整自拍和视频构图，并让拍合照的每个人都能自动入境。通过整合视频通话人物居中功能来自动调整画面构图，让用户在虚拟会议和 FaceTime 通话中稳居前排 C 位。你还将了解如何为实时视频会议实现视频防抖功能。
- [WWDC26-356] “赛博朋克 2077”登陆 Mac：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：深入了解幕后故事，看看“赛博朋克 2077”如何登陆 Mac，为 macOS 上的 3A 游戏体验树立新标杆。探索 CD PROJEKT RED 开发团队如何利用 Apple 强大的硬件、软件和开发工具，将这种高保真体验变为现实。了解如何将类似的技术应用到你的游戏中；以及创新的“针对此 Mac 优化”预设如何自动优化图形设置，在 Mac 全线产品上平衡视觉保真度和帧率。
- [WWDC26-357] 通过智能体编码加速你的游戏移植进程：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助游戏移植工具包 4 中全新的智能体功能，大幅加快你的游戏移植进程，从而快速开启游戏登陆 Apple 平台的旅程。探索如何与 AI 编码助手协同工作，以便采用 Metal 4、整合 MetalFX 并针对 Apple 硬件优化游戏。了解智能体如何利用 Metal 调试工具自动排查 GPU 渲染故障，助你专心处理最重要的事。
- [WWDC26-358] 巧用触控打造出色的游戏：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：深入了解相关技巧，为你的游戏构建引人入胜的触控体验。我们将分享从独立游戏开发到 3A 游戏开发的专家见解，探索打造直观触控操作的最佳做法，并介绍如何利用 Touch Controller 框架和 Metal 等 Apple 技术实现出色性能。
- [WWDC26-359] 使用 Metal 构建实时神经网络渲染管线：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何使用 Metal 4 将机器学习整合到实时渲染管线中。我们将介绍利用 MetalFX 神经网络降噪实现生产级效果的实用模式和最佳做法，并分享来自 Maxon Redshift Live 的真实经验。了解如何使用 ML 命令编码器，在图形工作流程中训练和部署神经网络色调映射器。最后，深入探索新的张量 API，直接在着色器中构建并评估小型专用神经网络。
- [WWDC26-378] 通过 StoreKit 和后台资源解锁游戏内内容：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 Steam Asset Converter 和新的 Unity 插件，简化你的跨平台开发，并为 App 内购买项目提供更好的支持。了解如何通过特定于语言的资源包，精准地分发恰如所需的内容，从而让你的游戏更精简，并为玩家带来更出色的体验。
- [WWDC26-388] 查找并修复 Metal 游戏中的性能问题：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用强大的 Metal 工具追踪难以发现的游戏性能问题。了解如何通过 Instruments 中的 Game Performance Overview 收集丰富的性能数据，在 macOS 和 iOS 上分别利用 metalperftrace 和控制中心来运行后台性能追踪，并使用全新的 StateReporting API 将指标直接关联到游戏的运行时状态。将数小时的遥测数据转化为清晰明确、切实可行的见解。
- [WWDC26-8015] Safari 浏览器和网页技术小组实验室：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，与 Apple 工程师一起深入探索 WWDC26。在这个以 Safari 浏览器和网页技术为主题的活动中，你可以提出问题、获取建议，并实时关注围绕大会一周的相关重磅发布展开的精彩讨论。活动语言为英语。
