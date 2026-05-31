# WWDC 2025 中文总结

WWDC 2025 全部 Session 的中文技术总结站，覆盖 130+ 篇文章，每篇包含核心洞察、代码片段和迁移建议。

## 特性

- 130+ 篇 WWDC 2025 Session 中文技术博客
- 每篇文章包含：一句话判断、深度分析、代码片段、最佳实践
- Apple 风格首页布局，分类多选筛选 + 关键词搜索
- 自动适配 Dark Mode
- 缩略图使用 Apple CDN 高清资源

## 技术栈

- [Astro 5](https://astro.build) — 静态站点生成
- Tailwind CSS v4 — 样式系统
- TypeScript — 类型安全
- Vercel — 部署平台

## 本地开发

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev

# 构建
pnpm build
```

## 项目结构

```
├── src/
│   ├── content/wwdc2025/    # 133 篇 Session 文章（Markdown）
│   ├── layouts/             # 页面布局
│   ├── pages/               # 路由页面
│   ├── styles/              # 全局样式
│   └── utils/               # 工具函数
├── public/                  # 静态资源
└── scripts/                 # 文章模板
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
