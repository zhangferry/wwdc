# Privacy & Security

## 领域判断

隐私、安全、权限、认证与数据最小化。本领域覆盖 61 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Privacy & Security**：iOS 18 用"进程外选择器"（out of process picker）的思路把隐私控制做到了极致——你的 App 永远看不到完整数据，只能拿到用户主动选中的那一条。；Automatic passkey upgrades 让你在零用户感知的情况下把现有密码账号升级为 passkey，这是推动行业消灭密码的最关键一步。；如果你的 App 有积分、内购或任何有价值的数字资产，App Attest 是防止篡改和伪造请求的必备防线——它在设备上生成不可伪造的断言（Assertion），让你的服务器可以验证请求确实来自一个未被篡改的 App。 来源：[WWDC24-10123]、[WWDC24-10125]、[WWDC21-10244]、[WWDC20-10110]
- **隐私与安全**：Wi Fi Aware 是 Apple 官方的 P2P 直连方案 不依赖路由器，不中断现有 Wi Fi 连接，高吞吐低延迟，配合 DeviceDiscoveryUI 和 AccessorySetupKit 做发现配对，用 Network framework 建连接。做本地文件传输、屏幕共享、配件控制的开发者终于有了一等公民 API。；UIKit 终于原生支持 Swift Observation 了——在 layoutSubviews 里引用 @Observable 对象，UIKit 会自动追踪依赖并在属性变化时精确失效视图，不再需要手动调 setNeedsLayout。；这场 Session 不是讲某个新 API，而是一套从规划到部署的隐私工程方法论——对有上架需求的团队来说，它是 App Store 审核合规的实操指南。 来源：[WWDC25-228]、[WWDC25-243]、[WWDC25-246]、[WWDC25-279]
- **Security**：✅ macOS 的考试模式（Assessment Mode）终于从“粗暴锁死全屏”进化到了“系统级精细化管控”，教育类 App 不用再自己写脆弱的防作弊拦截代码了。；Apple 终于把“防诈骗/防胁迫”做成了系统级 API，金融和社交 App 以后不用自己瞎猜用户是不是被洗脑了。；如果你在做企业应用，现在终于可以扔掉自己写的那套 MDM 配置解析代码了。 来源：[WWDC26-230]、[WWDC26-379]、[WWDC25-203]
- **macOS**：这场 Session 最值得关注的一件事是：Apple 终于把 App Attest 搬上了 macOS 27，并引入了基于 30 天内唯一密钥数量的 Fraud Metric（欺诈指标），这意味着靠改机软件和设备农场刷接口的黑产要迎来降维打击了。；✅ macOS 的考试模式（Assessment Mode）终于从“粗暴锁死全屏”进化到了“系统级精细化管控”，教育类 App 不用再自己写脆弱的防作弊拦截代码了。 来源：[WWDC26-201]、[WWDC26-230]
- **MDM**：✅ 声明式管理（DDM）在 macOS 27 彻底终结了传统配置描述文件，Platform SSO 新增的系统级 Web 视图让企业定制登录界面终于不用再跟系统权限死磕了。；如果你在做企业应用，现在终于可以扔掉自己写的那套 MDM 配置解析代码了。 来源：[WWDC26-206]、[WWDC25-203]
- **Swift & UI**：UICollectionView 在 iOS 14 中迎来了它历史上最大的 API 更新：Compositional Layout 支持列表布局、Diffable Data Source 支持重新排序、Cell Registration 大幅简化，这些变化让你几乎可以扔掉所有的 UICollectionView 扩展库。；iOS 14 把 AutoFill 从密码扩展到了所有类型的表单字段——姓名、邮箱、电话、信用卡、地址，甚至一次性验证码（OTP）。如果你的 App 有注册或支付流程，正确配置 AutoFill 能把用户填表时间缩短一半。 来源：[WWDC20-10097]、[WWDC20-10115]
- **System Frameworks**：iOS 18 把联系人权限从"全部给"或"全不给"改成了"按需给"，ContactAccessButton 让你在搜索流中逐个授权联系人，用户体验和隐私保护同时升级。；如果你还在用 URLSession 做"万能"网络请求，这个 Session 会告诉你如何利用 Network.framework 的 TLS 1.3、Multipath TCP、IPv6 Happy Eyeballs 等能力来打造更快更安全的网络层。 来源：[WWDC24-10121]、[WWDC20-10111]

## API 演进时间线

- **WWDC26**：4 场，代表来源：[WWDC26-201]、[WWDC26-206]、[WWDC26-230]、[WWDC26-379]
- **WWDC25**：11 场，代表来源：[WWDC25-203]、[WWDC25-208]、[WWDC25-228]、[WWDC25-243]、[WWDC25-246]
- **WWDC24**：4 场，代表来源：[WWDC24-10121]、[WWDC24-10123]、[WWDC24-10125]、[WWDC24-102]
- **WWDC23**：4 场，代表来源：[WWDC23-10040]、[WWDC23-10053]、[WWDC23-10060]、[WWDC23-10263]
- **WWDC22**：9 场，代表来源：[WWDC22-10022]、[WWDC22-10079]、[WWDC22-10092]、[WWDC22-10096]、[WWDC22-101]
- **WWDC21**：12 场，代表来源：[WWDC21-10033]、[WWDC21-10085]、[WWDC21-10089]、[WWDC21-10096]、[WWDC21-10102]
- **WWDC20**：17 场，代表来源：[WWDC20-10047]、[WWDC20-10097]、[WWDC20-10110]、[WWDC20-10111]、[WWDC20-10115]

## 决策启发式

- 已有项目的迁移策略 ：立刻停止在新的 macOS 27 部署中使用 Configuration Profiles 管理应用配置和隐私权限。把现有的 PPPC 和 App 配置全面翻译成 DDM 的 app.settings 和 safari.settings。如果你的 MDM 服务器还在用轮询（Polling）查设备状态，赶紧重构成事件驱动架构，订阅 DDM 的状态通道。
- 新项目的采用建议 ：IdP 开发者赶紧接入 Platform SSO 的 Web 视图 API。把那些花里胡哨的 MFA 流程、条件访问判断直接搬进系统底层的 Web 视图里，用户体验会比你自己画原生 UI 顺滑得多，而且天然防钓鱼。
- 实战中容易踩的坑 ：DDM 的凭证管理现在是多对多关系了。更新证书时，千万别再像以前那样把整个巨大的描述文件重新推一遍。直接在 DDM 里更新对应的 Asset（资产），设备会自动把新证书同步到所有引用它的配置里，能省下巨量的网络带宽。
- 已有项目的迁移策略 ：赶紧删掉你项目里那些用 CGEventTap 拦截键盘鼠标、用隐藏窗口遮挡 Dock 的“祖传代码”。把这些逻辑全部替换成 AEAssessmentConfiguration。自己造的轮子不仅容易在 macOS 大版本更新时崩溃，还会被系统判定为恶意行为。
- 新项目的采用建议 ：遵循“最小限制原则”。别一上来就把所有 allows... 都设为 false。先跑通一个宽松的版本，再根据实际作弊手段慢慢收紧权限。过度限制会导致考生的设备出现各种诡异的系统级 Bug。
- 实战中容易踩的坑 ：一定要注册 Session 转换的回调（Session transition callbacks）。考试结束或意外中断时，系统会退出 Assessment Mode，你的 App 必须在这个回调里清理状态，而不是等 App 被系统强杀。
- 先检查设备能力 。使用 WACapabilities.supportedFeatures 确认设备支持 Wi Fi Aware，再启用相关功能。
- 配对完成后用 WAPairedDevice.allDevices 监听配对设备列表变化 。用户可能在系统设置中删除配对设备，你的 app 需要响应这个变化。
- 连接建立后及时停止 listener 和 browser 。持续运行会消耗无线资源和电量，只在需要时开启。
- 使用 Traffic Service Class 区分数据优先级 。低优先级数据用 background class，避免干扰其他流量。视频流用 interactive video class。

## 反模式与坑

- iOS 27 新增 Authenticator data Extensions ：现在能直接拿到 App 的 Launch validation category（启动验证类别）和 Bundle version，服务端终于能精准识别出请求是来自 TestFlight 还是 App Store 正式版了。
- isSupported 的逆向思维 ：Apple 明确建议把 isSupported == false 当作 Fraud signal（欺诈信号），这在越狱检测库满天飞的今天，算是官方给的最稳妥的“照妖镜”。
- 密钥不跟随 iCloud 备份 ：App Attest 的密钥是和设备硬件绑定的，用户从 iCloud 备份恢复新手机时，旧密钥直接作废，客户端必须老老实实重新走一遍生成和 Attest 流程。
- Managed Migration（托管迁移） ：换 Mac 时，Migration Assistant（迁移助理）现在受 DDM 控制，能保留 MDM 注册和设置，IT 管理员可以精确控制哪些文件和账户能带到新电脑上。
- Shared iPad 的 Authenticated Guest Mode（认证访客模式） ：医疗和零售场景的福音，临时会话退出即焚，现在不仅支持联合认证，还能直接用来解锁 FileVault 加密的 Mac。
- Classroom App 的 Guided Browsing（引导浏览） ：老师能把学生死死按在某个网页的单个 Tab 里，限制网站内外导航，上课摸鱼彻底成为历史。
- 文件系统沙盒化 ：通过 allowedDirectoriesAndFiles 可以限制 Finder 和 Save Panel，让学生只能把考试草稿保存到特定的 Documents 子目录，碰不到桌面和其他文件。
- 输入法限制 ：新增了对 allowsStructuralInput（结构性输入）和 allowsEmojiKeyboard（表情符号键盘）的控制，防止学生通过拆字或表情包传递暗号。

## 高频主题

`隐私与安全` (7)、`Security` (3)、`系统服务` (3)、`macOS` (2)、`MDM` (2)、`SwiftUI` (2)、`App Attest` (1)、`DeviceCheck` (1)、`Secure Enclave` (1)、`Fraud Metric` (1)、`Declarative Management` (1)、`Platform SSO` (1)、`Endpoint Security` (1)、`Identity` (1)、`AutomaticAssessmentConfiguration` (1)、`Accessibility` (1)、`Education` (1)、`Trust Insights` (1)

## 关键 Session

- [WWDC26-201] 使用 App Attest 保护你的 App：这场 Session 最值得关注的一件事是：Apple 终于把 App Attest 搬上了 macOS 27，并引入了基于 30 天内唯一密钥数量的 Fraud Metric（欺诈指标），这意味着靠改机软件和设备农场刷接口的黑产要迎来降维打击了。
- [WWDC26-206] Apple 设备管理和身份管理方面的新动向：✅ 声明式管理（DDM）在 macOS 27 彻底终结了传统配置描述文件，Platform SSO 新增的系统级 Web 视图让企业定制登录界面终于不用再跟系统权限死磕了。
- [WWDC26-230] macOS 评估体验的新动向：✅ macOS 的考试模式（Assessment Mode）终于从“粗暴锁死全屏”进化到了“系统级精细化管控”，教育类 App 不用再自己写脆弱的防作弊拦截代码了。
- [WWDC26-379] 了解 Trust Insights：Apple 终于把“防诈骗/防胁迫”做成了系统级 API，金融和社交 App 以后不用自己瞎猜用户是不是被洗脑了。
- [WWDC25-203] 认识 ManagedApp 框架：如果你在做企业应用，现在终于可以扔掉自己写的那套 MDM 配置解析代码了。
- [WWDC25-208] HealthKit 新特性：HealthKitUI 的推出比新增的情绪数据类型影响更大——它宣告 Apple 认为健康数据可视化应该是系统级能力，不是每个 App 自己用 Charts 库画的活儿。
- [WWDC25-228] Supercharge device connectivity with Wi-Fi Aware：Wi Fi Aware 是 Apple 官方的 P2P 直连方案 不依赖路由器，不中断现有 Wi Fi 连接，高吞吐低延迟，配合 DeviceDiscoveryUI 和 AccessorySetupKit 做发现配对，用 Network framework 建连接。做本地文件传输、屏幕共享、配件控制的开发者终于有了一等公民 API。
- [WWDC25-243] UIKit 新特性：UIKit 终于原生支持 Swift Observation 了——在 layoutSubviews 里引用 @Observable 对象，UIKit 会自动追踪依赖并在属性变化时精确失效视图，不再需要手动调 setNeedsLayout。
- [WWDC25-246] 将隐私保护融入开发全流程：这场 Session 不是讲某个新 API，而是一套从规划到部署的隐私工程方法论——对有上架需求的团队来说，它是 App Store 审核合规的实操指南。
- [WWDC25-258] Apple 设备管理与身份认证年度更新：API 开放与 Tap to Login：这是一场面向 IT 管理员和 MDM 开发者的"解气"更新——ABM/ASM 终于有了 API，设备管理迁移不再需要全盘擦除，Vision Pro 支持 Return to Service，而 Tap to Login 用 iPhone/Apple Watch 一碰登录 Mac 的体验确实很酷。
- [WWDC25-279] Passkeys 新特性：Passkeys 的拼图终于补完了——从注册（Account Creation API）到维护（Signal API 同步凭证变更）到升级（零摩擦自动创建 passkey）到发现（well known 端点）再到迁移（凭证导入导出），全链路打通。这是对"密码该怎么死"这个问题最完整的回答。
- [WWDC25-293] Enhance child safety with PermissionKit：如果你的 app 有社交功能且用户包含未成年人，PermissionKit 是你今年必须接入的框架。它把"孩子想和某人聊天"这个请求，变成了一条 iMessage，父母直接在信息里批准或拒绝。整个流程优雅得不像 Apple 的 API（褒义）。
- [WWDC25-299] 在 App 中提供适龄体验：如果你的 App 有用户年龄分级的需求——社交、游戏、内容平台——Declared Age Range API 就是 Apple 给出的官方答案，别再自己做生日输入框了。
- [WWDC25-311] 安全地混合 C、C++ 和 Swift：Swift 终于给 C/C++ 指针互操作提供了「安全逃生通道」——通过注解让编译器帮你做 bounds 和 lifetime 检查，而不是靠人肉审计。
- [WWDC25-314] 提前应对量子安全加密：量子计算还没来，但"先收集后解密"攻击已经在发生——iOS 26 默认开启量子安全 TLS，CryptoKit 新增后量子加密 API，你没借口再拖了。
- [WWDC24-10121] 认识 ContactAccessButton：更精细的联系人权限控制：iOS 18 把联系人权限从"全部给"或"全不给"改成了"按需给"，ContactAccessButton 让你在搜索流中逐个授权联系人，用户体验和隐私保护同时升级。
- [WWDC24-10123] 隐私保护新动向：iOS 18 用"进程外选择器"（out of process picker）的思路把隐私控制做到了极致——你的 App 永远看不到完整数据，只能拿到用户主动选中的那一条。
- [WWDC24-10125] 用 Passkey 自动升级和凭证管理器简化登录：Automatic passkey upgrades 让你在零用户感知的情况下把现有密码账号升级为 passkey，这是推动行业消灭密码的最关键一步。
