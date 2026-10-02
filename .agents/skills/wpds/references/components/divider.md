---
title: "Divider"
description: "A divider is a thin rule or line that creates visual separation in a layout."
sourceUrl: "https://build.washingtonpost.com/components/divider"
---

# Divider

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/divider/anatomy.svg)

*Note: Image is not  to scale*

1. Divider

---

## Options

### Orientation

Dividers can be used to separate individual items in a list, or to to provide clearer visual distinction between two or more grouped elements. They can be oriented vertically or horizontally, depending on the layout in which they occur.

```jsx
return function Example() {
  return (
    <Box
      css={{
        width: "100%",
      }}
    >
      <Box
        css={{
          width: "100%",
          display: "flex",
          alignItems: "center",
          gap: "$100",
          marginBlock: "$200",
        }}
      >
        <Box css={{ color: "$accessible", fontWeight: "$normal" }}>
          Horizontal
        </Box>
        <Divider variant="strong" />
      </Box>
      <Box
        css={{
          width: "100%",
          height: "188px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          gap: "$100",
          marginBlock: "$200",
        }}
      >
        <Box css={{ color: "$accessible", fontWeight: "$normal" }}>
          Vertical
        </Box>
        <Divider variant="strong" orientation="vertical" />
      </Box>
    </Box>
  );
}
```

### Color

Sometimes it's helpful to use dividers as a means of delineating sections of a page or key areas of content. In many cases, a “strong” divider placed above the content can be used to mark the start of a new section and helps distinguish the area from the surrounding layout.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        width: "100%",
      }}
    >
      <Box
        css={{
          width: "100%",
          display: "flex",
          alignItems: "center",
          gap: "$100",
          marginBlock: "$200",
        }}
      >
        <Box css={{ color: "$accessible", fontWeight: "$normal" }}>Default</Box>
        <Divider />
      </Box>
      <Box
        css={{
          width: "100%",
          display: "flex",
          alignItems: "center",
          gap: "$100",
          marginBlock: "$200",
        }}
      >
        <Box css={{ color: "$accessible", fontWeight: "$normal" }}>Strong</Box>
        <Divider variant="strong" />
      </Box>
    </Box>
  );
}
```

## Behavior

### Fill Container

By default, a divider line should span the full horizontal or vertical dimension of its parent element. The actual height or width of the containing element should derive from its content, unless otherwise specified.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        width: "100%",
        height: "100%",
        display: "flex",
        gap: "$100",
      }}
    >
      <Box
        css={{
          backgroundColor: "$secondary",
          boxShadow: "$100",
          width: "100%",
          height: "100%",
          display: "flex",
          alignItems: "center",
        }}
      >
        <Divider />
      </Box>
      <Box
        css={{
          backgroundColor: "$secondary",
          boxShadow: "$100",
          width: "100%",
          height: "100%",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <Divider orientation="vertical" />
      </Box>
    </Box>
  );
}
```

## API Reference

## Props

#### Divider
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `variant` | `"strong" \| "default"` | No | default | Sets the color of the divider |
| `orientation` | `"horizontal" \| "vertical"` | No | — | Either `vertical` or `horizontal`. Defaults to `horizontal`. |
| `decorative` | `boolean` | No | — | Whether or not the component is purely decorative. When true, accessibility-related attributes are updated so that that the rendered element is removed from the accessibility tree. |
| `asChild` | `boolean` | No | — |  |
