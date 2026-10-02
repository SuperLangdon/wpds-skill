---
title: "Alert Banner"
description: "Alert banners notify the user of important messages, such as system alerts. They're meant to encourage the user to take an action."
sourceUrl: "https://build.washingtonpost.com/components/alert-banner"
---

# Alert Banner

---

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/alertbanner/anatomy.svg)

*Note: Image is not  to scale*

1. Icon - Semantic only
2. Text
3. App bar
4. Button icon

---

## Options

### Variants

There are four variants `warning`, `information`, `success`, and `error`.

```jsx
return function Example() {
  return (
    <Box
      css={{
        display: "flex",
        width: "100%",
        rowGap: "$100",
        flexDirection: "column",
      }}
    >
      <AlertBanner.Root variant="error">
        <AlertBanner.Content>Error</AlertBanner.Content>
      </AlertBanner.Root>
      <AlertBanner.Root variant="information">
        <AlertBanner.Content>Information</AlertBanner.Content>
      </AlertBanner.Root>
      <AlertBanner.Root variant="success">
        <AlertBanner.Content>Success</AlertBanner.Content>
      </AlertBanner.Root>
      <AlertBanner.Root variant="warning">
        <AlertBanner.Content>Warning</AlertBanner.Content>
      </AlertBanner.Root>
    </Box>
  );
}
```

### Shadow

Enable shadow by passing `shadow` property.

```jsx
export default function Example() {
  return (
    <AlertBanner.Root shadow variant="information">
      <AlertBanner.Content>Information</AlertBanner.Content>
    </AlertBanner.Root>
  );
}
```

### Dismissable

To allow the Alert Banner to be dismissed pass the `dismissable` property and add `<AlertBanner.Trigger/>`.

```jsx
export default function Example() {
  return (
    <AlertBanner.Root dismissable variant="information">
      <AlertBanner.Trigger />
      <AlertBanner.Content>Information</AlertBanner.Content>
    </AlertBanner.Root>
  );
}
```

---

## Behavior

### Text overflow

When the text overflows it will wrap and resize the AlertBanner.

```jsx
export default function Example() {
  return (
    <Box css={{ maxWidth: 400 }}>
      <AlertBanner.Root dismissable variant="information">
        <AlertBanner.Trigger />
        <AlertBanner.Content>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Est
          adipiscing nunc, ultricies in nibh mauris at. Ut aliquet felis platea
          dolor lacus, at at. Vitae est maecenas pulvinar aenean ullamcorper.
          Enim, nisi interdum mauris, accumsan gravida diam.
        </AlertBanner.Content>
      </AlertBanner.Root>
    </Box>
  );
}
```

---

## Guidance

### When to use shadows

Apply the property `shadow` when overlaying content.

![](https://build.washingtonpost.com/img/components/alertbanner/overlaying-content.svg)

### Semantic messaging only

The alert banner is strictly for semantic messaging around system status. This means the use of including marketing or other messaging diminishes the effectiveness of semantic messaging.

![](https://build.washingtonpost.com/img/components/alertbanner/semantic-messaging.svg)

---

## API Reference

## Props

#### AlertBannerRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `position` | `"fixed" \| "absolute" \| "relative" \| "sticky"` | No | — | App bar's position in time and space |
| `shadow` | `boolean \| "true"` | No | — | App bar's shadow in time and space |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `variant` | `"error" \| "warning" \| "success" \| "information"` | No | information as AlertBannerVariants[variant] | 4 predefined alert banners each tied to our symantic messaging on our site. They are Warning, Information, Success, and Error. |
| `dismissable` | `boolean \| "false"` | No | true as AlertBannerVariants[dismissable] | The alert banner can be permanent or dismissable. |

#### AlertBannerTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `icon` | `"left" \| "right" \| "center" \| "none"` | No | — |  |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `variant` | `"cta" \| "secondary" \| "primary"` | No | — |  |
| `density` | `"default" \| "compact"` | No | — |  |
| `isOutline` | `boolean \| "true" \| "false"` | No | — |  |

#### AlertBannerContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `as` | `never` | No | — | WPDS provides an as prop for changing which tag a component outputs. |
| `css` | `CSS<{ sm: `(max-width: ${string})`; md: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; lg: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; xxl: `(min-width: calc(${string} + 1px)) and (max-width: ${string})`; notS...` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
