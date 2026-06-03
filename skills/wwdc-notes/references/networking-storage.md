# Networking & Storage

## 领域判断

网络、数据持久化、CloudKit、SwiftData 与同步。本领域覆盖 48 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **CloudKit**：如果你的 App 用了 CloudKit 但从未打开过 Console 的 Telemetry 页面，你大概率遗漏了线上错误率和延迟的系统性问题——这场 Session 教你用对工具。；SwiftData 的 ModelContainer 和 ModelConfiguration 让你精细控制持久化策略——从内存数据库到多 CloudKit 容器，一套 API 全搞定。；CloudKit Console 终于从一个"能看数据库"的只读工具变成了一个完整的开发者控制台——新查询构建器、Schema 编辑器、Token 管理、团队协作支持，日常开发再也不用开 Xcode 了。 来源：[WWDC24-10122]、[WWDC23-10196]、[WWDC22-10115]、[WWDC21-10015]
- **SwiftData**：如果你的 App 需要离线同步、Widget 数据回传或增量式 UI 更新，SwiftData History 是今年最值得直接上手的新 API 之一。；SwiftData 今年补上了三个关键短板：唯一约束、自定义数据存储、复杂查询优化，从"能用的 Core Data 替代品"变成了"值得认真投入的数据层方案"。；这是一场手把手教学——用闪卡应用做实例，演示如何用 @Model、@Query、ModelContainer 三板斧在 SwiftUI 中集成 SwiftData，从零到完整持久化只需要改几行代码。 来源：[WWDC24-10075]、[WWDC24-10137]、[WWDC23-10154]、[WWDC23-10189]
- **CoreData**：NSPersistentCloudKitContainer 终于支持了多用户数据共享——这意味着协作类 app（共享笔记、共享列表）可以不用自建后端了，但共享粒度的控制还需要仔细设计。；Core Data 终于正式拥抱 Swift Concurrency——@MainActor 标注的 View Context 和 NSManagedObjectContext 的 perform 方法现在可以用 async/await 写了，不用再嵌套回调地狱。；Core Data 团队罕见地在 WWDC 上做了一场"知识补完" Session，涵盖并发、迁移、性能调优等长期困扰开发者的杂项——如果你还在用 Core Data，这是必看内容。 来源：[WWDC21-10015]、[WWDC21-10017]、[WWDC20-10017]、[WWDC20-10650]
- **Task**：CloudKit 这次的更新主要是"运维友好"方向：共享记录的权限细化、CloudKit Console 的 Web 版、以及 Schema 变更的声明式管理 —— 但如果你没用过 CloudKit，这些改进无法吸引你从 Firebase 迁移过来。；URLSession 的 async/await API 不是简单的语法糖 —— 它彻底消灭了嵌套回调地狱和手动管理 Resume Data 的复杂度，网络层代码量能砍掉一半，但你需要理解 structured concurrency 的取消语义才能用好它。；CloudKit Console 是旧版 CloudKit Dashboard 的 Web 重建版本 —— 终于可以在浏览器里直接写查询、查看日志、监控性能了，但还缺少批量数据导入和实时数据流查看这些高级功能。 来源：[WWDC21-10086]、[WWDC21-10095]、[WWDC21-10117]、[WWDC21-10258]
- **AVFoundation**：5G 不只是"更快的 4G" —— 苹果提供了 NWPathMonitor 的 5G 感知能力和 URLSession 的 allowsExpensiveNetworkAccess 属性，让你根据网络类型和资费状态做出不同的数据加载策略，这才是这集 Session 的真正价值。；AVAssetDownloadSession 在 iOS 14 中获得了完整的功能升级——支持 FairPlay DRM 离线下载、多语言音频轨道选择、以及后台下载恢复，做视频类 app 的离线缓存方案终于不用自己造轮子了。 来源：[WWDC21-10103]、[WWDC20-10655]
- **Swift & UI**：OpenAPI 规范驱动的代码生成，让 Swift 调用 REST API 从样板代码地狱中解脱出来。；SwiftData 用一个 @Model 宏替代了 Core Data 的整个 xcdatamodel 文件——数据持久化终于进入了纯 Swift 时代。 来源：[WWDC23-10171]、[WWDC23-10187]
- **System & Services**：L4S 能在拥挤网络中将视频通话的延迟降低 50%、丢包率降到接近零——如果你的 app 涉及实时通信，这个技术必须了解。；网络延迟优化的最大收益不在代码层面——启用 HTTP/3、配置 DNS 预解析、复用连接这三招能砍掉 50% 以上的延迟。 来源：[WWDC23-10004]、[WWDC21-10239]

## API 演进时间线

- **WWDC25**：5 场，代表来源：[WWDC25-212]、[WWDC25-234]、[WWDC25-250]、[WWDC25-291]、[WWDC25-346]
- **WWDC24**：4 场，代表来源：[WWDC24-10075]、[WWDC24-10122]、[WWDC24-10137]、[WWDC24-10138]
- **WWDC23**：13 场，代表来源：[WWDC23-10002]、[WWDC23-10004]、[WWDC23-10007]、[WWDC23-10154]、[WWDC23-10171]
- **WWDC22**：4 场，代表来源：[WWDC22-10078]、[WWDC22-10115]、[WWDC22-10119]、[WWDC22-10120]
- **WWDC21**：15 场，代表来源：[WWDC21-10015]、[WWDC21-10017]、[WWDC21-10031]、[WWDC21-10058]、[WWDC21-10086]
- **WWDC20**：7 场，代表来源：[WWDC20-10017]、[WWDC20-10110]、[WWDC20-10113]、[WWDC20-10151]、[WWDC20-10184]

## 决策启发式

- HTTP 网络请求继续使用 URLSession，不需要迁移到 Network framework。
- App to app 通信优先选择 Coder over TLS/QUIC，获得类型安全和零样板代码的双重收益。
- 对接已有服务器时，先确认服务器使用的协议格式，再选择 TLV framer 或 byte stream 模式。
- 为 NetworkConnection 安装 stateUpdateHandler 以在 UI 中反映连接状态，即使你不需要主动管理状态。
- 不同线程使用不同的 Command Allocator（Metal 4 类比：NetworkConnection 的 task 取消会自动清理连接，但自己创建的 task 仍需注意生命周期）。
- Wi Fi Aware 仅支持 iOS 26 的 iPhone，跨平台场景用 Bonjour + NetworkBrowser。
- 先画查询模式再决定模型结构。 列出你的所有 fetch/query 场景，统计 deep vs shallow search 的比例。继承不是默认选择。
- 迁移测试要覆盖完整升级路径。 用户可能从任何历史版本直接升级到最新版。用 versioned schema + migration plan 确保每一步都能正确执行。
- History token 要持久化。 存在 UserDefaults 或文件中，下次启动时从上次 token 继续，避免重复处理。
- @available 标记要同步。 子类、version schema、migration stage 都需要标注 iOS 26 availability，否则编译器会报错。

## 反模式与坑

- URLSessionTaskMetrics 新增了 TLS 握手和 DNS 解析的独立耗时，排查"为什么这个请求慢"终于不用抓包了。
- HTTP/3 连接建立优化在 Session 里被提及，但实际性能提升取决于你的用户网络环境和 CDN 配置，别指望开个开关就能提速。
- @Generable 宏可以简化 Codable 模型定义，但和类型化响应 API 是两个独立特性，别搞混了。
- iOS 26 新增 NEHotspotHelper 扩展 API，用于 Wi Fi 热点交互。
- VPN 的 excludeLocalNetworks 等异常选项现在大多数默认开启，但可以根据安全需求自定义。
- URL Filter 的 PIR 服务器有开源示例代码，包含完整的 PIR 服务器和 Privacy Pass Issuer 实现。
- 如果你之前使用的是 Network framework 的 C API 或偏好 completion handler 风格，不需要迁移——所有旧 API 继续得到完整支持。
- NetworkListener 自动为每个新连接启动 subtask，你可以在 handler 里直接做 async 操作而不用担心阻塞后续连接。

## 高频主题

`系统服务` (2)、`URLSession` (1)、`网络` (1)、`HTTP` (1)、`Swift Concurrency` (1)、`隐私` (1)、`应用服务` (1)、`Swift` (1)、`开发工具` (1)

## 关键 Session

- [WWDC25-212] URLSession 新特性：如果你还在每个网络调用点手写 JSONDecoder + decode() 的样板代码，这场 Session 直接帮你把这层废代码删掉了。
- [WWDC25-234] 用 NetworkExtension 过滤和隧道化网络流量：iOS 26 终于允许你根据完整 URL 而不只是 host 来做内容过滤了——但代价是你永远碰不到 URL 本身，系统用 Bloom filter + 同态加密 + Privacy Pass 做了一个隐私优先的方案。
- [WWDC25-250] Network framework 的结构化并发实践：Network framework 终于有了 Swift native 的声明式 API——NetworkConnection、NetworkListener、NetworkBrowser 三个类型把底层网络编程的门槛拉低到了 SwiftUI 的水平。
- [WWDC25-291] SwiftData: Dive into inheritance and schema migration：SwiftData 终于支持 class inheritance 了。但别高兴太早——继承只在你的模型确实构成 "is a" 关系、且查询模式同时需要 deep 和 shallow search 时才值得用。Apple 同时给出了从 iOS 17 到 iOS 26 的完整迁移方案，很实用。
- [WWDC25-346] 认识 Containerization：Apple 用 Swift 写了一个 Linux 容器框架，每个容器跑在独立的轻量级 VM 里，sub second 启动，没有 Docker Desktop 也能在 Mac 上跑容器了。
- [WWDC24-10075] 用 SwiftData History 追踪模型变更：如果你的 App 需要离线同步、Widget 数据回传或增量式 UI 更新，SwiftData History 是今年最值得直接上手的新 API 之一。
- [WWDC24-10122] 用 CloudKit Console 监控和优化数据库活动：如果你的 App 用了 CloudKit 但从未打开过 Console 的 Telemetry 页面，你大概率遗漏了线上错误率和延迟的系统性问题——这场 Session 教你用对工具。
- [WWDC24-10137] SwiftData 的新特性：SwiftData 今年补上了三个关键短板：唯一约束、自定义数据存储、复杂查询优化，从"能用的 Core Data 替代品"变成了"值得认真投入的数据层方案"。
- [WWDC24-10138] 用 SwiftData 打造自定义数据存储：SwiftData 终于开放了 DataStore 协议，你可以把底层的持久化方案换成任何你想要的格式（JSON、远程 API、内存数据库），而上层的 Model 和 View 代码一行都不用改。
- [WWDC23-10002] 使用网络中继保护应用流量：苹果把 iCloud Private Relay 背后的中继技术开放给了开发者——你可以为自己的 App 配置 MASQUE 中继，让服务器无法看到用户 IP 地址；也可以用中继替代企业 VPN 访问内部资源。
- [WWDC23-10004] 用 L4S 降低网络延迟：L4S 能在拥挤网络中将视频通话的延迟降低 50%、丢包率降到接近零——如果你的 app 涉及实时通信，这个技术必须了解。
- [WWDC23-10007] macOS Sonoma 虚拟化：可调整显示、状态保存与网络块设备：Virtualization 框架在 macOS Sonoma 中支持运行时调整虚拟机分辨率、保存/恢复虚拟机状态、网络块设备和 NVMe 控制器——虚拟 Mac 终于像原生 App 一样好用了。
- [WWDC23-10154] 用 SwiftData 构建应用：这是一场手把手教学——用闪卡应用做实例，演示如何用 @Model、@Query、ModelContainer 三板斧在 SwiftUI 中集成 SwiftData，从零到完整持久化只需要改几行代码。
- [WWDC23-10171] 认识 Swift OpenAPI Generator：OpenAPI 规范驱动的代码生成，让 Swift 调用 REST API 从样板代码地狱中解脱出来。
- [WWDC23-10186] Core Data 的新功能：Composite Attributes 让你终于可以用结构化的方式在 Core Data 中存储复杂类型，而不再依赖 Transformable 的黑盒序列化——而且还能在 NSPredicate 中用命名空间键路径查询。如果你之前因为 Transformable 的局限性而绕开 Core Data，现在值得重新评估。
- [WWDC23-10187] 认识 SwiftData：SwiftData 用一个 @Model 宏替代了 Core Data 的整个 xcdatamodel 文件——数据持久化终于进入了纯 Swift 时代。
- [WWDC23-10188] 用 CKSyncEngine 同步 iCloud 数据：少写代码，多同步：如果你不用 Core Data 但需要 CloudKit 同步，CKSyncEngine 帮你处理调度、推送通知、订阅管理和错误重试——你只管提供数据。
- [WWDC23-10189] 迁移到 SwiftData：Core Data 到 SwiftData 的迁移有两条路径——完全迁移（删掉 Core Data 栈，全面拥抱 SwiftData）和共存模式（两个栈共享同一个持久化存储，渐进式迁移），Xcode 的 Managed Object Model Editor 助手可以自动生成 SwiftData 模型类。
