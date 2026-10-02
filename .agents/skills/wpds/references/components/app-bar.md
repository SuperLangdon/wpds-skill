---
title: "App bar"
description: "The App Bar displays information and actions relating to the current screen."
sourceUrl: "https://build.washingtonpost.com/components/app-bar"
---

# App bar

## Anatomy

The anatomy of an app bar has no visual elements but rather is an empty container that has a built-in utility to make positioning on a layout easier.

---

## Options

### Position

The following position are available `sticky` `relative` `absolute` `fixed`. The behavior of the different options are described in the [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/CSS/position).

```jsx
return function Example() {
  return (
    <AppBar
      shadow
      position="sticky"
      css={{
        top: 0,
        left: 0,
      }}
    >
      <Container
        maxWidth="fluid"
        css={{
          height: 60,
          background: "$secondary",
          color: "$onSecondary",
          flexDirection: "row",
          textAlign: "center",
          justifyContent: "space-between",
          px: "$100",
        }}
      >
        <Icon size="$200" label="Open Section Navigation Menu">
          <Menu />
        </Icon>
        <Box
          css={{
            fill: "$onSecondary",
          }}
        >
          <WashingtonPost width={188} />
          <Box
            css={{
              fontFamily: "$body",
              fontSize: "$075",
              fontStyle: "italic",
            }}
          >
            Democracy Dies in Darkness (This is an example using the new system)
          </Box>
        </Box>
        <Icon size="$200" label="Open Account Menu">
          <Profile />
        </Icon>
      </Container>
    </AppBar>
  );
}
```

---

## API Reference

## Props

#### AppBar
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `position` | `"fixed" \| "absolute" \| "relative" \| "sticky"` | No | — | App bar's position in time and space |
| `shadow` | `boolean \| "true"` | No | — | App bar's shadow in time and space |
| `as` | `never` | No | — | WPDS provides an as prop for changing which tag a component outputs. |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
