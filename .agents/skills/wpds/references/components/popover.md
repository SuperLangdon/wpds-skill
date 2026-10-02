---
title: "Popover"
description: "A popup element that displays rich and actionable content. Unlike a tooltip, the popover is persistent and remains on the screen until dismissed."
sourceUrl: "https://build.washingtonpost.com/components/popover"
---

# Popover

---

## Anatomy

![Note: Image is not to scale](https://build.washingtonpost.com/img/components/popover/anatomy.svg)

*Note: Image is not to scale*

1. Content Container

---

## Options

### Positioning

The Popover can be positioned top, left, right, and bottom with each having ability to be positioned at the start, center, or end of the trigger.

> Note:
> 
> This option sets the preferred position of the popover to render against when open. Will be reversed when collisions occur with other elements.

```jsx
return function Example() {
  const triggerCss = {
    border: "none",
    color: "$gray80",
    padding: 0,
    backgroundColor: "transparent",
    fontWeight: "normal",
    textDecoration: "underline",
    "&:hover": {
      backgroundColor: "transparent",
    },
  };
  const Grid = styled("div", {
    display: "grid",
    gridTemplateRows: "auto auto auto",
    gridTemplateColumns: "auto auto auto auto auto",
    gridTemplateAreas:
      "'leftstart topstart topcenter topend rightstart' 'leftcenter blank blank blank rightcenter' 'leftend bottomstart bottomcenter bottomend rightend'",
    gap: "40px 105px",
  });

  return (
    <Grid>
      <Box css={{ gridArea: "leftstart" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="left" align="start" width={116}>
              Left Start
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "leftcenter" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="left" align="center" width={116}>
              Left Center
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "leftend" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="left" align="end" width={116}>
              Left End
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "topstart" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="top" align="start" width={116}>
              Top Start
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "topcenter" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="top" align="center" width={116}>
              Top Center
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "topend" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="top" align="end" width={116}>
              Top End
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "bottomstart" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="bottom" align="start" width={116}>
              Bottom Start
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "bottomcenter" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="bottom" align="center" width={116}>
              Bottom Center
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "bottomend" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="bottom" align="end" width={116}>
              Bottom End
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "rightstart" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="right" align="start" width={116}>
              Right Start
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "rightcenter" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="right" align="center" width={116}>
              Right Center
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
      <Box css={{ gridArea: "rightend" }}>
        <Popover.Root open={true}>
          <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
          <Popover.Portal>
            <Popover.Content side="right" align="end" width={116}>
              Right End
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </Box>
    </Grid>
  );
}
```

### Density

There are two options for the property density compact and default.

```jsx
export default function Example() {
  const triggerCss = {
    border: "none",
    color: "$gray80",
    padding: 0,
    backgroundColor: "transparent",
    fontWeight: "normal",
    textDecoration: "underline",
    "&:hover": {
      backgroundColor: "transparent",
    },
  };
  return (
    <Box
      css={{
        display: "flex",
        gap: theme.space["500"],
      }}
    >
      <Popover.Root open={true}>
        <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
        <Popover.Portal>
          <Popover.Content width={96}>
            <Box
              css={{
                backgroundColor: theme.colors.gray500,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                height: theme.space["500"],
              }}
            >
              Default
            </Box>
          </Popover.Content>
        </Popover.Portal>
      </Popover.Root>
      <Popover.Root open={true}>
        <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
        <Popover.Portal>
          <Popover.Content density="compact" width={88}>
            <Box
              css={{
                backgroundColor: theme.colors.gray500,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                height: theme.space["500"],
              }}
            >
              Compact
            </Box>
          </Popover.Content>
        </Popover.Portal>
      </Popover.Root>
    </Box>
  );
}
```

### Offset

The property `sideOffset` can use any spacing token to offset its position from the origin point of the tooltip. The default offset is the spacing token 025.

![](https://build.washingtonpost.com/img/components/popover/offset.svg)

---

## Behavior

### Avoids collisions

When close to the edge of the viewable area the side will be reversed to be visible.

![](https://build.washingtonpost.com/img/components/popover/collisions.svg)

---

## Guidance

### Avoid using popover for non-actionable ui

Popovers should not be used to display non-actionable ui that could otherwise live in something less persistent like a tooltip.

```jsx
export default function Example() {
  return (
    <Popover.Root defaultOpen={true}>
      <Popover.Trigger icon="center" css={{ marginBlockStart: "100px" }}>
        <Icon>
          <Info />
        </Icon>
      </Popover.Trigger>
      <Popover.Portal>
        <Popover.Content side="top">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Diam non eget
          consequat pretium.
        </Popover.Content>
      </Popover.Portal>
    </Popover.Root>
  );
}
```

### Do not nest Popovers or Tooltips

Popovers should not have additional tooltips or popovers within the same content container.

```jsx
export default function Example() {
  const triggerCss = {
    border: "none",
    color: "$gray80",
    padding: 0,
    backgroundColor: "transparent",
    fontWeight: "normal",
    textDecoration: "underline",
    "&:hover": {
      backgroundColor: "transparent",
    },
  };

  return (
    <Popover.Root defaultOpen={true}>
      <Popover.Trigger css={triggerCss}>Trigger</Popover.Trigger>
      <Popover.Portal>
        <Popover.Content>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.{" "}
          <Tooltip.Provider>
            <Tooltip.Root>
              <Tooltip.Trigger>
                <u>Hover over me</u>
              </Tooltip.Trigger>
              <Tooltip.Content>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </Tooltip.Content>
            </Tooltip.Root>
          </Tooltip.Provider>
          non eget consequat pretium.
        </Popover.Content>
      </Popover.Portal>
    </Popover.Root>
  );
}
```

---

## Accessibility

### Keyboard controls

A Popover will show/hide without delay when the trigger is in focus and space/enter is selected on the keyboard. If the Popover is open and either shift+tab, or tab, is selected on the keyboard it will move focus to the next focusable element. When Esc is selected on the keyboard it will close the popover and move the focus to the trigger.

---

## API Reference

## Props

#### PopoverAnchor
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `asChild` | `boolean` | No | — |  |
| `virtualRef` | `RefObject<Measurable>` | No | — |  |

#### PopoverClose
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

#### PopoverContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `sideOffset` | `number \| Token<"100" \| "125" \| "150" \| "175" \| "200" \| "225" \| "250" \| "275" \| "300" \| "350" \| "400" \| "450" \| "500" \| "075" \| "087" \| "025" \| "050", string, "space", "wpds">` | No | theme.space[025] | Distance between trigger and content |
| `width` | `number` | No | 240 | Width of the popover content |
| `density` | `"default" \| "compact"` | No | default |  |
| `sticky` | `"always" \| "partial"` | No | — |  |
| `asChild` | `boolean` | No | — |  |
| `side` | `"bottom" \| "left" \| "right" \| "top"` | No | — |  |
| `align` | `"center" \| "end" \| "start"` | No | — |  |
| `alignOffset` | `number` | No | — |  |
| `arrowPadding` | `number` | No | — |  |
| `avoidCollisions` | `boolean` | No | — |  |
| `collisionBoundary` | `Element \| Element[]` | No | — |  |
| `collisionPadding` | `number \| Partial<Record<"bottom" \| "left" \| "right" \| "top", number>>` | No | — |  |
| `hideWhenDetached` | `boolean` | No | — |  |
| `updatePositionStrategy` | `"always" \| "optimized"` | No | — |  |
| `onEscapeKeyDown` | `(event: KeyboardEvent) => void` | No | — | Event handler called when the escape key is down. Can be prevented. |
| `onPointerDownOutside` | `(event: PointerDownOutsideEvent) => void` | No | — | Event handler called when the a `pointerdown` event happens outside of the `DismissableLayer`. Can be prevented. |
| `onFocusOutside` | `(event: FocusOutsideEvent) => void` | No | — | Event handler called when the focus moves outside of the `DismissableLayer`. Can be prevented. |
| `onInteractOutside` | `(event: PointerDownOutsideEvent \| FocusOutsideEvent) => void` | No | — | Event handler called when an interaction happens outside the `DismissableLayer`. Specifically, when a `pointerdown` event happens outside or focus moves outside of it. Can be prevented. |
| `onOpenAutoFocus` | `(event: Event) => void` | No | — | Event handler called when auto-focusing on open. Can be prevented. |
| `onCloseAutoFocus` | `(event: Event) => void` | No | — | Event handler called when auto-focusing on close. Can be prevented. |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### PopoverPortal
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `container` | `Element \| DocumentFragment` | No | — | Specify a container element to portal the content into. |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### PopoverRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `open` | `boolean` | No | — |  |
| `defaultOpen` | `boolean` | No | — |  |
| `onOpenChange` | `(open: boolean) => void` | No | — |  |
| `modal` | `boolean` | No | — |  |

#### PopoverTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

```jsx
``
```
