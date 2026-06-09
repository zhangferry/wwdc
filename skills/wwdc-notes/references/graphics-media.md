# Graphics & Media

## 领域判断

Metal、图形、游戏、音视频、照片、相机与 WebKit。本领域覆盖 207 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Audio & Video**：iOS 26 的音频录制能力有了质的飞跃——AirPods 高质量录音、空间音频捕获、Audio Mix 后期处理，三者组合起来可以做出接近专业录音笔的移动端体验。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；如果你做 180/360/广角视频相关的产品，APMP 是你必须理解的格式规范。它定义了非矩形投影视频如何在 QuickTime/MP4 文件中被正确标记和传输——从投影类型到镜头畸变参数，从帧封装到 HLS 流媒体，一套规范覆盖全流程。 来源：[WWDC25-251]、[WWDC25-296]、[WWDC25-297]、[WWDC25-300]
- **AVFoundation**：这场 Session 最值得关注的一件事是：苹果终于把 Final Cut Pro 里那套极其好用的音频节拍和结构分析能力，剥离出来做成了系统级的 MusicUnderstanding 框架，第三方 App 终于不用自己手搓 FFT（快速傅里叶变换）或买昂贵的第三方 SDK 来做音乐卡点了。；✅ 视频播放器的脏活累活被 Apple 底层接管了：设备端 AI 字幕生成和实时样式预览现在对标准播放器“零代码”默认生效。；这场 Session 最值得关注的一件事是：Apple 终于官方下场解决了 AVCaptureSession 启动慢的顽疾，全新的 Deferred Start（延迟启动）API 让相机首帧预览时间大幅缩短，以前靠 Hack 实现的“秒开”现在成了标准操作。 来源：[WWDC26-253]、[WWDC26-256]、[WWDC26-303]、[WWDC26-304]
- **RealityKit**：SceneKit 正式 soft deprecated 了。现有 app 不会挂，但别指望新功能。如果你手上还有 SceneKit 项目，这是 Apple 给你的官方迁移指南——从资产转换到后处理 bloom，手把手把一个完整游戏搬到 RealityKit。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；如果你有一个基于 Metal 渲染的 iOS/iPadOS 游戏，这场 Session 提供了一套从"兼容模式运行"到"原生立体渲染"的渐进式升级路径，不需要一步到位重写整个游戏。 来源：[WWDC25-288]、[WWDC25-296]、[WWDC24-10093]、[WWDC24-111801]
- **图形与游戏**：Metal 4 的核心变化是"编码统一、资源规模化、管线预编译"——如果你的游戏引擎还在用 Metal 3 的 encoder 体系，这次升级的 ROI 非常高。；Metal 4 把 ML 正式纳入了 GPU 渲染管线——MTLTensor 解决了多维数据的资源管理，ML Command Encoder 让整网推理和渲染/计算命令在同一时间线上同步执行，而 Shader ML 允许你在 fragment shader 内部直接跑神经网络。这套组合拳瞄准的是实时渲染中 ML 最密集的三个场景：超分、材质压缩和光照计算。；RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。 来源：[WWDC25-254]、[WWDC25-262]、[WWDC25-287]、[WWDC25-288]
- **空间计算**：iOS 26 的音频录制能力有了质的飞跃——AirPods 高质量录音、空间音频捕获、Audio Mix 后期处理，三者组合起来可以做出接近专业录音笔的移动端体验。；Metal immersive 渲染今年加了四样东西：hover effects 让交互对象有视觉反馈、动态渲染质量按场景复杂度调分辨率、progressive immersion 用 stencil 裁剪门户外的像素、Mac 可以直接渲染 immersive content 流式投射到 Vision Pro。最后一个是最大的玩法变化。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。 来源：[WWDC25-251]、[WWDC25-294]、[WWDC25-296]、[WWDC25-304]
- **Graphics & Games**：统一游戏平台意味着你的游戏要同时适配 Mac、iPad、iPhone 三种形态——这篇 Session 给出了从首次启动到手柄适配的全套设计指南，核心原则是：让玩家零等待进入游戏，让 UI 适应设备而不是反过来。；Game Porting Toolkit 让你在几分钟内看到 Windows 游戏在 Mac 上的潜力，这是游戏移植的起点而非终点。；Metal 3 的新编译管线让着色器（Shader）编译从运行时提前到构建时——应用启动不再卡在 shader 编译上，帧率更稳定。 来源：[WWDC24-10085]、[WWDC23-10123]、[WWDC21-10229]、[WWDC20-10089]
- **Metal**：✅ "For this Mac" (针对此 Mac 优化) 预设把 Mac 游戏的画质调节从“玄学”变成了“一键最优解”，这是 3A 级图形应用在 Apple Silicon 上真正走向成熟的标志。；这场 Session 最值得关注的一件事是：Apple 终于把 Core ML 模型塞进了 RAW 解码管线（Pipeline），用神经网络接管了去马赛克（Demosaic）和降噪（Denoise），这意味着第三方修图 App 终于能拿到和系统相册一样“作弊”级别的 RAW 解析画质了。；这场 Session 最值得关注的一件事是：Apple 终于把“虚拟按键”提升到了和物理手柄同等的一等公民地位，TCTouchController 让你写一套输入逻辑就能同时搞定手柄和屏幕触控。 来源：[WWDC26-10356]、[WWDC26-305]、[WWDC26-358]、[WWDC26-388]

## API 演进时间线

- **WWDC26**：20 场，代表来源：[WWDC26-10356]、[WWDC26-204]、[WWDC26-216]、[WWDC26-224]、[WWDC26-226]
- **WWDC25**：35 场，代表来源：[WWDC25-101]、[WWDC25-102]、[WWDC25-201]、[WWDC25-205]、[WWDC25-209]
- **WWDC24**：14 场，代表来源：[WWDC24-10066]、[WWDC24-10085]、[WWDC24-10088]、[WWDC24-10089]、[WWDC24-10092]
- **WWDC23**：21 场，代表来源：[WWDC23-10071]、[WWDC23-10083]、[WWDC23-10088]、[WWDC23-10089]、[WWDC23-10105]
- **WWDC22**：28 场，代表来源：[WWDC22-10018]、[WWDC22-10022]、[WWDC22-10023]、[WWDC22-10048]、[WWDC22-10049]
- **WWDC21**：43 场，代表来源：[WWDC21-10021]、[WWDC21-10027]、[WWDC21-10030]、[WWDC21-10044]、[WWDC21-10045]
- **WWDC20**：46 场，代表来源：[WWDC20-10008]、[WWDC20-10009]、[WWDC20-10010]、[WWDC20-10011]、[WWDC20-10012]

## 决策启发式

- 已有项目的迁移策略
- 新项目的采用建议
- 实战中容易踩的坑
- 已有项目的迁移策略 ：千万别一上来就建个 macOS Target 开始写原生 Metal。先花两周时间，用 GPTK 把现有的 Windows/DX12 构建跑起来。用 Metal HUD 抓取 CPU/GPU 压力信号，把“翻译层导致的假卡顿”和“引擎本身的真瓶颈”分开，整理出一份优先级明确的移植 Backlog。
- 新项目的采用建议 ：把 MetalFX Upscaling 和 Dynamic Resolution Scaling 作为渲染管线的一等公民，而不是后期加的“优化补丁”。在架构设计阶段，就确保你的 G Buffer 和运动矢量能完美喂给 MetalFX 时间缩放器。
- 实战避坑 ：在 GPTK 评估阶段，如果遇到音频中间件卡顿或着色器编译导致的掉帧，直接忽略。这些是 D3DMetal 翻译层的已知开销，切到原生 Metal 构建后会自动消失。把精力集中在游戏逻辑线程的锁竞争和内存分配上。
- 已有 Chrome 扩展迁移 ：如果你的扩展已经是 Manifest V3，直接复用 95% 的代码。重点检查 background 脚本，Safari 强制要求使用 Service Worker，不支持 persistent background pages。另外，把 <all urls 这种宽泛权限拆成 Optional Host Permissions，在 Safari 里体验会好很多。
- 新项目架构建议 ：采用“核心逻辑纯 Web + 平台特性 Native”的架构。把 UI、网络拦截、DOM 操作全部用标准 Web API 写好，这部分代码可以跨浏览器复用。只有当需要用到 Touch ID、Keychain 或跨 App 通信时，才在 Xcode 里写一层薄薄的 Native Wrapper，通过 browser.runtime.sendNativeMessage 桥接。
- 调试避坑 ：在 Safari 设置里开启“允许未签名的扩展”后，每次修改代码不需要重启 Safari，只需在扩展管理面板点一下“重新加载”按钮。但如果修改了 manifest.json 里的权限，建议彻底关掉 Safari 再重开，避免权限缓存导致灵异事件。
- 全面排查自定义播放器 ：如果你的 App 用了自定义播放器 UI，赶紧检查是否暴露了字幕选择入口。如果没有，直接实例化 AVLegibleMediaOptionsMenuController 挂载到你的视图上，这是接入 AI 字幕和样式预览最省事的路径。

## 反模式与坑

- 搭配 "Gain insights into your Metal app with Xcode 12" 一起看，可以掌握完整的 Metal 调试工具链
- 架构桥接 (Architecture Bridge) 的单元测试 ：CDPR 在移植初期用单元测试验证了 x86 到 ARM 的内存对齐和字节序假设，这比在运行时抓 Crash 高效得多。
- 原生平台特性的全面接入 ：除了图形，他们还适配了 macOS 的窗口管理、App 切换、手柄/键鼠输入无缝切换以及 iCloud 云存档，这才是“Native Feel (原生体验)”的完整拼图。
- Agentic Coding (智能体编程) 的暗示 ：Session 结尾提到了 "Speedrun your game port with agentic coding"，暗示 Apple 正在推基于 AI 的自动化代码翻译和重构工具，这可能是明年 GPTK 的大招。
- CSS random() 函数 ：可以在 CSS 中直接生成随机数，配合命名作用域可以避免每次重绘都重新计算，做随机粒子背景非常方便。
- Emoji 17 bit 截断 Hack ：WebKit 在引擎层拦截了超过 16 bit 的 emoji 输入，以替代文本形式发给网页，强行修复了老旧网站用 .fromCharCode 导致的乱码问题。
- SVG 2 标准化推进 ：Apple 工程师直接参与了 SVG 工作组的规范制定，明确了径向渐变 fx/fy 的默认值，顺手在 Safari 27 里修了 75 个 SVG 渲染 bug。
- 原生消息传递 (Native Messaging) ：Session 展示了通过 Xcode 打包后，JS 可以直接和包含它的 macOS/iOS App 通信，这是解锁 Apple 平台专属能力（如 Local Authentication）的唯一途径。

## 高频主题

`空间计算` (11)、`Audio & Video` (10)、`图形与游戏` (10)、`AVFoundation` (6)、`SwiftUI` (6)、`Safari与Web` (6)、`Metal` (5)、`MetalFX` (5)、`应用服务` (5)、`Photos & Camera` (5)、`基础` (4)、`Game Porting Toolkit` (3)、`WebKit` (3)、`CSS` (3)、`Accessibility` (3)、`Camera` (3)、`Metal 4` (3)、`Design` (3)

## 关键 Session

- [WWDC26-10356] “赛博朋克 2077”登陆 Mac：✅ "For this Mac" (针对此 Mac 优化) 预设把 Mac 游戏的画质调节从“玄学”变成了“一键最优解”，这是 3A 级图形应用在 Apple Silicon 上真正走向成熟的标志。
- [WWDC26-204] 面向 Safari 浏览器 27 的 WebKit 新功能：Safari 终于原生支持 <select 深度定制和 <model 3D 渲染，Web 开发者不用再捏着鼻子写一堆 div 模拟表单和引入沉重的 Three.js 了。
- [WWDC26-216] 创建 Safari 浏览器的网页扩展：这场 Session 最值得关注的一件事是：Safari 扩展开发终于把前端开发者当人看了，全程无需打开 Xcode 就能完成 90% 的开发和调试。
- [WWDC26-224] 扩展虚拟化 App 的功能：✅ DiskImageKit 和 USB 直通的加入，让第三方虚拟机 App 终于能摆脱“玩具”标签，直接硬刚 Parallels Desktop 的核心体验。
- [WWDC26-226] 打造实时沟通体验：✅ CallKit 终于迎来了现代重构，LiveCommunicationKit 用统一的 Action 机制彻底解决了 VoIP 应用系统 UI 与 App 内 UI 状态撕裂的顽疾。
- [WWDC26-253] 了解 Music Understanding 框架：这场 Session 最值得关注的一件事是：苹果终于把 Final Cut Pro 里那套极其好用的音频节拍和结构分析能力，剥离出来做成了系统级的 MusicUnderstanding 框架，第三方 App 终于不用自己手搓 FFT（快速傅里叶变换）或买昂贵的第三方 SDK 来做音乐卡点了。
- [WWDC26-256] 探索生成式字幕和字幕样式：✅ 视频播放器的脏活累活被 Apple 底层接管了：设备端 AI 字幕生成和实时样式预览现在对标准播放器“零代码”默认生效。
- [WWDC26-297] 将视觉智能整合到 App 中的最佳做法：这场 Session 最值得关注的一件事是：Visual Intelligence（视觉智能）终于开放了基于本地图像特征的自定义搜索接入，你的 App 现在可以直接“看懂”用户框选的屏幕截图或相机画面，并把业务数据塞进系统的原生结果页了。
- [WWDC26-303] 构建灵敏还秒开的相机 App：这场 Session 最值得关注的一件事是：Apple 终于官方下场解决了 AVCaptureSession 启动慢的顽疾，全新的 Deferred Start（延迟启动）API 让相机首帧预览时间大幅缩短，以前靠 Hack 实现的“秒开”现在成了标准操作。
- [WWDC26-304] 实现高分辨率照片拍摄：这场 Session 最值得关注的一件事是：Apple 终于把原生相机 App 里“连拍不卡顿”的秘密武器——延迟照片处理 (Deferred photo processing) 和快速拍摄优先 (Fast capture prioritization) 彻底向第三方开放了。
- [WWDC26-305] 使用 Core Image 增强 RAW 图像处理：这场 Session 最值得关注的一件事是：Apple 终于把 Core ML 模型塞进了 RAW 解码管线（Pipeline），用神经网络接管了去马赛克（Demosaic）和降噪（Denoise），这意味着第三方修图 App 终于能拿到和系统相册一样“作弊”级别的 RAW 解析画质了。
- [WWDC26-314] 了解 CSS Grid Lanes：原生 CSS 终于干掉了瀑布流 JS 库，还顺手用 flow tolerance (流容差) 解决了键盘焦点乱跳的无障碍大坑。
- [WWDC26-315] 重新探索 HTML select 元素：✅ 前端开发者终于可以把那些臃肿的第三方 Select JS 库扔进垃圾桶，用纯 CSS 搞定带图标的下拉菜单，且完全不牺牲屏幕阅读器的体验。
- [WWDC26-322] 使用 SwiftUI 构建高级图形效果：这场 Session 最值得关注的一件事是：Apple 终于把 alignmentGuide (对齐参考线) 的隐藏潜力和 layerEffect (图层效果) 结合起来了，这意味着你纯靠 SwiftUI 就能复刻 Apple Music 歌词页那种“像素级扭曲背景+语义化浮动时间戳”的变态级 UI，不用再写一行 UIKit 或 Core Animation 胶水代码。
- [WWDC26-338] 为 Apple 沉浸视频构建实时制作工具：Apple 终于把 Vision Pro 的“看片”体验推向了广电级直播工业标准，SMPTE 2110 和流式 ProRes 的直接打通，意味着第三方导播台和即时回放系统可以无缝接入 Apple Immersive Video (AIV) 生态了。
- [WWDC26-341] 让你的 iOS App 支持 Center Stage 前置摄像头：前置摄像头换成方形传感器后，dynamicAspectRatio 让相机 App 终于能在不中断预览的情况下，无缝且无裁切地切换横竖屏构图了。
- [WWDC26-357] 通过智能体编码加速你的游戏移植进程：✅ "Game Porting Toolkit 4 把 AI Agent 变成了懂 Metal 4 底层细节的结对编程老手，打破了 AI 无法调试 GPU 渲染黑屏的死局。"
- [WWDC26-358] 巧用触控打造出色的游戏：这场 Session 最值得关注的一件事是：Apple 终于把“虚拟按键”提升到了和物理手柄同等的一等公民地位，TCTouchController 让你写一套输入逻辑就能同时搞定手柄和屏幕触控。
