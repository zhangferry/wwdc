# Spatial Computing

## 领域判断

visionOS、空间界面、RealityKit、ARKit 与沉浸体验。本领域覆盖 118 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **RealityKit**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 RealityKit 的最新进展，让 App 和游戏的沉浸感和真实感更胜以往。探索一众强大的新功能，包括交互式布料模拟、NavMesh 寻路、混合现实光照，以及让空间音频更出彩的自定混响网格。借助改进的阴影效果、角色渲染增强功能以及对高斯泼溅技术的支持，提升视觉保真度。；visionOS 26 把空间计算的开发门槛砍掉了一半——你不再需要学 RealityKit 就能做出像样的 3D 应用，但这也意味着 RealityKit 的定位正在被重新定义。；visionOS 26 的沉浸式视频播放现在覆盖了 180/360/Wide FOV + Spatial Video + Apple Immersive Video 全格式。Quick Look 零代码支持，AVKit 有新 API 做精确体验控制，RealityKit 给了你完全自定义的能力。选哪个框架取决于你要多少控制权。 来源：[WWDC26-279]、[WWDC25-220]、[WWDC25-296]、[WWDC24-10086]
- **Spatial Computing**：visionOS 2 的 Safari 不只是"在头显里看网页"，它给了网页真正的空间交互能力——眼动追踪的高亮区域可以用 SVG 精细控制、WebSpeech API 做免手操控的全语音交互、Spatial Photo 和 3D 模型直接嵌入网页——而且所有处理都在设备本地完成，不需要后端 API。；visionOS 2 把 HealthKit 带上了 Apple Vision Pro，你的 iPad 应用可以零改动运行，但真正有意思的是用空间计算做沉浸式健康数据体验——比如在一个隔离了所有干扰的 Immersive Space 里记录情绪状态。；这场 Session 给出了一套从设计到落地的完整工作流：用 DCC 工具建模、烘焙贴图降低运行时开销、导入 Reality Composer Pro 调材质，核心原则是"能用烘焙解决的就不要留给实时渲染"。 来源：[WWDC24-10065]、[WWDC24-10083]、[WWDC24-10087]、[WWDC24-10091]
- **visionOS**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解模型元素如何将交互式 3D 内容搬上你的网站，这项功能现已登陆 iOS、iPadOS、macOS 和 visionOS。探索用于创建和优化 3D 素材资源的工具。了解模型元素功能，看看各个网页标准如何构筑 3D 网页内容的未来。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何为你的 App、网站和同播共享体验创建栩栩如生的 visionOS 环境。探索相关设计原则，看看如何为环境带来真正的沉浸感；并了解如何创建或采集参考材料、准备高保真 CG 素材，以及制作实时效果 (例如动态和光效)。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解新的 Spatial Preview 框架如何将 Mac 上的内容直接带到 visionOS。探索如何通过跨两个平台进行实时同步和双向编辑来构建动态工作流程。了解 SpatialPreview API、设备发现、2D 和 3D 会话集成，以及新的快速查看功能，为你的 Mac App 提升空间体验。 来源：[WWDC26-215]、[WWDC26-234]、[WWDC26-282]、[WWDC26-283]
- **空间计算**：visionOS 26 的企业 API 迎来实质性的开放 UVC 视频和 Neural Engine 不再需要企业许可证，新增 Window Follow Mode、内容保护和 Camera Region API，加上自定义共享坐标空间，这是 visionOS 企业级应用的转折点。；HTML 有了一个新元素 <model ——它不是又一个 3D viewer 库，而是浏览器原生的立体渲染管道，3D 模型直接穿出页面表面以真实深度呈现，配合拖拽和 Quick Look 用户可以把模型从网页里"拿"出来放到自己空间里。；visionOS 上的 Widget 终于不再是 iPad 的"兼容模式移植"了——它有了自己的设计语言：持久锚定、物理尺寸、环境感知，这三个特性让 Widget 从"信息卡片"变成了"房间里的实物"。 来源：[WWDC25-223]、[WWDC25-237]、[WWDC25-255]、[WWDC25-273]
- **WindowGroup**：RealityKit 是空间计算的 3D 核心框架，通过 Model3D（简单）和 RealityView（完整控制）两种方式为你的 SwiftUI App 添加三维内容。；空间计算游戏不只是 VR——从桌面上的虚拟棋盘到完全沉浸的太空大战，四种沉浸等级覆盖所有游戏类型。；SwiftUI 是空间计算平台的首选 UI 框架，系统本身从控制中心到 Safari 都用它构建。三种场景类型（窗口、体积、全空间）构成了 App 的完整形态。 来源：[WWDC23-10080]、[WWDC23-10096]、[WWDC23-10109]、[WWDC23-10110]
- **Task**：visionOS 游戏输入的最佳策略是优先使用系统手势（间接输入为主），只在必要时才用 ARKit 自定义手势或外设——能让人拿起就玩的手势设计才是 spatial computing 游戏的王道。；visionOS 2 的 Quick Look 拿到了全新的 PreviewApplication API，几行代码就能在你的 app 里嵌入窗口化的空间媒体预览，加上 3D 模型的 Surface Mapping 和 Configurations 支持，这是做 visionOS 内容消费类应用必看的一场。；空间计算平台的 SharePlay 引入了"共享上下文"和"视觉一致性"两个核心概念——所有参与者看到相同的窗口位置和内容，手指指向的东西其他人也能看到。这不是简单的屏幕共享，是真正的"同处一室"体验。 来源：[WWDC24-10094]、[WWDC24-10105]、[WWDC23-10087]、[WWDC23-10100]
- **图形与游戏**：RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。；visionOS 终于支持实体手柄了。PS VR2 Sense 控制器和 Logitech Muse 是首批支持的空间配件，提供六自由度追踪和触觉反馈。GameController + RealityKit/ARKit 三件套打通，雕刻类和游戏类 app 的交互终于有了物理抓手。；Metal immersive 渲染今年加了四样东西：hover effects 让交互对象有视觉反馈、动态渲染质量按场景复杂度调分辨率、progressive immersion 用 stencil 裁剪门户外的像素、Mac 可以直接渲染 immersive content 流式投射到 Vision Pro。最后一个是最大的玩法变化。 来源：[WWDC25-287]、[WWDC25-289]、[WWDC25-294]、[WWDC25-305]

## API 演进时间线

- **WWDC26**：15 场，代表来源：[WWDC26-204]、[WWDC26-215]、[WWDC26-234]、[WWDC26-279]、[WWDC26-280]
- **WWDC25**：18 场，代表来源：[WWDC25-101]、[WWDC25-201]、[WWDC25-220]、[WWDC25-223]、[WWDC25-237]
- **WWDC24**：25 场，代表来源：[WWDC24-10065]、[WWDC24-10066]、[WWDC24-10083]、[WWDC24-10086]、[WWDC24-10087]
- **WWDC23**：41 场，代表来源：[WWDC23-10012]、[WWDC23-10034]、[WWDC23-10045]、[WWDC23-10048]、[WWDC23-10070]
- **WWDC22**：5 场，代表来源：[WWDC22-10024]、[WWDC22-10025]、[WWDC22-10126]、[WWDC22-10127]、[WWDC22-10131]
- **WWDC21**：9 场，代表来源：[WWDC21-10073]、[WWDC21-10074]、[WWDC21-10075]、[WWDC21-10076]、[WWDC21-10077]
- **WWDC20**：5 场，代表来源：[WWDC20-10601]、[WWDC20-10604]、[WWDC20-10611]、[WWDC20-10612]、[WWDC20-10613]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 立即 recompile 你的 app 看 Liquid Glass 效果 。标准控件自动更新，不需要改代码。然后逐步审计自定义组件，优先替换为框架原生视图。
- Foundation Models 适合做内容生成、摘要、分类等"日常智能"任务 。不适合需要最新知识或超长上下文的场景。用 tool calling 补齐信息缺口。
- Xcode coding assistant 的对话历史功能是安全网 。大胆探索不同实现方案，随时回滚到任意历史节点。
- Swift 6.2 迁移建议 ：先在模块级别开启 MainActor by default，确认没有误杀并发代码后再逐步清理 warning。
- App 图标现在要过四关 ：全彩、tint、clear、macOS 圆角矩形。用 Icon Composer 从一开始就设计多层结构。
- 企业许可证管理现在更简单了 。License 文件在 Apple Developer 账户中直接管理，续期自动推送。用 VisionEntitlementServices 在运行时检查权限状态，不要硬编码许可逻辑。
- Camera Region 的资源消耗与区域大小成正比 。Apple 建议 CameraRegionAnchor 占整体可见区域的六分之一或更小。在设计时做好性能评估。

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

`空间计算` (15)、`visionOS` (11)、`SwiftUI` (6)、`Design` (6)、`图形与游戏` (4)、`visionOS & Spatial Computing` (3)、`Audio & Video` (3)、`RealityKit` (2)、`基础` (2)、`WebKit` (1)、`Safari` (1)、`Xcode` (1)、`Metal` (1)、`GPU` (1)、`MetalFX` (1)、`着色器` (1)、`应用服务` (1)、`商业与教育` (1)

## 关键 Session

- [WWDC26-204] 面向 Safari 浏览器 27 的 WebKit 新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 WebKit 的新功能：从 Grid Lanes 和可自定选择，到 HTML 模型和沉浸式环境，再到最新的网页扩展，种种创新为你再添助力。你还将走进上千项浏览器引擎改进的幕后，了解这些让网页更可靠的改进是如何实现的。
- [WWDC26-215] HTML 模型元素入门：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解模型元素如何将交互式 3D 内容搬上你的网站，这项功能现已登陆 iOS、iPadOS、macOS 和 visionOS。探索用于创建和优化 3D 素材资源的工具。了解模型元素功能，看看各个网页标准如何构筑 3D 网页内容的未来。
- [WWDC26-234] 为 visionOS App 和空间网络设计沉浸式环境：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何为你的 App、网站和同播共享体验创建栩栩如生的 visionOS 环境。探索相关设计原则，看看如何为环境带来真正的沉浸感；并了解如何创建或采集参考材料、准备高保真 CG 素材，以及制作实时效果 (例如动态和光效)。
- [WWDC26-279] 探索 RealityKit 的新进展：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 RealityKit 的最新进展，让 App 和游戏的沉浸感和真实感更胜以往。探索一众强大的新功能，包括交互式布料模拟、NavMesh 寻路、混合现实光照，以及让空间音频更出彩的自定混响网格。借助改进的阴影效果、角色渲染增强功能以及对高斯泼溅技术的支持，提升视觉保真度。
- [WWDC26-280] 使用 Reality Composer Pro 3 加速空间场景迭代：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 Reality Composer Pro 3 中强大的新功能，构建出色的空间体验。了解如何为沉浸式场景添加内容、视觉效果、光照和交互，而且全程无需离开编辑器。探索如何在编辑器中使用 AI 辅助功能进行快速迭代。
- [WWDC26-281] 使用 Xcode 扩展 Reality Composer Pro 3 的功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Reality Composer Pro 3 如何助你构建规模更大、更具雄心的空间项目。了解如何创建项目专属插件，以便编辑自定组件、运行自定系统，并构建自己的 ScriptGraph 节点，从而全面掌控你的空间创作工作流程。
- [WWDC26-282] 探索 Spatial Preview 框架：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解新的 Spatial Preview 框架如何将 Mac 上的内容直接带到 visionOS。探索如何通过跨两个平台进行实时同步和双向编辑来构建动态工作流程。了解 SpatialPreview API、设备发现、2D 和 3D 会话集成，以及新的快速查看功能，为你的 Mac App 提升空间体验。
- [WWDC26-283] 探索 visionOS 对象追踪的增强功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 visionOS 如何提升对象追踪和空间配件输入能力。探索追踪动态手持对象的新方法，巧妙地连接物理世界和数字世界。了解新增的空间配件支持类别，以及构建专属自定配件需要什么，以便在你的 App 中实现独一无二的交互模式。
- [WWDC26-284] 在 visionOS 中协作处理结构化 3D 模型：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何在 visionOS 中生动呈现结构化 3D 模型。我们将介绍 USDZ 的准备工作，演示如何在分层装配中操作单个实体，并利用剖切面检查模型的内部组件。创建令人惊叹的分解视图动画，打造基于 Apple Vision Pro 的设计审查和协作体验。
- [WWDC26-286] 使用 Foveated Streaming 将沉浸式内容融入 visionOS：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 Foveated Streaming 如何以高保真质量将远程渲染的场景传输到 Apple Vision Pro。探索这个框架如何通过完全无线的方式，将 visionOS 原生功能与第三方流媒体技术相结合，并通过 OpenXR 场景和 NVIDIA CloudXR 进行演示。了解 Foveated Streaming 框架、与 NVIDIA CloudXR SDK 的集成，以及动态注视点流式传输技术如何在保护隐私的同时带来种种好处。
- [WWDC26-287] 利用 visionOS 27 打造新一代体验：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 visionOS 27 的新功能，打造新一代 App、游戏和空间体验。探索在 visionOS 上构建体验的多种途径，比如使用原生 Apple 工具和框架、从 Mac 或 PC 流式传输沉浸式内容、利用第三方引擎，或移植现有的 iOS App。了解如何利用 3D 内容创建、沉浸式媒体和对象追踪方面的最新进展，让你的空间计算项目更上一层楼。
- [WWDC26-320] 探索 visionOS 中的沉浸式网站环境：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 JavaScript 中新推出的 Immersive API，将你的网站访客带入 Apple Vision Pro 中的虚拟环境。探索如何从内联模型元素请求沉浸式过渡，利用视频对接等功能打造引人入胜的沉浸式体验，并优化性能以实现按真实比例复刻的丰富体验——只需在你的网站上运行几行代码即可。
- [WWDC26-338] 为 Apple 沉浸视频构建实时制作工具：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：深入了解 Apple 沉浸视频实时制作的幕后过程。探索如何打包沉浸视频、空间音频和场景元数据，以便使用 SMPTE 2110 标准通过 IP 网络传输内容。借助 Apple 推出的 Immersive Media Support、Video Toolbox 和 AVFoundation 框架，实现 Apple 沉浸视频的实时制作流程。为了充分从这个讲座中获益，建议你观看 WWDC25 视频“了解 Apple 沉浸视频技术”。
- [WWDC26-393] 使用 Reality Composer Pro 3 加速你的空间工作流程：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何完全在 Reality Composer Pro 内，利用其强大的图形化工具套件来构建丰富的交互功能和惊艳的视觉效果。了解如何使用 Shader Graph 制作动态材质、将骨骼动画与 Animation Graph 相融合，并使用 Compute Graph 模拟粒子效果。你还将深入探索如何通过 Script Graph 实现 App 交互、使用 Sequencer 协调场景事件，并利用 Behavior Trees 来设计智能的 NPC 行为——所有操作都无需离开编辑器。
- [WWDC26-8004] visionOS 小组实验室：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，与 Apple 工程师和设计师一起深入探索 WWDC26。在这个以 visionOS 为主题的活动中，你可以提出问题、获取建议，并实时关注围绕大会一周的相关重磅发布展开的精彩讨论。活动语言为英语。
- [WWDC25-101] Keynote：Liquid Glass 是 iOS 7 以来最大的设计变革，Foundation Models 框架让端侧 AI 真正落地到每个 app，Xcode 26 接入多模型 coding assistant 这一届 WWDC 把设计、AI 和工具链三条线同时拉满了。
- [WWDC25-201] Metal 新特性：Metal 终于开始帮你管那些你一直在手动管的东西了——渲染状态、Shader 编译、分辨率折中——这次更新的信号是：别自己造轮子了，用框架的。
- [WWDC25-220] visionOS 新特性：visionOS 26 把空间计算的开发门槛砍掉了一半——你不再需要学 RealityKit 就能做出像样的 3D 应用，但这也意味着 RealityKit 的定位正在被重新定义。
