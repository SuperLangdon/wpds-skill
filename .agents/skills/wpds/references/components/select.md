---
title: "Select"
description: "A select is a type of form element that provides a method for choosing one item from a list of options."
sourceUrl: "https://build.washingtonpost.com/components/select"
---

# Select

---

## Anatomy

![](https://build.washingtonpost.com/img/components/select/anatomy.svg)

1. Selected value
2. Label/placeholder
3. Helper text (optional)
4. Chevron icon (actionable)
5. Border
6. Check icon (indicates selected option)
7. Options list
8. Option hover state
9. Option

---

## Options

### No styling options

The select component currently only supports one size and variant.

```jsx
return function Example() {
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
        <Select.Root>
          <Select.Trigger aria-label="Countries">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="france">France</Select.Item>
            <Select.Item value="united-kingdom">
              United Kingdom - Scotland, Ireland, Wales, Great Britain
            </Select.Item>
            <Select.Item value="spain">Spain</Select.Item>
            <Select.Item value="peru">Peru</Select.Item>
            <Select.Item value="chile">Chile</Select.Item>
            <Select.Item value="ecuador">Ecuador</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

---

## Behavior

### Options list (Active)

Clicking or tapping the select field initiates the active state, revealing an options list that consists of a set of values. When in the active state, the label/placeholder is reduced in size and the chevron icon rotates 180 degrees, pointing upwards.

The options list may contain as many values as needed and becomes scrollable if there are more options than what is currently in view.

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
        <Select.Root>
          <Select.Trigger aria-label="example-1">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="1">Option 1 value</Select.Item>
            <Select.Item value="2">Option 2 value</Select.Item>
            <Select.Item value="3">Option 3 value</Select.Item>
            <Select.Item value="4">Option 4 value</Select.Item>
            <Select.Item value="5">Option 5 value</Select.Item>
            <Select.Item value="6">Option 6 value</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

### Making a selection (Active)

The options list can be navigated by mouse hover or via the up/down arrow keys (indicated by a faint highlight). clicking or tapping an option in the list will select the chosen value (indicated by the check icon)

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
        <Select.Root open={true} defaultValue="7">
          <Select.Trigger aria-label="example-2">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="7">Option 1 value</Select.Item>
            <Select.Item value="8">Option 2 value</Select.Item>
            <Select.Item value="9">Option 3 value</Select.Item>
            <Select.Item value="10">Option 4 value</Select.Item>
            <Select.Item value="11">Option 5 value</Select.Item>
            <Select.Item value="12">Option 6 value</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

Once a selection is made, the chosen value is displayed within the select field and the options list is automatically dismissed. Selection can also be achieved by pressing the Enter/Return key while an option is highlighted. to cancel selection/dismiss the options list, click or tap outside the element or press the Esc key.

### Select groups

The options list can be segmented into groups. Grouping options within a select field can be helpful for creating categories or subcategories of similar items.

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
        <Select.Root defaultValue="apple" open={true}>
          <Select.Trigger aria-label="example-3">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Group label="Fruit">
              <Select.Item value="apple">Apple</Select.Item>
              <Select.Item value="banana">Banana</Select.Item>
              <Select.Item value="orange">Orange</Select.Item>
            </Select.Group>
            <Select.Group label="Vegetable">
              <Select.Item value="broccoli">Broccoli</Select.Item>
              <Select.Item value="carrot">Carrot</Select.Item>
              <Select.Item value="onion">Onion</Select.Item>
            </Select.Group>
            <Select.Group label="Protein">
              <Select.Item value="fish">Fish</Select.Item>
              <Select.Item value="chicken">Chicken</Select.Item>
              <Select.Item value="beef">Beer</Select.Item>
            </Select.Group>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

### Text overflow

Overflow of the selected value is indicated by an ellipsis

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
        <Select.Root defaultValue="tv">
          <Select.Trigger aria-label="example-4">
            <Select.Label>How did you hear about us?</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="tv">
              From a television, magazine or newspaper or other print or media
              options.
            </Select.Item>
            <Select.Item value="ig">instagram</Select.Item>
            <Select.Item value="tiktok">tiktok</Select.Item>
            <Select.Item value="fb">facebook ads</Select.Item>
            <Select.Item value="google">
              google search or search engine
            </Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

### Show required

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
        <Select.Root required>
          <Select.Trigger aria-label="example-4">
            <Select.Label>Country</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="spain">Spain</Select.Item>
            <Select.Item value="peru">Peru</Select.Item>
            <Select.Item value="chile">Chile</Select.Item>
            <Select.Item value="ecuador">Ecuador</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

### Focus

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
        <Select.Root defaultValue="13">
          <Select.Trigger aria-label="example-2">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="13">Value</Select.Item>
            <Select.Item value="14">Option 2 value</Select.Item>
            <Select.Item value="15">Option 3 value</Select.Item>
            <Select.Item value="16">Option 4 value</Select.Item>
            <Select.Item value="17">Option 5 value</Select.Item>
            <Select.Item value="18">Option 6 value</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

### Error

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
        <Select.Root defaultValue="19" error>
          <Select.Trigger aria-label="example-2">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="19">Value</Select.Item>
            <Select.Item value="20">Option 2 value</Select.Item>
            <Select.Item value="21">Option 3 value</Select.Item>
            <Select.Item value="22">Option 4 value</Select.Item>
            <Select.Item value="23">Option 5 value</Select.Item>
            <Select.Item value="24">Option 6 value</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

### Success

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
        <Select.Root defaultValue="25" success>
          <Select.Trigger aria-label="example-2">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="25">Value</Select.Item>
            <Select.Item value="26">Option 2 value</Select.Item>
            <Select.Item value="27">Option 3 value</Select.Item>
            <Select.Item value="28">Option 4 value</Select.Item>
            <Select.Item value="29">Option 5 value</Select.Item>
            <Select.Item value="30">Option 6 value</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

### Disabled

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
        <Select.Root disabled>
          <Select.Trigger aria-label="example-2">
            <Select.Label>Label/Placeholder</Select.Label>
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Item value="25">Value</Select.Item>
            <Select.Item value="26">Option 2 value</Select.Item>
            <Select.Item value="27">Option 3 value</Select.Item>
            <Select.Item value="28">Option 4 value</Select.Item>
            <Select.Item value="29">Option 5 value</Select.Item>
            <Select.Item value="30">Option 6 value</Select.Item>
          </Select.Content>
        </Select.Root>
      </Box>
    </>
  );
}
```

---

## Accessibility

### ARIA

Assistive technologies (e.g. screen readers) announce the element clearly to users, including its role, name and state.

### Accessibility

The listbox position is adjusted (i.e. does not get cut off the screen).

---

## API Reference

## Props

#### SelectRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Used to insert select elements into the root component |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `disabled` | `boolean` | No | — | The underlying input element disabled attribute |
| `error` | `boolean` | No | — | Indicates there is an error |
| `errorMessage` | `ReactNode` | No | — | Text displayed below the select to describe the cause of the error |
| `helperText` | `ReactNode` | No | — | Text displayed below the input to provide additional context |
| `onValueChange` | `((value: string) => void) \| ((state: string) => void)` | No | — | Event handler called when the value changes. |
| `required` | `boolean` | No | — | The select element's required attribute |
| `success` | `boolean` | No | — | Indicates there is a success |
| `value` | `string` | No | — | The controlled value of the select. Should be used in conjunction with onValueChange |
| `defaultValue` | `string` | No | — | The value of the select when initially rendered. Use when you do not need to control the state of the select. |
| `open` | `boolean` | No | — | force overlay open |

#### SelectTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Used to insert select elements into the root component |
| `asChild` | `boolean` | No | — |  |
| `success` | `boolean \| "true"` | No | — |  |
| `error` | `boolean \| "true"` | No | — |  |
| `isInvalid` | `boolean \| "true"` | No | — |  |
| `isDisabled` | `boolean \| "true"` | No | — |  |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |

#### SelectLabel
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `isFloating` | `boolean \| "true"` | No | — |  |
| `isDisabled` | `boolean \| "true"` | No | — |  |
| `children` | `ReactNode` | No | — | Used to insert select elements into the root component |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `title` | `string` | No | — |  |

#### SelectValue
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `isDisabled` | `boolean \| "true"` | No | — |  |
| `placeholder` | `ReactNode & string` | No | — |  |
| `children` | `ReactNode` | No | — | Used to insert select elements into the root component |
| `asChild` | `boolean` | No | — |  |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |

#### SelectContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Used to insert select elements into the root component |
| `css` | `{} & { alignContent?: AlignContent \| ScaleValue \| Globals \| Index; alignItems?: AlignItems \| ScaleValue \| Globals \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `position` | `"item-aligned" \| "popper"` | No | — |  |
| `sticky` | `"always" \| "partial"` | No | — |  |
| `asChild` | `boolean` | No | — |  |
| `side` | `"bottom" \| "left" \| "right" \| "top"` | No | — |  |
| `sideOffset` | `number` | No | — |  |
| `align` | `"center" \| "end" \| "start"` | No | — |  |
| `alignOffset` | `number` | No | — |  |
| `arrowPadding` | `number` | No | — |  |
| `avoidCollisions` | `boolean` | No | — |  |
| `collisionBoundary` | `Element \| Element[]` | No | — |  |
| `collisionPadding` | `number \| Partial<Record<"bottom" \| "left" \| "right" \| "top", number>>` | No | — |  |
| `hideWhenDetached` | `boolean` | No | — |  |
| `updatePositionStrategy` | `"always" \| "optimized"` | No | — |  |
| `onCloseAutoFocus` | `(event: Event) => void` | No | — | Event handler called when auto-focusing on close. Can be prevented. |
| `onEscapeKeyDown` | `(event: KeyboardEvent) => void` | No | — | Event handler called when the escape key is down. Can be prevented. |
| `onPointerDownOutside` | `(event: PointerDownOutsideEvent) => void` | No | — | Event handler called when the a `pointerdown` event happens outside of the `DismissableLayer`. Can be prevented. |

#### SelectItem
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Used to insert select elements into the root component |
| `disabled` | `boolean` | No | — |  |
| `value` | `string` | Yes | — | The value associated with this item |
| `css` | `{} & { alignContent?: AlignContent \| ScaleValue \| Globals \| Index; alignItems?: AlignItems \| ScaleValue \| Globals \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |
| `textValue` | `string` | No | — |  |

#### SelectGroup
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Used to insert select elements into the root component |
| `css` | `{} & { alignContent?: AlignContent \| ScaleValue \| Globals \| Index; alignItems?: AlignItems \| ScaleValue \| Globals \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `none` | `boolean \| "true"` | No | — |  |
| `label` | `string` | No | — | The value of the select when initially rendered. Use when you do not need to control the state of the select. |
