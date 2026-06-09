# App Distribution

## 领域判断

App Store、TestFlight、签名、审核与分发。本领域覆盖 64 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **App Store & Distribution**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：通过在新位置展示相关图像和视频，重新构想你在 App Store 上推广 App 和游戏的方式。探索如何在 App Store 上的产品页面、搜索结果和 Apple Ads 广告系列中，利用新的视觉素材展示位置以更丰富生动的故事打动用户。了解如何使用全新的 Asset Library 将所有视觉素材汇于一处来简化管理，以及如何借助一款新工具在产品页面上线之前预览效果。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何利用 Retention Messaging 的强大功能，在用户取消订阅之前及时触达他们。了解如何在 App Store Connect 中设置这项功能并添加订阅优惠，同时利用 Retention Messaging API 推送实时消息和替代选项，从而鼓励用户持续订阅你的 App 或游戏。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索通过多席位购买扩大订阅用户群的两种新方法：群组购买允许单个订阅者购买多个席位，并直接… 来源：[WWDC26-205]、[WWDC26-309]、[WWDC26-391]、[WWDC26-8010]
- **App Store, Distribution & Marketing**：Offer code 终于不再局限于自动续期订阅——消耗品、非消耗品、非续期订阅现在都能用 offer code 了，这对做促销活动和用户召回来说是一个被低估的变化。；App Analytics 终于补上了付费用户转化漏斗和订阅留存的完整分析能力——如果你之前只能看 proceeds 和 downloads，现在能看清每个环节到底差在哪了。；等了好几年，App Store Connect 终于有了 Webhook 和 Build Upload API——CI/CD 里最缺失的那一环现在补上了。 来源：[WWDC25-241]、[WWDC25-252]、[WWDC25-324]、[WWDC25-328]
- **App Store Distribution & Marketing**：iOS 18 终于把已完成的消耗品交易纳入交易历史 API，同时新增货币和价格字段、win back offers 和更强大的 StoreKit Views，这三个改动组合起来让内购管理从"头疼"变成了"基本不用操心"。；如果你在做什么内购系统却还没用上 App Store Server API 和 Server Library，这个 session 就是你的必读清单——尤其是退款决策和订阅续期的新能力，直接关系到钱。；今年 App Store Connect 最重要的更新是 Featuring Nominations——你终于可以主动告诉 App Store 编辑团队"我的 App 要更新了，请考虑推荐"，而不是被动等待被发现。 来源：[WWDC24-10061]、[WWDC24-10062]、[WWDC24-10063]、[WWDC24-10110]
- **Developer Tools**：App Store 推广购买、Billing Issue 消息、SHA 256 迁移——StoreKit 2 今年带来了多项实用更新。；这是一场信息密度极高的全景扫描——Swift 并发、Xcode Cloud、StoreKit 2、SharePlay 四大主题构成了 2021 年 Apple 开发者生态的骨架。；Xcode 13 的 Organizer 终于把崩溃分析、用户反馈和指标数据放在了一个地方——你不用再在 App Store Connect 网页和邮件之间来回跳了。 来源：[WWDC23-10140]、[WWDC21-102]、[WWDC21-10203]、[WWDC21-10205]
- **应用服务**：Offer code 终于不再局限于自动续期订阅——消耗品、非消耗品、非续期订阅现在都能用 offer code 了，这对做促销活动和用户召回来说是一个被低估的变化。；appTransactionId 终于统一了所有交易对象的标识符体系——如果你还在用 originalTransactionId 做跨产品的用户关联，是时候迁移了。；On Demand Resources 要退役了，Background Assets 的 Managed 模式接管——Apple 帮你托管 200GB 的资源包，系统自动下载、更新、压缩，你甚至不需要写 downloader extension。 来源：[WWDC25-241]、[WWDC25-249]、[WWDC25-325]
- **StoreKit**：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 12 个月承诺期的月度订阅，为用户提供更实惠的订阅支付方式，同时巩固长期订阅关系。探索如何使用 App Store Connect、StoreKit API、Xcode 测试以及其他工具，配置并测试这一全新的支付选项。你还将了解优惠代码兑换 API 的改进，以及 App 审核内容提交体验的提升。；我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 Steam Asset Converter 和新的 Unity 插件，简化你的跨平台开发，并为 App 内购买项目提供更好的支持。了解如何通过特定于语言的资源包，精准地分发恰如所需的内容，从而让你的游戏更精简，并为玩家带来更出色的体验。 来源：[WWDC26-210]、[WWDC26-378]
- **Task**：ASC 今年是「功能大年」——Build Upload 可视化、App Store Tags、Custom Product Page 关键词、Offer Codes 全品类、Accessibility Nutrition Labels，每一项都直接影响你的上架效率和获客能力。；StoreKit 2 是 IAP（In App Purchase）开发体验的全面翻新 —— 用 async/await + Swift 原生 API 替代了 delegate 回调地狱，用 JWS 签名的事务替代了不可读的收据（Receipt），整个内购模块的代码量能砍掉三分之二。 来源：[WWDC25-328]、[WWDC21-10114]

## API 演进时间线

- **WWDC26**：7 场，代表来源：[WWDC26-205]、[WWDC26-210]、[WWDC26-254]、[WWDC26-309]、[WWDC26-378]
- **WWDC25**：8 场，代表来源：[WWDC25-202]、[WWDC25-241]、[WWDC25-249]、[WWDC25-252]、[WWDC25-324]
- **WWDC24**：5 场，代表来源：[WWDC24-10061]、[WWDC24-10062]、[WWDC24-10063]、[WWDC24-10110]、[WWDC24-10214]
- **WWDC23**：8 场，代表来源：[WWDC23-10013]、[WWDC23-10014]、[WWDC23-10015]、[WWDC23-10061]、[WWDC23-10117]
- **WWDC22**：7 场，代表来源：[WWDC22-10007]、[WWDC22-10039]、[WWDC22-10040]、[WWDC22-10043]、[WWDC22-10044]
- **WWDC21**：15 场，代表来源：[WWDC21-10012]、[WWDC21-10013]、[WWDC21-10114]、[WWDC21-10115]、[WWDC21-10170]
- **WWDC20**：14 场，代表来源：[WWDC20-10004]、[WWDC20-10118]、[WWDC20-10120]、[WWDC20-10147]、[WWDC20-10204]

## 决策启发式

- 先用本页确认 Session 是否与你的项目相关，再针对具体 API 查阅 Apple Developer Documentation。
- 涉及最低系统版本、弃用状态和运行时行为时，以 Xcode 27 SDK 与正式文档为准。
- 当前不要把章节摘要当作完整迁移指南；待 transcript 发布后再做架构和兼容性决策。
- 新项目统一使用 appTransactionId 作为交易关联的主键，避免混用多种标识符导致的逻辑复杂化。
- 使用 App Store Server Library 的 JWS 签名生成器，不要自己实现签名逻辑。
- 对所有产品类型的退款通知都实现处理逻辑，包括 non consumable 和 non renewing subscription。
- 在服务端维护准确的消费状态，以便在 CONSUMPTION REQUEST 时提供精确的 consumptionPercentage。
- V1 的 Send Consumption Information 端点已废弃，新集成直接用 V2。
- 定期检查 App Store Server API 的 GitHub 仓库，Apple 持续更新 server library。
- 定期检查 Download to Paid Conversion 的 benchmark，如果低于 50th percentile，优先优化转化漏斗而不是拉新。

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

`App Store, Distribution & Marketing` (6)、`App Store & Distribution` (4)、`应用服务` (3)、`StoreKit` (2)、`Xcode` (1)、`MusicKit` (1)、`Wallet` (1)、`PassKit` (1)、`Apple Pay` (1)、`Live Activity` (1)、`图形与游戏` (1)、`系统服务` (1)、`Swift` (1)、`开发工具` (1)

## 关键 Session

- [WWDC26-205] 提升 App 在 App Store 上的表现：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：通过在新位置展示相关图像和视频，重新构想你在 App Store 上推广 App 和游戏的方式。探索如何在 App Store 上的产品页面、搜索结果和 Apple Ads 广告系列中，利用新的视觉素材展示位置以更丰富生动的故事打动用户。了解如何使用全新的 Asset Library 将所有视觉素材汇于一处来简化管理，以及如何借助一款新工具在产品页面上线之前预览效果。
- [WWDC26-210] Apple App 内购买项目的新功能：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：了解如何利用 12 个月承诺期的月度订阅，为用户提供更实惠的订阅支付方式，同时巩固长期订阅关系。探索如何使用 App Store Connect、StoreKit API、Xcode 测试以及其他工具，配置并测试这一全新的支付选项。你还将了解优惠代码兑换 API 的改进，以及 App 审核内容提交体验的提升。
- [WWDC26-254] 将 MusicKit 整合到你的 App 中：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 MusicKit 将 Apple Music 的强大功能融入你的 App。我们将介绍授权、订阅状态检查、音乐选择、播放控制以及跨平台歌曲共享。了解如何使用新的音乐选择器，方便用户浏览 Apple Music 目录和自己的个人音乐库。我们还将详细讲解 SystemMusicPlayer 和 ApplicationMusicPlayer 之间的区别，并展示如何观察播放状态。
- [WWDC26-309] 在 App Store Connect 中探索 Retention Messaging：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索如何利用 Retention Messaging 的强大功能，在用户取消订阅之前及时触达他们。了解如何在 App Store Connect 中设置这项功能并添加订阅优惠，同时利用 Retention Messaging API 推送实时消息和替代选项，从而鼓励用户持续订阅你的 App 或游戏。
- [WWDC26-378] 通过 StoreKit 和后台资源解锁游戏内内容：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：使用 Steam Asset Converter 和新的 Unity 插件，简化你的跨平台开发，并为 App 内购买项目提供更好的支持。了解如何通过特定于语言的资源包，精准地分发恰如所需的内容，从而让你的游戏更精简，并为玩家带来更出色的体验。
- [WWDC26-391] 利用多席位订阅来拓展订阅用户群并触达新受众：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：探索通过多席位购买扩大订阅用户群的两种新方法：群组购买允许单个订阅者购买多个席位，并直接从你的 App 邀请其他用户；批量购买则通过 Apple 商务和 Apple 校园教务管理进行，可将你的订阅呈现给大规模采购 App 的企业客户和教育机构客户。了解如何支持多席位订阅，以及在 App Store Connect 中配置价格与销售范围的选项。
- [WWDC26-8010] App Store Connect 小组实验室：我的判断是，这场 Session 当前最值得先掌握的内容已经写在 Apple 的官方概述里：参加我们的线上活动，与 Apple 工程师和设计师一起深入探索 WWDC26。在这个以 App Store Connect 为主题的活动中，你可以提出问题、获取建议，并实时关注围绕大会一周的相关重磅发布展开的精彩讨论。活动语言为英语。
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
