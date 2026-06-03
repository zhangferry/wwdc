# WWDC Notes

WWDC Session 中文笔记站，覆盖 2020-2025 六届 WWDC，930+ 篇文章，每篇包含核心洞察、代码片段和迁移建议。

![WWDC 中文总结首页](public/screenshot.png)

## 特性

- 900+ 篇 WWDC Session 中文技术博客（2020-2025）
- 每篇文章包含：一句话判断、深度分析、代码片段、最佳实践
- Apple 风格首页布局，年份筛选 + 分类多选 + 关键词搜索
- 自动适配 Dark Mode
- 缩略图使用 Apple CDN 高清资源

## 覆盖年份

| 年份 | 文章数 |
|------|--------|
| WWDC 2025 | 133 |
| WWDC 2024 | 122 |
| WWDC 2023 | 177 |
| WWDC 2022 | 184 |
| WWDC 2021 | 207 |
| WWDC 2020 | 209 |


## WWDC Notes Skill

本项目同时维护一个可独立安装的 `wwdc-notes` skill，用于在 Codex 或 Claude 中离线查询 WWDC 2020-2025 Apple 平台开发知识。

推荐使用 `skills` CLI 安装。它会从仓库的 `skills/` 目录发现可用 skill，并提示选择 skill 与支持的 agent：

```bash
npx skills@latest add zhangferry/wwdc --skill wwdc-notes
```

## 文章结构

每篇文章遵循统一模板：

1. **一句话判断** — 这场 Session 最值得开发者关注的一件事
2. **这场 Session 讲了什么** — 核心变化的叙事式概述
3. **值得深挖的点** — 1-2 个技术点的深度分析
4. **代码片段** — 2-3 个可直接使用的代码示例
5. **最佳实践** — 针对已有项目和新项目的迁移建议
6. **还有什么值得关注** — 次要但有趣的变化

## License

MIT
