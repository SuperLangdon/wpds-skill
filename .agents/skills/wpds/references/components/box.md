---
title: "Box"
description: "This component is used to create a box element with a set of default styles. It's best used in protoyping and playing with components. For production code, we recommend using \"styled\" or \"css\" functions intead."
sourceUrl: "https://build.washingtonpost.com/components/box"
---

# Box

## Options

### `as`

The `as` prop allows you to change the underlying HTML element that is rendered. This is useful for when you want to use a component that is not a `div` by default. Do not use this `as` to replace our Button component. Use the Button component for buttons.

```jsx
<Box as="span">I am a span</Box>
```

### `css`

The `css` props allows you to pass in a style object that will be applied to the underlying HTML element.

```jsx
<Box css={{ padding: "$100" }}>I am a regular ol' box.</Box>
```

---

## Guidance

### Protoyping

This component is used to create a box element with a set of default styles. It's best used in protoyping and playing with components. For production code, we recommend using "styled" or "css" functions intead. Prototyping is a great way to get started with a new project. It's a great way to get a feel for the components you'll need and how they'll work together. It's also a great way to get a feel for the design system you'll be using.

```jsx
<Box css={{ padding: "$100" }}>I am a regular ol' box.</Box>
```

### Production

For production code, we recommend using "styled" or "css" functions intead. Production code is code that is ready to be shipped to production. It's code that we can be confident will work as expected like having built in best practices like accessibility and performance.

```jsx
<Box css={{ padding: "$100" }}>I am a regular ol' box.</Box>
```

---

## Accessibility

This component is not accessible by default. You should always use the `as` prop to change the underlying HTML element to something more semantic.

```jsx
<Box as="span">I am a span</Box>
```

---

## API Reference

## Props

#### Box
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `as` | `never` | No | — | WPDS provides an as prop for changing which tag a component outputs. |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
