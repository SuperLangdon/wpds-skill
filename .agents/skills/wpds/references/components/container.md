---
title: "Container"
description: "The container centers your content horizontally. It's the most basic layout element."
sourceUrl: "https://build.washingtonpost.com/components/container"
---

# Container

## Anatomy

The anatomy of a container has no visual elements. It is an empty container used for layout and is tied to [our breakpoints](../foundations/breakpoints.md).

---

## Options

### Max width

Determine the max width of the container. The container width grows with the size of the screen. Set the container width to `fluid` for a full width container.

```jsx
<Box
  css={{
    display: "grid",
    width: "100%",
    gridTemplateRows: "1fr",
    rowGap: "$100",
    "& > *": {
      border: "1px dashed $subtle",
      background: "$alpha25",
      height: "$200",
      color: "$primary",
    },
  }}
>
  <Container maxWidth="xl">Extra lg</Container>
  <Container maxWidth="lg">lg</Container>
  <Container maxWidth="md">md</Container>
  <Container maxWidth="sm">sm</Container>
  <Container maxWidth="fluid">Fluid</Container>
</Box>
```

---

## API Reference

## Props

#### Container
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `maxWidth` | `"sm" \| "md" \| "lg" \| "xl" \| "fluid"` | No | — | the max width of them all |
| `as` | `never` | No | — | WPDS provides an as prop for changing which tag a component outputs. |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
