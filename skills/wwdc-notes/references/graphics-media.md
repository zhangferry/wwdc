# Graphics & Media

## 领域判断

Metal、图形、游戏、音视频、照片、相机与 WebKit。本领域覆盖 187 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Audio & Video**：iOS 26 的音频录制能力有了质的飞跃——AirPods 高质量录音、空间音频捕获、Audio Mix 后期处理，三者组合起来可以做出接近专业录音笔的移动端体验。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；如果你做 180/360/广角视频相关的产品，APMP 是你必须理解的格式规范。它定义了非矩形投影视频如何在 QuickTime/MP4 文件中被正确标记和传输——从投影类型到镜头畸变参数，从帧封装到 HLS 流媒体，一套规范覆盖全流程。 来源：[WWDC25-251]、[WWDC25-296]、[WWDC25-297]、[WWDC25-300]
- **AVFoundation**：如果你还在用 UIViewRepresentable 包相机预览，这场 Session 能让你删掉一半的胶水代码——但仅限 iOS 19+。；多路音视频同步播放——体育赛事多机位、演唱会多视角、手语流——以前要自己管状态同步和 AirPlay 路由，现在 AVFoundation 和 AVRouting 给了一套完整方案。；iOS 18 的 AVMetrics API 让你能以事件流的方式精确追踪 HLS 播放的每一个环节——从 playlist 请求到 content key 获取到 stall 发生——终于可以在客户端层面系统性地诊断播放质量问题了。 来源：[WWDC25-211]、[WWDC25-302]、[WWDC24-10113]、[WWDC24-10166]
- **RealityKit**：SceneKit 正式 soft deprecated 了。现有 app 不会挂，但别指望新功能。如果你手上还有 SceneKit 项目，这是 Apple 给你的官方迁移指南——从资产转换到后处理 bloom，手把手把一个完整游戏搬到 RealityKit。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；如果你有一个基于 Metal 渲染的 iOS/iPadOS 游戏，这场 Session 提供了一套从"兼容模式运行"到"原生立体渲染"的渐进式升级路径，不需要一步到位重写整个游戏。 来源：[WWDC25-288]、[WWDC25-296]、[WWDC24-10093]、[WWDC24-111801]
- **图形与游戏**：Metal 4 的核心变化是"编码统一、资源规模化、管线预编译"——如果你的游戏引擎还在用 Metal 3 的 encoder 体系，这次升级的 ROI 非常高。；Metal 4 把 ML 正式纳入了 GPU 渲染管线——MTLTensor 解决了多维数据的资源管理，ML Command Encoder 让整网推理和渲染/计算命令在同一时间线上同步执行，而 Shader ML 允许你在 fragment shader 内部直接跑神经网络。这套组合拳瞄准的是实时渲染中 ML 最密集的三个场景：超分、材质压缩和光照计算。；RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。 来源：[WWDC25-254]、[WWDC25-262]、[WWDC25-287]、[WWDC25-288]
- **空间计算**：iOS 26 的音频录制能力有了质的飞跃——AirPods 高质量录音、空间音频捕获、Audio Mix 后期处理，三者组合起来可以做出接近专业录音笔的移动端体验。；Metal immersive 渲染今年加了四样东西：hover effects 让交互对象有视觉反馈、动态渲染质量按场景复杂度调分辨率、progressive immersion 用 stencil 裁剪门户外的像素、Mac 可以直接渲染 immersive content 流式投射到 Vision Pro。最后一个是最大的玩法变化。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。 来源：[WWDC25-251]、[WWDC25-294]、[WWDC25-296]、[WWDC25-304]
- **Graphics & Games**：统一游戏平台意味着你的游戏要同时适配 Mac、iPad、iPhone 三种形态——这篇 Session 给出了从首次启动到手柄适配的全套设计指南，核心原则是：让玩家零等待进入游戏，让 UI 适应设备而不是反过来。；Game Porting Toolkit 让你在几分钟内看到 Windows 游戏在 Mac 上的潜力，这是游戏移植的起点而非终点。；Metal 3 的新编译管线让着色器（Shader）编译从运行时提前到构建时——应用启动不再卡在 shader 编译上，帧率更稳定。 来源：[WWDC24-10085]、[WWDC23-10123]、[WWDC21-10229]、[WWDC20-10089]
- **Safari与Web**：如果你之前在 SwiftUI 里用 UIViewRepresentable 包装 WKWebView，现在可以把那坨胶水代码删掉了——WebKit for SwiftUI 的原生 API 把 web 内容集成简化到了"传个 URL 就行"的程度。；上传身份证照片做在线身份验证的时代终于要结束了——W3C Digital Credentials API 让网站可以直接从 Wallet 里的证件获取加密验证过的身份信息，用户只需 Face ID 授权。；Safari 19 一口气补齐了 scroll driven animations、anchor positioning 和 cross document view transitions 这三个 CSS 大特性，终于不用再为这些写一堆 JavaScript polyfill 了。 来源：[WWDC25-231]、[WWDC25-232]、[WWDC25-233]、[WWDC25-235]

## API 演进时间线

- **WWDC25**：35 场，代表来源：[WWDC25-101]、[WWDC25-102]、[WWDC25-201]、[WWDC25-205]、[WWDC25-209]
- **WWDC24**：14 场，代表来源：[WWDC24-10066]、[WWDC24-10085]、[WWDC24-10088]、[WWDC24-10089]、[WWDC24-10092]
- **WWDC23**：21 场，代表来源：[WWDC23-10071]、[WWDC23-10083]、[WWDC23-10088]、[WWDC23-10089]、[WWDC23-10105]
- **WWDC22**：28 场，代表来源：[WWDC22-10018]、[WWDC22-10022]、[WWDC22-10023]、[WWDC22-10048]、[WWDC22-10049]
- **WWDC21**：43 场，代表来源：[WWDC21-10021]、[WWDC21-10027]、[WWDC21-10030]、[WWDC21-10044]、[WWDC21-10045]
- **WWDC20**：46 场，代表来源：[WWDC20-10008]、[WWDC20-10009]、[WWDC20-10010]、[WWDC20-10011]、[WWDC20-10012]

## 决策启发式

- 立即 recompile 你的 app 看 Liquid Glass 效果 。标准控件自动更新，不需要改代码。然后逐步审计自定义组件，优先替换为框架原生视图。
- Foundation Models 适合做内容生成、摘要、分类等"日常智能"任务 。不适合需要最新知识或超长上下文的场景。用 tool calling 补齐信息缺口。
- Xcode coding assistant 的对话历史功能是安全网 。大胆探索不同实现方案，随时回滚到任意历史节点。
- Swift 6.2 迁移建议 ：先在模块级别开启 MainActor by default，确认没有误杀并发代码后再逐步清理 warning。
- App 图标现在要过四关 ：全彩、tint、clear、macOS 圆角矩形。用 Icon Composer 从一开始就设计多层结构。
- Liquid Glass adoption 不要一步到位 。先 recompile 看效果，再用 toolbar spacer、tint 等 API 微调，最后处理自定义控件。很多自定义背景和边框现在可以删掉了。
- Foundation Models 用 playground 宏做 prompt engineering 。在 Xcode 中用 playground 快速迭代不同 prompt，找到最佳结果后再集成到 app。
- SwiftData 在今年获得了 model subclassing 和 entity inheritance 。如果你之前因为数据模型灵活性不够而犹豫，现在可以重新评估。
- Metal 4 的 neural rendering 是游戏图形的下一个范式 。在 shader 中直接跑推理网络计算光照和材质，这对光线追踪的性能优化意义重大。
- 对于服务端 Swift 开发者 ，立即试试 Containerization 框架。它提供了在 Mac 上创建、下载、运行 Linux 容器的完整工具链。

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

`空间计算` (11)、`Audio & Video` (10)、`图形与游戏` (10)、`Safari与Web` (6)、`应用服务` (5)、`Photos & Camera` (5)、`基础` (4)、`SwiftUI` (4)、`Design` (3)、`GPU` (2)、`MetalFX` (2)、`机器学习` (2)、`Metal` (1)、`着色器` (1)、`visionOS` (1)、`Metal 4` (1)、`Machine Learning` (1)、`WebKit` (1)

## 关键 Session

- [WWDC25-101] Keynote：Liquid Glass 是 iOS 7 以来最大的设计变革，Foundation Models 框架让端侧 AI 真正落地到每个 app，Xcode 26 接入多模型 coding assistant 这一届 WWDC 把设计、AI 和工具链三条线同时拉满了。
- [WWDC25-102] Platforms State of the Union：如果说 Keynote 是面向用户的发布会，PSOTU 就是面向开发者的施工图 Liquid Glass 的 API 落地细节、Foundation Models 的 tool calling 和 guided generation、Swift 6.2 的并发简化、Metal 4 的 neural rendering，全部在这里展开。
- [WWDC25-201] Metal 新特性：Metal 终于开始帮你管那些你一直在手动管的东西了——渲染状态、Shader 编译、分辨率折中——这次更新的信号是：别自己造轮子了，用框架的。
- [WWDC25-205] 探索 Metal 4：Metal 4 真正的卖点不是某个新 API，而是它让图形渲染和 ML 推理第一次在 GPU 命令层面上成为同一件事——如果你做游戏或者实时图像处理，这意味着你可以把 Neural Engine 和 GPU 当成一个统一的计算池来调度。
- [WWDC25-209] WebKit 新特性：如果你的 App 里有 WKWebView，今年最该关注的不是某个 CSS 特性，而是 Web Push 和 callAsyncJavaScript 的增强——这两项直接决定了混合架构能走多远。
- [WWDC25-210] Photos 新特性：Apple 终于把照片库的"理解能力"交给了第三方——PhotoAnalysis API 是今年 Photos 框架里真正改变游戏规则的东西，PHPicker 智能筛选和编辑管线反而是锦上添花。
- [WWDC25-211] AVFoundation 新特性：如果你还在用 UIViewRepresentable 包相机预览，这场 Session 能让你删掉一半的胶水代码——但仅限 iOS 19+。
- [WWDC25-231] 认识 WebKit for SwiftUI：如果你之前在 SwiftUI 里用 UIViewRepresentable 包装 WKWebView，现在可以把那坨胶水代码删掉了——WebKit for SwiftUI 的原生 API 把 web 内容集成简化到了"传个 URL 就行"的程度。
- [WWDC25-232] 在 Web 上验证身份证件：上传身份证照片做在线身份验证的时代终于要结束了——W3C Digital Credentials API 让网站可以直接从 Wallet 里的证件获取加密验证过的身份信息，用户只需 Face ID 授权。
- [WWDC25-233] Safari 与 WebKit 新特性：Safari 19 一口气补齐了 scroll driven animations、anchor positioning 和 cross document view transitions 这三个 CSS 大特性，终于不用再为这些写一堆 JavaScript polyfill 了。
- [WWDC25-235] 深入了解声明式 Web Push：如果你的 Web Push Service Worker 代码 90% 的逻辑只是把 push 消息翻译成 showNotification() 调用，那声明式 Web Push 让你可以直接删掉整个 Service Worker——浏览器会自动处理剩下的事。
- [WWDC25-236] 用 WebGPU 解锁 GPU 计算能力：WebGPU 在 Apple 平台上几乎是一对一映射 Metal 的——如果你熟悉 Metal，上手 WebGPU 的障碍接近于零；如果你只熟悉 WebGL，那 compute shader 的能力会让你重新思考"浏览器里能做什么"。
- [WWDC25-251] 增强 app 的音频录制能力：iOS 26 的音频录制能力有了质的飞跃——AirPods 高质量录音、空间音频捕获、Audio Mix 后期处理，三者组合起来可以做出接近专业录音笔的移动端体验。
- [WWDC25-253] 用 Capture Controls 增强相机体验：物理按键拍照 + AirPods 远程快门 + Camera Control 的自定义设置调节——三个 API 组合起来，你的第三方相机 app 可以做到和系统相机一样"手不离键"的操作体验。
- [WWDC25-254] Metal 4 游戏开发深度探索：Metal 4 的核心变化是"编码统一、资源规模化、管线预编译"——如果你的游戏引擎还在用 Metal 3 的 encoder 体系，这次升级的 ROI 非常高。
- [WWDC25-262] Metal 4 ML 与图形融合：Tensor、ML Encoder 和 Shader ML：Metal 4 把 ML 正式纳入了 GPU 渲染管线——MTLTensor 解决了多维数据的资源管理，ML Command Encoder 让整网推理和渲染/计算命令在同一时间线上同步执行，而 Shader ML 允许你在 fragment shader 内部直接跑神经网络。这套组合拳瞄准的是实时渲染中 ML 最密集的三个场景：超分、材质压缩和光照计算。
- [WWDC25-268] UIKit 新特性：UIKit 终于在 layoutSubviews() 里原生支持了 @Observable，这比 Liquid Glass 的视觉更新重要得多——它意味着你终于可以把项目里那些散落各处的 KVO（键值观察）和 NotificationCenter（通知中心）监听一次性干掉了。
- [WWDC25-287] What's new in RealityKit：RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。
