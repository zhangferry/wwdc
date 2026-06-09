# Privacy & Security

## 领域判断

隐私、安全、权限、认证与数据最小化。本领域覆盖 60 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **Privacy & Security**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：充分利用 App Attest 保护你的 App 免遭欺诈和未经授权的修改。探索攻击者如何利用修改后的 App 来伪造数据并绕过安全检查，以及 App Attest 如何防御这些威胁。了解如何生成和管理与安全隔区绑定的 App Attest 密钥，对证明和断言进行验证，并利用欺诈指标来检测滥用行为。探索适合各个 Apple 平台的最佳做法，包括 iOS 27 中助你加强验证的新信号。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解声明式设备管理、Apple 商务和 Apple 校园教务管理平台的最新进展。探索这些优化升级如何帮助你简化部署、增强安全性，并提升受管理设备的用户体验。你还将了解到运用这些新功能的实用技巧，无论你是想构建设备管理解决方案，还是要管理企业设备群，都能从中受益。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，与 Apple 工程师和设计师一起深入探索 WWDC26。在这个以隐私和安全为主题的活动中… 来源：[WWDC26-201]、[WWDC26-206]、[WWDC26-8009]、[WWDC24-10123]
- **隐私与安全**：Wi Fi Aware 是 Apple 官方的 P2P 直连方案 不依赖路由器，不中断现有 Wi Fi 连接，高吞吐低延迟，配合 DeviceDiscoveryUI 和 AccessorySetupKit 做发现配对，用 Network framework 建连接。做本地文件传输、屏幕共享、配件控制的开发者终于有了一等公民 API。；UIKit 终于原生支持 Swift Observation 了——在 layoutSubviews 里引用 @Observable 对象，UIKit 会自动追踪依赖并在属性变化时精确失效视图，不再需要手动调 setNeedsLayout。；这场 Session 不是讲某个新 API，而是一套从规划到部署的隐私工程方法论——对有上架需求的团队来说，它是 App Store 审核合规的实操指南。 来源：[WWDC25-228]、[WWDC25-243]、[WWDC25-246]、[WWDC25-279]
- **Swift & UI**：UICollectionView 在 iOS 14 中迎来了它历史上最大的 API 更新：Compositional Layout 支持列表布局、Diffable Data Source 支持重新排序、Cell Registration 大幅简化，这些变化让你几乎可以扔掉所有的 UICollectionView 扩展库。；iOS 14 把 AutoFill 从密码扩展到了所有类型的表单字段——姓名、邮箱、电话、信用卡、地址，甚至一次性验证码（OTP）。如果你的 App 有注册或支付流程，正确配置 AutoFill 能把用户填表时间缩短一半。 来源：[WWDC20-10097]、[WWDC20-10115]
- **System Frameworks**：iOS 18 把联系人权限从"全部给"或"全不给"改成了"按需给"，ContactAccessButton 让你在搜索流中逐个授权联系人，用户体验和隐私保护同时升级。；如果你还在用 URLSession 做"万能"网络请求，这个 Session 会告诉你如何利用 Network.framework 的 TLS 1.3、Multipath TCP、IPv6 Happy Eyeballs 等能力来打造更快更安全的网络层。 来源：[WWDC24-10121]、[WWDC20-10111]
- **系统服务**：如果你的 App 有用户年龄分级的需求——社交、游戏、内容平台——Declared Age Range API 就是 Apple 给出的官方答案，别再自己做生日输入框了。；量子计算还没来，但"先收集后解密"攻击已经在发生——iOS 26 默认开启量子安全 TLS，CryptoKit 新增后量子加密 API，你没借口再拖了。 来源：[WWDC25-299]、[WWDC25-314]
- **ABM/ASM API 的意义被低估了**：这是一场面向 IT 管理员和 MDM 开发者的"解气"更新——ABM/ASM 终于有了 API，设备管理迁移不再需要全盘擦除，Vision Pro 支持 Return to Service，而 Tap to Login 用 iPhone/Apple Watch 一碰登录 Mac 的体验确实很酷。 来源：[WWDC25-258]
- **Accessory Configuration 的安全模型**：Nearby Interaction 框架支持第三方 UWB（Ultra Wideband）配件意味着你的 App 可以精确知道"钥匙在哪里、钱包在哪里、宠物在哪里"——精度达到厘米级，这比 BLE 的"大概在 3 米内"强了一个维度。 来源：[WWDC21-10165]

## API 演进时间线

- **WWDC26**：3 场，代表来源：[WWDC26-201]、[WWDC26-206]、[WWDC26-8009]
- **WWDC25**：11 场，代表来源：[WWDC25-203]、[WWDC25-208]、[WWDC25-228]、[WWDC25-243]、[WWDC25-246]
- **WWDC24**：4 场，代表来源：[WWDC24-10121]、[WWDC24-10123]、[WWDC24-10125]、[WWDC24-102]
- **WWDC23**：4 场，代表来源：[WWDC23-10040]、[WWDC23-10053]、[WWDC23-10060]、[WWDC23-10263]
- **WWDC22**：9 场，代表来源：[WWDC22-10022]、[WWDC22-10079]、[WWDC22-10092]、[WWDC22-10096]、[WWDC22-101]
- **WWDC21**：12 场，代表来源：[WWDC21-10033]、[WWDC21-10085]、[WWDC21-10089]、[WWDC21-10096]、[WWDC21-10102]
- **WWDC20**：17 场，代表来源：[WWDC20-10047]、[WWDC20-10097]、[WWDC20-10110]、[WWDC20-10111]、[WWDC20-10115]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 先检查设备能力 。使用 WACapabilities.supportedFeatures 确认设备支持 Wi Fi Aware，再启用相关功能。
- 配对完成后用 WAPairedDevice.allDevices 监听配对设备列表变化 。用户可能在系统设置中删除配对设备，你的 app 需要响应这个变化。
- 连接建立后及时停止 listener 和 browser 。持续运行会消耗无线资源和电量，只在需要时开启。
- 使用 Traffic Service Class 区分数据优先级 。低优先级数据用 background class，避免干扰其他流量。视频流用 interactive video class。
- 在真实 Wi Fi 环境中测试 。Wi Fi 干扰、信号强度变化、设备能力差异都会影响实际性能。用 performanceReport 监控连接质量。
- 在规划阶段用四大支柱（数据最小化、设备端处理、透明与控制、安全保护）定义隐私保证声明，再从声明推导工程需求。
- 优先使用系统提供的 picker（PhotosPicker、ContactPicker）替代广权限 API，避免不必要的权限弹窗。

## 反模式与坑

- ManagedApp 框架和 ABM/ASM 的集成是双向的：你在代码里加一个带描述的配置项，ABM 管理界面自动生成对应的表单字段，不需要 IT 管理员手动配置 key value。
- 框架对 App Config 的替代不是强制的，两种方案可以共存，但长期来看 ManagedApp 会是 Apple 推荐的方向。
- 证书类型的配置支持自动续期，但具体行为取决于 MDM 服务器的实现，这一点 Session 里没有展开讲。
- 运动恢复指数（Recovery Index）是配合 Apple Watch 新传感器的数据类型，适合健身 App 从"记录训练"升级到"指导恢复"，但数据源目前主要依赖 Apple Watch。
- HKAuthorizationRequest 新增了按时间段授权的能力，用户可以只授权最近三个月的数据而不是全部历史，这对隐私敏感型用户是个大加分。
- HealthKitUI 仅在 iOS 19+ 可用，没有向下兼容方案，如果你的 min deployment target 还在 iOS 17，这个框架暂时用不了。
- Apple 提供了 Wi Fi Aware 配件设计指南（Accessory Design Guidelines），硬件制造商应遵循该指南确保与 Apple 设备的互操作性。
- Sample app 展示了不同性能配置对实际行为的影响，建议下载体验。

## 高频主题

`隐私与安全` (7)、`Privacy & Security` (3)、`系统服务` (3)、`SwiftUI` (2)、`ManagedApp` (1)、`Enterprise` (1)、`MDM` (1)、`Security` (1)、`HealthKit` (1)、`健康` (1)、`隐私` (1)、`数据共享` (1)、`商业与教育` (1)、`应用服务` (1)、`Swift` (1)

## 关键 Session

- [WWDC26-201] 使用 App Attest 保护你的 App：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：充分利用 App Attest 保护你的 App 免遭欺诈和未经授权的修改。探索攻击者如何利用修改后的 App 来伪造数据并绕过安全检查，以及 App Attest 如何防御这些威胁。了解如何生成和管理与安全隔区绑定的 App Attest 密钥，对证明和断言进行验证，并利用欺诈指标来检测滥用行为。探索适合各个 Apple 平台的最佳做法，包括 iOS 27 中助你加强验证的新信号。
- [WWDC26-206] Apple 设备管理和身份管理方面的新动向：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解声明式设备管理、Apple 商务和 Apple 校园教务管理平台的最新进展。探索这些优化升级如何帮助你简化部署、增强安全性，并提升受管理设备的用户体验。你还将了解到运用这些新功能的实用技巧，无论你是想构建设备管理解决方案，还是要管理企业设备群，都能从中受益。
- [WWDC26-8009] 隐私和安全小组实验室：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，与 Apple 工程师和设计师一起深入探索 WWDC26。在这个以隐私和安全为主题的活动中，你可以提出问题、获取建议，并实时关注围绕大会一周的相关重磅发布展开的精彩讨论。活动语言为英语。
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
- [WWDC24-102] 平台技术综述：这是 WWDC 2024 技术层面的"全局地图"——Apple Intelligence 的端侧+云端双轨架构、Private Cloud Compute 的安全模型、以及全平台 API 的关键更新都在这里集中展示，如果你只看一场 Session 来把握今年方向，就是这场。
