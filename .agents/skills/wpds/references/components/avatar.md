---
title: "Avatar"
description: "Avatar is a round container that holds a profile image to be used."
sourceUrl: "https://build.washingtonpost.com/components/avatar"
---

# Avatar

---

## Anatomy

![Note: Image is not to scale](https://build.washingtonpost.com/img/components/avatar/anatomy.svg)

*Note: Image is not to scale*

1. Image container

---

## Options

### Size

Avatar supports any size token. The default size token is 200.

```jsx
return function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <Avatar size="200">
        <img
          src="https://i.pravatar.cc/300"
          alt="An avatar is an atomic component that represents an individual’s identity through a circular photo."
        />
      </Avatar>
      <Avatar size="300">
        <img
          src="https://i.pravatar.cc/300"
          alt="An avatar is an atomic component that represents an individual’s identity through a circular photo."
        />
      </Avatar>
      <Avatar size="400">
        <img
          src="https://i.pravatar.cc/300"
          alt="An avatar is an atomic component that represents an individual’s identity through a circular photo."
        />
      </Avatar>
      <Avatar size="500">
        <img
          src="https://i.pravatar.cc/300"
          alt="An avatar is an atomic component that represents an individual’s identity through a circular photo."
        />
      </Avatar>
    </Box>
  );
}
```

---

## Guidance

### Supports only 1:1 image ratios

Images set to the height and clipped in a round container. When images are not in a 1:1 aspect they will be distorted.

```jsx
export default function Example() {
  return (
    <Box
      css={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
        gap: "$100",
      }}
    >
      <img
        height="64"
        src="https://i.pravatar.cc/300"
        alt="An avatar is an atomic component that represents an individual’s identity through a circular photo."
      />
      <Avatar size="400">
        <img
          src="https://i.pravatar.cc/300"
          alt="An avatar is an atomic component that represents an individual’s identity through a circular photo."
        />
      </Avatar>
      <img
        width="64"
        height="96"
        src="https://images.pexels.com/photos/2220401/pexels-photo-2220401.jpeg?dpr=2"
        alt="A 64px wide and 96 pixel high image."
      />
      <Avatar size="400">
        <img
          width="64"
          height="96"
          src="https://images.pexels.com/photos/2220401/pexels-photo-2220401.jpeg?dpr=2"
          alt="A 64px wide and 96 pixel high image."
        />
      </Avatar>
    </Box>
  );
}
```

### Recommended spacing

When inline, Avatars should maintain at least the recommended spacing

![](https://build.washingtonpost.com/img/components/avatar/avatar-label-spacing.svg)

---

## Accessibility

Avatars should always include alt text of the image.

---

## API Reference

## Props

#### Avatar
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `size` | `number \| "100" \| "125" \| "150" \| "175" \| "200" \| "225" \| "250" \| "275" \| "300" \| "350" \| "400" \| "450" \| "500" \| "075" \| "087" \| "025" \| "050"` | No | 200 | Sizes - supports any size token |
| `asChild` | `boolean` | No | — |  |
| `css` | `{} & { alignContent?: AlignContent \| Globals \| ScaleValue \| Index; alignItems?: AlignItems \| Globals \| ScaleValue \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
