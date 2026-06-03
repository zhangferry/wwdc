# Machine Learning & AI

## 领域判断

Core ML、Create ML、端侧推理、模型优化与 Apple Intelligence。本领域覆盖 73 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **机器学习**：App Intents 已经从"可选的 Shortcuts 集成"变成了 Apple Intelligence 时代 app 的必修课——如果你还没接入，现在是认真考虑的时候了。；如果你想给 app 加端侧 AI 功能但不知道从哪里开始，这场 Session 是手把手级别的教程——从 prompt 工程到 tool calling 到流式输出到性能优化，完整走了一遍构建旅行规划 app 的全过程。；Shortcuts 今年最大的变化是 Use Model action——用户可以在快捷指令中直接调用 Apple Intelligence 模型，而你的 App Entity 会被序列化成 JSON 传给模型推理。这意味着你的实体定义不仅决定了 UI 展示，还决定了模型能"看到"什么信息。 来源：[WWDC25-244]、[WWDC25-259]、[WWDC25-260]、[WWDC25-272]
- **AppIntent**：App Intents 已经从"可选的 Shortcuts 集成"变成了 Apple Intelligence 时代 app 的必修课——如果你还没接入，现在是认真考虑的时候了。；App Intents 终于从"系统替你展示一个静态结果"进化到了"用户可以直接在 Snippet 里交互"——按钮、Toggle、多选项、撤销手势全部打通，而且 App Intent 的代码可以完全不做修改就用在 Snippet 里。；Snippet 从"系统替你弹一个结果卡片"变成了"你的 App 可以在系统层做轻量级交互"——按钮、数据更新、确认流程全支持。设计指南的核心矛盾是：既要信息密度够高，又要一眼就能扫完。 来源：[WWDC25-244]、[WWDC25-275]、[WWDC25-281]、[WWDC24-101]
- **CoreML**：从找到开源模型到实机运行——这场 Session 是一份完整的端到端 ML 应用开发流程演示，特别适合第一次把 ML 模型集成到 iOS 应用的开发者。；Core ML 模型的性能调优不只是换小模型——compute unit 选择、模型量化（Quantization）和批量预测优化这三个维度同时调才能榨干最后一滴性能。；Create ML 的手势分类器（Hand Pose Classifier）让不擅长 ML 的 iOS 开发者也能做出手势识别功能——你只需要准备标注好的手势图片，剩下的交给 Create ML。 来源：[WWDC22-10017]、[WWDC21-10038]、[WWDC21-10039]、[WWDC20-10043]
- **Machine Learning & AI**：iOS 18 的 Core ML Tools 把模型压缩的粒度从"per tensor"推到了"per block"级别——同样压缩到 4 bit，以前图像糊成马赛克，现在几乎无损，这让大模型上 iPhone 变得现实。；PyTorch MPS backend 今年在三个方面有实质性提升——int8/int4 量化、fused SDPA、统一内存支持——让你可以在 Mac 上用更大的模型做更快的训练，而不需要把 tensor 在 CPU 和 GPU 之间来回拷贝。；Core ML 今年引入的 MLTensor 类型解决了一个长期痛点：模型推理之外的计算胶水代码终于不用手写底层 API 了——这让大语言模型的端侧部署代码量直接砍半。 来源：[WWDC24-10159]、[WWDC24-10160]、[WWDC24-10161]、[WWDC24-10183]
- **基础**：如果说 Keynote 是面向用户的发布会，PSOTU 就是面向开发者的施工图 Liquid Glass 的 API 落地细节、Foundation Models 的 tool calling 和 guided generation、Swift 6.2 的并发简化、Metal 4 的 neural rendering，全部在这里展开。；这是 Keynote 的 ASL（美国手语）版本，内容与 Session 101 完全一致，适合需要手语辅助理解的开发者观看。；这是 Apple ML/AI 生态的「总导览图」——从系统级智能到 Foundation Models 框架到 Core ML 到 MLX，帮你快速定位该用哪个工具解决什么问题。 来源：[WWDC25-102]、[WWDC25-111]、[WWDC25-360]、[WWDC25-364]
- **AppIntents**：这是 WWDC 2024 技术层面的"全局地图"——Apple Intelligence 的端侧+云端双轨架构、Private Cloud Compute 的安全模型、以及全平台 API 的关键更新都在这里集中展示，如果你只看一场 Session 来把握今年方向，就是这场。；WWDC 2024 Keynote 的核心叙事只有一个：Apple Intelligence——从系统级 AI 能力到开发者工具链，Apple 在全面铺设自己的 AI 基础设施。；Platforms State of the Union 是开发者视角的 WWDC 重头戏——Apple Intelligence 的端侧模型架构（Adapter 机制 + 4 bit 量化 + Neural Engine 优化）、Private Cloud Compute 的安全设计、Swift 6 的并发安全迁移、以及 Xcode 16 的预测代码补全，这些都会直接影响你接下来的开发工作。 来源：[WWDC24-102]、[WWDC24-111]、[WWDC24-112]
- **AVFoundation**：Apple 通过一个完整的健身动作追踪 App 示例，展示了如何将 Vision 框架的人体姿态检测（Body Pose）能力集成到实际产品中，是学习 Vision 框架实战应用的最佳起点。；Create ML 现在支持风格迁移了——不需要懂神经网络，拖几张风格图进去就能训练出一个能把照片变成油画风格的核心模型。 来源：[WWDC20-10099]、[WWDC20-10642]

## API 演进时间线

- **WWDC25**：24 场，代表来源：[WWDC25-101]、[WWDC25-102]、[WWDC25-111]、[WWDC25-204]、[WWDC25-205]
- **WWDC24**：13 场，代表来源：[WWDC24-10075]、[WWDC24-101]、[WWDC24-10159]、[WWDC24-10160]、[WWDC24-10161]
- **WWDC23**：8 场，代表来源：[WWDC23-10042]、[WWDC23-10044]、[WWDC23-10047]、[WWDC23-10049]、[WWDC23-10050]
- **WWDC22**：8 场，代表来源：[WWDC22-10017]、[WWDC22-10019]、[WWDC22-10020]、[WWDC22-10027]、[WWDC22-10063]
- **WWDC21**：9 场，代表来源：[WWDC21-10036]、[WWDC21-10037]、[WWDC21-10038]、[WWDC21-10039]、[WWDC21-10040]
- **WWDC20**：11 场，代表来源：[WWDC20-10043]、[WWDC20-10099]、[WWDC20-10152]、[WWDC20-10153]、[WWDC20-10156]

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

- App Intents + Visual Intelligence ：你的 app 可以注册 Visual Search schema，让用户通过相机识别直接跳转到你的 app。
- Background Tasks API 更新 ：支持后台长时间任务（如视频导出），CarPlay 支持 Live Activities。
- Terminal 更新 ：24 bit 色彩、Liquid Glass 主题、Powerline 字体支持。
- PermissionKit 框架 ：为儿童通信提供家长监督机制。
- Declared Age Range API ：在不侵犯隐私的前提下适龄调整 app 体验。
- Liquid Glass 不只是视觉改版
- Foundation Models 的 @Generable 是杀手级 API
- Xcode 26 的模型接入是开放架构

## 高频主题

`机器学习` (17)、`基础` (5)、`Design` (2)、`图形与游戏` (2)、`MapKit` (1)、`GeoToolbox` (1)、`PlaceDescriptor` (1)、`Geocoding` (1)、`Metal 4` (1)、`GPU` (1)、`MetalFX` (1)、`Machine Learning` (1)、`App Intents` (1)、`Siri` (1)、`Shortcuts` (1)、`Apple Intelligence` (1)、`AI` (1)、`应用服务` (1)

## 关键 Session

- [WWDC25-101] Keynote：Liquid Glass 是 iOS 7 以来最大的设计变革，Foundation Models 框架让端侧 AI 真正落地到每个 app，Xcode 26 接入多模型 coding assistant 这一届 WWDC 把设计、AI 和工具链三条线同时拉满了。
- [WWDC25-102] Platforms State of the Union：如果说 Keynote 是面向用户的发布会，PSOTU 就是面向开发者的施工图 Liquid Glass 的 API 落地细节、Foundation Models 的 tool calling 和 guided generation、Swift 6.2 的并发简化、Metal 4 的 neural rendering，全部在这里展开。
- [WWDC25-111] Keynote (ASL)：这是 Keynote 的 ASL（美国手语）版本，内容与 Session 101 完全一致，适合需要手语辅助理解的开发者观看。
- [WWDC25-204] 深入探索 MapKit：如果你的 app 里有任何"把别人的地点 ID 塞进 MapKit"的胶水代码，这场 Session 直接帮你删掉它。
- [WWDC25-205] 探索 Metal 4：Metal 4 真正的卖点不是某个新 API，而是它让图形渲染和 ML 推理第一次在 GPU 命令层面上成为同一件事——如果你做游戏或者实时图像处理，这意味着你可以把 Neural Engine 和 GPU 当成一个统一的计算池来调度。
- [WWDC25-216] App Intents 新特性：如果你现在还不给应用加 App Intents，等 Apple Intelligence 在国内落地那天，你的应用在 Siri 里就是隐形的。
- [WWDC25-244] App Intents 框架全面入门：App Intents 已经从"可选的 Shortcuts 集成"变成了 Apple Intelligence 时代 app 的必修课——如果你还没接入，现在是认真考虑的时候了。
- [WWDC25-248] 端侧大模型的 Prompt 设计与安全策略：如果你打算用 Foundation Models framework 做任何用户可输入的功能，这场 Session 里关于安全分层防御的部分比 prompt 技巧本身重要十倍。
- [WWDC25-259] 实战：用 Foundation Models 框架为 app 加入端侧 AI：如果你想给 app 加端侧 AI 功能但不知道从哪里开始，这场 Session 是手把手级别的教程——从 prompt 工程到 tool calling 到流式输出到性能优化，完整走了一遍构建旅行规划 app 的全过程。
- [WWDC25-260] 用 App Intents 适配 Shortcuts 与 Spotlight：Use Model 是今年的重头戏：Shortcuts 今年最大的变化是 Use Model action——用户可以在快捷指令中直接调用 Apple Intelligence 模型，而你的 App Entity 会被序列化成 JSON 传给模型推理。这意味着你的实体定义不仅决定了 UI 展示，还决定了模型能"看到"什么信息。
- [WWDC25-262] Metal 4 ML 与图形融合：Tensor、ML Encoder 和 Shader ML：Metal 4 把 ML 正式纳入了 GPU 渲染管线——MTLTensor 解决了多维数据的资源管理，ML Command Encoder 让整网推理和渲染/计算命令在同一时间线上同步执行，而 Shader ML 允许你在 fragment shader 内部直接跑神经网络。这套组合拳瞄准的是实时渲染中 ML 最密集的三个场景：超分、材质压缩和光照计算。
- [WWDC25-265] 深入 Writing Tools：富文本、语义样式与自定义文本引擎集成：Writing Tools 今年的核心改进是富文本支持的精细化——display attributes 和 presentation intents 的区分是理解一切的关键。如果你有自定义文本引擎，Writing Tools Coordinator API 给了你完整的集成路径，但这是一份需要仔细对待的 delegate 实现工作。
- [WWDC25-272] 用 Vision 框架读取文档：结构化识别与镜头污渍检测：RecognizeDocumentsRequest 是 RecognizeTextRequest 的结构化升级版——它不只识别文字，还能解析表格行列、列表层级、段落分组，并自动检测邮箱/电话/URL 等关键数据。如果你之前用 RecognizeTextRequest 然后自己用坐标计算表格结构，现在可以大幅简化代码了。
- [WWDC25-275] App Intents 框架进阶：App Intents 终于从"系统替你展示一个静态结果"进化到了"用户可以直接在 Snippet 里交互"——按钮、Toggle、多选项、撤销手势全部打通，而且 App Intent 的代码可以完全不做修改就用在 Snippet 里。
- [WWDC25-276] BNNS Graph 新特性：BNNS Graph Builder API 让你用纯 Swift 写推理图——不再需要维护单独的 PyTorch/CoreML 文件，编译期就能做类型检查，而且 FP16 比 FP32 快了一大截。这对实时音频和图像预处理场景是重大利好。
- [WWDC25-277] 用 SpeechAnalyzer 实现高级语音转文字：SFSpeechRecognizer 的继任者来了——SpeechAnalyzer 用 Swift Concurrency 和 AsyncSequence 重构了整套语音转文字 API，模型完全离线运行且不占用 App 内存空间，支持长音频、远距离拾音和 volatile 实时预览结果。
- [WWDC25-281] 设计交互式 Snippet：Snippet 从"系统替你弹一个结果卡片"变成了"你的 App 可以在系统层做轻量级交互"——按钮、数据更新、确认流程全支持。设计指南的核心矛盾是：既要信息密度够高，又要一眼就能扫完。
- [WWDC25-286] Meet the Foundation Models framework：Apple 终于把 Apple Intelligence 背后那个 3B 参数的大模型开放给开发者了，而且是纯 Swift API、完全 on device、零服务端依赖。这是今年 ML 方向最重磅的框架，没有之一。
