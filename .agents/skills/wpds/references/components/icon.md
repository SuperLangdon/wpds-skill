---
title: "Icon Component"
description: "The icon component sets the size of an icon and adds a label that will be announced by screen readers."
sourceUrl: "https://build.washingtonpost.com/components/icon"
---

# Icon Component

## Anatomy

![Icon component shown with an Add icon asset. Inspect the HTML to see the props. Or use a screen reader to read the label.](https://build.washingtonpost.com/img/components/icon/anatomy.svg)

*Icon component shown with an Add icon asset. Inspect the HTML to see the props. Or use a screen reader to read the label.*

1. Container
2. Icon glyph
3. Label [Visually Hidden](./visually-hidden.md)

---

## Options

### Size

The `size` can be `100`, `150`, or `200`. The size sets the width and height of the SVG.

```jsx
return function Example() {
  return (
    <>
      <Icon label="" size="100" fill={theme.colors.primary}>
        <ChevronRight />
      </Icon>
      <Icon label="" size="150" fill={theme.colors.primary}>
        <ChevronRight />
      </Icon>
      <Icon label="" size="200" fill={theme.colors.primary}>
        <ChevronRight />
      </Icon>
    </>
  );
}
```

### Label

The `label` is required for screen readers. It is used to describe the icon to screen readers. It is also used as the `aria-label` for the icon. It is recommended to use a short, descriptive label. For example, "Go to Next Page".

```jsx
export default function Example() {
  return (
    <>
      <Icon label="Go to Next Page" size="100" fill={theme.colors.primary}>
        <ChevronRight />
      </Icon>
      <Icon label="Go to Next Page" size="150" fill={theme.colors.primary}>
        <ChevronRight />
      </Icon>
      <Icon label="Go to Next Page" size="200" fill={theme.colors.primary}>
        <ChevronRight />
      </Icon>
    </>
  );
}
```

---

## API Reference

## Props

#### Icon
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fill` | `string \| WPDSThemeColorObject` | No | currentColor |  |
| `className` | `string` | No |  |  |
| `id` | `string` | No | — |  |
| `size` | `number \| "100" \| "150" \| "200"` | No | 100 |  |
| `label` | `string` | Yes | — | The name of the icon to display. |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `alt` | `string` | No | — |  |
