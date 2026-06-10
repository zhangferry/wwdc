# PRD：WWDC Notes 已读 & 收藏功能

**版本**: v1.0  
**日期**: 2026-06-09  
**作者**: WWDC Notes Team  
**状态**: 待评审

---

## 1. 背景与目标

### 1.1 问题陈述

WWDC Notes 目前收录了 2020-2026 共 7 年约 1100+ 场 Session 总结。用户在浏览时面临两个痛点：

1. **阅读进度不可见**：用户无法快速识别哪些 Session 已经读过，每次进入列表页都要靠记忆判断，导致重复阅读或遗漏。
2. **重点内容难找回**：用户在阅读过程中会遇到高价值内容，但缺乏轻量级的收藏机制，只能依赖浏览器书签或外部工具，体验割裂。

### 1.2 目标

- 让用户能够**一键标记**已读状态，并在列表页直观看到阅读进度
- 让用户能够**收藏**高价值 Session，并通过筛选快速找回
- 所有状态**本地存储**，无需后端服务，保护用户隐私

### 1.3 非目标

- 不引入用户账号系统（纯客户端方案）
- 不做跨设备同步
- 不做阅读时长统计或阅读进度条（仅二态：已读/未读）
- 不做社交分享或排行榜

---

## 2. 用户场景

### 场景 1：批量浏览时的进度管理

> 小明每天下班后会花 30 分钟刷 WWDC26 的 Session 总结。他打开列表页，一眼看到已经读过的 Session 卡片上有一个"已读"标记，于是直接跳过，专注于未读的内容。

### 场景 2：收藏高价值内容

> 小红在阅读 "What's new in SwiftUI" 时发现里面的 Liquid Glass 设计语言对她的项目很有帮助。她在文章标题右侧点击星标"收藏"按钮，图标变为实心黄色。之后她在筛选栏选择"只看收藏"，快速找到这篇内容。

### 场景 3：过滤已读内容

> 小李已经读完了大部分 WWDC25 的 Session，他想看看还有哪些没读。他在筛选栏点击"隐藏已读"，列表立即过滤出未读的 Session，他从中挑选感兴趣的继续阅读。

---

## 3. 功能需求

### 3.1 已读功能

#### 3.1.1 文章详情页：标记已读按钮

**位置**: 文章末尾，Tags 区域下方  
**UI 形态**:
- 未读状态：空心圆形图标 + "标记为已读" 文字
- 已读状态：实心勾选图标 + "已读" 文字（可点击取消）

**交互**:
- 点击按钮立即切换状态，无加载延迟
- 状态变更后按钮图标和文字同步更新
- 点击已读按钮可取消已读（变为未读）

**示例 UI**:
```
┌─────────────────────────────────────┐
│  📋 Tags: [SwiftUI] [Liquid Glass]  │
├─────────────────────────────────────┤
│                                     │
│     [○ 标记为已读]  (未读状态)       │
│                                     │
│     [✓ 已读]        (已读状态)       │
│                                     │
└─────────────────────────────────────┘
```

#### 3.1.2 列表页卡片：已读状态标识

**位置**: 卡片右上角（覆盖在缩略图上）  
**UI 形态**:
- 未读：不显示任何标识
- 已读：显示半透明圆形勾选图标（绿色背景 + 白色勾）

**交互**:
- 仅展示，不可点击（标记操作在文章详情页）
- 图标尺寸：24x24px，带 4px 圆角

**示例 UI**:
```
┌─────────────────────────────────┐
│  ┌──────────────────────────┐ ✓ │
│  │                          │   │
│  │      Thumbnail           │   │
│  │                          │   │
│  └──────────────────────────┘   │
│  Track: SwiftUI  Level: 中级     │
│  SwiftUI 的新功能                 │
│  What's new in SwiftUI           │
└─────────────────────────────────┘
```

#### 3.1.3 筛选栏：已读过滤

**位置**: 现有 Track 筛选 pill 右侧  
**UI 形态**:
- 新增一个"隐藏已读"开关（Checkbox 或 Toggle）
- 默认状态：关闭（不过滤，显示所有 Session）

**交互**:
- 开启后：列表仅显示未读 Session
- 关闭后：恢复显示所有 Session
- 与 Track 筛选联动：可同时按 Track + 已读状态过滤

**示例 UI**:
```
┌─────────────────────────────────────────────────────────────┐
│  [全部] [SwiftUI & UI] [Swift & Data] ...   ☐ 隐藏已读     │
└─────────────────────────────────────────────────────────────┘
```

---

### 3.2 收藏功能

#### 3.2.1 文章详情页：收藏按钮

**位置**: 文章头部，Title 右侧  
**UI 形态**:
- 未收藏：空心星标图标（☆）
- 已收藏：实心黄色星标图标（★）

**交互**:
- 点击立即切换状态，无加载延迟
- 状态变更后图标颜色同步更新（灰色 → 黄色）
- 支持 hover 提示："收藏此 Session" / "取消收藏"

**示例 UI**:
```
┌─────────────────────────────────────────────────────────────┐
│  Track: SwiftUI  Level: 中级  Duration: 28min               │
│                                                             │
│  SwiftUI 的新功能                              [☆] (未收藏)  │
│  What's new in SwiftUI                                      │
│                                                             │
│  2026-06-10                                    [★] (已收藏)  │
└─────────────────────────────────────────────────────────────┘
```

#### 3.2.2 列表页卡片：收藏状态标识

**位置**: 卡片右上角（与已读图标同位置，已读图标优先级更高）  
**UI 形态**:
- 未收藏：不显示标识
- 已收藏：显示黄色实心星标（16x16px）

**优先级规则**:
- 同时已读 + 收藏：显示已读勾选图标（绿色）
- 仅收藏：显示黄色星标
- 仅已读：显示绿色勾选
- 都未标记：不显示

**示例 UI**:
```
┌─────────────────────────────────┐
│  ┌──────────────────────────┐ ★ │  (仅收藏)
│  │                          │   │
│  │      Thumbnail           │   │
│  └──────────────────────────┘   │
│  ...                            │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  ┌──────────────────────────┐ ✓ │  (已读，优先级更高)
│  │                          │   │
│  │      Thumbnail           │   │
│  └──────────────────────────┘   │
│  ...                            │
└─────────────────────────────────┘
```

#### 3.2.3 筛选栏：收藏过滤

**位置**: "隐藏已读"开关右侧  
**UI 形态**:
- 新增一个"只看收藏"开关（Checkbox 或 Toggle）
- 默认状态：关闭（不过滤，显示所有 Session）

**交互**:
- 开启后：列表仅显示已收藏 Session
- 关闭后：恢复显示所有 Session
- 与 Track + 已读筛选联动：可同时按 Track + 已读 + 收藏过滤

**冲突处理**:
- "隐藏已读" + "只看收藏" 同时开启：显示**已收藏且未读**的 Session
- 空状态提示："当前筛选条件下暂无 Session"

**示例 UI**:
```
┌──────────────────────────────────────────────────────────────────┐
│  [全部] [SwiftUI & UI] ...   ☐ 隐藏已读   ☐ 只看收藏            │
└──────────────────────────────────────────────────────────────────┘
```

---

## 4. 技术方案

### 4.1 数据存储

**存储介质**: `localStorage`（浏览器本地存储）  
**Key 设计**:
```typescript
// 已读状态
localStorage.setItem('wwdc-read-{year}-{id}', '1')  // 已读
localStorage.removeItem('wwdc-read-{year}-{id}')     // 未读

// 收藏状态
localStorage.setItem('wwdc-favorite-{year}-{id}', '1')  // 已收藏
localStorage.removeItem('wwdc-favorite-{year}-{id}')     // 取消收藏
```

**示例**:
- Session 2026-209 已读：`localStorage['wwdc-read-2026-209'] = '1'`
- Session 2025-201 已收藏：`localStorage['wwdc-favorite-2025-201'] = '1'`

**容量估算**:
- 每个状态占用 ~30 bytes
- 1100 个 Session 全部标记：~33KB
- localStorage 上限 5MB，完全够用

### 4.2 组件修改

#### 4.2.1 SessionCard.astro

**新增 Props**:
```typescript
interface Props {
  // ... existing props
  isRead?: boolean;      // 已读状态
  isFavorite?: boolean;  // 收藏状态
}
```

**新增 UI**:
- 右上角状态图标区域（已读 > 收藏 > 无）
- 传递 `data-read` 和 `data-favorite` 属性用于客户端筛选

#### 4.2.2 PostLayout.astro

**新增 Props**:
```typescript
interface Props {
  // ... existing props
  year: string;  // 用于构建 localStorage key
  id: string;    // 用于构建 localStorage key
}
```

**新增 UI**:
1. 头部收藏按钮（Title 右侧）
2. 底部已读按钮（Tags 下方）

**新增 Script**:
```typescript
// 初始化状态
const readKey = `wwdc-read-${year}-${id}`;
const favKey = `wwdc-favorite-${year}-${id}`;
const isRead = localStorage.getItem(readKey) === '1';
const isFavorite = localStorage.getItem(favKey) === '1';

// 更新 UI
updateReadButton(isRead);
updateFavoriteButton(isFavorite);

// 绑定事件
readButton.addEventListener('click', () => {
  const newState = !isRead;
  if (newState) {
    localStorage.setItem(readKey, '1');
  } else {
    localStorage.removeItem(readKey);
  }
  updateReadButton(newState);
});

favoriteButton.addEventListener('click', () => {
  const newState = !isFavorite;
  if (newState) {
    localStorage.setItem(favKey, '1');
  } else {
    localStorage.removeItem(favKey);
  }
  updateFavoriteButton(newState);
});
```

#### 4.2.3 FilterBar.astro

**新增 UI**:
```html
<div class="flex items-center gap-4 ml-auto">
  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" id="hide-read" />
    <span>隐藏已读</span>
  </label>
  <label class="flex items-center gap-2 cursor-pointer">
    <input type="checkbox" id="show-favorite" />
    <span>只看收藏</span>
  </label>
</div>
```

**新增 Script** (在 [year]/index.astro):
```typescript
const hideReadCheckbox = document.getElementById('hide-read');
const showFavoriteCheckbox = document.getElementById('show-favorite');

function applyFilters() {
  const track = activePill.dataset.track || '';
  const hideRead = hideReadCheckbox.checked;
  const showFavorite = showFavoriteCheckbox.checked;

  cards.forEach(card => {
    const cardTrack = card.dataset.track;
    const cardRead = card.dataset.read === '1';
    const cardFavorite = card.dataset.favorite === '1';

    const matchTrack = !track || cardTrack === track;
    const matchRead = !hideRead || !cardRead;
    const matchFavorite = !showFavorite || cardFavorite;

    const show = matchTrack && matchRead && matchFavorite;
    card.style.display = show ? '' : 'none';
  });
}

hideReadCheckbox.addEventListener('change', applyFilters);
showFavoriteCheckbox.addEventListener('change', applyFilters);
```

#### 4.2.4 [year]/index.astro

**修改 SessionCard 调用**:
```typescript
<SessionCard
  // ... existing props
  isRead={typeof localStorage !== 'undefined' && localStorage.getItem(`wwdc-read-${yearNum}-${session.data.id}`) === '1'}
  isFavorite={typeof localStorage !== 'undefined' && localStorage.getItem(`wwdc-favorite-${yearNum}-${session.data.id}`) === '1'}
/>
```

**注意**: Astro 是静态站点，`localStorage` 仅在客户端可用。需要在 `<script>` 中动态设置 `data-read` 和 `data-favorite` 属性。

**修正方案**:
```typescript
<div
  class="session-card-wrapper"
  data-track={session.data.track}
  data-year={yearNum}
  data-id={session.data.id}
>
  <SessionCard ... />
</div>

<script>
  // 客户端动态设置状态
  document.querySelectorAll('.session-card-wrapper').forEach(wrapper => {
    const year = wrapper.dataset.year;
    const id = wrapper.dataset.id;
    const isRead = localStorage.getItem(`wwdc-read-${year}-${id}`) === '1';
    const isFavorite = localStorage.getItem(`wwdc-favorite-${year}-${id}`) === '1';
    wrapper.dataset.read = isRead ? '1' : '0';
    wrapper.dataset.favorite = isFavorite ? '1' : '0';
  });
</script>
```

---

## 5. UI/UX 规范

### 5.1 颜色

| 元素 | 颜色 | 用途 |
|------|------|------|
| 已读图标背景 | `#10B981` (Emerald-500) | 成功/完成状态 |
| 已读图标前景 | `#FFFFFF` (White) | 图标对比 |
| 收藏图标 | `#FBBF24` (Amber-400) | 收藏/高亮状态 |
| 未收藏图标 | `#9CA3AF` (Gray-400) | 未激活状态 |

### 5.2 尺寸

| 元素 | 尺寸 |
|------|------|
| 卡片状态图标 | 24x24px |
| 头部收藏图标 | 28x28px |
| 底部已读按钮 | 高度 44px，宽度自适应 |
| 筛选栏 Checkbox | 16x16px |

### 5.3 动画

- 状态切换：`transition: all 0.2s ease-in-out`
- 图标缩放：点击时 `transform: scale(0.9)` → `scale(1)`
- 颜色过渡：`background-color 0.15s ease`

### 5.4 无障碍

- 所有按钮添加 `aria-label`（如 "标记为已读"、"取消收藏"）
- Checkbox 添加 `aria-labelledby` 关联文字标签
- 图标使用 `aria-hidden="true"`，文字标签提供语义

---

## 6. 测试计划

### 6.1 功能测试

#### 6.1.1 已读功能基础测试

| 测试用例 | 预期结果 |
|----------|----------|
| 点击文章末尾"标记为已读" | 按钮变为"已读"，图标变绿，文案更新 |
| 刷新页面后检查已读状态 | 状态保持，按钮仍为"已读"，localStorage 值正确 |
| 点击已读按钮取消已读 | 按钮恢复为"标记为已读"，localStorage 项删除 |
| 列表页卡片显示已读图标 | 右上角显示绿色勾选 ✓，24x24px |
| 未读 Session 卡片 | 右上角无任何状态图标 |
| 已读状态在多个标签页同步 | 在标签页 A 标记已读，标签页 B 刷新后状态同步 |

#### 6.1.2 收藏功能基础测试

| 测试用例 | 预期结果 |
|----------|----------|
| 点击头部收藏按钮（未收藏→已收藏） | 星标变黄实心 ★，hover 提示"取消收藏" |
| 刷新页面后检查收藏状态 | 状态保持，星标仍为黄色，localStorage 值正确 |
| 点击收藏按钮取消收藏 | 星标恢复灰色空心 ☆，localStorage 项删除 |
| 列表页卡片显示收藏图标 | 右上角显示黄色星标 ★，16x16px |
| 未收藏 Session 卡片 | 右上角无星标（除非已读） |
| 收藏状态在多个标签页同步 | 在标签页 A 收藏，标签页 B 刷新后状态同步 |

#### 6.1.3 状态图标优先级测试

| 测试用例 | 预期结果 |
|----------|----------|
| 同时已读 + 收藏 | 显示已读勾选图标（绿色 ✓），不显示星标 |
| 仅收藏（未读） | 显示黄色星标 ★ |
| 仅已读（未收藏） | 显示绿色勾选 ✓ |
| 都未标记 | 不显示任何图标 |
| 先标记已读再收藏 | 图标从 ✓ 保持不变（已读优先级高） |
| 先收藏再标记已读 | 图标从 ★ 变为 ✓（已读覆盖收藏） |

#### 6.1.4 筛选功能测试

| 测试用例 | 预期结果 |
|----------|----------|
| 筛选栏开启"隐藏已读" | 列表仅显示未读 Session，已读卡片隐藏 |
| 筛选栏关闭"隐藏已读" | 恢复显示所有 Session |
| 筛选栏开启"只看收藏" | 列表仅显示已收藏 Session |
| 筛选栏关闭"只看收藏" | 恢复显示所有 Session |
| 同时开启"隐藏已读" + "只看收藏" | 显示已收藏且未读的 Session（交集） |
| Track 筛选 + "隐藏已读" | 同时生效，显示指定 Track 的未读 Session |
| Track 筛选 + "只看收藏" | 同时生效，显示指定 Track 的已收藏 Session |
| Track + 已读 + 收藏三维筛选 | 三者交集过滤，正确显示符合条件的 Session |
| 筛选后无匹配结果 | 显示空状态提示"当前筛选条件下暂无 Session" |
| 筛选状态在页面刷新后 | 筛选条件重置为默认（全部关闭） |

#### 6.1.5 数据持久化测试

| 测试用例 | 预期结果 |
|----------|----------|
| 标记已读后关闭浏览器重新打开 | 状态保持，localStorage 数据未丢失 |
| 收藏后关闭浏览器重新打开 | 状态保持，localStorage 数据未丢失 |
| 清除浏览器缓存和 Cookie | 所有已读/收藏状态重置，localStorage 清空 |
| 使用隐身模式访问 | 关闭窗口后状态丢失（符合隐身模式行为） |
| localStorage 存储配额检查 | 1100 个 Session 全部标记占用 ~33KB，远低于 5MB 上限 |
| Key 命名规范验证 | `wwdc-read-{year}-{id}` 和 `wwdc-favorite-{year}-{id}` 格式正确 |

### 6.2 兼容性测试

| 浏览器 | 版本 | 预期 |
|--------|------|------|
| Chrome | 最新稳定版 | 功能正常，localStorage 读写正常 |
| Safari | 最新稳定版 | 功能正常，iOS Safari 需特别测试 |
| Firefox | 最新稳定版 | 功能正常，隐私模式下 localStorage 可能受限 |
| Edge | 最新稳定版 | 功能正常（Chromium 内核） |
| Opera | 最新稳定版 | 功能正常（Chromium 内核） |
| 移动端 Safari | iOS 15+ | 触摸操作正常，图标显示正确 |
| 移动端 Chrome | Android 10+ | 触摸操作正常，性能流畅 |
| 平板 Safari | iPadOS 15+ | 横竖屏切换后布局正常 |

### 6.3 边界测试

| 场景 | 预期 |
|------|------|
| localStorage 被禁用 | 按钮显示为禁用状态，点击无响应，console 输出警告 |
| localStorage 空间不足（模拟） | 捕获 QuotaExceededError，显示友好提示 |
| 清除浏览器数据 | 所有状态重置为未读/未收藏，UI 正确更新 |
| 1100 个 Session 全部标记已读 | localStorage 占用 ~16.5KB，性能无影响，列表页加载流畅 |
| 1100 个 Session 全部收藏 | localStorage 占用 ~16.5KB，筛选"只看收藏"响应时间 < 100ms |
| 快速连续点击按钮（10 次/秒） | 防抖处理生效，最终状态正确，无竞态条件 |
| 同时操作多个 Session 的状态 | 各 Session 状态独立，localStorage 无冲突 |
| 年份边界（2020 vs 2026） | 不同年份的相同 ID Session 状态独立存储 |
| 特殊字符 ID（如 "100a"） | localStorage Key 正确生成，无转义问题 |
| 极长标题（>100 字符） | 卡片布局正常，标题截断显示，状态图标位置正确 |

### 6.4 性能测试

| 测试用例 | 预期结果 |
|----------|----------|
| 列表页加载 1100 个 Session | 首次加载时间 < 2s，状态图标渲染无闪烁 |
| 筛选操作响应时间 | 切换筛选条件后，卡片显隐动画 < 300ms |
| localStorage 读写性能 | 单次读写操作 < 1ms，不影响页面流畅度 |
| 大量状态变更（批量标记） | 100 个 Session 批量标记已读，总耗时 < 500ms |
| 内存占用 | 1100 个 Session 全部标记，内存增长 < 5MB |
| 动画性能 | 状态切换动画 60fps，无卡顿或掉帧 |

### 6.5 用户体验测试

| 测试用例 | 预期结果 |
|----------|----------|
| 按钮点击反馈 | 点击时有 `scale(0.9)` 缩放动画，视觉反馈明确 |
| 状态切换动画 | 颜色过渡 `background-color 0.15s ease`，平滑自然 |
| Hover 提示 | 收藏按钮 hover 显示"收藏此 Session" / "取消收藏" tooltip |
| 键盘操作 | 按钮支持 Tab 聚焦、Enter/Space 触发，焦点样式清晰 |
| 屏幕阅读器 | `aria-label` 正确朗读，状态变更有 aria-live 通知 |
| 高对比度模式 | 图标和按钮在高对比度主题下清晰可见 |
| 深色模式 | 图标颜色在深色背景下对比度充足（≥ 4.5:1） |
| 响应式布局 | 移动端按钮尺寸 ≥ 44x44px，触摸区域充足 |

### 6.6 回归测试

| 测试用例 | 预期结果 |
|----------|----------|
| 原有 Track 筛选功能 | 不受新功能影响，正常工作 |
| 原有 Session 卡片点击跳转 | 不受状态图标影响，点击区域正确 |
| 原有文章详情页渲染 | 新增按钮不影响 Markdown 内容和代码高亮 |
| 原有响应式布局 | 新增筛选栏 Checkbox 不破坏移动端布局 |
| 原有 SEO 元数据 | 新增客户端脚本不影响静态生成的 meta 标签 |
| 原有 Vercel 部署流程 | 新增功能不引入构建错误，部署成功率 100% |

### 6.7 异常场景测试

| 场景 | 预期 |
|------|------|
| localStorage 读取失败（数据损坏） | 捕获异常，降级为未读/未收藏状态，console 输出错误 |
| 网络断开时操作 | 已读/收藏功能正常工作（纯客户端，不依赖网络） |
| JavaScript 被禁用 | 按钮隐藏或显示为不可用状态，不影响基础阅读体验 |
| Astro hydration 失败 | 按钮降级为静态 HTML，点击无响应但不报错 |
| 并发写入 localStorage（多标签页） | 最后写入的值生效，无数据覆盖或丢失 |
| 浏览器扩展修改 localStorage | 应用能正确处理外部修改，状态同步更新 |

---

## 7. 上线计划

### 7.1 开发阶段（预计 2 天）

| 任务 | 工时 | 优先级 |
|------|------|--------|
| PostLayout.astro 添加已读/收藏按钮 | 2h | P0 |
| SessionCard.astro 添加状态图标 | 1h | P0 |
| FilterBar.astro 添加筛选 Checkbox | 1h | P0 |
| [year]/index.astro 客户端状态同步 | 2h | P0 |
| UI 样式调整与动画 | 2h | P1 |
| 无障碍优化 | 1h | P1 |
| 单元测试 | 2h | P1 |
| 集成测试 | 1h | P0 |

### 7.2 上线步骤

1. **开发分支**: 从 `main` 创建 `feat/read-and-favorite`
2. **开发 & 测试**: 完成功能开发与本地测试
3. **PR 评审**: 提交 Pull Request，等待 Code Review
4. **合并上线**: 合并到 `main`，Vercel 自动部署
5. **监控**: 观察 Vercel 构建日志，确认无报错
6. **验证**: 在生产环境验证核心功能

### 7.3 回滚方案

- 如发现问题，立即 Revert Commit 并重新部署
- 已存储的 localStorage 数据不会丢失，下次上线可继续使用

---

## 8. 后续迭代（可选）

### 8.1 阅读统计

- 显示"已读 X / Y 个 Session"进度条
- 按 Track 分类统计已读数量
- 生成阅读报告（每周/每月读了多少）

### 8.2 跨设备同步

- 引入可选的云同步（如 Firebase、Supabase）
- 用户登录后可跨设备同步已读/收藏状态
- 提供导出/导入功能（JSON 格式）

### 8.3 收藏分组

- 支持创建多个收藏夹（如"SwiftUI 精选"、"性能优化"）
- 收藏时可添加到指定分组
- 筛选栏支持按收藏夹过滤

### 8.4 分享功能

- 一键分享已读/收藏列表到社交媒体
- 生成个人阅读清单链接

---

## 9. 附录

### 9.1 相关文件清单

| 文件 | 修改内容 |
|------|----------|
| `src/components/SessionCard.astro` | 添加状态图标 |
| `src/components/FilterBar.astro` | 添加筛选 Checkbox |
| `src/layouts/PostLayout.astro` | 添加已读/收藏按钮 |
| `src/pages/[year]/index.astro` | 客户端状态同步 + 筛选逻辑 |
| `src/pages/[year]/[id].astro` | 传递 year 和 id props |

### 9.2 参考资源

- [Astro 客户端脚本](https://docs.astro.build/en/guides/client-side-scripts/)
- [localStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [Tailwind CSS 颜色](https://tailwindcss.com/docs/customizing-colors)

---

**文档结束**
