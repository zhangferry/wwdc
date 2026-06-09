# Networking & Storage

## 领域判断

网络、数据持久化、CloudKit、SwiftData 与同步。本领域覆盖 51 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **SwiftData**：这场 Session 最值得关注的一件事是：SwiftData 终于把数据监听能力从 SwiftUI 视图里剥离出来了，ModelResultsObserver 让你能在纯 ViewModel 或后台服务里优雅地响应数据库变化，不用再写恶心的 workaround。；这场 Session 最值得关注的一件事是：SwiftData 迁移绝不是无脑加 @Model 宏，它强迫你重构底层数据结构（比如把 Enum 拍平成 Class 继承），并且苹果终于用全新的 withContinuousObservation API 解决了 @Model 里 didSet 失效的痛点。；这场 Session 最值得关注的一件事是：Apple 正在用 Group Labs（小组实验室）全面替代传统的 1 on 1 Labs，这意味着你在 WWDC 期间想白嫖 Apple 工程师帮你单对单 debug 的机会变少了，但“围观”别人踩坑的机会变多了。 来源：[WWDC26-274]、[WWDC26-275]、[WWDC26-394]、[WWDC24-10075]
- **CloudKit**：如果你的 App 用了 CloudKit 但从未打开过 Console 的 Telemetry 页面，你大概率遗漏了线上错误率和延迟的系统性问题——这场 Session 教你用对工具。；SwiftData 的 ModelContainer 和 ModelConfiguration 让你精细控制持久化策略——从内存数据库到多 CloudKit 容器，一套 API 全搞定。；CloudKit Console 终于从一个"能看数据库"的只读工具变成了一个完整的开发者控制台——新查询构建器、Schema 编辑器、Token 管理、团队协作支持，日常开发再也不用开 Xcode 了。 来源：[WWDC24-10122]、[WWDC23-10196]、[WWDC22-10115]、[WWDC21-10015]
- **CoreData**：NSPersistentCloudKitContainer 终于支持了多用户数据共享——这意味着协作类 app（共享笔记、共享列表）可以不用自建后端了，但共享粒度的控制还需要仔细设计。；Core Data 终于正式拥抱 Swift Concurrency——@MainActor 标注的 View Context 和 NSManagedObjectContext 的 perform 方法现在可以用 async/await 写了，不用再嵌套回调地狱。；Core Data 团队罕见地在 WWDC 上做了一场"知识补完" Session，涵盖并发、迁移、性能调优等长期困扰开发者的杂项——如果你还在用 Core Data，这是必看内容。 来源：[WWDC21-10015]、[WWDC21-10017]、[WWDC20-10017]、[WWDC20-10650]
- **Task**：CloudKit 这次的更新主要是"运维友好"方向：共享记录的权限细化、CloudKit Console 的 Web 版、以及 Schema 变更的声明式管理 —— 但如果你没用过 CloudKit，这些改进无法吸引你从 Firebase 迁移过来。；URLSession 的 async/await API 不是简单的语法糖 —— 它彻底消灭了嵌套回调地狱和手动管理 Resume Data 的复杂度，网络层代码量能砍掉一半，但你需要理解 structured concurrency 的取消语义才能用好它。；CloudKit Console 是旧版 CloudKit Dashboard 的 Web 重建版本 —— 终于可以在浏览器里直接写查询、查看日志、监控性能了，但还缺少批量数据导入和实时数据流查看这些高级功能。 来源：[WWDC21-10086]、[WWDC21-10095]、[WWDC21-10117]、[WWDC21-10258]
- **AVFoundation**：5G 不只是"更快的 4G" —— 苹果提供了 NWPathMonitor 的 5G 感知能力和 URLSession 的 allowsExpensiveNetworkAccess 属性，让你根据网络类型和资费状态做出不同的数据加载策略，这才是这集 Session 的真正价值。；AVAssetDownloadSession 在 iOS 14 中获得了完整的功能升级——支持 FairPlay DRM 离线下载、多语言音频轨道选择、以及后台下载恢复，做视频类 app 的离线缓存方案终于不用自己造轮子了。 来源：[WWDC21-10103]、[WWDC20-10655]
- **Swift & UI**：OpenAPI 规范驱动的代码生成，让 Swift 调用 REST API 从样板代码地狱中解脱出来。；SwiftData 用一个 @Model 宏替代了 Core Data 的整个 xcdatamodel 文件——数据持久化终于进入了纯 Swift 时代。 来源：[WWDC23-10171]、[WWDC23-10187]
- **System & Services**：L4S 能在拥挤网络中将视频通话的延迟降低 50%、丢包率降到接近零——如果你的 app 涉及实时通信，这个技术必须了解。；网络延迟优化的最大收益不在代码层面——启用 HTTP/3、配置 DNS 预解析、复用连接这三招能砍掉 50% 以上的延迟。 来源：[WWDC23-10004]、[WWDC21-10239]

## API 演进时间线

- **WWDC26**：3 场，代表来源：[WWDC26-274]、[WWDC26-275]、[WWDC26-394]
- **WWDC25**：5 场，代表来源：[WWDC25-212]、[WWDC25-234]、[WWDC25-250]、[WWDC25-291]、[WWDC25-346]
- **WWDC24**：4 场，代表来源：[WWDC24-10075]、[WWDC24-10122]、[WWDC24-10137]、[WWDC24-10138]
- **WWDC23**：13 场，代表来源：[WWDC23-10002]、[WWDC23-10004]、[WWDC23-10007]、[WWDC23-10154]、[WWDC23-10171]
- **WWDC22**：4 场，代表来源：[WWDC22-10078]、[WWDC22-10115]、[WWDC22-10119]、[WWDC22-10120]
- **WWDC21**：15 场，代表来源：[WWDC21-10015]、[WWDC21-10017]、[WWDC21-10031]、[WWDC21-10058]、[WWDC21-10086]
- **WWDC20**：7 场，代表来源：[WWDC20-10017]、[WWDC20-10110]、[WWDC20-10113]、[WWDC20-10151]、[WWDC20-10184]

## 决策启发式

- 已有项目的迁移策略 ：如果你之前为了在非 UI 层监听 SwiftData 数据，写了基于 NSManagedObjectContextDidSave 的 Notification 监听，或者搞了个隐藏的 SwiftUI View 来桥接 @Query，现在可以全部删掉，替换为 ModelResultsObserver。这能让你的 ViewModel 或 Controller 代码干净一半。
- 新项目的采用建议 ：大胆把数据获取逻辑从 View 层抽离。View 层的 @Query 只用于最简单的列表渲染；涉及复杂计算、网络请求联动、地图边界计算的场景，统统交给持有 ModelResultsObserver 的 @Observable 状态对象。
- 实战中容易踩的坑 ：使用 HistoryObserver 做云端同步时，一定要在初始化时传入 authors 参数（比如 ["App"]）。如果不加过滤，你会把从服务器拉取下来的数据变更再次触发同步，直接导致死循环。
- 已有项目的迁移策略 ：别想着一步到位。先剥离内存 DataSource，把纯数据模型改成 @Model。遇到 Enum 状态机，果断重构为 Class 继承体系。把环境对象（EnvironmentObject）替换为 @Query 时，按视图层级逐个替换，确保每次替换后 UI 渲染正常。
- 新项目的采用建议 ：直接在 Model 层设计好继承体系，别用 Enum 凑合。对于需要频繁查询的字段，确保它们是可被 Predicate 解析的基础类型。
- 实战中容易踩的坑 ：@Model 里的属性如果是自定义类型（比如示例中的 TripCollection 枚举），必须显式实现 Codable 协议，否则 SwiftData 无法将其序列化到数据库列中，会直接抛出编译错误。
- 已有项目的迁移策略 ：WWDC 期间不要急着把新 API 合入主分支。建一个 wwdc26 experiment 分支，把 SOTU 里提到的新特性（比如新的 Swift 并发模型或 SwiftUI 宏）在隔离环境里跑通。等 Xcode 正式版（通常是 9 月）发布后再做实际迁移。
- 新项目的采用建议 ：如果你刚好在 WWDC 后启动新项目，直接用上最新版的 Swift 和 Xcode beta。但切记，UI 层可以用最新的 SwiftUI 特性，底层数据持久化和网络层尽量用成熟方案（如 CoreData/URLSession），beta 版的底层框架往往在 Beta 3 之后才会稳定。
- 实战中容易踩的坑 ：看 Session 视频时，千万别只看中文字幕。很多关键的 API 命名和参数类型，字幕翻译会丢失上下文。遇到听不懂的地方，直接切到英文 CC 字幕，或者去 Apple Developer 网站看 Session 的 Text Transcript（文字版），Cmd+F 搜索 API 名字最准。
- HTTP 网络请求继续使用 URLSession，不需要迁移到 Network framework。

## 反模式与坑

- HistoryObserver 的 eventCounter ：Apple 没有给历史记录搞复杂的回调，而是暴露了一个简单的递增计数器 eventCounter，配合 fetchHistory() 使用，这种 "拉" 而不是 "推" 的设计大大降低了状态同步的复杂度。
- ObservationTracking.Token 的生命周期 ：这次 Session 反复强调要把 token 存起来，这暗示了 Swift Observation 框架底层的监听机制是弱引用的，忘记存 token 将是未来一年 Swift 论坛里最常见的 Bug 提问。
- Section 的底层实现 ： trips.sections 返回的集合直接实现了 RandomAccessCollection，这意味着在 SwiftUI 里嵌套 ForEach 时，性能和自己手写 Dictionary 分组没有区别，Apple 在底层做了优化。
- 绝对不能
- 内联缩略图数据 ：示例中将 thumbnailData: Data? 直接存入数据库，而不是只存文件路径。这避免了文件被系统清理或移动导致路径失效的问题，对于小体积图片来说，读取效率反而更高。
- FetchDescriptor 的 fetchLimit ：在首页展示“最近旅行”时，使用了 fetchLimit: 5。这是一个极其好用的内存保护机制，直接限制底层 SQL 拉取的条数，避免一次性把几千条数据全加载到内存里。
- 运行时错误暴露 ：Session 提到了使用 SwiftUI view modifiers 来捕获和展示 SwiftData 的运行时错误（如数据库损坏或 Schema 迁移失败），这在以前只能靠 do catch 盲猜，现在有了更优雅的 UI 降级方案。
- Clarus the Dogcow 回归 ：Apple 居然把远古 Mac 时代的吉祥物 Dogcow 做成了贴纸，老 Mac 开发者看到估计会泪目，记得去 App 里领。

## 高频主题

`SwiftData` (3)、`SwiftUI` (2)、`系统服务` (2)、`ModelResultsObserver` (1)、`Codable` (1)、`Observation` (1)、`Data Modeling` (1)、`@Query` (1)、`Persistence` (1)、`WWDC26` (1)、`Group Labs` (1)、`Developer App` (1)、`EventKit` (1)、`URLSession` (1)、`网络` (1)、`HTTP` (1)、`Swift Concurrency` (1)、`隐私` (1)

## 关键 Session

- [WWDC26-274] SwiftData 的新功能：这场 Session 最值得关注的一件事是：SwiftData 终于把数据监听能力从 SwiftUI 视图里剥离出来了，ModelResultsObserver 让你能在纯 ViewModel 或后台服务里优雅地响应数据库变化，不用再写恶心的 workaround。
- [WWDC26-275] 跟随编程：使用 SwiftData 添加持久化功能：这场 Session 最值得关注的一件事是：SwiftData 迁移绝不是无脑加 @Model 宏，它强迫你重构底层数据结构（比如把 Enum 拍平成 Class 继承），并且苹果终于用全新的 withContinuousObservation API 解决了 @Model 里 didSet 失效的痛点。
- [WWDC26-394] 为 WWDC26 做好准备：这场 Session 最值得关注的一件事是：Apple 正在用 Group Labs（小组实验室）全面替代传统的 1 on 1 Labs，这意味着你在 WWDC 期间想白嫖 Apple 工程师帮你单对单 debug 的机会变少了，但“围观”别人踩坑的机会变多了。
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
