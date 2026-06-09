# Machine Learning & AI

## 领域判断

Core ML、Core AI、MLX、Foundation Models、端侧推理、模型优化与 Apple Intelligence。本领域覆盖 108 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **机器学习**：App Intents 已经从"可选的 Shortcuts 集成"变成了 Apple Intelligence 时代 app 的必修课——如果你还没接入，现在是认真考虑的时候了。；如果你想给 app 加端侧 AI 功能但不知道从哪里开始，这场 Session 是手把手级别的教程——从 prompt 工程到 tool calling 到流式输出到性能优化，完整走了一遍构建旅行规划 app 的全过程。；Shortcuts 今年最大的变化是 Use Model action——用户可以在快捷指令中直接调用 Apple Intelligence 模型，而你的 App Entity 会被序列化成 JSON 传给模型推理。这意味着你的实体定义不仅决定了 UI 展示，还决定了模型能"看到"什么信息。 来源：[WWDC25-244]、[WWDC25-259]、[WWDC25-260]、[WWDC25-272]
- **Foundation Models**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 Vision 框架和 Foundation Models 框架的最新更新，解锁强大的图像理解能力。新的轻点分割请求为你带来图像分割的新方式，而且 Vision 框架现在还支持 watchOS。将 Apple Foundation Models 中全新的图像支持与 OCR、条形码扫描以及你自己的工具相结合，为你的 App 构建由 LLM 支持的视觉理解能力。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Foundation Models 框架的新功能。了解如何访问专用云计算、整合第三方模型及开源模型，并构建优化视觉功能。探索上下文管理 API、内置的语义搜索，以及用于为你的 App 创建智能体体验的强大原语。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 Foundation Models 框架原语，在动态上下文和智能体工作流程中进一步提升你的智能功能。我们将逐步讲解如何构建共享上下文、设置隐私边界，并管理键值缓存。… 来源：[WWDC26-237]、[WWDC26-241]、[WWDC26-242]、[WWDC26-319]
- **AI & Machine Learning**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 SpotlightSearchTool 和 LanguageModelSession，将基础搜索升级为检索增强系统。探索 Core Spotlight 集成功能、委托式数据填充模式，以及元数据质量对搜索结果的影响。了解如何使用自定 PipelineStages 执行情感分析等任务。探索相关最佳做法，以便在你的 App 中建立索引，并构建灵活又贴合情境的搜索体验。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 Evaluations 框架的高级功能，为你的 App 构建稳健的评估。探索涉及工具调用和动态条件的评估流程，以及如何为你的用例定义正确的行为。了解如何生成合成数据、有效使用评审模型，并验证你的数据集以便获得可靠的结果。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索各种技巧，了解如何利用你 App 的内容构建强大的快捷指令。新的自动化功能为 App 与系统的集成解锁了更多可能。借助新的“使用模型”转录功能，优化… 来源：[WWDC26-246]、[WWDC26-299]、[WWDC26-310]、[WWDC26-379]
- **AppIntent**：App Intents 已经从"可选的 Shortcuts 集成"变成了 Apple Intelligence 时代 app 的必修课——如果你还没接入，现在是认真考虑的时候了。；App Intents 终于从"系统替你展示一个静态结果"进化到了"用户可以直接在 Snippet 里交互"——按钮、Toggle、多选项、撤销手势全部打通，而且 App Intent 的代码可以完全不做修改就用在 Snippet 里。；Snippet 从"系统替你弹一个结果卡片"变成了"你的 App 可以在系统层做轻量级交互"——按钮、数据更新、确认流程全支持。设计指南的核心矛盾是：既要信息密度够高，又要一眼就能扫完。 来源：[WWDC25-244]、[WWDC25-275]、[WWDC25-281]、[WWDC24-101]
- **CoreML**：从找到开源模型到实机运行——这场 Session 是一份完整的端到端 ML 应用开发流程演示，特别适合第一次把 ML 模型集成到 iOS 应用的开发者。；Core ML 模型的性能调优不只是换小模型——compute unit 选择、模型量化（Quantization）和批量预测优化这三个维度同时调才能榨干最后一滴性能。；Create ML 的手势分类器（Hand Pose Classifier）让不擅长 ML 的 iOS 开发者也能做出手势识别功能——你只需要准备标注好的手势图片，剩下的交给 Create ML。 来源：[WWDC22-10017]、[WWDC21-10038]、[WWDC21-10039]、[WWDC20-10043]
- **Machine Learning & AI**：iOS 18 的 Core ML Tools 把模型压缩的粒度从"per tensor"推到了"per block"级别——同样压缩到 4 bit，以前图像糊成马赛克，现在几乎无损，这让大模型上 iPhone 变得现实。；PyTorch MPS backend 今年在三个方面有实质性提升——int8/int4 量化、fused SDPA、统一内存支持——让你可以在 Mac 上用更大的模型做更快的训练，而不需要把 tensor 在 CPU 和 GPU 之间来回拷贝。；Core ML 今年引入的 MLTensor 类型解决了一个长期痛点：模型推理之外的计算胶水代码终于不用手写底层 API 了——这让大语言模型的端侧部署代码量直接砍半。 来源：[WWDC24-10159]、[WWDC24-10160]、[WWDC24-10161]、[WWDC24-10183]
- **Siri**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：Introducing Siri AI in iOS 27, with more power than ever. Transform your images with next generation AI. Create photorealistic imagery for wallpapers, Contact Posters, and backgrounds across the system in Image Playground. Use a more conversational Siri AI with natural language abilities to edit and write emails, texts, and documents. Keep your personal information safe…；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：利用 App Intents，将你 App 的内容和操作带到 Siri。通过 App Entities 对… 来源：[WWDC26-121]、[WWDC26-240]、[WWDC26-295]、[WWDC26-343]

## API 演进时间线

- **WWDC26**：33 场，代表来源：[WWDC26-121]、[WWDC26-213]、[WWDC26-215]、[WWDC26-232]、[WWDC26-233]
- **WWDC25**：26 场，代表来源：[WWDC25-101]、[WWDC25-102]、[WWDC25-111]、[WWDC25-112]、[WWDC25-204]
- **WWDC24**：13 场，代表来源：[WWDC24-10075]、[WWDC24-101]、[WWDC24-10159]、[WWDC24-10160]、[WWDC24-10161]
- **WWDC23**：8 场，代表来源：[WWDC23-10042]、[WWDC23-10044]、[WWDC23-10047]、[WWDC23-10049]、[WWDC23-10050]
- **WWDC22**：8 场，代表来源：[WWDC22-10017]、[WWDC22-10019]、[WWDC22-10020]、[WWDC22-10027]、[WWDC22-10063]
- **WWDC21**：9 场，代表来源：[WWDC21-10036]、[WWDC21-10037]、[WWDC21-10038]、[WWDC21-10039]、[WWDC21-10040]
- **WWDC20**：11 场，代表来源：[WWDC20-10043]、[WWDC20-10099]、[WWDC20-10152]、[WWDC20-10153]、[WWDC20-10156]

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

- App Intents + Visual Intelligence ：你的 app 可以注册 Visual Search schema，让用户通过相机识别直接跳转到你的 app。
- Background Tasks API 更新 ：支持后台长时间任务（如视频导出），CarPlay 支持 Live Activities。
- Terminal 更新 ：24 bit 色彩、Liquid Glass 主题、Powerline 字体支持。
- PermissionKit 框架 ：为儿童通信提供家长监督机制。
- Declared Age Range API ：在不侵犯隐私的前提下适龄调整 app 体验。
- Liquid Glass 不只是视觉改版
- Foundation Models 的 @Generable 是杀手级 API
- Xcode 26 的模型接入是开放架构

## 高频主题

`机器学习` (17)、`Foundation Models` (7)、`基础` (7)、`Siri` (6)、`Xcode` (6)、`AI & Machine Learning` (6)、`App Intents` (5)、`Core AI` (4)、`Metal` (4)、`MLX` (3)、`Design` (3)、`Swift` (2)、`图形与游戏` (2)、`visionOS` (1)、`Instruments` (1)、`Swift & Data` (1)、`Other` (1)、`MapKit` (1)

## 关键 Session

- [WWDC26-121] Announcing Apple’s next big step for Siri and iPhone：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：Introducing Siri AI in iOS 27, with more power than ever. Transform your images with next generation AI. Create photorealistic imagery for wallpapers, Contact Posters, and backgrounds across the system in Image Playground. Use a more conversational Siri AI with natural language abilities to edit and write emails, texts, and documents. Keep your personal information safe…
- [WWDC26-213] 使用 Xcode 中的智能体翻译你的 App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解 Xcode 和编码智能体如何根据 App 的情境帮助你翻译字符串目录。我们将介绍审核翻译输出和迭代本地化的策略，以便你为全球用户提供量身定制的体验。
- [WWDC26-215] HTML 模型元素入门：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解模型元素如何将交互式 3D 内容搬上你的网站，这项功能现已登陆 iOS、iPadOS、macOS 和 visionOS。探索用于创建和优化 3D 素材资源的工具。了解模型元素功能，看看各个网页标准如何构筑 3D 网页内容的未来。
- [WWDC26-232] 使用 MLX 在 Mac 上本地运行 AI 智能体：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：在本地运行 AI 智能体，兼顾隐私保护、低延迟和离线访问。深入了解 MLX 改进和 Mac 硬件如何彼此配合，让强大的智能体工作流程能完全在设备端实现。你将探索 OpenCode 等编码智能体，看看这些智能体如何集成到 Xcode 中；还将了解实现多台 Mac 扩展的技巧，以及不用切换设备就能无缝整合各种工具的做法。
- [WWDC26-233] 使用 MLX 探索分布式推理和训练：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 MLX 将机器学习工作负载扩展到多台 Mac。了解如何解决互连效率、大模型推理、请求批处理和分布式训练方面的难题。探索如何只用几台 Mac 来替代昂贵的云基础设施，从而满足 AI 工作负载的高要求。
- [WWDC26-237] 图像理解方面的新动向：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助 Vision 框架和 Foundation Models 框架的最新更新，解锁强大的图像理解能力。新的轻点分割请求为你带来图像分割的新方式，而且 Vision 框架现在还支持 watchOS。将 Apple Foundation Models 中全新的图像支持与 OCR、条形码扫描以及你自己的工具相结合，为你的 App 构建由 LLM 支持的视觉理解能力。
- [WWDC26-240] 使用 App Schemas 打造智能 Siri 体验：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：利用 App Intents，将你 App 的内容和操作带到 Siri。通过 App Entities 对数据进行建模，使用 App Schemas 实现强大的系统操作，并为依托 Apple 智能的自然语言交互提供支持。探索如何启用语义搜索、跨 App 执行操作，以及利用屏幕感知和内容传输功能打造贴合情境的用户体验。了解一些最佳做法和测试工具，助你构建快速、可靠的 Siri 体验。
- [WWDC26-241] Foundation Models 框架的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Foundation Models 框架的新功能。了解如何访问专用云计算、整合第三方模型及开源模型，并构建优化视觉功能。探索上下文管理 API、内置的语义搜索，以及用于为你的 App 创建智能体体验的强大原语。
- [WWDC26-242] 使用 Foundation Models 框架构建智能体 App 体验：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 Foundation Models 框架原语，在动态上下文和智能体工作流程中进一步提升你的智能功能。我们将逐步讲解如何构建共享上下文、设置隐私边界，并管理键值缓存。你还将探索如何协调本地模型与服务器模型的平滑交接。
- [WWDC26-243] 使用 Instruments 调试和分析智能体 App 体验：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索 Xcode 中增强的 Foundation Models Instrument，以便检查相关行为表现，并优化智能体流程的性能。了解如何在涉及多个 LanguageModelSession 和配置的高级用例中，检查提示词、分析延迟并追踪控制流。
- [WWDC26-246] 使用 Core Spotlight 进行 LLM 搜索：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 SpotlightSearchTool 和 LanguageModelSession，将基础搜索升级为检索增强系统。探索 Core Spotlight 集成功能、委托式数据填充模式，以及元数据质量对搜索结果的影响。了解如何使用自定 PipelineStages 执行情感分析等任务。探索相关最佳做法，以便在你的 App 中建立索引，并构建灵活又贴合情境的搜索体验。
- [WWDC26-295] 使用 AppIntentsTesting 验证你的 App Intents 采用情况：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：AppIntentsTesting 是一个全新的框架，可通过 Siri、“快捷指令”和“聚焦”所使用的同款基础架构来验证你的 App Intents。探索如何执行意图、检查结果，并测试实体和查询——全程无需 UI 自动化。了解如何验证视图注释和“聚焦”索引等集成功能，助你在开发流程中尽早发现错误。
- [WWDC26-298] 了解 Evaluations 框架：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何使用 Evaluations 框架来评估模型驱动的体验。在概率世界中，仅靠单元测试是不够的。探索如何定义指标、自动评估输出质量并汇总统计数据，以便确保由 AI 支持的功能在各个 Apple 平台上都能稳定可靠地运行。
- [WWDC26-299] 为智能体 App 打造稳健的评估：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 Evaluations 框架的高级功能，为你的 App 构建稳健的评估。探索涉及工具调用和动态条件的评估流程，以及如何为你的用例定义正确的行为。了解如何生成合成数据、有效使用评审模型，并验证你的数据集以便获得可靠的结果。
- [WWDC26-310] 快捷指令的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索各种技巧，了解如何利用你 App 的内容构建强大的快捷指令。新的自动化功能为 App 与系统的集成解锁了更多可能。借助新的“使用模型”转录功能，优化 App 实体在 LLM 中的呈现方式。将 App 中的丰富信息存储在跨设备保持同步的快捷指令中。了解如何结合使用这些功能，通过无缝整合你 App 中的内容和功能来构建智能、强大的自动化。
- [WWDC26-319] 通过专用云计算充分利用 [Model Name]：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：借助专用云计算，你能够访问功能强大的前沿模型，同时保护用户隐私。了解专用云计算的运行机制，以及如何利用 Foundation Models 框架访问这项功能。探索在你的 App 中检查可用性并平稳地处理回退事件的最佳做法。
- [WWDC26-324] 了解 Core AI：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：认识一下 Core AI，这是 Apple 新推出的设备端 AI 模型部署框架。一起浏览这个包罗万象的生态系统，看看如何借助 Python 资源库进行模型的转换、创建和优化，如何利用一种 Swift API 实现简单的即插即用推断，并构建高级用例来满足严格的延迟和内存要求等等。探索全新的 Core AI 模型存储库，其中包含适用于热门架构的现成示例。了解 Xcode 的深度集成 (包括模型的提前编译) 如何简化工作流程，从而帮助你交付更智能、更灵敏的 App 体验。
- [WWDC26-325] 深入探索 Core AI 模型编写与优化：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：深入探索适用于 Apple 芯片的自定模型部署流程，同时充分发挥全新 Core AI 框架的优势。了解使用自定 Metal 内核编写模型的超实用技巧，以及平台感知压缩策略。全新的 Core AI 调试器可提供深度内在分析；还有 AI 辅助的工作流程引导你逐步完善，从最初的概念构思到优化后的设备端执行，全称助你一臂之力。
