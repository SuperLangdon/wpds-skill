# wpds-skill

English | [简体中文](README_CN.md)

A skill that gives coding agents accurate, source-backed knowledge of **[WPDS — The Washington Post Design System](https://build.washingtonpost.com/)**, built from the official documentation.

## Why

WPDS is far too niche for a model to recall reliably — ask an agent to write WPDS code from memory and it will invent props, tokens, and APIs. This skill ships the complete official docs (80 pages, archived 2026-10-02 from build.washingtonpost.com) together with a decision guide that makes the agent check the docs before writing any code.

## Install

```bash
pnpx skills add SuperLangdon/wpds-skill
# or
npx skills add SuperLangdon/wpds-skill
```

To install manually, copy the whole `.agents/skills/wpds/` directory into the target project's `.agents/skills/`, or into your user-level `~/.agents/skills/`.

To search the archive by hand:

```bash
python .agents/skills/wpds/scripts/search_docs.py "dark mode"
```

## Repository structure

```text
wpds-skill/
└── .agents/skills/wpds/         # The agent-discoverable skill
    ├── SKILL.md                 # Decision guide: Scope / Source Policy / Process / Output
    ├── references/              # 80 docs (79 topic docs + release notes), organized by knowledge area
    │   ├── index.md             # Routing index: a "use when" table covering every doc
    │   ├── components/          # 28 components (props tables, variants, guidance)
    │   ├── foundations/         # 13 design-token docs (space / color / typography / ...)
    │   ├── guides/              # 13 guides (React / Next.js, theming, migration)
    │   ├── accessibility/       # 10 accessibility standards
    │   ├── tutorials/           # 4 tutorials
    │   ├── tools/               # 2 tool docs
    │   ├── workshops/           # 4 workshop notes
    │   └── support/             # 6 support docs (status, releases, platforms)
    └── scripts/
        └── search_docs.py       # Dependency-free full-text search (python scripts/search_docs.py "query")
```

## Design

`SKILL.md` does not duplicate documentation content — it only tells the model **how to use** the docs:

1. **Route first** — consult `references/index.md` before anything else; when in doubt, run the search script and read only the files that are needed.
2. **Verify before writing code** — before writing any WPDS component code, read that component's props table. Inventing from memory is not allowed.
3. **Known gaps** — color-token hex values, the icon/logo catalog, and the Tachyons converter are interactive widgets on the official site and have no archived equivalent. The skill explicitly requires the agent to point to the `sourceUrl` in that case instead of making values up.
4. **Version handling** — v0/Tachyons is treated as legacy; component status (Alpha/Beta/Stable) must be checked and flagged.

## Disclaimer

> **Unofficial project**
>
> This is an unofficial community project, independently maintained by a third party. It is not affiliated with, associated with, sponsored by, authorized by, or endorsed by The Washington Post, the Washington Post Design System (WPDS), or any of their affiliates. References to "WPDS" and "Washington Post" are solely to identify the documentation source and compatibility target; all trademarks, names, documentation, and design-system content remain the property of their respective owners.
>
> The official documentation archived under `.agents/skills/wpds/references/` is for offline search and development reference only, and all rights belong to the original copyright holders. 

## License

The code and skill content in this repository (`SKILL.md`, `scripts/`, and the routing index) are released under the [MIT License](LICENSE).

The WPDS documentation archived under `.agents/skills/wpds/references/` is **not** covered by this license; all rights remain with the original rights holders.
