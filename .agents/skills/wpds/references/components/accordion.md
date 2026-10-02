---
title: "Accordion"
description: "An accordion is a type of flexible container that allows the user to control the display of content by manually expanding and collapsing the container."
sourceUrl: "https://build.washingtonpost.com/components/accordion"
---

# Accordion

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/accordion/anatomy.svg)

*Note: Image is not  to scale*

1. Header *(text label)*
2. Panel *(text or mixed content)*
3. Icon *(state indicator e.g., Expanded, Collapsed)*
4. Divider
5. Background color *(set manually, default is "none")*

---

## Options

### Density: Default

By default, accordion items are styled with a padding value that is appropriate for most use-cases.

```jsx
return function Example() {
  return (
    <Box
      css={{
        display: "flex",
        width: 500,
        rowGap: "$100",
        flexDirection: "column",
      }}
    >
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value={"item-1"}>
          <Accordion.Trigger>
            Here's some sample text for an accordion header item
          </Accordion.Trigger>
          <Accordion.Content>
            No! You don't even believe that! Gus has cameras everywhere, please.
            Listen to yourself! No, he has known everything, all along. Where
            were you today? In the lab? And you don't think it's possible that
            Tyrus lifted the cigarette out of your locker? Come on! Don't you
            see? You are the last piece of the puzzle. You are everything that
            he's wanted.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

### Density: Compact

"Compact" density applies a minimal amout of padding to the accordion item, producing a slimmer footprint that takes up less visual space.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        width: 500,
        rowGap: "$100",
        flexDirection: "column",
      }}
    >
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value={"item-1"}>
          <Accordion.Trigger density={ACCORDION_DENSITY.compact}>
            Here's some sample text for an accordion header item
          </Accordion.Trigger>
          <Accordion.Content>
            No! You don't even believe that! Gus has cameras everywhere, please.
            Listen to yourself! No, he has known everything, all along. Where
            were you today? In the lab? And you don't think it's possible that
            Tyrus lifted the cigarette out of your locker? Come on! Don't you
            see? You are the last piece of the puzzle. You are everything that
            he's wanted.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

### Density: Loose

"Loose" density applies a generous amount of padding to the accordion item, producing a larger footprint that occupies more visual space.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        width: 500,
        rowGap: "$100",
        flexDirection: "column",
      }}
    >
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value={"item-1"}>
          <Accordion.Trigger density={ACCORDION_DENSITY.loose}>
            Here's some sample text for an accordion header item
          </Accordion.Trigger>
          <Accordion.Content>
            No! You don't even believe that! Gus has cameras everywhere, please.
            Listen to yourself! No, he has known everything, all along. Where
            were you today? In the lab? And you don't think it's possible that
            Tyrus lifted the cigarette out of your locker? Come on! Don't you
            see? You are the last piece of the puzzle. You are everything that
            he's wanted.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

---

## Behavior

### Collapsed

Each accordion item consists of two main parts - the *header*, or item title and the *panel*, or item content. In the collapsed state, only the header is visible. When collapsed, the chevron icon also points *down* to provide a visual signal for revealing additional information. By default, all items in the accordion are displayed in the collapsed state unless otherwise specified.

```jsx
export default function Example() {
  return (
    <Box css={{ width: 500 }}>
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value={"item-1"}>
          <Accordion.Trigger
            css={{
              fontWeight: theme.fontWeights.bold,
            }}
          >
            Header example text
          </Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

### Expanded

Users can access additional information by clicking or tapping the accordion item to reveal the expanded state. In the expanded state, the *panel* is displayed directly below the *header*. The chevron icon points *up* to indicate the current state and to provide a visual signal for returning the accordion item to its collapsed state.

```jsx
export default function Example() {
  return (
    <Box css={{ width: 500 }}>
      <Accordion.Root
        type={ACCORDION_TYPE.single}
        defaultValue="item-1"
        collapsible={true}
      >
        <Accordion.Item value="item-1">
          <Accordion.Trigger
            css={{
              fontWeight: theme.fontWeights.bold,
            }}
          >
            Header example text
          </Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

### Focus / Keyboard interaction

The accordion component is accessible via keyboard interaction. The "tab" key can be used to navigate items from top to bottom. The item currently in focus is denoted by a blue *outline*, using the CSS outline property. Pressing the "enter" ("return") key will expand or collapse the item in focus.

```jsx
export default function Example() {
  return (
    <Box css={{ width: 500 }}>
      <Accordion.Root
        type={ACCORDION_TYPE.single}
        defaultValue="item-1"
        collapsible={true}
      >
        <Accordion.Item value="item-1">
          <Accordion.Trigger forcefocus="true">
            Header text item one
          </Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
        <Accordion.Item value="item-2">
          <Accordion.Trigger>Header text item two</Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

### Disabled

The purpose of the accordion is to act as a container and visual interface for displaying static information upon user interaction. It is not intended to be used as an input element or form field. The accordion component does not require conditional logic to achieve its functionality and therefore **does not feautre a special disabled state** or possess any manner of error-handling. If visual feedback for a disabled state is desired, consider using the [.not-allowed] CSS property.

```jsx
export default function Example() {
  return (
    <Box css={{ width: 500 }}>
      <Accordion.Root
        type={ACCORDION_TYPE.single}
        collapsible={true}
        disabled={true}
      >
        <Accordion.Item value="item-1">
          <Accordion.Trigger>Header example text</Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

---

## Guidance

### Font family overrides

By default, the accordion component uses "Franklin Light" as its primary font for both the *header* and *panel* - however, font family overrides are premitted depending on the use-case. Below, the header has been set in "Postoni".

```jsx
export default function Example() {
  return (
    <Box css={{ width: 500 }}>
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value="item-1">
          <Accordion.Trigger
            css={{
              fontFamily: theme.fonts.headline,
              fontSize: theme.fontSizes[125],
              fontWeight: theme.fontWeights.bold,
            }}
          >
            Header example text
          </Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

### Font size overrides

The accordion component uses "size100" as its default font size. If a larger font size is desired, be mindful in choosing a size that is suitable for the use-case and appropriate for the space available. Avoid using font sizes that are excessively small or large, which may negatively affect your layout.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        width: "100%",
        rowGap: "$100",
        flexDirection: "column",
        marginTop: "50px",
      }}
    >
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value="item-1">
          <Accordion.Trigger
            css={{
              fontSize: theme.fontSizes["075"],
            }}
          >
            This header is too small
          </Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        width: "100%",
        rowGap: "$100",
        flexDirection: "column",
        marginTop: "50px",
      }}
    >
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value="item-1">
          <Accordion.Trigger
            css={{
              fontSize: theme.fontSizes[500],
              fontFamily: theme.fonts.headline,
            }}
          >
            This header is too large
          </Accordion.Trigger>
          <Accordion.Content>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in
            augue in felis pharetra finibus. In sagittis aliquam augue. Lorem
            ipsum dolor sit amet, consectetur adipiscing elit.
          </Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

### Don't split or truncate content

The header of the accordion should be a complete sentence or statement. It *should not* start in the header and continue in the panel.

```jsx
export default function Example() {
  return (
    <Box css={{ width: 500 }}>
      <Accordion.Root type={ACCORDION_TYPE.single} collapsible={true}>
        <Accordion.Item value="item-1">
          <Accordion.Trigger>The rest of the sentence is...</Accordion.Trigger>
          <Accordion.Content>inside of the content.</Accordion.Content>
        </Accordion.Item>
      </Accordion.Root>
    </Box>
  );
}
```

---

## API Reference

## Props

#### AccordionRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | `"single" \| "multiple"` | Yes | — |  |
| `value` | `string \| string[]` | No | — | The controlled stateful value of the accordion item whose content is expanded. The controlled stateful value of the accordion items whose contents are expanded. |
| `defaultValue` | `string \| string[]` | No | — | The value of the item whose content is expanded when the accordion is initially rendered. Use `defaultValue` if you do not need to control the state of an accordion. The value of the items whose contents are expanded when the accordion is initially rendered. Use `defaultValue` if you do not need to control the state of an accordion. |
| `onValueChange` | `((value: string) => void) \| ((value: string[]) => void)` | No | — | The callback that fires when the state of the accordion changes. |
| `collapsible` | `boolean` | No | false | Whether an accordion item can be collapsed after it has been opened. |
| `disabled` | `boolean & (boolean \| "true"` | No | — | Whether or not an accordion is disabled from user interaction. @defaultValue false |
| `orientation` | `"horizontal" \| "vertical"` | No | vertical | The layout in which the Accordion operates. |
| `dir` | `Direction` | No | — | The language read direction. |
| `asChild` | `boolean` | No | — |  |

#### AccordionContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### AccordionItem
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `disabled` | `boolean` | No | — | Whether or not an accordion item is disabled from user interaction. @defaultValue false |
| `value` | `string` | Yes | — | A string value for the accordion item. All items within an accordion should use a unique value. |
| `asChild` | `boolean` | No | — |  |

#### AccordionHeader
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

#### AccordionTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `asChild` | `boolean` | No | — |  |
| `density` | `"default" \| "loose" \| "compact"` | No | — |  |
| `forcefocus` | `(boolean \| "true"` | No | — |  |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
