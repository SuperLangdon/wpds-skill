---
title: "Tabs"
description: "Tabs are used to navigate between sections of content in the same area without reloading the page."
sourceUrl: "https://build.washingtonpost.com/components/tabs"
---

# Tabs

---

## Anatomy

![Note: Image is not to scale](https://build.washingtonpost.com/img/components/tabs/anatomy.svg)

*Note: Image is not to scale*

1. Tab
2. Selection indicator
3. Icon (optional)
4. Tab bar

---

## Options

### Selection

This option indicates whether a tab is selected (and thereby showing content) or not.

```jsx
return function Example() {
  const StyledContent = styled(Tabs.Content, {
    minHeight: "50px",
    paddingTop: "20px",
    color: theme.colors.primary,
  });

  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Tabs.Root defaultValue="tab1" align="center">
          <Tabs.List aria-label="Countries' information">
            <Tabs.Trigger value="tab1"> France </Tabs.Trigger>
            <Tabs.Trigger value="tab2">Kenya</Tabs.Trigger>
            <Tabs.Trigger value="tab3">Austria</Tabs.Trigger>
          </Tabs.List>
          <StyledContent value="tab1">France is here 🇫🇷</StyledContent>
          <StyledContent value="tab2">Kenya is here 🇰🇪</StyledContent>
          <StyledContent value="tab3">Austria is here 🇦🇹</StyledContent>
        </Tabs.Root>
      </Box>
    </>
  );
}
```

### Alignment

This option determines whether the tabs are left or center aligned along the tab bar.

```jsx
export default function Example() {
  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1" align="center">
            <Tabs.List aria-label="Countries' information">
              <Tabs.Trigger value="tab1"> France </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
              <Tabs.Trigger value="tab3">Vietnam</Tabs.Trigger>
            </Tabs.List>
          </Tabs.Root>
        </Box>
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1" align="left">
            <Tabs.List aria-label="Countries' information">
              <Tabs.Trigger value="tab1"> France </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
              <Tabs.Trigger value="tab3">Vietnam</Tabs.Trigger>
            </Tabs.List>
          </Tabs.Root>
        </Box>
      </Box>
    </>
  );
}
```

### Density

This option determines the overall size of the component: compact, default, or loose.

```jsx
export default function Example() {
  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information" density="compact">
              <Tabs.Trigger value="tab1"> France </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
              <Tabs.Trigger value="tab3">Vietnam</Tabs.Trigger>
            </Tabs.List>
          </Tabs.Root>
        </Box>
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information" density="default">
              <Tabs.Trigger value="tab1"> France </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
              <Tabs.Trigger value="tab3">Vietnam</Tabs.Trigger>
            </Tabs.List>
          </Tabs.Root>
        </Box>
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information" density="loose">
              <Tabs.Trigger value="tab1"> France </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
              <Tabs.Trigger value="tab3">Vietnam</Tabs.Trigger>
            </Tabs.List>
          </Tabs.Root>
        </Box>
      </Box>
    </>
  );
}
```

---

## Behavior

### Hover

Hovering over an unselected tab causes a lighter selection bar to appear below.

```jsx
export default function Example() {
  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Tabs.Root defaultValue="tab1" align="center">
          <Tabs.List aria-label="Countries' information">
            <Tabs.Trigger value="tab1">France</Tabs.Trigger>
            <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
            <Tabs.Trigger value="tab3">Vietnam</Tabs.Trigger>
          </Tabs.List>
        </Tabs.Root>
      </Box>
    </>
  );
}
```

### Disabled

A disabled tab changes to color subtle.

```jsx
export default function Example() {
  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Tabs.Root defaultValue="tab1" align="center">
          <Tabs.List aria-label="Countries' information">
            <Tabs.Trigger value="tab1">France</Tabs.Trigger>
            <Tabs.Trigger value="tab2" disabled>
              Brazil
            </Tabs.Trigger>
            <Tabs.Trigger value="tab3">Vietnam</Tabs.Trigger>
          </Tabs.List>
        </Tabs.Root>
      </Box>
    </>
  );
}
```

### Tab overflow

When there are more tabs than can be displayed, the behavior will match our secondary navigation. The tabs will be cut off and hidden on the far right and accessible via scrolling.

```jsx
export default function Example() {
  const StyledContent = styled(Tabs.Content, {
    minHeight: "50px",
    paddingTop: "20px",
    color: theme.colors.primary,
  });
  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Tabs.Root defaultValue="tab1">
          <Tabs.List aria-label="Countries' information">
            <Tabs.Trigger value="tab1">
              <Icon label="trigger icon" size="100">
                <Info />
              </Icon>
              France
            </Tabs.Trigger>
            <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
            <Tabs.Trigger value="tab3">
              <Icon label="trigger icon" size="100">
                <Info />
              </Icon>
              The Democratic Republic of the Congo
            </Tabs.Trigger>
            <Tabs.Trigger value="tab4">Vietnam</Tabs.Trigger>
            <Tabs.Trigger value="tab5">Papua New Guinea</Tabs.Trigger>
            <Tabs.Trigger value="tab6">Venezuela</Tabs.Trigger>
            <Tabs.Trigger value="tab7">Kenya</Tabs.Trigger>
            <Tabs.Trigger value="tab8">Austria</Tabs.Trigger>
          </Tabs.List>
          <StyledContent value="tab1">France is here 🇫🇷</StyledContent>
          <StyledContent value="tab2">Brazil is here 🇧🇷</StyledContent>
          <StyledContent value="tab3">
            The Democratic Republic of the Congo is here 🇨🇩
          </StyledContent>
          <StyledContent value="tab4">Vietnam is here 🇻🇳</StyledContent>
          <StyledContent value="tab5">
            Papua New Guinea is here 🇵🇬
          </StyledContent>
          <StyledContent value="tab6">Venezuela is here 🇻🇪</StyledContent>
          <StyledContent value="tab7">Kenya is here 🇰🇪</StyledContent>
          <StyledContent value="tab8">Austria is here 🇦🇹</StyledContent>
        </Tabs.Root>
      </Box>
    </>
  );
}
```

---

## Guidance

### Tab number

Use at least 2 tabs or more.

```jsx
export default function Example() {
  const StyledContent = styled(Tabs.Content, {
    minHeight: "50px",
    paddingTop: "20px",
    color: theme.colors.primary,
  });

  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information">
              <Tabs.Trigger value="tab1"> France </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
            </Tabs.List>
            <StyledContent value="tab1">France is here 🇫🇷</StyledContent>
            <StyledContent value="tab2">Brazil is here 🇧🇷</StyledContent>
          </Tabs.Root>
        </Box>
      </Box>
    </>
  );
}
```

### Text overflow

Avoid using long titles for tab copy. Thirty characters or less is our recommendation. If text does overflow, it is truncated with an ellipsis and the full text is shown in a tooltip on hover.

```jsx
export default function Example() {
  const StyledContent = styled(Tabs.Content, {
    minHeight: "50px",
    paddingTop: "20px",
    color: theme.colors.primary,
  });

  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information">
              <Tabs.Trigger value="tab1">
                <Icon label="trigger icon" size="100">
                  <Info />
                </Icon>
                France
              </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
              <Tabs.Trigger value="tab3">
                <Icon label="trigger icon" size="100">
                  <Info />
                </Icon>
                The Democratic Republic of the Congo
              </Tabs.Trigger>
              <Tabs.Trigger value="tab4">Vietnam</Tabs.Trigger>
            </Tabs.List>
            <StyledContent value="tab1">France is here 🇫🇷</StyledContent>
            <StyledContent value="tab2">Brazil is here 🇧🇷</StyledContent>
            <StyledContent value="tab3">
              The Democratic Republic of the Congo is here 🇨🇩
            </StyledContent>
            <StyledContent value="tab4">Vietnam is here 🇻🇳</StyledContent>
          </Tabs.Root>
        </Box>
      </Box>
    </>
  );
}
```

### Icon placement

Don't put icons on the right.

```jsx
export default function Example() {
  const StyledContent = styled(Tabs.Content, {
    minHeight: "50px",
    paddingTop: "20px",
    color: theme.colors.primary,
  });

  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information">
              <Tabs.Trigger value="tab1">
                France
                <Icon label="trigger icon" size="100">
                  <Info />
                </Icon>
              </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
            </Tabs.List>
            <StyledContent value="tab1">France is here 🇫🇷</StyledContent>
            <StyledContent value="tab2">Brazil is here 🇧🇷</StyledContent>
          </Tabs.Root>
        </Box>
      </Box>
    </>
  );
}
```

### Linking

Tabs should not link to another page.

```jsx
export default function Example() {
  const StyledContent = styled(Tabs.Content, {
    minHeight: "50px",
    paddingTop: "20px",
    color: theme.colors.primary,
  });

  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information">
              <Tabs.Trigger value="tab1">
                <Icon label="trigger icon" size="100">
                  <External />
                </Icon>
                France
              </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
            </Tabs.List>
          </Tabs.Root>
        </Box>
      </Box>
    </>
  );
}
```

### Icons

When using icons, it is best to use them as a prefix to the label, rather than following the label. This ensures that the icon is properly associated with the label and is more easily recognizable by users.

```jsx
export default function Example() {
  const StyledContent = styled(Tabs.Content, {
    minHeight: "50px",
    paddingTop: "20px",
    color: theme.colors.primary,
  });

  return (
    <>
      <Box
        css={{
          display: "flex",
          width: 500,
          rowGap: "$100",
          flexDirection: "column",
        }}
      >
        <Box
          css={{
            display: "flex",
            width: 500,
            rowGap: "$100",
            flexDirection: "column",
            padding: "10px",
            border: "1px dashed black",
          }}
        >
          <Tabs.Root defaultValue="tab1">
            <Tabs.List aria-label="Countries' information">
              <Tabs.Trigger value="tab1">
                <Icon label="trigger icon" size="100">
                  <Info />
                </Icon>
                France
              </Tabs.Trigger>
              <Tabs.Trigger value="tab2">Brazil</Tabs.Trigger>
            </Tabs.List>
            <StyledContent value="tab1">France is here 🇫🇷</StyledContent>
            <StyledContent value="tab2">Brazil is here 🇧🇷</StyledContent>
          </Tabs.Root>
        </Box>
      </Box>
    </>
  );
}
```

---

## Accessibility

### Keyboard interactions

Using the left and right arrow keys will move focus between tabs. You can press enter to make that focused tab active.

---

## API Reference

## Props

#### Tabs

Tabs

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |

#### TabsRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `defaultValue` | `string` | No | — | The value of the tab to select by default, if uncontrolled |
| `dir` | `Direction` | No | — | The direction of navigation between toolbar items. |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `asChild` | `boolean` | No | — |  |
| `value` | `string` | No | — | The value for the selected tab, if controlled |
| `onValueChange` | `(value: string) => void` | No | — | A function called when a new tab is selected |
| `orientation` | `"horizontal" \| "vertical"` | No | — | The orientation the tabs are layed out. Mainly so arrow navigation is done accordingly (left & right vs. up & down) @defaultValue horizontal |
| `activationMode` | `"manual" \| "automatic"` | No | — | Whether a tab is activated automatically or manually. @defaultValue automatic |
| `css` | `{} & { alignContent?: AlignContent \| Globals \| ScaleValue \| Index; alignItems?: AlignItems \| Globals \| ScaleValue \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |

#### TabsList
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `asChild` | `boolean` | No | — |  |
| `loop` | `boolean` | No | — |  |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `align` | `("left" \| "center") & ("left" \| "center"` | No | left | the alignment of the list content along the tab bar. Default is left aligned |
| `density` | `"default" \| "loose" \| "compact"` | No | default | the overall size of the component. Default is default (theme.fontSizes[100]) |

#### TabsTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | `string` | Yes | — | A unique value that associates the trigger with a content. |
| `disabled` | `boolean` | No | — | The value whether the trigger should be disabled |
| `css` | `{} & { alignContent?: AlignContent \| Globals \| ScaleValue \| Index; alignItems?: AlignItems \| Globals \| ScaleValue \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |
| `density` | `"default" \| "loose" \| "compact"` | No | — |  |
| `active` | `boolean \| "true"` | No | — |  |

#### TabsContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | `string` | Yes | — |  |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |
| `asChild` | `boolean` | No | — |  |
