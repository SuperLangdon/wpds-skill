# wpds-skill

[English](README.md) | 简体中文

一个为编码智能体提供准确、有据可查的 **[WPDS（The Washington Post Design System）](https://build.washingtonpost.com/)** 知识的技能，基于官方文档构建。

## 为什么需要它

WPDS 过于小众，模型凭记忆并不可靠——让智能体直接写 WPDS 代码，往往会编造 Props、令牌和 API。本技能内置完整官方文档（80 篇，2026-10-02 自 build.washingtonpost.com 存档），并附带一份决策指南，强制智能体写码前先查文档。

## 安装

```bash
pnpx skills add SuperLangdon/wpds-skill
# 或
npx skills add SuperLangdon/wpds-skill
```

手动安装：把整个 `.agents/skills/wpds/` 目录复制到目标项目的 `.agents/skills/`，或用户级 `~/.agents/skills/`。

手动检索文档：

```bash
python .agents/skills/wpds/scripts/search_docs.py "dark mode"
```

## 仓库结构

```text
wpds-skill/
└── .agents/skills/wpds/         # 可被智能体发现的技能
    ├── SKILL.md                 # 决策指南：Scope / Source Policy / Process / Output
    ├── references/              # 80 篇文档（79 篇正文 + release notes），按知识主题组织
    │   ├── index.md             # 路由索引：全部文档的 "use when" 对照表
    │   ├── components/          # 28 个组件（Props 表、变体、指南）
    │   ├── foundations/         # 13 篇设计令牌（space/color/typography/...）
    │   ├── guides/              # 13 篇指南（React/Next.js、主题、迁移）
    │   ├── accessibility/       # 10 篇无障碍标准
    │   ├── tutorials/           # 4 篇教程
    │   ├── tools/               # 2 篇工具
    │   ├── workshops/           # 4 篇工作坊记录
    │   └── support/             # 6 篇支持文档（状态、发布、平台）
    └── scripts/
        └── search_docs.py       # 零依赖全文检索（python scripts/search_docs.py "query"）
```

## 设计思路

`SKILL.md` 不复制文档内容，只规定模型**如何使用**文档：

1. **路由优先** — 先查 `references/index.md`；不确定时运行检索脚本，只读需要的文件。
2. **写码先查证** — 写任何 WPDS 组件代码前，先读该组件文档的 Props 表，禁止凭记忆编造。
3. **已知缺口** — 颜色令牌色值、图标/Logo 目录、Tachyons 转换器在官网是交互组件，存档中没有对应数据。技能明确要求此时给出文件 frontmatter 中的 `sourceUrl`，而不是编造。
4. **版本处理** — v0/Tachyons 视为遗留；组件状态（Alpha/Beta/Stable）需检查并标注。

## 免责声明

> **非官方项目**
>
> 本项目是非官方社区项目，由第三方独立维护，与《华盛顿邮报》（The Washington Post）、Washington Post Design System（WPDS）及其关联公司不存在任何隶属、合作、赞助、授权或背书关系。项目中对 "WPDS""Washington Post" 等名称的引用仅用于说明文档来源与兼容目标；相关商标、名称、文档及设计系统内容的权利归各自所有者。
>
> `.agents/skills/wpds/references/` 中的官方文档存档仅用于离线检索与开发参考，版权归原权利人所有。

## 许可证

本仓库中的代码与技能内容（`SKILL.md`、`scripts/` 及路由索引）基于 [MIT License](LICENSE) 发布。

`.agents/skills/wpds/references/` 中的 WPDS 官方文档存档**不**在本许可证覆盖范围内，版权归原权利人所有。
