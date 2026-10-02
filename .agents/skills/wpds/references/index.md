# WPDS Documentation Index

Routing table for the full WPDS archive (80 documents, exported 2026-10-02 from
build.washingtonpost.com). Every file's frontmatter carries its official `sourceUrl`.

How to use this index: match the topic column, open the one file you need, read its
Props/token tables. If several candidates match or nothing does, run
`python scripts/search_docs.py "<terms>"` from the skill root instead of reading files
at random.

Legend for known gaps: ⚠ = page contains interactive-component placeholders, so some
content (color values, asset catalogs) is not in the archive — see SKILL.md.

## Foundations — design tokens (13)

| Topic | File | Use when |
| --- | --- | --- |
| Design principles | `foundations/principles.md` | Why WPDS exists; reusable/functional/adaptable/predictable/accessible principles |
| Base size | `foundations/base.md` | The 16px root value that space/size/font/radius scales derive from |
| Space | `foundations/space.md` | Padding/margin tokens `$025`–`$500` (values included) |
| Size | `foundations/size.md` | Fixed width/height tokens `theme.sizes` (values included) |
| Color | `foundations/color.md` ⚠ | Color semantics (primary/onPrimary/accessible/surface), contrast targets, light/dark — hex values NOT archived |
| Typography | `foundations/typography.md` | Font families (Postoni/Franklin/georgia), sizes, weights, line heights (values included) |
| Radius | `foundations/radius.md` | `borderRadius` tokens incl. `$round` (values included) |
| Shadow | `foundations/shadow.md` | Box-shadow tokens `$050`–`$500` (values included) |
| Z-index | `foundations/z-index.md` | Layering tokens for overlays, portals, menus |
| Breakpoints | `foundations/breakpoints.md` ⚠ | sm/md/lg/xl/xxl values, media at-rules, mobile-first `minSm` aliases |
| Icons | `foundations/icons.md` ⚠ | Icon assets — catalog itself not archived; use WAM |
| Logos | `foundations/logos.md` ⚠ | Logo assets — catalog itself not archived; use WAM |
| Asset manager | `foundations/wam.md` | WAM package: how SVG assets are managed and contributed |

## Components (28)

| Topic | File | Use when |
| --- | --- | --- |
| Accordion | `components/accordion.md` | Expand/collapse content sections |
| Action Menu | `components/action-menu.md` | Overlay menu of commands executed on selection; needs a trigger |
| Alert Banner | `components/alert-banner.md` | System alerts that prompt user action |
| App bar | `components/app-bar.md` | Top bar with info/actions for the current screen |
| Avatar | `components/avatar.md` | Round container for a profile image |
| Box | `components/box.md` | Prototyping box with default styles — NOT for production (use `styled`/`css`) |
| Button | `components/button.md` | Variants primary/secondary/cta, `isOutline`, `density`, `icon` placement |
| Card | `components/card.md` | Contained unit holding related elements |
| Carousel | `components/carousel.md` | Linear sequence of ≥4 items with prev/next navigation |
| Checkbox | `components/checkbox.md` | Binary/multiple selection; sizes `125`/`087` |
| Container | `components/container.md` | Horizontally centered layout wrapper |
| Dialog | `components/dialog.md` | Modal overlay requiring user action |
| Divider | `components/divider.md` | Thin rule separating layout regions |
| Drawer | `components/drawer.md` | Off-canvas panel sliding from a screen edge |
| Icon component | `components/icon.md` | Wrapping SVGs for size + screen-reader labels |
| Input Password | `components/input-password.md` | Password field with show/hide toggle, helper text |
| Input Search | `components/input-search.md` | Keyword entry with results (largest component doc) |
| Input Text | `components/input-text.md` | Single-line text field |
| Input Text Area | `components/input-textarea.md` | Multi-line long-form text |
| Navigation Menu | `components/navigation-menu.md` | Group of links for page/section navigation |
| Pagination Dots | `components/pagination-dots.md` | Progress dots through a range of elements |
| Popover | `components/popover.md` | Persistent popup with rich content (vs tooltip) |
| Radio Group | `components/radio-group.md` | Mutually exclusive single selection |
| Select | `components/select.md` | Choosing one item from a list of options |
| Switch | `components/switch.md` | Binary on/off toggle |
| Tabs | `components/tabs.md` | Switching content sections without reload |
| Tooltip | `components/tooltip.md` | Non-actionable informational text on hover |
| Visually Hidden | `components/visually-hidden.md` | Content hidden visually, kept for screen readers |

## Guides — how to build with WPDS (13)

| Topic | File | Use when |
| --- | --- | --- |
| React Guide | `guides/react-guide.md` | Installing the UI Kit, SSR `getCssText()`, first styled component, `theme` object |
| Coding a page | `guides/coding-a-page.md` | Full page build with Next.js + UI Kit; variants + `@sm`/`@initial` responsive props |
| Stitches rationale | `guides/stitches.md` | Why WPDS chose Stitches |
| Theming | `guides/themes.md` | Using Stitches to style projects via the UI Kit |
| Migrating Tachyons→Stitches | `guides/tachyons-stitches.md` | Conceptual differences between the two styling approaches |
| Migrating to new palette | `guides/migrating-to-our-new-palette.md` | Old v1/v0 color tokens → unified palette |
| Creating custom icons | `guides/creating-custom-icons.md` | Using your own SVGs in the Icon component |
| Contribute a component | `guides/contribute-a-component.md` | Process for contributing components to WPDS |
| Figma guide | `guides/figma-guide.md` | Designing with the WPDS Figma library |
| Zeplin guide | `guides/zeplin-guide.md` | Design-to-code handoff with Zeplin |
| User education | `guides/user-education.md` | Choosing components for onboarding/education experiences |
| Emoji guide | `guides/emoji-guide.md` | Emoji decisions in product/marketing contexts |
| Performance & SEO | `guides/performance-and-seo.md` | Web performance and SEO best practices |

## Accessibility standards (10)

| Topic | File | Use when |
| --- | --- | --- |
| Checklist | `accessibility/accessibility-checklist.md` | Overall a11y review checklist |
| Alt text | `accessibility/alt-text.md` | Describing images for blind/low-vision users |
| Audio & video | `accessibility/audio-and-video.md` | Captions, transcripts, controls, no autoplay |
| Automated testing | `accessibility/automated-testing.md` | Tooling that catches some a11y issues |
| Color | `accessibility/color.md` | Contrast, colorblindness, light/dark mode |
| Keyboard | `accessibility/keyboard-accessibility.md` | Navigation without a mouse |
| Plain language | `accessibility/plain-language-and-labeling.md` | Inclusive writing, symbols, form labels |
| Screen readers | `accessibility/screen-readers.md` | How to test with screen readers |
| Semantic HTML | `accessibility/semantic-html.md` | Heading order, tables, labels, ARIA |
| Text size & zoom | `accessibility/text-size-and-zoom.md` | Responsive fonts and zoom settings |

## Tutorials (4)

| Topic | File | Use when |
| --- | --- | --- |
| Theme tokens | `tutorials/how-to-use-our-theme.md` | How theme tokens abstract color intention |
| Slots | `tutorials/how-to-use-slots.md` | Nesting patterns in the Figma UI kit |
| Carousel in Figma | `tutorials/carousel.md` | Configuring the Carousel component in designs |
| 5-minute a11y audit | `tutorials/five-minute-accessibility-audit.md` | Quick audits for color, sizing, keyboard, screen readers |

## Tools (2)

| Topic | File | Use when |
| --- | --- | --- |
| Tachyons converter | `tools/tachyons-to-stitches.md` ⚠ | Online Tachyons→Stitches converter (the tool itself is not archived) |
| Tailwind theme | `tools/tailwind-theme.md` | Tailwind CSS theme built on WPDS tokens |

## Workshops — recorded sessions (4)

| Topic | File | Use when |
| --- | --- | --- |
| Design workshop 1 | `workshops/design_3-16-22.md` | WPDS v1 design rollout |
| Design workshop 2 | `workshops/design_4-6-22.md` | Continued design deep-dive |
| Developer workshop 1 | `workshops/developer_3-17-22.md` | WPDS v1 developer rollout |
| Developer workshop 2 | `workshops/developer_4-7-22.md` | Same topics, different approach |

## Support & process (6)

| Topic | File | Use when |
| --- | --- | --- |
| Component status | `support/component-status.md` | Coming soon / Alpha / Beta / Stable lifecycle meanings |
| Release cycles | `support/release-cycles.md` | Patch weekly / minor monthly / major quarterly; docs = supported |
| Supported platforms | `support/supported-platforms.md` | Browsers, Node 16/18, React 18, Next.js 14+, TS ≥ 3.8 |
| Legacy v0 | `support/legacy-v0.md` | v0 deprecation status |
| Get help | `support/get-help.md` | Slack #wpds, GitHub issues, wpds@washingtonpost.com |
| Release notes | `support/release-notes.md` | Links to npm/GitHub release histories |
