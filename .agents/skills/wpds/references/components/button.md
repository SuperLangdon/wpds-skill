---
title: "Button"
sourceUrl: "https://build.washingtonpost.com/components/button"
---

# Button

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/button/anatomy.svg)

*Note: Image is not  to scale*

1. Icon
2. Background Fill
3. Text

---

## Types

### Text buttons

Text buttons are buttons that use text paired with or without an icon.

```jsx
return function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        flexWrap: "wrap",
        gap: "$100",
      }}
    >
      <Button variant="primary" icon="left">
        <Icon size="100">
          <BookmarkSolid />
        </Icon>
        Text button
      </Button>
      <Button variant="primary" icon="right">
        <Icon size="100">
          <BookmarkSolid />
        </Icon>
        Text button
      </Button>
      <Button variant="primary">Text button</Button>
    </Box>
  );
}
```

### Icon buttons

An icon button is a button that uses only an icon.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        flexWrap: "wrap",
        gap: "$100",
      }}
    >
      <Button variant="primary" icon="center">
        <Icon size="100">
          <Add />
        </Icon>
      </Button>
    </Box>
  );
}
```

---

## Options

### Variant

There are 3 variants available `primary` `secondary` & `cta`.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        flexWrap: "wrap",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button variant="primary" icon="left">
        <Icon size="100">
          <Add />
        </Icon>
        Text button
      </Button>
      <Button variant="secondary" icon="left">
        <Icon size="100">
          <Add />
        </Icon>
        Text button
      </Button>
      <Button variant="cta" icon="left">
        <Icon size="100">
          <Add />
        </Icon>
        Text button
      </Button>
    </Box>
  );
}
```

### isOutline

Adding the property `isOutline` will set the button appearance as an outline.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button variant="primary" isOutline icon="left">
        <Icon size="100">
          <Add />
        </Icon>
        Text button
      </Button>
      <Box css={{ backgroundColor: "$gray60", padding: "$100" }}>
        <Button variant="secondary" isOutline icon="left">
          <Icon size="100">
            <Add />
          </Icon>
          Text button
        </Button>
      </Box>
      <Button variant="cta" isOutline icon="left">
        <Icon size="100">
          <Add />
        </Icon>
        Text button
      </Button>
    </Box>
  );
}
```

### Density

There are two options for the property density `compact` and `default`.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button variant="primary" density="compact" icon="left">
        <Icon size="100">
          <BookmarkSolid />
        </Icon>
        Text button
      </Button>
      <Button variant="primary" density="compact" icon="center">
        <Icon size="100">
          <BookmarkSolid />
        </Icon>
        Text button
      </Button>
      <Button variant="primary" density="default" icon="left">
        <Icon size="100">
          <BookmarkSolid />
        </Icon>
        Text button
      </Button>
      <Button variant="primary" density="default" icon="center">
        <Icon size="100">
          <BookmarkSolid />
        </Icon>
        Text button
      </Button>
    </Box>
  );
}
```

---

## Behavior

### Disabled

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button disabled variant="primary" isOutline icon="left">
        <Icon size="100">
          <Add />
        </Icon>
        Text button
      </Button>
      <Button disabled variant="primary" isOutline icon="center">
        <Icon size="100">
          <Add />
        </Icon>
      </Button>
    </Box>
  );
}
```

---

## Guidance

### Avoid small width buttons

Buttons do not have a minimum width but should still avoid being smaller than `120px`.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button variant="primary">Small</Button>
    </Box>
  );
}
```

### Mixing button densities

Buttons within the same layout should have the same `density`.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button variant="primary" density="compact">
        Compact
      </Button>
      <Button variant="primary" density="default">
        Default
      </Button>
    </Box>
  );
}
```

### Button without borders

Buttons can have no borders, but will need to be manually applied.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button
        variant="primary"
        isOutline
        css={{ border: "none" }}
        icon="center"
      >
        <Icon size="100">
          <Add />
        </Icon>
      </Button>
      <Button variant="primary" isOutline css={{ border: "none" }}>
        Text button
      </Button>
    </Box>
  );
}
```

---

## Accessiblity

### Pair icons with text

When possible use text button with an icon. The pairing of text acts as a label to help contextualize the action being taken when clicked/tapped.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Button variant="primary" icon="left">
        <Icon size="100">
          <Share />
        </Icon>
        Share
      </Button>
    </Box>
  );
}
```

---

## API Reference

## Props

#### Button
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `variant` | `"cta" \| "secondary" \| "primary"` | No | — |  |
| `density` | `"default" \| "compact"` | No | — |  |
| `isOutline` | `boolean \| "true" \| "false"` | No | — |  |
| `icon` | `"left" \| "right" \| "center" \| "none"` | No | — |  |
| `as` | `never` | No | — | WPDS provides an as prop for changing which tag a component outputs. |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
