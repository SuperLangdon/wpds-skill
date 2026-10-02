---
title: "Tooltip"
description: "Non-actionable UI element that only contains text and does not require the user to take action but serves only to inform the user before taking an action, contextualizing an action, or act as simply supplementary information to an element."
sourceUrl: "https://build.washingtonpost.com/components/tooltip"
---

# Tooltip

---

## Anatomy

![Note: Image is not to scale](https://build.washingtonpost.com/img/components/tooltip/anatomy.svg)

*Note: Image is not to scale*

1. Content Container
2. Arrow

---

## Options

### Positioning

The tooltip can be positioned top, left, right, and bottom with each having ability to position at the start, or end of the content container.

> **Note: **This option sets the preferred position of the tooltip to render against when open. Will be reveresed when collisions occur with other elements.

```jsx
return function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
        gap: "$350",
        height: "300px",
      }}
    >
      <Box>
        <Tooltip.Provider>
          <Tooltip.Root defaultOpen={true}>
            <Tooltip.Trigger>
              <Box
                css={{
                  height: "100px",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                Trigger
              </Box>
            </Tooltip.Trigger>
            <Tooltip.Content side="left" align="start" offsetAlign="5.8rem">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Left-Start
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
            <Tooltip.Content side="left">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Left-Center
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
            <Tooltip.Content side="left" align="end" offsetAlign="5.8rem">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Left-End
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
          </Tooltip.Root>
        </Tooltip.Provider>
      </Box>
      <Box>
        <Tooltip.Provider>
          <Tooltip.Root defaultOpen={true}>
            <Tooltip.Trigger>
              <Box
                css={{
                  height: "70px",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                Trigger
              </Box>
            </Tooltip.Trigger>
            <Tooltip.Content side="top" align="end" sideOffset={"0rem"}>
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Top-End
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
            <Tooltip.Content side="bottom" align="end" sideOffset={"0rem"}>
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Bottom-End
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
          </Tooltip.Root>
        </Tooltip.Provider>
      </Box>
      <Box>
        <Tooltip.Provider>
          <Tooltip.Root defaultOpen={true}>
            <Tooltip.Trigger>
              <Box
                css={{
                  height: "70px",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                Trigger
              </Box>
            </Tooltip.Trigger>
            <Tooltip.Content side="top" sideOffset={"0rem"}>
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Top-Center
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
            <Tooltip.Content side="bottom" sideOffset={"0rem"}>
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Bottom-Center
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
          </Tooltip.Root>
        </Tooltip.Provider>
      </Box>
      <Box>
        <Tooltip.Provider>
          <Tooltip.Root defaultOpen={true}>
            <Tooltip.Trigger>
              <Box
                css={{
                  height: "70px",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                Trigger
              </Box>
            </Tooltip.Trigger>
            <Tooltip.Content side="top" align="start" sideOffset={"0rem"}>
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Top-Start
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
            <Tooltip.Content side="bottom" align="start" sideOffset={"0rem"}>
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Bottom-Start
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
          </Tooltip.Root>
        </Tooltip.Provider>
      </Box>
      <Box>
        <Tooltip.Provider>
          <Tooltip.Root defaultOpen={true}>
            <Tooltip.Trigger>
              <Box
                css={{
                  height: "100px",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                Trigger
              </Box>
            </Tooltip.Trigger>
            <Tooltip.Content side="right" align="start" offsetAlign="5.8rem">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Right-Start
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
            <Tooltip.Content side="right">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Right-Center
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
            <Tooltip.Content side="right" align="end" offsetAlign="5.8rem">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Right-End
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
          </Tooltip.Root>
        </Tooltip.Provider>
      </Box>
    </Box>
  );
}
```

### Density

There are two options for the property density: compact and default.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
        gap: "125px",
      }}
    >
      <Box>
        <Tooltip.Provider>
          <Tooltip.Root defaultOpen={true}>
            <Tooltip.Trigger>
              <Box>Trigger</Box>
            </Tooltip.Trigger>
            <Tooltip.Content side="bottom">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Bottom-Center
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
          </Tooltip.Root>
        </Tooltip.Provider>
      </Box>
      <Box>
        <Tooltip.Provider>
          <Tooltip.Root defaultOpen={true}>
            <Tooltip.Trigger>
              <Box>Trigger</Box>
            </Tooltip.Trigger>
            <Tooltip.Content side="bottom" density="compact">
              <Box
                css={{
                  height: "48px",
                  backgroundColor: theme.colors.gray500,
                  alignSelf: "stretch",
                  flexGrow: 1,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: 0,
                }}
              >
                <Box
                  css={{
                    fontSize: "$075",
                    fontWeight: "$bold",
                    color: "$primary",
                  }}
                >
                  Bottom-Center
                </Box>
                <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                  (swap with local component)
                </Box>
              </Box>
            </Tooltip.Content>
          </Tooltip.Root>
        </Tooltip.Provider>
      </Box>
    </Box>
  );
}
```

### Offset

The option offset can use any spacing token to offset its position from the origin point of the tooltip. The default offset is the spacing token 025.

![](https://build.washingtonpost.com/img/components/tooltip/offset.svg)

---

## Behavior

### Avoids collisions

When appropriate, helper text should be placed closest to the Legend.

![](https://build.washingtonpost.com/img/components/tooltip/collisions.svg)

---

## Guidance

### Do not hide content

A tooltip is not meant to hide necessary contextual information. It should only be used as a supplementary element. The nautre of a tooltip is non-persistent and should not require users to discover content within a tooltip.

```jsx
export default function Example() {
  return (
    <Box>
      <Tooltip.Provider>
        <Tooltip.Root defaultOpen={true}>
          <Tooltip.Trigger>
            <Box
              css={{
                textDecoration: "underline",
                fontWeight: theme.fontWeights.light,
                fontSize: theme.fontSizes[100],
                color: theme.colors.accessible,
              }}
            >
              Find your state
            </Box>
          </Tooltip.Trigger>
          <Tooltip.Content side="bottom">
            <InputText icon="right" label="Search">
              <Icon label="State">
                <Search />
              </Icon>
            </InputText>
          </Tooltip.Content>
        </Tooltip.Root>
      </Tooltip.Provider>
    </Box>
  );
}
```

### Avoid nesting actionable elements

The nautre of the tooltip is non-persistent. When the user is required to take an action on an element nested inside the tooltip it makes the action less accessible for those with limited mobility.

```jsx
export default function Example() {
  return (
    <Box>
      <Tooltip.Provider>
        <Tooltip.Root defaultOpen={true}>
          <Tooltip.Trigger>
            <Box
              css={{
                textDecoration: "underline",
                fontWeight: theme.fontWeights.light,
                fontSize: theme.fontSizes[100],
                color: theme.colors.accessible,
              }}
            >
              Find your state
            </Box>
          </Tooltip.Trigger>
          <Tooltip.Content side="bottom">
            <InputText icon="right" label="Search">
              <Icon label="State">
                <Search />
              </Icon>
            </InputText>
          </Tooltip.Content>
        </Tooltip.Root>
      </Tooltip.Provider>
    </Box>
  );
}
```

### Do not nest Popovers or Tooltips

Tooltips should not have additional tooltips or popover within the same container.

```jsx
export default function Example() {
  return (
    <Box>
      <Tooltip.Provider>
        <Tooltip.Root defaultOpen={true}>
          <Tooltip.Trigger>
            <Box>
              <Tooltip.Provider>
                <Tooltip.Root defaultOpen={true}>
                  <Tooltip.Trigger>
                    <Box
                      css={{
                        textDecoration: "underline",
                        fontWeight: theme.fontWeights.light,
                        fontSize: theme.fontSizes[100],
                        color: theme.colors.accessible,
                      }}
                    >
                      Trigger
                    </Box>
                  </Tooltip.Trigger>
                  <Tooltip.Content side="bottom">
                    <Box
                      css={{
                        height: "48px",
                        backgroundColor: theme.colors.gray500,
                        alignSelf: "stretch",
                        flexGrow: 1,
                        display: "flex",
                        flexDirection: "column",
                        justifyContent: "center",
                        alignItems: "center",
                        padding: 0,
                      }}
                    >
                      <Box
                        css={{
                          fontSize: "$075",
                          fontWeight: "$bold",
                          color: "$primary",
                        }}
                      >
                        Trigger 2
                      </Box>
                      <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                        (swap with local component)
                      </Box>
                    </Box>
                  </Tooltip.Content>
                </Tooltip.Root>
              </Tooltip.Provider>
            </Box>
          </Tooltip.Trigger>
          <Tooltip.Content side="left" align="start" offsetAlign="31.25rem">
            <Box
              css={{
                height: "48px",
                backgroundColor: theme.colors.gray500,
                alignSelf: "stretch",
                flexGrow: 1,
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                padding: 0,
              }}
            >
              <Box
                css={{
                  fontSize: "$075",
                  fontWeight: "$bold",
                  color: "$primary",
                }}
              >
                Slot
              </Box>
              <Box css={{ fontSize: "8px", fontWeight: "$light" }}>
                (swap with local component)
              </Box>
            </Box>
          </Tooltip.Content>
        </Tooltip.Root>
      </Tooltip.Provider>
    </Box>
  );
}
```

---

## Accessibility

### Design considerations

While tooltips are a convenient way of revealing content, please keep in mind the nautre of a tooltip and how it shows/hides on hover. consider alternatives like a more persistent element like a popover.

### Keyboard controls

Tooltips will show/hide without delay when the trigger is in focus and **tab** is selected on the keyboard. If the tooltip is open and either **escape, space,** or **enter** is selected on the keyboard, it will close the tooltip.

---

## API Reference

## Props

#### TooltipRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `open` | `boolean` | No | — |  |
| `defaultOpen` | `boolean` | No | — |  |
| `onOpenChange` | `(open: boolean) => void` | No | — |  |
| `delayDuration` | `number` | No | — | The duration from when the pointer enters the trigger until the tooltip gets opened. This will override the prop with the same name passed to Provider. @defaultValue 700 |
| `disableHoverableContent` | `boolean` | No | — | When `true`, trying to hover the content will result in the tooltip closing as the pointer leaves the trigger. @defaultValue false |

#### TooltipPortal
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `container` | `Element \| DocumentFragment` | No | — | Specify a container element to portal the content into. |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### TooltipProvider
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `delayDuration` | `number` | No | — | The duration from when the pointer enters the trigger until the tooltip gets opened. @defaultValue 700 |
| `skipDelayDuration` | `number` | No | — | How much time a user has to enter another trigger without incurring a delay again. @defaultValue 300 |
| `disableHoverableContent` | `boolean` | No | — | When `true`, trying to hover the content will result in the tooltip closing as the pointer leaves the trigger. @defaultValue false |

#### Tooltip

Tooltip

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |

#### TooltipContent

Tooltip.Content

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `disabled` | `boolean` | No | false | Prevent the tooltip from showing up |
| `offsetSide` | `string \| number \| WPDSThemeSpaceObject` | No | theme.space[025] |  |
| `side` | `"bottom" \| "left" \| "right" \| "top"` | No | top |  |
| `align` | `"center" \| "end" \| "start"` | No | center |  |
| `offsetAlign` | `string \| number \| WPDSThemeSpaceObject` | No | 0 |  |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |
| `aria-label` | `string` | No | — | A more descriptive label for accessibility purpose |
| `onEscapeKeyDown` | `(event: KeyboardEvent) => void` | No | — | Event handler called when the escape key is down. Can be prevented. |
| `onPointerDownOutside` | `(event: PointerDownOutsideEvent) => void` | No | — | Event handler called when the a `pointerdown` event happens outside of the `Tooltip`. Can be prevented. |
| `asChild` | `boolean` | No | — |  |
| `sticky` | `"always" \| "partial"` | No | — |  |
| `sideOffset` | `number` | No | — |  |
| `alignOffset` | `number` | No | — |  |
| `arrowPadding` | `number` | No | — |  |
| `avoidCollisions` | `boolean` | No | — |  |
| `collisionBoundary` | `Element \| Element[]` | No | — |  |
| `collisionPadding` | `number \| Partial<Record<"bottom" \| "left" \| "right" \| "top", number>>` | No | — |  |
| `hideWhenDetached` | `boolean` | No | — |  |
| `updatePositionStrategy` | `"always" \| "optimized"` | No | — |  |
| `density` | `"default" \| "compact"` | No | — | Specify the amount of padding for the inner components. |

#### TooltipTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

```jsx
``
```
