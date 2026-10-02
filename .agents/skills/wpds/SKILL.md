---
name: wpds
description: >
  Domain knowledge and decision guide for WPDS, The Washington Post Design System
  (build.washingtonpost.com). Use whenever the user mentions WPDS, the Washington Post
  design system, @washingtonpost/wpds-ui-kit, wpds-assets, wpds-tailwind-theme, WPDS
  components (Button, Accordion, Dialog, Tooltip, Carousel, ...), WPDS design tokens,
  Stitches styling, theme colors, breakpoints, Tachyons-to-Stitches migration, or asks
  how to build/access WPDS UI in React or Next.js — even if they don't say "WPDS" and
  just ask about a component name that exists in this system.
---

# WPDS — The Washington Post Design System

WPDS is the design system of The Washington Post: a React + TypeScript component
library styled with Stitches, plus design tokens and usage guidance. The complete
documentation (80 documents archived 2026-10-02 from build.washingtonpost.com) lives
in this skill's `references/` — treat it as the source of truth, not your training
data, because WPDS is too niche for reliable recall.

## Scope

This skill covers:

- WPDS components: anatomy, props, variants, behavior, guidance, accessibility notes
- Design tokens: space, size, color, typography, radius, shadow, z-index, breakpoints
- Setup and usage: installing `@washingtonpost/wpds-ui-kit`, SSR, theming, icons
- Migrations: Tachyons → Stitches, old palette → unified palette, v0 → v1
- Accessibility guidance for WPDS-based products
- Design-side workflows: Figma, Zeplin, slots, user education
- Process: contributing components, release cycles, component status

It does not cover:

- Generic React/Next.js/TypeScript questions unrelated to WPDS
- The deprecated WPDS v0 API (only its status — see Version handling)
- Non-WPDS component libraries (MUI, Ant Design, Chakra, ...)

## Key facts

Keep these in mind; they prevent the most common mistakes:

- Install: `npm install @stitches/react @washingtonpost/wpds-ui-kit`.
  Icons come from `@washingtonpost/wpds-assets` (e.g.
  `import Add from "@washingtonpost/wpds-assets/asset/add"`).
- SSR is mandatory in Next.js: call `getCssText()` from
  `@washingtonpost/wpds-ui-kit` into the document `<head>` to avoid FOUC
  (`references/guides/react-guide.md`).
- Token access, two equivalent forms:
  - in a `css` object or the `css` prop: shorthand strings — `gap: "$100"`,
    `"@sm": { ... }` for media queries (`@initial` for the base state)
  - in `styled()` or TS logic: the `theme` object — `theme.space["100"]`,
    `theme.colors.primary`, `theme.fonts.headline`
- Every WPDS component accepts a `css` prop for token-aware overrides.
- `baseSize` is 16px; all numeric scale tokens are multiples of it
  (`$100` = 1rem = 16px, `$050` = 8px, `$125` = 20px, `$round` = 9999px).
- Breakpoints: sm 768 / md 900 / lg 1024 / xl 1280 / xxl 1440.
  Mobile-first aliases exist (`minSm`, `minMd`, ... = the breakpoint and above).
- Icons must be wrapped in the `Icon` component (`<Icon label="..." size="$100">`)
  so screen readers announce them; raw SVG usage is an accessibility bug.

## Known gaps in the archive — never invent these

The official site rendered some content as interactive widgets that do not export to
markdown. They appear as `<!-- Name: interactive component, rendered on the official
site only -->` placeholders. The archive therefore does NOT contain:

- **Color token values.** Semantic structure, naming (`primary`, `onPrimary`,
  `accessible`, `gray700`, ...), and usage rules ARE documented, but the actual hex
  values are not. Never output a WPDS hex value from memory — say the values aren't
  archived and point to the `sourceUrl` in the file's frontmatter.
- **The icon and logo catalogs** (names of available assets). Use WAM /
  `@washingtonpost/wpds-assets` and the sourceUrl instead.
- **The Tachyons→Stitches converter output.** The migration guide documents the
  mapping rules by hand.

The same applies to any `<!-- ... interactive component ... -->` you encounter: read
around it, and treat its content as missing rather than reconstructing it.

## Version handling

- WPDS v1 is current. v0 (2018–2019) is deprecated, legacy-only — if a user shows v0
  code or old Tachyons classes, route to the migration guides, and never present v0
  behavior as current.
- Components carry a lifecycle status: Coming soon / Alpha (breaking changes
  expected) / Beta (stable API, docs final) / Stable (no banner shown). Check the top
  of the component doc; when a component is Alpha, say so in the answer.
- Package versions: `references/support/release-notes.md` links to the npm/GitHub
  release histories. Do not cite specific version numbers that are not in the docs.

## Source policy

Priority when sources conflict:

1. `references/` documentation (the archived official docs)
2. The user's project code, when they share it — reflect what they actually have
3. The official site via the file's `sourceUrl` frontmatter (for archive gaps)

Never:

- Invent props, token names, variants, or behaviors that are not in the docs.
  The Props table at the bottom of each component page is the authority.
- Mix WPDS conventions with generic Stitches or other libraries' conventions.
- Guess at content behind an interactive-component placeholder (see above).

If the documentation does not answer the question, say exactly that ("not documented
in the archived WPDS docs") and, where useful, point to the sourceUrl.

## Process

1. **Classify the request**: component usage · tokens/styling · project setup ·
   migration · accessibility · design-side (Figma/Zeplin) · process/status.
2. **Route**: look up the topic in `references/index.md` (the routing table for all
   80 documents). Go directly to a known file when confident. When unsure where a
   term lives, run the search script:
   `python scripts/search_docs.py "your terms"` from this skill's directory.
3. **Read only what you need** — usually one component doc or one foundation doc.
   Do not read the whole library for a single question.
4. **Verify before answering**: confirm names against the Props / token tables, and
   check the doc's Guidance and Accessibility sections for constraints.
5. **Answer** following the output conventions below.

## Writing WPDS code

Do not write WPDS component code from memory. Before generating any component code:

1. Open that component's doc in `references/components/` and read its Props table.
2. Use exact prop names/values from the table (`variant="cta"`, `icon="left"`,
   `density="compact"`, ...).
3. Prefer tokens over raw values (`gap: "$100"`, not `gap: "16px"`), except where
   the docs themselves use raw values (e.g. the 120px button min-width guidance).
4. Import icons via `@washingtonpost/wpds-assets` and wrap them in `Icon` with a
   `label` when they carry meaning.
5. Respect the component doc's Guidance section (e.g. don't mix button densities;
   pair icon buttons with text when possible; carousels need ≥ 4 items).

## Output conventions

For code answers: JSX with correct imports, tokens instead of raw values, and a note
when the component status is not Stable.

For knowledge answers: lead with the direct answer, then details, then cite the
reference file path(s) used, e.g. `(references/components/button.md)`.

For undocumented questions: state clearly what is missing and give the sourceUrl.

## References

| Path | Use when |
| --- | --- |
| `references/index.md` | Routing table for the entire library — start here |
| `references/components/*.md` | Any component: props, variants, guidance (28 docs) |
| `references/foundations/*.md` | Tokens: space, size, color, type, radius, shadow, z-index, breakpoints, icons, WAM (13 docs) |
| `references/guides/*.md` | React/Next.js setup, coding a page, theming, Stitches rationale, migrations, Figma/Zeplin (13 docs) |
| `references/accessibility/*.md` | A11y standards: alt text, contrast, keyboard, screen readers, ARIA (10 docs) |
| `references/tutorials/*.md` | Hands-on walkthroughs: theme tokens, slots, carousel, a11y audit (4 docs) |
| `references/tools/*.md` | Tachyons converter, Tailwind theme (2 docs) |
| `references/workshops/*.md` | Recorded design/developer workshop transcripts (4 docs) |
| `references/support/*.md` | Component status, release cycles, supported platforms, get help, v0, release notes (6 docs) |
| `scripts/search_docs.py` | Full-text search across all references when routing is unclear |

## Final verification

Before finishing an answer:

- [ ] Claims come from `references/`, not memory
- [ ] No invented props, tokens, or hex values (color values are not archived)
- [ ] Component status checked; Alpha components flagged
- [ ] v0/Tachyons treated as legacy, routed to migration guides
- [ ] Code uses exact prop names from the Props table and tokens over raw values
- [ ] Source file path cited
