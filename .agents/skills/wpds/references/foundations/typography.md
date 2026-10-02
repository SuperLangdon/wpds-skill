---
title: "Typography"
sourceUrl: "https://build.washingtonpost.com/foundations/typography"
---

# Typography

## Table of contents

- [Font](./typography.md#Font)
- [Font size](./typography.md#Font%20size)
- [Font weight](./typography.md#Font%20weight)
- [Line height](./typography.md#Line%20height)

---

## Font

Font tokens tie an intention to a font family.

```jsx
return function Example() {
  const Headline = styled("h1", {
    fontFamily: theme.fonts.headline, // font family example
    fontSize: theme.fontSizes["200"],
    color: theme.colors.primary,
    marginBlock: 0,
  });
  const Subhead = styled("h2", {
    fontFamily: theme.fonts.subhead, // font family example
    fontWeight: theme.fontWeights.light,
    fontSize: theme.fontSizes["150"],
    color: theme.colors.accessible,
    marginBlock: 0,
  });
  const Body = styled("p", {
    fontFamily: theme.fonts.body, // font family example
    fontSize: theme.fontSizes["100"],
    marginBlock: 0,
  });
  const Meta = styled("p", {
    fontFamily: theme.fonts.meta, // font family example
    fontSize: theme.fontSizes["075"],
    color: theme.colors.accessible,
    marginBlock: 0,
  });
  const Magazine = styled("p", {
    fontFamily: theme.fonts.magazine, // font family example
    fontWeight: theme.fontWeights.ultra,
    fontSize: theme.fontSizes["200"],
    color: theme.colors.primary,
    marginBlock: 0,
  });
  return (
    <div>
      <Headline>Headline</Headline>
      <Magazine>Magazine</Magazine>
      <Subhead>Subheadline</Subhead>
      <Body>Body text</Body>
      <Meta>Meta text</Meta>
    </div>
  );
}
```

| Name | Value | Description |
| --- | --- | --- |
| `$headline` | `Postoni, Postoni-fallback, serif` |  |
| `$subhead` | `Franklin, Franklin-fallback, sans-serif` |  |
| `$body` | `georgia, Times New Roman, serif` |  |
| `$meta` | `Franklin, Franklin-fallback, sans-serif` |  |
| `$magazine` | `PostoniDisplayMag, PostoniDisplayMag-fallback, serif` |  |

---

## Font size

Font size tokens are relative to the [baseSize](./base.md). Use font size tokens to define the size of the font.

```jsx
export default function Example() {
  const FontSizeExample = styled("p", {
    fontFamily: theme.fonts.headline,
    fontSize: theme.fontSizes["200"], // font size example
    color: theme.colors.primary,
  });

  return <FontSizeExample>Headline</FontSizeExample>;
}
```

| Name | Value | Calculated | Description |
| --- | --- | --- | --- |
| `$100` | `1rem` | 16px |  |
| `$112` | `1.125rem` | 18px |  |
| `$125` | `1.25rem` | 20px |  |
| `$150` | `1.5rem` | 24px |  |
| `$162` | `1.625rem` | 26px |  |
| `$175` | `1.75rem` | 28px |  |
| `$200` | `2rem` | 32px |  |
| `$225` | `2.25rem` | 36px |  |
| `$250` | `2.5rem` | 40px |  |
| `$275` | `2.75rem` | 44px |  |
| `$300` | `3rem` | 48px |  |
| `$350` | `3.5rem` | 56px |  |
| `$400` | `4rem` | 64px |  |
| `$450` | `4.5rem` | 72px |  |
| `$500` | `5rem` | 80px |  |
| `$075` | `0.75rem` | 12px |  |
| `$087` | `0.875rem` | 14px |  |

---

## Font weight

Font weight tokens define the weight of the font face.

```jsx
export default function Example() {
  const FontWeightExample = styled("p", {
    fontFamily: theme.fonts.subhead,
    fontWeight: theme.fontWeights.light, // font weight example
    fontSize: theme.fontSizes["200"],
    color: theme.colors.primary,
  });

  return <FontWeightExample>Headline</FontWeightExample>;
}
```

| Name | Value | Description |
| --- | --- | --- |
| `$light` | `300` |  |
| `$regular` | `400` |  |
| `$bold` | `700` |  |
| `$ultra` | `800` |  |

---

## Line height

Line height tokens are unitless values that define the height of a text element based on its current font size.

```jsx
export default function Example() {
  const LineHeightExample = styled("p", {
    fontFamily: theme.fonts.body,
    lineHeight: theme.lineHeights["125"], //Line height example
    fontSize: theme.fontSizes["125"],
    color: theme.colors.primary,
    width: 250,
  });

  return (
    <LineHeightExample>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </LineHeightExample>
  );
}
```

| Name | Value | Description |
| --- | --- | --- |
| `$100` | `1` |  |
| `$110` | `1.1` |  |
| `$125` | `1.25` |  |
| `$150` | `1.5` |  |
| `$160` | `1.6` |  |
| `$175` | `1.75` |  |
| `$200` | `2` |  |
| `$240` | `2.4` |  |
