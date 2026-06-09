# App Distribution

## 领域判断

App Store、TestFlight、签名、审核与分发。本领域覆盖 63 场 WWDC Session，回答时优先把 API 变化放回年度语境里判断。

## 核心模型

- **App Store & Distribution**：Cloud Signing 终于让你不用再管本地证书和 provisioning profile 的同步问题——私钥存在 Apple 服务器上，团队成员谁都能签名。；如果你的教育 App 是基于文档的（如笔记、练习册），ClassKit 的新文件集成让学生在 Schoolwork 中直接打开你的文件，完成后自动汇报进度——不需要在两个 App 之间切换。；macOS Monterey 的公证（Notarization）流程从"提交等几分钟查邮件"简化成了"一条命令搞定"——notarytool 替代了 altool，支持提交、等待和装订（Staple）一步完成。 来源：[WWDC21-10204]、[WWDC21-10257]、[WWDC21-10261]、[WWDC20-10118]
- **App Store, Distribution & Marketing**：Offer code 终于不再局限于自动续期订阅——消耗品、非消耗品、非续期订阅现在都能用 offer code 了，这对做促销活动和用户召回来说是一个被低估的变化。；App Analytics 终于补上了付费用户转化漏斗和订阅留存的完整分析能力——如果你之前只能看 proceeds 和 downloads，现在能看清每个环节到底差在哪了。；等了好几年，App Store Connect 终于有了 Webhook 和 Build Upload API——CI/CD 里最缺失的那一环现在补上了。 来源：[WWDC25-241]、[WWDC25-252]、[WWDC25-324]、[WWDC25-328]
- **App Store Distribution & Marketing**：iOS 18 终于把已完成的消耗品交易纳入交易历史 API，同时新增货币和价格字段、win back offers 和更强大的 StoreKit Views，这三个改动组合起来让内购管理从"头疼"变成了"基本不用操心"。；如果你在做什么内购系统却还没用上 App Store Server API 和 Server Library，这个 session 就是你的必读清单——尤其是退款决策和订阅续期的新能力，直接关系到钱。；今年 App Store Connect 最重要的更新是 Featuring Nominations——你终于可以主动告诉 App Store 编辑团队"我的 App 要更新了，请考虑推荐"，而不是被动等待被发现。 来源：[WWDC24-10061]、[WWDC24-10062]、[WWDC24-10063]、[WWDC24-10110]
- **Developer Tools**：App Store 推广购买、Billing Issue 消息、SHA 256 迁移——StoreKit 2 今年带来了多项实用更新。；这是一场信息密度极高的全景扫描——Swift 并发、Xcode Cloud、StoreKit 2、SharePlay 四大主题构成了 2021 年 Apple 开发者生态的骨架。；Xcode 13 的 Organizer 终于把崩溃分析、用户反馈和指标数据放在了一个地方——你不用再在 App Store Connect 网页和邮件之间来回跳了。 来源：[WWDC23-10140]、[WWDC21-102]、[WWDC21-10203]、[WWDC21-10205]
- **StoreKit**：✅ 年度订阅终于能官方“分期付款”了，这是提升订阅转化率最实用的商业武器，比任何 StoreKit 代码层面的更新都值钱。；这场 Session 最值得关注的一件事是：Apple 终于开放了订阅取消页面的 Server to Server (S2S) 实时拦截接口，让订阅防流失从“统一发优惠券”变成了基于用户画像的“精准狙击”。；✅ Apple 官方下场帮 Unity 开发者把 Steam 资产和 IAP 无缝搬到 Apple 平台了，这是明抢 PC 游戏开发者。 来源：[WWDC26-210]、[WWDC26-309]、[WWDC26-378]
- **应用服务**：Offer code 终于不再局限于自动续期订阅——消耗品、非消耗品、非续期订阅现在都能用 offer code 了，这对做促销活动和用户召回来说是一个被低估的变化。；appTransactionId 终于统一了所有交易对象的标识符体系——如果你还在用 originalTransactionId 做跨产品的用户关联，是时候迁移了。；On Demand Resources 要退役了，Background Assets 的 Managed 模式接管——Apple 帮你托管 200GB 的资源包，系统自动下载、更新、压缩，你甚至不需要写 downloader extension。 来源：[WWDC25-241]、[WWDC25-249]、[WWDC25-325]
- **App Store Connect API**：✅ 年度订阅终于能官方“分期付款”了，这是提升订阅转化率最实用的商业武器，比任何 StoreKit 代码层面的更新都值钱。；这场 Session 最值得关注的一件事是：Apple 终于开放了订阅取消页面的 Server to Server (S2S) 实时拦截接口，让订阅防流失从“统一发优惠券”变成了基于用户画像的“精准狙击”。 来源：[WWDC26-210]、[WWDC26-309]

## API 演进时间线

- **WWDC26**：6 场，代表来源：[WWDC26-205]、[WWDC26-210]、[WWDC26-254]、[WWDC26-309]、[WWDC26-378]
- **WWDC25**：8 场，代表来源：[WWDC25-202]、[WWDC25-241]、[WWDC25-249]、[WWDC25-252]、[WWDC25-324]
- **WWDC24**：5 场，代表来源：[WWDC24-10061]、[WWDC24-10062]、[WWDC24-10063]、[WWDC24-10110]、[WWDC24-10214]
- **WWDC23**：8 场，代表来源：[WWDC23-10013]、[WWDC23-10014]、[WWDC23-10015]、[WWDC23-10061]、[WWDC23-10117]
- **WWDC22**：7 场，代表来源：[WWDC22-10007]、[WWDC22-10039]、[WWDC22-10040]、[WWDC22-10043]、[WWDC22-10044]
- **WWDC21**：15 场，代表来源：[WWDC21-10012]、[WWDC21-10013]、[WWDC21-10114]、[WWDC21-10115]、[WWDC21-10170]
- **WWDC20**：14 场，代表来源：[WWDC20-10004]、[WWDC20-10118]、[WWDC20-10120]、[WWDC20-10147]、[WWDC20-10204]

## 决策启发式

- 已有项目的迁移策略 ：别急着把现有截图换成 Header。先让设计团队产出 2 3 套不同风格的 Header 素材（比如一套强调品牌调性，一套强调核心功能），利用 Product Page Optimization（产品页面优化，简称 PPO）跑两周 A/B 测试，用数据决定最终方案。
- 新项目的采用建议 ：从第一天起就建立 Asset Library（素材库）的管理规范。把截图、预览视频、In App Event 图片和 Header 素材分门别类打标签，避免后期素材一多变成垃圾场。
- 实战中容易踩的坑 ：Header 素材和 App Icon（应用图标）在视觉上是紧挨着的。设计 Header 时，千万别在底部正中间放重要元素，否则会被 App Icon 挡住。一定要用 App Store Connect 里新的 Preview（预览）工具在真机尺寸下确认遮挡关系。
- 已有项目的迁移策略 ：立刻检查你的 CI/CD 脚本。如果你在用 Fastlane 的 deliver 提交 IAP，准备迎接 App Store Connect API 的变更，将旧的 IAP 提交逻辑迁移到 reviewSubmissions 集合中。同时，全局搜索 presentOfferCodeRedeemSheet，把旧的优惠码兑换逻辑替换为带 RedeemOption 和 VerificationResult 回调的新 API，现在你终于能准确知道用户兑换成功了没。
- 新项目的采用建议 ：所有订阅类 App，无脑加上“12个月承诺期按月订阅”选项，并和普通的“年度预付”做 A/B 测试。在 UI 上，用 billingDisplayPrice 展示月供，用 commitmentInfo.price 展示总价，一定要在付款按钮上方清晰写明“承诺 12 个月”，避免客诉。
- 实战中容易踩的坑 ：在 Xcode 27 的 StoreKit Testing 中配置好 Billing Plan 后，别忘了在 Transaction Inspector 里手动模拟“用户中途取消”和“扣款失败”的场景，确保你的服务端状态机能正确处理 commitmentInfo 的变化。
- 已有项目的迁移策略 ：先别急着上 Real time API。第一步先在 App Store Connect 里把静态的 Retention Messaging 配好，把基础的图片和 Retention Offer 挂上，吃掉那 82% 的挽留率红利。第二步再让后端团队开发 S2S 接口，做 A/B 测试对比动态策略的收益。
- 新项目的采用建议 ：后端接口设计必须把“低延迟”放在第一位。不要在 S2S 处理逻辑里做复杂的数据库联表查询或调用第三方风控接口。把用户画像数据提前缓存到 Redis 里，收到 originalTransactionId 直接查缓存返回结果。
- 实战中容易踩的坑 ：千万不要在 S2S 接口里返回错误的 JSON 格式或超时的响应。虽然 Apple 有 Fallback 机制会降级到 ASC 的静态配置，但如果你的接口频繁超时，Apple 可能会在系统层面降低对你端点的调用权重，甚至直接熔断。Sandbox 里的 /performanceTest 必须认真跑，确保 P99 延迟在 Apple 要求的阈值内。
- 老项目迁移 ：别急着全量重构。先接入 StoreKit Unity 插件替换掉现有的第三方 IAP 桥接，跑通 Transaction.Updates 监听。资源包方面，挑体积最大的多语言语音包，用 xcrun ba package 转成 Localized asset packs (本地化资源包) 试水。

## 反模式与坑

- PPO 支持新素材 ：Product Page Optimization（产品页面优化）现在可以直接拿 Product Page Header 和搜索结果素材做 A/B 测试，不用靠猜。
- Apple Ads 无缝复用 ：你在 Asset Library 里传好的素材，可以直接一键导入 Apple Search Ads（Apple 搜索广告）的 Today（今天）标签页或搜索结果广告系列里，省去了重复上传的麻烦。
- 多端多语言预览 ：提交审核前，新的 Preview 工具支持同时查看 iPhone/iPad 在不同屏幕方向和不同语言下的渲染效果，强迫症福音。
- Bundles and Suites（订阅捆绑和套件） ：支持跨 App 的订阅打包销售，目前只能在 Xcode 27 里测试 API，具体商业化细节 Apple 卖了个关子，下半年再公布。
- Offer Code Redemption（优惠码兑换）API 升级 ：兑换接口现在返回 VerificationResult，不用再靠监听 Transaction.updates 去盲猜兑换结果了。
- Retention Messaging API 支持新订阅 ：服务器到服务器的留存消息 API 现在能识别 12 个月承诺期用户，方便你在他们快到期时精准推送挽留优惠。
- 跨区内容等效 ：MusicCatalogResourceRequest 新增了 .findEquivalents 选项，当请求的特定歌曲在用户所在区服不可用时，自动返回等效的替代版本，避免开天窗。
- 异步状态监听 ：MusicSubscription.subscriptionUpdates 和播放器的状态都全面拥抱了 Swift Concurrency，用 for await 监听状态变化比以前的 Combine 或 Delegate 模式清爽太多。

## 高频主题

`App Store, Distribution & Marketing` (6)、`StoreKit` (3)、`应用服务` (3)、`App Store Connect API` (2)、`App Store Connect` (1)、`ASO` (1)、`Asset Library` (1)、`Custom Product Pages` (1)、`In-App Purchase` (1)、`Subscriptions` (1)、`MusicKit` (1)、`SwiftUI` (1)、`SystemMusicPlayer` (1)、`MusicPicker` (1)、`Apple Music` (1)、`Subscription` (1)、`Retention Messaging` (1)、`Server-to-Server` (1)

## 关键 Session

- [WWDC26-205] 提升 App 在 App Store 上的表现：✅ App Store 终于把产品页和搜索结果变成了真正的 Landing Page，并且营销素材审核正式与 App 发版解耦。
- [WWDC26-210] Apple App 内购买项目的新功能：✅ 年度订阅终于能官方“分期付款”了，这是提升订阅转化率最实用的商业武器，比任何 StoreKit 代码层面的更新都值钱。
- [WWDC26-254] 将 MusicKit 整合到你的 App 中：✅ MusicKit 终于把授权、选歌、播放和订阅转化打磨成了一套极其顺滑的 SwiftUI 原生体验，非音乐类 App 接入 Apple Music 的门槛降到了历史最低。
- [WWDC26-309] 在 App Store Connect 中探索 Retention Messaging：这场 Session 最值得关注的一件事是：Apple 终于开放了订阅取消页面的 Server to Server (S2S) 实时拦截接口，让订阅防流失从“统一发优惠券”变成了基于用户画像的“精准狙击”。
- [WWDC26-378] 通过 StoreKit 和后台资源解锁游戏内内容：✅ Apple 官方下场帮 Unity 开发者把 Steam 资产和 IAP 无缝搬到 Apple 平台了，这是明抢 PC 游戏开发者。
- [WWDC26-391] 利用多席位订阅来拓展订阅用户群并触达新受众：Apple 终于官方接管了 B2B 订阅的“席位分发”和“阶梯定价”，做团队协作或企业应用的开发者不用再自己手写那套反人类的 License 邀请系统了。
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
