---
title: "Drawer"
description: "A drawer is a panel that is typically overlaid on top of a page and slides in from off-canvas (tied to a side of the screen). It contains a set of information or actions. Since the user can interact with the Drawer without leaving the current page, tasks can be achieved more efficiently within the same context."
sourceUrl: "https://build.washingtonpost.com/components/drawer"
---

# Drawer

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/drawer/anatomy.svg)

*Note: Image is not  to scale*

1. Container
2. Button icon
3. Scrim

---

## Options

### Position

The drawer can be attached to any side of the screen.

```jsx
return function Example() {
  return (
    <Box
      css={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Drawer.Root id="top-id">
        <Drawer.Trigger css={{ minWidth: "93px" }}>Top</Drawer.Trigger>
        <Drawer.Content position="top" height="200px">
          Your Drawer Content. Click scrim to close
        </Drawer.Content>
        <Drawer.Scrim />
      </Drawer.Root>
      <Box
        css={{
          display: "flex",
          gap: "$050",
          marginBlock: "$050",
        }}
      >
        <Drawer.Root id="left-id">
          <Drawer.Trigger css={{ minWidth: "93px" }}>Left</Drawer.Trigger>
          <Drawer.Content position="left">
            Your Drawer Content. Click scrim to close
          </Drawer.Content>
          <Drawer.Scrim />
        </Drawer.Root>
        <Drawer.Root id="right-id">
          <Drawer.Trigger css={{ minWidth: "93px" }}>Right</Drawer.Trigger>
          <Drawer.Content position="right">
            Your Drawer Content. Click scrim to close
          </Drawer.Content>
          <Drawer.Scrim />
        </Drawer.Root>
      </Box>
      <Drawer.Root id="bottom-id">
        <Drawer.Trigger css={{ minWidth: "93px" }}>Bottom</Drawer.Trigger>
        <Drawer.Content position="bottom" height="200px">
          Your Drawer Content. Click scrim to close
        </Drawer.Content>
        <Drawer.Scrim />
      </Drawer.Root>
    </Box>
  );
}
```

### Optional Close

The drawer close button icon can be optional.

```jsx
export default function Example() {
  return (
    <Drawer.Root id="optional-close">
      <Box css={{ display: "flex", flexDirection: "column", gap: "$100" }}>
        <Drawer.Trigger>See example</Drawer.Trigger>
        <p>Click button to see option</p>
      </Box>
      <Drawer.Content height="200px">
        Close is optional. Click outside the drawer to close click the scrim to
        close the drawer.
      </Drawer.Content>
      <Drawer.Scrim />
    </Drawer.Root>
  );
}
```

### Optional Scrim

The scrim is optional when using the drawer. Should note that without a scrim, it is recommended to have a close button to ensure users can close the drawer if that is desired.

```jsx
export default function Example() {
  return (
    <Drawer.Root id="optional-scrim">
      <Box css={{ display: "flex", flexDirection: "column", gap: "$100" }}>
        <Drawer.Trigger>See example</Drawer.Trigger>
        <p>Click button to see option</p>
      </Box>
      <Drawer.Content height="200px">
        <Drawer.Close />
        Scrim is optional
      </Drawer.Content>
    </Drawer.Root>
  );
}
```

### Optional Scrim color

The scrim color can be changed by defining the color using one of our background colors from our tokens

```jsx
export default function Example() {
  return (
    <Drawer.Root id="scrim-color">
      <Box css={{ display: "flex", flexDirection: "column", gap: "$100" }}>
        <Drawer.Trigger>See example</Drawer.Trigger>
        <p>Click button to see option</p>
      </Box>
      <Drawer.Content height="200px">
        <Drawer.Close />
        This uses red500 as the scrim background
      </Drawer.Content>
      <Drawer.Scrim css={{ backgroundColor: "$red500" }} />
    </Drawer.Root>
  );
}
```

### Drawer color

The drawer color can be changed by defining the color using one of our background colors from our tokens.

```jsx
export default function Example() {
  return (
    <Drawer.Root id="background-color">
      <Box css={{ display: "flex", flexDirection: "column", gap: "$100" }}>
        <Drawer.Trigger>See example</Drawer.Trigger>
        <p>Click button to see option</p>
      </Box>
      <Drawer.Content
        height="200px"
        css={{ backgroundColor: "$primary", color: "$onPrimary" }}
      >
        <Drawer.Close /> A dark drawer
      </Drawer.Content>
      <Drawer.Scrim />
    </Drawer.Root>
  );
}
```

### Height and Width

Drawer width and height can be defined. Height can be defined if the position is `top` or `bottom` and width can be defined if the position is `right` or `left`.

```jsx
export default function Example() {
  return (
    <Box css={{ display: "flex", flexDirection: "column", gap: "$100" }}>
      <Drawer.Root id="set-height">
        <Drawer.Trigger>See bottom example</Drawer.Trigger>
        <Drawer.Content height="200px">
          This drawer is set to 200px height.
        </Drawer.Content>
        <Drawer.Scrim />
      </Drawer.Root>
      <Drawer.Root id="set-width">
        <Drawer.Trigger>See left example</Drawer.Trigger>
        <Drawer.Content width="200px" position="left">
          This drawer is set to 200px width.
        </Drawer.Content>
        <Drawer.Scrim />
      </Drawer.Root>
    </Box>
  );
}
```

---

## Behavior

### Closing

When the close button icon is rendered, the drawer can be closed by either clicking the scrim or the close button. Note: The drawer can be set to open and will remain open even if the scrim is clicked on.

```jsx
export default function Example() {
  return (
    <Drawer.Root id="close-options">
      <Drawer.Trigger>Scrim / button to close</Drawer.Trigger>
      <Drawer.Content height="200px">
        <Drawer.Close />
        Click scrim or button to close
      </Drawer.Content>
      <Drawer.Scrim />
    </Drawer.Root>
  );
}
```

### Content overflow

Content will overflow, both vertically and horizontally, in the drawer by default.

```jsx
export default function Example() {
  return (
    <Drawer.Root id="overflow">
      <Drawer.Trigger>See drawer with overflow</Drawer.Trigger>
      <Drawer.Content height="200px">
        <Drawer.Close />
        <Box
          css={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            height: "100vh",
          }}
        >
          Overflow by scrolling
        </Box>
      </Drawer.Content>
      <Drawer.Scrim />
    </Drawer.Root>
  );
}
```

---

## Guidance

### Content should be accessible

Do not combine colors of the drawer where text is not accessible to the user. Read more about [WCAG accessible contrast requirements](https://webaim.org/articles/contrast/).

```jsx
export default function Example() {
  return (
    <Drawer.Root id="low-contrast">
      <Drawer.Trigger>See bad example</Drawer.Trigger>
      <Drawer.Content
        css={{ backgroundColor: "$primary", color: "$onDisabled" }}
        height="200px"
      >
        <Drawer.Close /> Text should be accessible
      </Drawer.Content>
      <Drawer.Scrim />
    </Drawer.Root>
  );
}
```

### Avoid full screen

A drawer should never take the fullscreen of the viewer window. The drawer should always leave at least 1/3 of the screen available.

```jsx
export default function Example() {
  return (
    <Drawer.Root id="fullscreen">
      <Drawer.Trigger>See example</Drawer.Trigger>
      <Drawer.Content>
        <Drawer.Close /> Click close button to close
      </Drawer.Content>
    </Drawer.Root>
  );
}
```

---

## API Reference

## Props

#### DrawerRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | Yes | — | content id used for a11y |
| `onOpenChange` | `(boolean: any) => void` | No | — | callback to respond to open state |
| `zIndex` | `ZIndex \| Token<"shell", string, "zIndices", "wpds">` | No | 300 | Css z-index of drawer @default theme.zIndices.shell |
| `open` | `boolean` | No | — | controlled drawer open state, used with onOpenChange |
| `defaultOpen` | `boolean` | No | — | uncontrolled drawer open on mount |

#### DrawerContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `height` | `number \| "auto"` | No | 500 | Height for a top or bottom positioned drawer  @default 500 |
| `position` | `"bottom" \| "left" \| "right" \| "top"` | No | bottom |  |
| `width` | `number \| "auto"` | No | 400 | Width for a left or right positioned drawer  @default 400 |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `innerClassName` | `string` | No | — | Additional class names for inner drawer element |
| `loopFocus` | `boolean` | No | true | When `true`, tabbing from last item will focus first tabbable and shift+tab from first item will focus last tababble. @defaultValue true |
| `trapFocus` | `boolean` | No | false | When `true`, focus cannot escape the `Content` via keyboard, pointer, or a programmatic focus  @defaultValue false |

#### DrawerTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `icon` | `"left" \| "right" \| "center" \| "none"` | No | — |  |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `variant` | `"cta" \| "secondary" \| "primary"` | No | — |  |
| `density` | `"default" \| "compact"` | No | — |  |
| `isOutline` | `boolean \| "true" \| "false"` | No | — |  |

#### DrawerClose
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sticky` | `(boolean \| "true"` | No | true |  |
| `icon` | `("left" \| "right" \| "center" \| "none"` | No | center |  |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `variant` | `("cta" \| "secondary" \| "primary"` | No | secondary |  |
| `density` | `("default" \| "compact"` | No | compact |  |
| `isOutline` | `boolean \| "true" \| "false"` | No | — |  |

#### DrawerCustomTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `as` | `string` | No | — | WPDS provides an as prop for changing which tag a component outputs. |

#### DrawerScrim
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `lockScroll` | `boolean` | No | — | Whether scrollbars should be hidden and scroll locked when the scrim is shown @default true |
