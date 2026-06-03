# App Distribution

## 领域判断

App Store、TestFlight、签名、审核与分发。本领域覆盖 57 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **App Store & Distribution**：Cloud Signing 终于让你不用再管本地证书和 provisioning profile 的同步问题——私钥存在 Apple 服务器上，团队成员谁都能签名。；如果你的教育 App 是基于文档的（如笔记、练习册），ClassKit 的新文件集成让学生在 Schoolwork 中直接打开你的文件，完成后自动汇报进度——不需要在两个 App 之间切换。；macOS Monterey 的公证（Notarization）流程从"提交等几分钟查邮件"简化成了"一条命令搞定"——notarytool 替代了 altool，支持提交、等待和装订（Staple）一步完成。 来源：[WWDC21-10204]、[WWDC21-10257]、[WWDC21-10261]、[WWDC20-10118]
- **App Store, Distribution & Marketing**：Offer code 终于不再局限于自动续期订阅——消耗品、非消耗品、非续期订阅现在都能用 offer code 了，这对做促销活动和用户召回来说是一个被低估的变化。；App Analytics 终于补上了付费用户转化漏斗和订阅留存的完整分析能力——如果你之前只能看 proceeds 和 downloads，现在能看清每个环节到底差在哪了。；等了好几年，App Store Connect 终于有了 Webhook 和 Build Upload API——CI/CD 里最缺失的那一环现在补上了。 来源：[WWDC25-241]、[WWDC25-252]、[WWDC25-324]、[WWDC25-328]
- **App Store Distribution & Marketing**：iOS 18 终于把已完成的消耗品交易纳入交易历史 API，同时新增货币和价格字段、win back offers 和更强大的 StoreKit Views，这三个改动组合起来让内购管理从"头疼"变成了"基本不用操心"。；如果你在做什么内购系统却还没用上 App Store Server API 和 Server Library，这个 session 就是你的必读清单——尤其是退款决策和订阅续期的新能力，直接关系到钱。；今年 App Store Connect 最重要的更新是 Featuring Nominations——你终于可以主动告诉 App Store 编辑团队"我的 App 要更新了，请考虑推荐"，而不是被动等待被发现。 来源：[WWDC24-10061]、[WWDC24-10062]、[WWDC24-10063]、[WWDC24-10110]
- **Developer Tools**：App Store 推广购买、Billing Issue 消息、SHA 256 迁移——StoreKit 2 今年带来了多项实用更新。；这是一场信息密度极高的全景扫描——Swift 并发、Xcode Cloud、StoreKit 2、SharePlay 四大主题构成了 2021 年 Apple 开发者生态的骨架。；Xcode 13 的 Organizer 终于把崩溃分析、用户反馈和指标数据放在了一个地方——你不用再在 App Store Connect 网页和邮件之间来回跳了。 来源：[WWDC23-10140]、[WWDC21-102]、[WWDC21-10203]、[WWDC21-10205]
- **应用服务**：Offer code 终于不再局限于自动续期订阅——消耗品、非消耗品、非续期订阅现在都能用 offer code 了，这对做促销活动和用户召回来说是一个被低估的变化。；appTransactionId 终于统一了所有交易对象的标识符体系——如果你还在用 originalTransactionId 做跨产品的用户关联，是时候迁移了。；On Demand Resources 要退役了，Background Assets 的 Managed 模式接管——Apple 帮你托管 200GB 的资源包，系统自动下载、更新、压缩，你甚至不需要写 downloader extension。 来源：[WWDC25-241]、[WWDC25-249]、[WWDC25-325]
- **Task**：ASC 今年是「功能大年」——Build Upload 可视化、App Store Tags、Custom Product Page 关键词、Offer Codes 全品类、Accessibility Nutrition Labels，每一项都直接影响你的上架效率和获客能力。；StoreKit 2 是 IAP（In App Purchase）开发体验的全面翻新 —— 用 async/await + Swift 原生 API 替代了 delegate 回调地狱，用 JWS 签名的事务替代了不可读的收据（Receipt），整个内购模块的代码量能砍掉三分之二。 来源：[WWDC25-328]、[WWDC21-10114]
- **365 天的预购窗口期**：App Store 预订购终于支持按地区独立管理了——你可以先在一个地区发布 App，然后在其他地区开放预订购，这对灰度发布和分地区运营策略来说是关键能力。 来源：[WWDC23-10015]

## API 演进时间线

- **WWDC25**：8 场，代表来源：[WWDC25-202]、[WWDC25-241]、[WWDC25-249]、[WWDC25-252]、[WWDC25-324]
- **WWDC24**：5 场，代表来源：[WWDC24-10061]、[WWDC24-10062]、[WWDC24-10063]、[WWDC24-10110]、[WWDC24-10214]
- **WWDC23**：8 场，代表来源：[WWDC23-10013]、[WWDC23-10014]、[WWDC23-10015]、[WWDC23-10061]、[WWDC23-10117]
- **WWDC22**：7 场，代表来源：[WWDC22-10007]、[WWDC22-10039]、[WWDC22-10040]、[WWDC22-10043]、[WWDC22-10044]
- **WWDC21**：15 场，代表来源：[WWDC21-10012]、[WWDC21-10013]、[WWDC21-10114]、[WWDC21-10115]、[WWDC21-10170]
- **WWDC20**：14 场，代表来源：[WWDC20-10004]、[WWDC20-10118]、[WWDC20-10120]、[WWDC20-10147]、[WWDC20-10204]

## 决策启发式

- 新项目统一使用 appTransactionId 作为交易关联的主键，避免混用多种标识符导致的逻辑复杂化。
- 使用 App Store Server Library 的 JWS 签名生成器，不要自己实现签名逻辑。
- 对所有产品类型的退款通知都实现处理逻辑，包括 non consumable 和 non renewing subscription。
- 在服务端维护准确的消费状态，以便在 CONSUMPTION REQUEST 时提供精确的 consumptionPercentage。
- V1 的 Send Consumption Information 端点已废弃，新集成直接用 V2。
- 定期检查 App Store Server API 的 GitHub 仓库，Apple 持续更新 server library。
- 定期检查 Download to Paid Conversion 的 benchmark，如果低于 50th percentile，优先优化转化漏斗而不是拉新。
- 用 custom product page 过滤 cohort 数据，识别不同获客渠道的用户价值差异，指导营销预算分配。
- 关注 Subscription Retention 的 6 个月留存率，如果低于 peer group，考虑引入 intro offer 或改善 onboarding。
- 对每个 offer 单独追踪转化率和留存率，确认 offer 吸引的是高价值用户而不是薅羊毛用户。

## 反模式与坑

- Live Activity 支持通过信息分享航班状态，这对出行场景是社交属性的补完，但实现上依赖 Widget Extension，项目配置别忘了。
- 登机牌现在集成了 Maps 机场导航和 Find My 行李追踪，虽然不是开发者直接控制的功能，但如果你的登机牌语义标签够完整，这些系统能力会自动解锁。
- upcomingPassInformation 中的日期必须按时间顺序排列，否则 Wallet 界面会乱序展示——这个没有校验提示，出了 bug 很难排查。
- appAccountToken 现在也出现在 RenewalInfo 中，方便你在续期时关联用户账号。
- UI context purchase 方法（iOS 18.2+）要求指定购买发起的 UIViewController 或 NSWindow，StoreKit 视图自动处理。
- 高级商务 API（Advanced Commerce API）新增了 AdvancedCommerceProduct 类型，支持大型内容目录和创作者体验。
- Get App Transaction Info 端点允许直接在服务端获取 AppTransaction 信息，不需要依赖设备——这对服务端驱动的业务逻辑校验非常有用。
- JWS introductory offer 签名允许按用户、按交易自定义 introductory offer 资格，比以前的全局资格控制更精细。

## 高频主题

`App Store, Distribution & Marketing` (6)、`应用服务` (3)、`Wallet` (1)、`PassKit` (1)、`Apple Pay` (1)、`Live Activity` (1)、`图形与游戏` (1)、`系统服务` (1)、`Swift` (1)、`开发工具` (1)

## 关键 Session

- [WWDC25-202] Wallet 新特性：如果你做票务或航空 App，今年 Wallet 的更新能让你砍掉一半的推送逻辑和通行证管理代码——前提是你愿意把航班状态追踪这类核心体验交给 Apple 的系统服务。
- [WWDC25-241] StoreKit 与内购新特性：Offer code 终于不再局限于自动续期订阅——消耗品、非消耗品、非续期订阅现在都能用 offer code 了，这对做促销活动和用户召回来说是一个被低估的变化。
- [WWDC25-249] App Store 服务端 API 深度解析：appTransactionId 终于统一了所有交易对象的标识符体系——如果你还在用 originalTransactionId 做跨产品的用户关联，是时候迁移了。
- [WWDC25-252] 用 App Analytics 优化变现策略：App Analytics 终于补上了付费用户转化漏斗和订阅留存的完整分析能力——如果你之前只能看 proceeds 和 downloads，现在能看清每个环节到底差在哪了。
- [WWDC25-324] 用 App Store Connect API 自动化你的开发流程：等了好几年，App Store Connect 终于有了 Webhook 和 Build Upload API——CI/CD 里最缺失的那一环现在补上了。
- [WWDC25-325] 探索 Apple 托管的 Background Assets：On Demand Resources 要退役了，Background Assets 的 Managed 模式接管——Apple 帮你托管 200GB 的资源包，系统自动下载、更新、压缩，你甚至不需要写 downloader extension。
- [WWDC25-328] App Store Connect 今年有什么新东西：ASC 今年是「功能大年」——Build Upload 可视化、App Store Tags、Custom Product Page 关键词、Offer Codes 全品类、Accessibility Nutrition Labels，每一项都直接影响你的上架效率和获客能力。
- [WWDC25-344] Record, replay, and review: UI automation with Xcode：Xcode 的 UI 自动化工作流终于形成闭环了 Record 录制交互生成代码，Test Plan 配置多语言/多设备回放，Xcode Cloud 云端执行，Test Report 带视频回放和故障点定位。关键是 accessibility 做好了，UI 自动化自然就好用了。
- [WWDC24-10061] StoreKit 和应用内购买的新变化：iOS 18 终于把已完成的消耗品交易纳入交易历史 API，同时新增货币和价格字段、win back offers 和更强大的 StoreKit Views，这三个改动组合起来让内购管理从"头疼"变成了"基本不用操心"。
- [WWDC24-10062] 深入探索 App Store Server API 与内购服务端集成：如果你在做什么内购系统却还没用上 App Store Server API 和 Server Library，这个 session 就是你的必读清单——尤其是退款决策和订阅续期的新能力，直接关系到钱。
- [WWDC24-10063] App Store Connect 新功能一览：今年 App Store Connect 最重要的更新是 Featuring Nominations——你终于可以主动告诉 App Store 编辑团队"我的 App 要更新了，请考虑推荐"，而不是被动等待被发现。
- [WWDC24-10110] 实现 App Store 订阅优惠：Win back Offers 是今年订阅体系最重要的新增：Apple 替你筛选流失用户、替你分发优惠卡片，你只需要在 App Store Connect 里配规则、在应用里处理兑换逻辑。
- [WWDC24-10214] 充分发挥 Apple Pencil 的能力：PKToolPicker 今年开放了自定义工具的能力，你的 App 终于可以把画笔、橡皮、印章等自定义绘制工具直接嵌入系统工具栏，和 PencilKit 原生工具混排。
- [WWDC23-10013] 认识 StoreKit 的 SwiftUI 视图：StoreKit 终于有了原生的 SwiftUI 视图，几行代码就能搭建完整的内购商店界面。
- [WWDC23-10014] App Store 定价新变化：App Store 推出了自上线以来最大规模的定价能力升级——900 个价格点、175 个区域中任选基准区域、自动汇率和税率调整，加上定时调价功能，让全球定价管理从噩梦变成了配置问题。
- [WWDC23-10015] App Store 预订购的新功能：App Store 预订购终于支持按地区独立管理了——你可以先在一个地区发布 App，然后在其他地区开放预订购，这对灰度发布和分地区运营策略来说是关键能力。
- [WWDC23-10061] 用数字签名验证应用依赖的完整性：Xcode 15 内置了依赖签名自动验证功能——当你引入的第三方 xcframework 被篡改或签名身份变更时，构建会直接报错拦截，供应链安全从此不需要手动检查了。
- [WWDC23-10117] App Store Connect 的新功能：今年的 App Store Connect 更新覆盖了整个 App 生命周期——从 StoreKit for SwiftUI 的几行代码接入内购，到 900 个价格点位的灵活定价，到 TestFlight 的家庭共享测试，再到 xrOS 的隐私数据类型，每个环节都有实质性改进。
