---
title: "Action Menu"
description: "A temporary overlay containing a list of items (commands or actions) relevant to the user’s current context. An item in the menu is immediately executed upon selection. Action menus must be paired with a trigger (button or text link) that reveals the menu on click or tap."
sourceUrl: "https://build.washingtonpost.com/components/action-menu"
---

# Action Menu

---

## Anatomy

1. Trigger
2. Item label
3. Submenu indicator
4. Group label
5. Group divider
6. Item icon (optional)
7. Selected item
8. Unselected item

---

## Options

### Density

The following options can be applied to specify the density of the items: `default`, `loose`, and `compact`.

```jsx
<Box
  css={{
    paddingTop: "5%",
    width: "100%",
    height: "100vh",
  }}
>
  <ActionMenu.Root open density={"default"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Default</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content align="end">
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
  <ActionMenu.Root open density={"compact"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Compact</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content>
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
  <ActionMenu.Root open density={"loose"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Loose</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content>
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
</Box>
```

### Trigger

The Action List can be triggered with a button, a link, an icon, or similar visual cue.

```jsx
<Box
  css={{
    paddingTop: "5%",
    width: "100%",
    height: "100vh",
  }}
>
  <ActionMenu.Root>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "25px", marginRight: "25px" }}>
        {`Action Button`}
      </Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content>
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
      <ActionMenu.Item>Action 4</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
  <ActionMenu.Root>
    <ActionMenu.Trigger asChild>
      <Button icon="center" css={{ marginLeft: "25px", marginRight: "25px" }}>
        <Icon label="Expand">
          <DotsVertical />
        </Icon>
      </Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content>
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
      <ActionMenu.Item>Action 4</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
  <ActionMenu.Root>
    <ActionMenu.Trigger
      css={{ fontWeight: "bold", textDecoration: "underline" }}
      asChild
    >
      <a style={{ marginLeft: "35px", marginRight: "35px" }}>Action Link</a>
    </ActionMenu.Trigger>
    <ActionMenu.Content>
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
      <ActionMenu.Item>Action 4</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
  <ActionMenu.Root>
    <ActionMenu.Trigger asChild>
      <Icon css={{ marginLeft: "45px", marginRight: "45px" }} label="Actions">
        <MixerVertical />
      </Icon>
    </ActionMenu.Trigger>
    <ActionMenu.Content>
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
      <ActionMenu.Item>Action 4</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
</Box>
```

---

## Behavior

### Disabled

A menu item can be set to ‘disabled’, according to the user’s current context and relevance of option(s).

```jsx
<Box
  css={{
    paddingTop: "5%",
    width: "100%",
    height: "100vh",
  }}
>
  <ActionMenu.Root open density={"default"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Default</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content align="end">
      <ActionMenu.Item disabled>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
</Box>
```

### Hover

Items display background color ‘$faint’ on mouse over

```jsx
<Box
  css={{
    paddingTop: "5%",
    width: "100%",
    height: "100vh",
  }}
>
  <ActionMenu.Root open density={"default"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Default</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content align="end">
      <ActionMenu.Item disabled>Action 1</ActionMenu.Item>
      <ActionMenu.Item>Action 2</ActionMenu.Item>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
</Box>
```

### Select

Action menu items can be made selectable using radio (I.E. only one option permitted) or multi-select functionality. Menu items are selected or deselected via user input. Selected items are visually indicated in bold along with the ([glyph: check]) icon.

```jsx
<Box
  css={{
    paddingTop: "5%",
    width: "100%",
    height: "100vh",
  }}
>
  <ActionMenu.Root open density={"default"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Default</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content align="end">
      <ActionMenu.Group>
        <ActionMenu.Label>Checkbox Item Examples</ActionMenu.Label>
        <ActionMenu.CheckboxItem checked>
          <ActionMenu.ItemIndicator />
          Left
        </ActionMenu.CheckboxItem>
        <ActionMenu.CheckboxItem checked>
          <ActionMenu.ItemIndicator />
          Neither
        </ActionMenu.CheckboxItem>
        <ActionMenu.CheckboxItem>
          <ActionMenu.ItemIndicator />
          Right
          <ActionMenu.Icon side="right">
            <Icon label="bell" size="100">
              <Bookmark />
            </Icon>
          </ActionMenu.Icon>
        </ActionMenu.CheckboxItem>
        <ActionMenu.CheckboxItem>
          <ActionMenu.ItemIndicator />
          Both
          <ActionMenu.Icon side="right">
            <Icon label="bell" size="100">
              <Bookmark />
            </Icon>
          </ActionMenu.Icon>
        </ActionMenu.CheckboxItem>
      </ActionMenu.Group>
    </ActionMenu.Content>
  </ActionMenu.Root>
  <ActionMenu.Root open density={"default"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Default</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content align="end">
      <ActionMenu.Label>Radio Group Example</ActionMenu.Label>
      <ActionMenu.RadioGroup value="radio2">
        <ActionMenu.RadioItem value="radio1">
          <ActionMenu.ItemIndicator />
          Radio 1
        </ActionMenu.RadioItem>
        <ActionMenu.RadioItem value="radio2">
          <ActionMenu.ItemIndicator />
          Radio 2
        </ActionMenu.RadioItem>
        <ActionMenu.RadioItem value="radio3">
          <ActionMenu.ItemIndicator />
          Radio 3
        </ActionMenu.RadioItem>
      </ActionMenu.RadioGroup>
    </ActionMenu.Content>
  </ActionMenu.Root>
</Box>
```

### Submenu

The submenu indicator, ([glyph: chevron-right]) is used to identify items containing a submenu. Action menu supports up to three layers of submenu — level 1 (i.e., root), level 2 and level 3. To access a submenu, hover over the menu item or use keyboard navigation. Each menu level has a specific elevation in the stacking order, corresponding to its place in the nesting hierarchy. Additionally, menu containers for levels 1, 2 and 3 possess individual shadow depths, corresponding to shadow tokens ‘$300, ‘$400’, and ‘$500’, respectively.

```jsx
<Box
  css={{
    paddingTop: "5%",
    width: "100%",
    height: "100vh",
  }}
>
  <ActionMenu.Root open density={"default"}>
    <ActionMenu.Trigger asChild>
      <Button css={{ marginLeft: "15px", marginRight: "15px" }}>Default</Button>
    </ActionMenu.Trigger>
    <ActionMenu.Content>
      <ActionMenu.Item>Action 1</ActionMenu.Item>
      <ActionMenu.Sub open>
        <ActionMenu.SubTrigger>Action 2</ActionMenu.SubTrigger>
        <ActionMenu.SubContent>
          <ActionMenu.Item>Action 2.1</ActionMenu.Item>
          <ActionMenu.Item>Action 2.2</ActionMenu.Item>
          <ActionMenu.Sub open>
            <ActionMenu.SubTrigger>Action 2.3</ActionMenu.SubTrigger>
            <ActionMenu.SubContent>
              <ActionMenu.Item>Action 2.1.1</ActionMenu.Item>
              <ActionMenu.Item>Action 2.1.2</ActionMenu.Item>
              <ActionMenu.Item>Action 2.1.3</ActionMenu.Item>
              <ActionMenu.Item>Action 2.1.4</ActionMenu.Item>
            </ActionMenu.SubContent>
          </ActionMenu.Sub>
          <ActionMenu.Item>Action 2.4</ActionMenu.Item>
        </ActionMenu.SubContent>
      </ActionMenu.Sub>
      <ActionMenu.Item>Action 3</ActionMenu.Item>
      <ActionMenu.Item>Action 4</ActionMenu.Item>
    </ActionMenu.Content>
  </ActionMenu.Root>
</Box>
```

---

## Guidance

### Number of menu items

It’s recommended to limit the number of items to no more than five (5) options in a given menu list. Reducing the number of options avoids overwhelming the user and aides in making an accurate selection. If your action menu requires more options, consider using group labels to provide additional visual clarity.

### Order of menu items

In general, it’s best to place the most frequently used or encouraged options towards the top of the menu list, for easier scannability.

## Accessibility

### Keyboard controls

| Key | Description |
| --- | --- |
| Space | When focus is on DropdownMenu.Trigger, opens the dropdown menu and focuses the first item. When focus is on an item, activates the focused item. |
| Enter | When focus is on DropdownMenu.Trigger, opens the dropdown menu and focuses the first item. When focus is on an item, activates the focused item. |
| ArrowDown | When focus is on DropdownMenu.Trigger, opens the dropdown menu. When focus is on an item, moves focus to the next item. |
| ArrowUp | When focus is on an item, moves focus to the previous item. |
| ArrowRight, ArrowLeft | When focus is on DropdownMenu.SubTrigger, opens or closes the submenu depending on reading direction. |
| Esc | Closes the dropdown menu and moves focus to DropdownMenu.Trigger. |

---

## API Reference

## Props

#### ActionMenuCheckboxItem
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `onSelect` | `(event: Event) => void` | No | — |  |
| `asChild` | `boolean` | No | — |  |
| `disabled` | `boolean` | No | — |  |
| `textValue` | `string` | No | — |  |
| `checked` | `CheckedState` | No | — |  |
| `onCheckedChange` | `(checked: boolean) => void` | No | — |  |

#### ActionMenuContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |
| `side` | `"left" \| "right" \| "bottom" \| "top"` | No | — |  |
| `sideOffset` | `number` | No | — |  |
| `align` | `"center" \| "end" \| "start"` | No | — |  |
| `alignOffset` | `number` | No | — |  |
| `arrowPadding` | `number` | No | — |  |
| `avoidCollisions` | `boolean` | No | — |  |
| `collisionBoundary` | `Element \| Element[]` | No | — |  |
| `collisionPadding` | `number \| Partial<Record<"left" \| "right" \| "bottom" \| "top", number>>` | No | — |  |
| `sticky` | `"always" \| "partial"` | No | — |  |
| `hideWhenDetached` | `boolean` | No | — |  |
| `updatePositionStrategy` | `"always" \| "optimized"` | No | — |  |
| `onCloseAutoFocus` | `(event: Event) => void` | No | — | Event handler called when auto-focusing on close. Can be prevented. |
| `loop` | `boolean` | No | — | Whether keyboard navigation should loop around @defaultValue false |
| `onEscapeKeyDown` | `(event: KeyboardEvent) => void` | No | — |  |
| `onPointerDownOutside` | `(event: PointerDownOutsideEvent) => void` | No | — |  |
| `onFocusOutside` | `(event: FocusOutsideEvent) => void` | No | — |  |
| `onInteractOutside` | `(event: PointerDownOutsideEvent \| FocusOutsideEvent) => void` | No | — |  |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### ActionMenuGroup
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

#### ActionMenuIcon
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `side` | `"left" \| "right"` | No | left |  |

#### ActionMenuItem
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `onSelect` | `(event: Event) => void` | No | — |  |
| `asChild` | `boolean` | No | — |  |
| `disabled` | `boolean` | No | — |  |
| `textValue` | `string` | No | — |  |

#### ActionMenuItemIndicator
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### ActionMenuLabel
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

#### ActionMenuPortal
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `container` | `Element \| DocumentFragment` | No | — | Specify a container element to portal the content into. |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### ActionMenuRadioGroup
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |
| `value` | `string` | No | — |  |
| `onValueChange` | `(value: string) => void` | No | — |  |

#### ActionMenuRadioItem
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `onSelect` | `(event: Event) => void` | No | — |  |
| `asChild` | `boolean` | No | — |  |
| `disabled` | `boolean` | No | — |  |
| `textValue` | `string` | No | — |  |
| `value` | `string` | Yes | — |  |

#### ActionMenuRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `density` | `DensityProp` | No | default |  |
| `dir` | `Direction` | No | — |  |
| `open` | `boolean` | No | — |  |
| `defaultOpen` | `boolean` | No | — |  |
| `onOpenChange` | `(open: boolean) => void` | No | — |  |
| `modal` | `boolean` | No | — |  |

#### ActionMenuSeparator
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

#### ActionMenuSub
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `open` | `boolean` | No | — |  |
| `defaultOpen` | `boolean` | No | — |  |
| `onOpenChange` | `(open: boolean) => void` | No | — |  |

#### ActionMenuSubContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `shadowSize` | `ShadowProp` | No | — |  |
| `asChild` | `boolean` | No | — |  |
| `sideOffset` | `number` | No | — |  |
| `alignOffset` | `number` | No | — |  |
| `arrowPadding` | `number` | No | — |  |
| `avoidCollisions` | `boolean` | No | — |  |
| `collisionBoundary` | `Element \| Element[]` | No | — |  |
| `collisionPadding` | `number \| Partial<Record<"left" \| "right" \| "bottom" \| "top", number>>` | No | — |  |
| `sticky` | `"always" \| "partial"` | No | — |  |
| `hideWhenDetached` | `boolean` | No | — |  |
| `updatePositionStrategy` | `"always" \| "optimized"` | No | — |  |
| `loop` | `boolean` | No | — | Whether keyboard navigation should loop around @defaultValue false |
| `onEscapeKeyDown` | `(event: KeyboardEvent) => void` | No | — |  |
| `onPointerDownOutside` | `(event: PointerDownOutsideEvent) => void` | No | — |  |
| `onFocusOutside` | `(event: FocusOutsideEvent) => void` | No | — |  |
| `onInteractOutside` | `(event: PointerDownOutsideEvent \| FocusOutsideEvent) => void` | No | — |  |
| `forceMount` | `true` | No | — | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### ActionMenuSubTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `onClick` | `(() => void) & MouseEventHandler<HTMLDivElement>` | No | — |  |
| `asChild` | `boolean` | No | — |  |
| `disabled` | `boolean` | No | — |  |
| `textValue` | `string` | No | — |  |

#### ActionMenuTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child to allow for formatting |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

```jsx
``
```
