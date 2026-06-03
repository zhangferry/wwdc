# Spatial Computing

## 领域判断

visionOS、空间界面、RealityKit、ARKit 与沉浸体验。本领域覆盖 103 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **RealityKit**：visionOS 26 把空间计算的开发门槛砍掉了一半——你不再需要学 RealityKit 就能做出像样的 3D 应用，但这也意味着 RealityKit 的定位正在被重新定义。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；visionOS 上最好的 App 不是把 iPad 版搬过来，而是找到了"只有空间计算才能做到"的那个瞬间——Session 通过 JigSpace、Loona、Lowe's 等实际案例给出了三条可复用的设计策略。 来源：[WWDC25-220]、[WWDC25-296]、[WWDC24-10086]、[WWDC24-10093]
- **Spatial Computing**：visionOS 2 的 Safari 不只是"在头显里看网页"，它给了网页真正的空间交互能力——眼动追踪的高亮区域可以用 SVG 精细控制、WebSpeech API 做免手操控的全语音交互、Spatial Photo 和 3D 模型直接嵌入网页——而且所有处理都在设备本地完成，不需要后端 API。；visionOS 2 把 HealthKit 带上了 Apple Vision Pro，你的 iPad 应用可以零改动运行，但真正有意思的是用空间计算做沉浸式健康数据体验——比如在一个隔离了所有干扰的 Immersive Space 里记录情绪状态。；这场 Session 给出了一套从设计到落地的完整工作流：用 DCC 工具建模、烘焙贴图降低运行时开销、导入 Reality Composer Pro 调材质，核心原则是"能用烘焙解决的就不要留给实时渲染"。 来源：[WWDC24-10065]、[WWDC24-10083]、[WWDC24-10087]、[WWDC24-10091]
- **空间计算**：visionOS 26 的企业 API 迎来实质性的开放 UVC 视频和 Neural Engine 不再需要企业许可证，新增 Window Follow Mode、内容保护和 Camera Region API，加上自定义共享坐标空间，这是 visionOS 企业级应用的转折点。；HTML 有了一个新元素 <model ——它不是又一个 3D viewer 库，而是浏览器原生的立体渲染管道，3D 模型直接穿出页面表面以真实深度呈现，配合拖拽和 Quick Look 用户可以把模型从网页里"拿"出来放到自己空间里。；visionOS 上的 Widget 终于不再是 iPad 的"兼容模式移植"了——它有了自己的设计语言：持久锚定、物理尺寸、环境感知，这三个特性让 Widget 从"信息卡片"变成了"房间里的实物"。 来源：[WWDC25-223]、[WWDC25-237]、[WWDC25-255]、[WWDC25-273]
- **WindowGroup**：RealityKit 是空间计算的 3D 核心框架，通过 Model3D（简单）和 RealityView（完整控制）两种方式为你的 SwiftUI App 添加三维内容。；空间计算游戏不只是 VR——从桌面上的虚拟棋盘到完全沉浸的太空大战，四种沉浸等级覆盖所有游戏类型。；SwiftUI 是空间计算平台的首选 UI 框架，系统本身从控制中心到 Safari 都用它构建。三种场景类型（窗口、体积、全空间）构成了 App 的完整形态。 来源：[WWDC23-10080]、[WWDC23-10096]、[WWDC23-10109]、[WWDC23-10110]
- **Task**：visionOS 游戏输入的最佳策略是优先使用系统手势（间接输入为主），只在必要时才用 ARKit 自定义手势或外设——能让人拿起就玩的手势设计才是 spatial computing 游戏的王道。；visionOS 2 的 Quick Look 拿到了全新的 PreviewApplication API，几行代码就能在你的 app 里嵌入窗口化的空间媒体预览，加上 3D 模型的 Surface Mapping 和 Configurations 支持，这是做 visionOS 内容消费类应用必看的一场。；空间计算平台的 SharePlay 引入了"共享上下文"和"视觉一致性"两个核心概念——所有参与者看到相同的窗口位置和内容，手指指向的东西其他人也能看到。这不是简单的屏幕共享，是真正的"同处一室"体验。 来源：[WWDC24-10094]、[WWDC24-10105]、[WWDC23-10087]、[WWDC23-10100]
- **图形与游戏**：RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。；visionOS 终于支持实体手柄了。PS VR2 Sense 控制器和 Logitech Muse 是首批支持的空间配件，提供六自由度追踪和触觉反馈。GameController + RealityKit/ARKit 三件套打通，雕刻类和游戏类 app 的交互终于有了物理抓手。；Metal immersive 渲染今年加了四样东西：hover effects 让交互对象有视觉反馈、动态渲染质量按场景复杂度调分辨率、progressive immersion 用 stencil 裁剪门户外的像素、Mac 可以直接渲染 immersive content 流式投射到 Vision Pro。最后一个是最大的玩法变化。 来源：[WWDC25-287]、[WWDC25-289]、[WWDC25-294]、[WWDC25-305]
- **Audio & Video**：visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。；visionOS 26 的 SharePlay 终于支持同一房间的多人协作——窗口栏上一个分享按钮，就能让所有人看到同一个 app 在同一个位置，而且已有 SharePlay 代码零改动就能用。；如果你要做 Apple Vision Pro 上的沉浸式视频内容，这个 session 是技术入口——从 AIVU 文件格式、ImmersiveMediaSupport 框架到 ASAF 空间音频，把制作到发布的全链路讲清楚了。 来源：[WWDC25-296]、[WWDC25-318]、[WWDC25-403]

## API 演进时间线

- **WWDC25**：18 场，代表来源：[WWDC25-101]、[WWDC25-201]、[WWDC25-220]、[WWDC25-223]、[WWDC25-237]
- **WWDC24**：25 场，代表来源：[WWDC24-10065]、[WWDC24-10066]、[WWDC24-10083]、[WWDC24-10086]、[WWDC24-10087]
- **WWDC23**：41 场，代表来源：[WWDC23-10012]、[WWDC23-10034]、[WWDC23-10045]、[WWDC23-10048]、[WWDC23-10070]
- **WWDC22**：5 场，代表来源：[WWDC22-10024]、[WWDC22-10025]、[WWDC22-10126]、[WWDC22-10127]、[WWDC22-10131]
- **WWDC21**：9 场，代表来源：[WWDC21-10073]、[WWDC21-10074]、[WWDC21-10075]、[WWDC21-10076]、[WWDC21-10077]
- **WWDC20**：5 场，代表来源：[WWDC20-10601]、[WWDC20-10604]、[WWDC20-10611]、[WWDC20-10612]、[WWDC20-10613]

## 决策启发式

- 立即 recompile 你的 app 看 Liquid Glass 效果 。标准控件自动更新，不需要改代码。然后逐步审计自定义组件，优先替换为框架原生视图。
- Foundation Models 适合做内容生成、摘要、分类等"日常智能"任务 。不适合需要最新知识或超长上下文的场景。用 tool calling 补齐信息缺口。
- Xcode coding assistant 的对话历史功能是安全网 。大胆探索不同实现方案，随时回滚到任意历史节点。
- Swift 6.2 迁移建议 ：先在模块级别开启 MainActor by default，确认没有误杀并发代码后再逐步清理 warning。
- App 图标现在要过四关 ：全彩、tint、clear、macOS 圆角矩形。用 Icon Composer 从一开始就设计多层结构。
- 企业许可证管理现在更简单了 。License 文件在 Apple Developer 账户中直接管理，续期自动推送。用 VisionEntitlementServices 在运行时检查权限状态，不要硬编码许可逻辑。
- Camera Region 的资源消耗与区域大小成正比 。Apple 建议 CameraRegionAnchor 占整体可见区域的六分之一或更小。在设计时做好性能评估。
- Window Follow Mode 是全局行为 。一旦 entitlement 生效，设备上所有 app 的窗口都可以使用 follow 模式，不只是你的 app。
- 共享坐标空间的网络传输完全由你控制 。你可以选择任何本地网络传输方式（TCP/UDP/自定义协议），ARKit 只负责坐标对齐。
- 以房间为单位思考 Widget 设计 。Widget 不会悬浮在虚拟环境中，它只贴附在物理表面上。设计时要考虑它会出现在厨房、客厅还是办公室，这直接影响尺寸和内容密度的选择。

## 反模式与坑

- RecRoom 是用 Unity + CompositorServices + ARKit 的实际案例
- App Intents + Visual Intelligence ：你的 app 可以注册 Visual Search schema，让用户通过相机识别直接跳转到你的 app。
- Background Tasks API 更新 ：支持后台长时间任务（如视频导出），CarPlay 支持 Live Activities。
- Terminal 更新 ：24 bit 色彩、Liquid Glass 主题、Powerline 字体支持。
- PermissionKit 框架 ：为儿童通信提供家长监督机制。
- Declared Age Range API ：在不侵犯隐私的前提下适龄调整 app 体验。
- Liquid Glass 不只是视觉改版
- Foundation Models 的 @Generable 是杀手级 API

## 高频主题

`空间计算` (15)、`SwiftUI` (6)、`Design` (6)、`图形与游戏` (4)、`Audio & Video` (3)、`基础` (2)、`visionOS` (2)、`Metal` (1)、`GPU` (1)、`MetalFX` (1)、`着色器` (1)、`RealityKit` (1)、`应用服务` (1)、`商业与教育` (1)、`Safari与Web` (1)、`开发工具` (1)

## 关键 Session

- [WWDC25-101] Keynote：Liquid Glass 是 iOS 7 以来最大的设计变革，Foundation Models 框架让端侧 AI 真正落地到每个 app，Xcode 26 接入多模型 coding assistant 这一届 WWDC 把设计、AI 和工具链三条线同时拉满了。
- [WWDC25-201] Metal 新特性：Metal 终于开始帮你管那些你一直在手动管的东西了——渲染状态、Shader 编译、分辨率折中——这次更新的信号是：别自己造轮子了，用框架的。
- [WWDC25-220] visionOS 新特性：visionOS 26 把空间计算的开发门槛砍掉了一半——你不再需要学 RealityKit 就能做出像样的 3D 应用，但这也意味着 RealityKit 的定位正在被重新定义。
- [WWDC25-223] Explore enhancements to your spatial business app：visionOS 26 的企业 API 迎来实质性的开放 UVC 视频和 Neural Engine 不再需要企业许可证，新增 Window Follow Mode、内容保护和 Camera Region API，加上自定义共享坐标空间，这是 visionOS 企业级应用的转折点。
- [WWDC25-237] 空间 Web 新特性：HTML 有了一个新元素 <model ——它不是又一个 3D viewer 库，而是浏览器原生的立体渲染管道，3D 模型直接穿出页面表面以真实深度呈现，配合拖拽和 Quick Look 用户可以把模型从网页里"拿"出来放到自己空间里。
- [WWDC25-255] 为 visionOS 设计 Widget：从屏幕到空间：visionOS 上的 Widget 终于不再是 iPad 的"兼容模式移植"了——它有了自己的设计语言：持久锚定、物理尺寸、环境感知，这三个特性让 Widget 从"信息卡片"变成了"房间里的实物"。
- [WWDC25-256] SwiftUI 年度更新：Liquid Glass、性能飞跃与三维布局：SwiftUI 今年的更新覆盖了从视觉到性能到生态的全链路——Liquid Glass 设计语言让你重新编译就焕然一新，列表性能提升 16 倍，WebView 和富文本终于官方支持，visionOS 三维布局正式成型。
- [WWDC25-273] SwiftUI 空间布局入门：用 2D 思维构建 3D 体验：如果你熟悉 SwiftUI 的 2D 布局（VStack/HStack/alignment），现在可以直接用同样的心智模型构建 visionOS 的 3D 体验——每个视图多了 depth 和 Z position，alignment 多了深度维度，新增的 rotation3DLayout 和 SpatialContainer 解决了 2D modifier 在 3D 空间中的失效问题。
- [WWDC25-274] SwiftUI 与 RealityKit 的合体之路：SwiftUI 和 RealityKit 终于从"各干各的"变成了"双向奔赴"——Entity 现在可以当数据模型用，SwiftUI 动画可以直接驱动 RealityKit 组件变化。但双向数据流是把双刃剑，用不好就会陷入无限循环。
- [WWDC25-287] What's new in RealityKit：RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。
- [WWDC25-289] Explore spatial accessory input on visionOS：visionOS 终于支持实体手柄了。PS VR2 Sense 控制器和 Logitech Muse 是首批支持的空间配件，提供六自由度追踪和触觉反馈。GameController + RealityKit/ARKit 三件套打通，雕刻类和游戏类 app 的交互终于有了物理抓手。
- [WWDC25-290] Set the scene with SwiftUI in visionOS：visionOS 26 的 SwiftUI scene 系统做了一轮全面升级：窗口可以锁房间、Volume 可以吸墙面和桌面、immersive space 支持 Mac 远程渲染、UIKit 也能桥接 Volume 了。如果你在做 visionOS app，这篇是必读。
- [WWDC25-294] What's new in Metal rendering for immersive apps：Metal immersive 渲染今年加了四样东西：hover effects 让交互对象有视觉反馈、动态渲染质量按场景复杂度调分辨率、progressive immersion 用 stencil 裁剪门户外的像素、Mac 可以直接渲染 immersive content 流式投射到 Vision Pro。最后一个是最大的玩法变化。
- [WWDC25-296] Support immersive video playback in visionOS apps：visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。
- [WWDC25-303] 设计 visionOS 悬停交互：visionOS 的 hover 效果不是简单的 hover 态 CSS——它是隐私保护下的状态机动画、眼动驱动的滚动、以及媒体控件的持久化显示，这三个机制合在一起才是完整的交互模型。
- [WWDC25-305] 优化 visionOS 自定义环境：1 亿面的渲染级场景压到 20 万面以内跑在 Vision Pro 上——这不是魔法，是一套用 Houdini 做的程序化优化流水线，核心武器是 Immersive Boundary 视角裁剪 + 烘焙光照。
- [WWDC25-318] 与附近的人共享 visionOS 体验：visionOS 26 的 SharePlay 终于支持同一房间的多人协作——窗口栏上一个分享按钮，就能让所有人看到同一个 app 在同一个位置，而且已有 SharePlay 代码零改动就能用。
- [WWDC25-403] 了解 Apple 沉浸式视频技术：如果你要做 Apple Vision Pro 上的沉浸式视频内容，这个 session 是技术入口——从 AIVU 文件格式、ImmersiveMediaSupport 框架到 ASAF 空间音频，把制作到发布的全链路讲清楚了。
