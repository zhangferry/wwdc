# AGENTS.md — WWDC 中文总结博客

## 项目概述

Astro 5 静态站点，托管 WWDC Session 的中文技术总结。覆盖 WWDC 2020-2025，共 930+ 篇文章。

## 技术栈

- Astro 5 + Tailwind CSS v4 + TypeScript
- pnpm 包管理
- Content Collections 管理 Markdown 文章
- 部署在 Vercel

## 关键架构

### Content Collections

- `src/content/wwdc2024/` — WWDC 2024 文章
- `src/content/wwdc2025/` — WWDC 2025 文章
- Schema 定义在 `src/content.config.ts`，两个字段共享同一 schema
- 每篇文章 frontmatter 字段：id, title, titleZh, track, level, duration, date, thumbnail, videoUrl, tags

### 路由

- `src/pages/index.astro` — 首页，合并显示所有年份
- `src/pages/[year]/index.astro` — 年份页
- `src/pages/[year]/[id].astro` — 文章详情页
- 年份 URL 格式：`/wwdc2025/267`、`/wwdc2024/10136`

### 分类系统

- 文章原始 `track` 字段保持不变
- 显示层通过 `consolidateTrack()` 做映射合并（定义在 `src/utils/format.ts`）
- 首页侧边栏：年份用 radio 单选，分类用 checkbox 多选

## 踩过的坑

### 缩略图

**Apple CDN 只有 250x141 和 1280x720 两个尺寸可用**。700x394、720x405、400x225 等尺寸全部返回 403 Forbidden。

- 正确的 URL 格式：`https://devimages-cdn.apple.com/wwdc-services/images/{HASH}/{IMG_ID}/{IMG_ID}_wide_1280x720_2x.jpg`
- **每年 hash 不同**：WWDC 2025 用 `3055294D-836B-4513-B7B0-0BC5666246B0`，WWDC 2024 用 `C03E6E6D-A32A-41D0-9E50-C3C6059820AA`。抓取时必须从对应年份的列表页获取正确 hash，不能复用其他年份的 hash
- 缩略图来源：Apple 的 all-videos 列表页（`https://developer.apple.com/videos/all-videos/`）
- 部分 session 不在列表页（如某些 "What's new in X" session），需要用同主题的其他 session 缩略图替代
- 修复脚本：`bash scripts/fix-thumbnails.sh [--fix]`

### Content Collection

- `level` 字段只接受 `beginner`、`intermediate`、`advanced`。Apple 官网用 `introductory`，必须转换为 `beginner`
- 添加新年份需要：1) 在 content.config.ts 添加 collection 2) 在 collections.ts 添加映射 3) 更新路由的 getStaticPaths

### 样式

- Tailwind v4 preflight 会移除列表样式，`.prose ul` 和 `.prose ol` 需要显式设置 `list-style-type`
- 列表 marker 颜色用 `.prose li::marker { color: var(--color-text-tertiary); }`

### 文章生成

- Transcript 来源：Apple session 页面的 `id="transcript-content"` 区域
- 并行 agent 建议：不超过 5 个同时运行，10 个容易触发 API 速率限制（429）
- 部分 session 是宣传视频（如 "18 things from WWDC24"），transcript 无技术内容，应跳过

## 常用命令

```bash
pnpm dev          # 启动开发服务器 (localhost:4321)
pnpm build        # 构建静态站点
```
