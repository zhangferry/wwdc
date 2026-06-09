---
name: wwdc-notes
description: 独立查询 WWDC 2020-2026 Apple 平台开发知识。用于回答 Swift、SwiftUI、UIKit、AppKit、并发、Xcode、visionOS、Core AI、Foundation Models、MLX、网络存储、图形媒体、系统服务、隐私安全、设计与分发问题；需要按年份追踪 API 演进或检索 WWDC Session 来源时使用此 skill。
---

# WWDC Notes

这是一个离线 WWDC 知识库。默认只读取 skill 自带文件，不假设外部项目或资料存在。

## 回答协议

先判断问题类型：

| 类型 | 行动 |
| --- | --- |
| 概念解释 | 读取相关领域 reference，给出简洁解释和来源 |
| API 选型 | 对比适用场景、迁移成本、反模式，并标注 Session |
| 跨年演进 | 读取 overview 与领域 reference，用时间线回答 |
| 代码建议 | 先检索具体 Session；最低系统版本需要官方文档确认 |
| 最新状态 | 查询 Apple 官方文档，不只依赖 WWDC 摘要 |

需要具体 API、代码、迁移细节或更多证据时，运行本地索引检索：

```bash
python3 scripts/search.py "查询内容" --limit 8
```

回答时引用 `[WWDC25-266]` 这类来源格式。不要假设 Session ID 长度固定。

WWDC 2026 内容当前为首发速览版，依据 Apple 官方标题、简介、章节摘要和示例代码索引整理。完整 transcript 尚未发布时，回答中应明确资料状态，不把章节摘要扩写成 Apple 未声明的实现细节。

## 领域路由

| 主题 | Reference |
| --- | --- |
| SwiftUI、视图、布局、导航、动画、Observation | [swiftui.md](references/swiftui.md) |
| async/await、Actor、Sendable、任务、线程安全 | [swift-concurrency.md](references/swift-concurrency.md) |
| UIKit、AppKit、生命周期、互操作 | [uikit-appkit.md](references/uikit-appkit.md) |
| Xcode、调试、Instruments、测试、性能 | [xcode-tools.md](references/xcode-tools.md) |
| visionOS、空间计算、RealityKit、ARKit | [spatial-computing.md](references/spatial-computing.md) |
| Core ML、Create ML、端侧模型、AI | [machine-learning.md](references/machine-learning.md) |
| URLSession、Network、SwiftData、Core Data、CloudKit | [networking-storage.md](references/networking-storage.md) |
| Metal、图形、游戏、音视频、相机、WebKit | [graphics-media.md](references/graphics-media.md) |
| Widget、App Intents、Live Activity、通知、系统集成 | [platform-services.md](references/platform-services.md) |
| App Store、TestFlight、签名、分发 | [app-distribution.md](references/app-distribution.md) |
| 隐私、安全、权限、Passkey | [privacy-security.md](references/privacy-security.md) |
| Design、无障碍、本地化 | [design-accessibility.md](references/design-accessibility.md) |

## 回答规范

- 默认用中文回答，保留 API 英文名称。
- 涉及多年变化时优先给出时间线。
- 涉及当前 SDK 状态、最低系统版本或弃用状态时，查 Apple 官方文档确认。
- 将 Session 中的建议表述为 WWDC 知识，不要把推断写成 Apple 官方保证。
- 本地资料不足时明确说明缺口，不编造来源。
