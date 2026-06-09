# Spatial Computing

## 领域判断

visionOS、空间界面、RealityKit、ARKit 与沉浸体验。本领域覆盖 119 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **RealityKit**：visionOS 的沉浸式环境根本不是 360 度全景照片，而是把 14K 全景图贴在带真实深度的 3D 网格上实时渲染的 CG 场景。；这场 Session 最值得关注的一件事是：Reality Composer Pro 3 的 ScriptGraph 配合即将推出的 Vision Pro 实机 Live Preview，彻底把 visionOS 空间交互的“调参权”从程序员手里抢走，交给了设计师。；✅ RealityKit 正式跨过"3D 模型查看器"门槛，原生导航网格 (Navigation Mesh) 和物理空间光照 (Physical Space Lighting) 让它具备了开发重度 visionOS 空间游戏的底层基建能力。 来源：[WWDC26-234]、[WWDC26-252]、[WWDC26-279]、[WWDC26-281]
- **Spatial Computing**：✅ Web 端 3D 展示终于从“引入几十 KB 的 JS 库”变成了“写一个 <model 标签”。；visionOS 2 的 Safari 不只是"在头显里看网页"，它给了网页真正的空间交互能力——眼动追踪的高亮区域可以用 SVG 精细控制、WebSpeech API 做免手操控的全语音交互、Spatial Photo 和 3D 模型直接嵌入网页——而且所有处理都在设备本地完成，不需要后端 API。；visionOS 2 把 HealthKit 带上了 Apple Vision Pro，你的 iPad 应用可以零改动运行，但真正有意思的是用空间计算做沉浸式健康数据体验——比如在一个隔离了所有干扰的 Immersive Space 里记录情绪状态。 来源：[WWDC26-215]、[WWDC24-10065]、[WWDC24-10083]、[WWDC24-10087]
- **visionOS**：Safari 终于原生支持 <select 深度定制和 <model 3D 渲染，Web 开发者不用再捏着鼻子写一堆 div 模拟表单和引入沉重的 Three.js 了。；✅ Web 端 3D 展示终于从“引入几十 KB 的 JS 库”变成了“写一个 <model 标签”。；visionOS 的沉浸式环境根本不是 360 度全景照片，而是把 14K 全景图贴在带真实深度的 3D 网格上实时渲染的 CG 场景。 来源：[WWDC26-204]、[WWDC26-215]、[WWDC26-234]、[WWDC26-252]
- **空间计算**：visionOS 26 的企业 API 迎来实质性的开放 UVC 视频和 Neural Engine 不再需要企业许可证，新增 Window Follow Mode、内容保护和 Camera Region API，加上自定义共享坐标空间，这是 visionOS 企业级应用的转折点。；HTML 有了一个新元素 <model ——它不是又一个 3D viewer 库，而是浏览器原生的立体渲染管道，3D 模型直接穿出页面表面以真实深度呈现，配合拖拽和 Quick Look 用户可以把模型从网页里"拿"出来放到自己空间里。；visionOS 上的 Widget 终于不再是 iPad 的"兼容模式移植"了——它有了自己的设计语言：持久锚定、物理尺寸、环境感知，这三个特性让 Widget 从"信息卡片"变成了"房间里的实物"。 来源：[WWDC25-223]、[WWDC25-237]、[WWDC25-255]、[WWDC25-273]
- **WindowGroup**：RealityKit 是空间计算的 3D 核心框架，通过 Model3D（简单）和 RealityView（完整控制）两种方式为你的 SwiftUI App 添加三维内容。；空间计算游戏不只是 VR——从桌面上的虚拟棋盘到完全沉浸的太空大战，四种沉浸等级覆盖所有游戏类型。；SwiftUI 是空间计算平台的首选 UI 框架，系统本身从控制中心到 Safari 都用它构建。三种场景类型（窗口、体积、全空间）构成了 App 的完整形态。 来源：[WWDC23-10080]、[WWDC23-10096]、[WWDC23-10109]、[WWDC23-10110]
- **Task**：visionOS 游戏输入的最佳策略是优先使用系统手势（间接输入为主），只在必要时才用 ARKit 自定义手势或外设——能让人拿起就玩的手势设计才是 spatial computing 游戏的王道。；visionOS 2 的 Quick Look 拿到了全新的 PreviewApplication API，几行代码就能在你的 app 里嵌入窗口化的空间媒体预览，加上 3D 模型的 Surface Mapping 和 Configurations 支持，这是做 visionOS 内容消费类应用必看的一场。；空间计算平台的 SharePlay 引入了"共享上下文"和"视觉一致性"两个核心概念——所有参与者看到相同的窗口位置和内容，手指指向的东西其他人也能看到。这不是简单的屏幕共享，是真正的"同处一室"体验。 来源：[WWDC24-10094]、[WWDC24-10105]、[WWDC23-10087]、[WWDC23-10100]
- **图形与游戏**：RealityKit 今年迎来了一次能力大爆发：原生 ARKit 数据直通、手势操控组件、环境遮挡、GPU instancing、沉浸式媒体全格式支持，外加 tvOS 新平台。如果你还在用 SceneKit，这是最后的迁移信号。；visionOS 终于支持实体手柄了。PS VR2 Sense 控制器和 Logitech Muse 是首批支持的空间配件，提供六自由度追踪和触觉反馈。GameController + RealityKit/ARKit 三件套打通，雕刻类和游戏类 app 的交互终于有了物理抓手。；Metal immersive 渲染今年加了四样东西：hover effects 让交互对象有视觉反馈、动态渲染质量按场景复杂度调分辨率、progressive immersion 用 stencil 裁剪门户外的像素、Mac 可以直接渲染 immersive content 流式投射到 Vision Pro。最后一个是最大的玩法变化。 来源：[WWDC25-287]、[WWDC25-289]、[WWDC25-294]、[WWDC25-305]

## API 演进时间线

- **WWDC26**：16 场，代表来源：[WWDC26-204]、[WWDC26-215]、[WWDC26-234]、[WWDC26-252]、[WWDC26-279]
- **WWDC25**：18 场，代表来源：[WWDC25-101]、[WWDC25-201]、[WWDC25-220]、[WWDC25-223]、[WWDC25-237]
- **WWDC24**：25 场，代表来源：[WWDC24-10065]、[WWDC24-10066]、[WWDC24-10083]、[WWDC24-10086]、[WWDC24-10087]
- **WWDC23**：41 场，代表来源：[WWDC23-10012]、[WWDC23-10034]、[WWDC23-10045]、[WWDC23-10048]、[WWDC23-10070]
- **WWDC22**：5 场，代表来源：[WWDC22-10024]、[WWDC22-10025]、[WWDC22-10126]、[WWDC22-10127]、[WWDC22-10131]
- **WWDC21**：9 场，代表来源：[WWDC21-10073]、[WWDC21-10074]、[WWDC21-10075]、[WWDC21-10076]、[WWDC21-10077]
- **WWDC20**：5 场，代表来源：[WWDC20-10601]、[WWDC20-10604]、[WWDC20-10611]、[WWDC20-10612]、[WWDC20-10613]

## 决策启发式

- 已有项目的迁移策略 ：如果你之前的 App 用的是 PanoramicImage 或者简单的天空盒 (Skybox) 做背景，现在必须废弃。把现有的全景图导入 Blender 或 Maya，使用投影映射 (Projection Mapping) 技术，将其贴到一个基础的地形网格上，导出为 USDZ 格式再引入 Reality Composer Pro。
- 新项目的采用建议 ：不要一开始就想着去实地拍摄。除非你有专业的摄影测量 (Photogrammetry) 团队，否则强烈建议直接使用 Unreal Engine 或 Blender 进行全 CG 渲染。在 CG 软件里直接输出 14400x7200 的全景图和对应的深度图 (Depth Map)，这比去野外拍完再后期修补穿帮镜头要省钱、可控得多。
- 实战中容易踩的坑 ：在后期清理全景图时，千万不要把地平线附近的远景抹掉。visionOS 的 81 度主视野意味着用户稍微一低头或转头，就会看到全景图的边缘。如果边缘是黑边或者模糊的修补痕迹，沉浸感会瞬间崩塌。务必使用副机位素材或 CG 延伸来补全所有盲区。
- 新项目采用建议 ：把 ScriptGraph 当作“胶水”和“原型工具”。用它来处理手势反馈、简单的物理碰撞、动画状态机和 UI 触发时机。一旦涉及网络请求、复杂数据解析或 ECS 系统级查询，立刻切回 Swift 代码。
- 已有项目迁移 ：不需要把现有的 RealityKit 逻辑推翻重写。你可以把 ScriptGraph 生成的逻辑封装成独立的 Scripting Component，与现有的自定义 Component 和 System 共存。
- 实战避坑 ：在 ScriptGraph 里大量使用 Prototyped Subgraph（原型子图）来封装常用逻辑（比如“检测变量是否改变”）。如果不做封装，你的节点图在两周内就会变成无法维护的蜘蛛网。
- 热状态管理是必修课 ：visionOS 散热受限，Session 里专门提了监听 ProcessInfo.thermalState。当状态变成 .serious 或 .critical 时，必须动态降低阴影质量或强制切换更激进的 LOD。别等系统把你的 App 降频卡顿了才想起来做优化。
- NavMesh 的异步陷阱 ：NavigationController.computePath 是 async 的，这意味着你拿到路径时，NPC 的位置可能已经变了。在写移动逻辑时，一定要把路径的第一个点设为 NPC 当前位置到路径起点的平滑过渡，否则 NPC 会瞬移。
- 新项目直接上 Reality Composer Pro 3 ：今年光照烘焙 (Lightmap)、NavMesh 绘制都在 RCP3 里可视化了。别在代码里硬算间接光照和手写 NavMesh 顶点，用官方工具链能省去 80% 的调试时间。
- 已有项目迁移 ：如果你之前的 App 追踪手持物体老是丢，赶紧用 Create ML 的 extended 模式重新训练 .referenceobject，并在代码里开启 highFrameRateTrackingEnabled。这能解决大部分动态遮挡丢追踪的问题。

## 反模式与坑

- RecRoom 是用 Unity + CompositorServices + ARKit 的实际案例
- CSS random() 函数 ：可以在 CSS 中直接生成随机数，配合命名作用域可以避免每次重绘都重新计算，做随机粒子背景非常方便。
- Emoji 17 bit 截断 Hack ：WebKit 在引擎层拦截了超过 16 bit 的 emoji 输入，以替代文本形式发给网页，强行修复了老旧网站用 .fromCharCode 导致的乱码问题。
- SVG 2 标准化推进 ：Apple 工程师直接参与了 SVG 工作组的规范制定，明确了径向渐变 fx/fy 的默认值，顺手在 Safari 27 里修了 75 个 SVG 渲染 bug。
- AI 生成 3D 资产被官方盖章 ：Apple 在 Session 里点名了 Tripo3D 和 Meshy.ai，说明 AI 文本/图片生成 USDZ 已经成为官方认可的资产生产工作流，不用再死磕传统建模了。
- AR Quick Look 的无缝衔接 ：只需用 <a rel="ar" 标签把 <model 包裹起来指向同一个 USDZ 文件，iOS 端就能直接唤起原生的 AR 放置体验，无需额外写 JS 桥接。
- W3C 标准化窗口期 ：Apple 正在把这个元素推向 W3C 沉浸式 Web 社区组（Immersive Web Community Group），现在去提 Issue 和反馈，最容易影响最终跨平台 API 的设计走向。
- 动态与能效的平衡 ：Apple 强调环境中的动态元素（如水流、树叶摇晃）必须使用自定义 Shader (Custom Shader) 来实现，而不是靠骨骼动画或粒子系统，这是为了在维持 90fps 的同时严格控制头显的发热和功耗。

## 高频主题

`visionOS` (16)、`空间计算` (15)、`RealityKit` (10)、`SwiftUI` (7)、`Design` (6)、`图形与游戏` (4)、`USDZ` (3)、`Reality Composer Pro` (3)、`Audio & Video` (3)、`Spatial Audio` (2)、`RealityComposerPro` (2)、`Compute Graph` (2)、`Spatial Preview` (2)、`USDKit` (2)、`基础` (2)、`WebKit` (1)、`CSS` (1)、`HTML Model` (1)

## 关键 Session

- [WWDC26-204] 面向 Safari 浏览器 27 的 WebKit 新功能：Safari 终于原生支持 <select 深度定制和 <model 3D 渲染，Web 开发者不用再捏着鼻子写一堆 div 模拟表单和引入沉重的 Three.js 了。
- [WWDC26-215] HTML 模型元素入门：✅ Web 端 3D 展示终于从“引入几十 KB 的 JS 库”变成了“写一个 <model 标签”。
- [WWDC26-234] 为 visionOS App 和空间网络设计沉浸式环境：visionOS 的沉浸式环境根本不是 360 度全景照片，而是把 14K 全景图贴在带真实深度的 3D 网格上实时渲染的 CG 场景。
- [WWDC26-252] 使用 Reality Composer Pro 3 设计无代码游戏：这场 Session 最值得关注的一件事是：Reality Composer Pro 3 的 ScriptGraph 配合即将推出的 Vision Pro 实机 Live Preview，彻底把 visionOS 空间交互的“调参权”从程序员手里抢走，交给了设计师。
- [WWDC26-279] 探索 RealityKit 的新进展：✅ RealityKit 正式跨过"3D 模型查看器"门槛，原生导航网格 (Navigation Mesh) 和物理空间光照 (Physical Space Lighting) 让它具备了开发重度 visionOS 空间游戏的底层基建能力。
- [WWDC26-280] 使用 Reality Composer Pro 3 加速空间场景迭代：Reality Composer Pro 终于脱离 Xcode 变成独立应用，并补齐了 Prefab（原型）和真机实时预览，Apple 算是正式把它当正经 3D 引擎编辑器来做了。
- [WWDC26-281] 使用 Xcode 扩展 Reality Composer Pro 3 的功能：✅ Reality Composer Pro 终于补齐了类似 Unity Editor Scripting 的能力，技术美术（TA）和艺术家不用再等工程师编译 App，就能在编辑器里实时跑自定义 Swift 逻辑了。
- [WWDC26-282] 探索 Spatial Preview 框架：这场 Session 最值得关注的一件事是：Mac 开发者现在可以零 visionOS 代码，把 Mac App 里的 3D 模型和文档直接扔进 visionOS 的 Quick Look 里做双向实时编辑。
- [WWDC26-283] 探索 visionOS 对象追踪的增强功能：✅ visionOS 对象追踪终于从“看静态摆件”进化到了“精准操控动态手持工具”，并彻底开放了第三方空间配件的硬件定义权。
- [WWDC26-284] 在 visionOS 中协作处理结构化 3D 模型：这场 Session 最值得关注的一件事是：RealityKit 新增的 ClippingComponent（剖切组件）和 ManipulationComponent（操控组件）的层级传递模式，直接把工业级 3D 模型的“拆解、剖切、爆炸图”交互从“手搓数学题”降维成了“搭积木”。
- [WWDC26-285] 探索 USDKit 以及 OpenUSD 的新进展：✅ Apple 终于用纯 Swift 重写了 USD 绑定（USDKit），让 3D 场景组装从“啃 C++ 头文件”变成了“写 SwiftUI 一样的日常”。
- [WWDC26-286] 使用 Foveated Streaming 将沉浸式内容融入 visionOS：这场 Session 最值得关注的一件事是：Apple 终于官方下场做“串流”了，FoveatedStreaming 框架让 visionOS 能直接当 PC 的“高级显示器”，把跑不动的重度 OpenXR 应用通过眼动追踪优化带宽后无线串流过来，而且还能和原生 3D 物体无缝缝合。
- [WWDC26-287] 利用 visionOS 27 打造新一代体验：Foveated Streaming（注视点流式传输）框架的推出是这场 Session 最值得关注的事，Apple 终于承认了"纯靠头显 M5 芯片搞不定重度 3D"的现实，把 PC 串流做成了官方一等公民。
- [WWDC26-320] 探索 visionOS 中的沉浸式网站环境：网页终于能原生“击穿”浏览器边界做 VR 体验了，不用写一行 Swift 代码，几行 JS 就能把用户直接拉进 1:1 的 3D 场景里。
- [WWDC26-338] 为 Apple 沉浸视频构建实时制作工具：Apple 终于把 Vision Pro 的“看片”体验推向了广电级直播工业标准，SMPTE 2110 和流式 ProRes 的直接打通，意味着第三方导播台和即时回放系统可以无缝接入 Apple Immersive Video (AIV) 生态了。
- [WWDC26-393] 使用 Reality Composer Pro 3 加速你的空间工作流程：这场 Session 最值得关注的一件事是：Reality Composer Pro 3 (RCP3) 终于把 visionOS 的场景搭建从“程序员手搓代码”变成了“TA（技术美术）和设计师能直接上手的节点连线游戏”。以前做个 NPC 巡逻或者复杂粒子，得在 Xcode 里写一堆 Swift 和 RealityKit API，改个参数就要重新编译；现在直接在 RCP3 里连节点就能搞定，这对开发效率的提升是降维打击级别的。
- [WWDC25-101] Keynote：Liquid Glass 是 iOS 7 以来最大的设计变革，Foundation Models 框架让端侧 AI 真正落地到每个 app，Xcode 26 接入多模型 coding assistant 这一届 WWDC 把设计、AI 和工具链三条线同时拉满了。
- [WWDC25-201] Metal 新特性：Metal 终于开始帮你管那些你一直在手动管的东西了——渲染状态、Shader 编译、分辨率折中——这次更新的信号是：别自己造轮子了，用框架的。
