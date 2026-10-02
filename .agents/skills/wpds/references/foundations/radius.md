---
title: "Radius"
sourceUrl: "https://build.washingtonpost.com/foundations/radius"
---

# Radius

Radius tokens are relative to the [baseSize](./base.md). Use radius tokens to define the border-radius of an element. When using border-radius tokens in code, you can access them using `theme.radii[tokenName]`

```jsx
return function Example() {
  const SpaceExample = styled("div", {
    padding: theme.space["300"],
    borderRadius: theme.radii["075"], // Radius example
    backgroundColor: theme.colors.primary,
    color: theme.colors.onPrimary,
  });
  return (
    <>
      <SpaceExample>Example</SpaceExample>
    </>
  );
}
```

| Name | Value | Calculated | Description |
| --- | --- | --- | --- |
| `$100` | `1rem` | 16px |  |
| `$125` | `1.25rem` | 20px |  |
| `$150` | `1.5rem` | 24px |  |
| `$012` | `0.125rem` | 2px |  |
| `$025` | `0.25rem` | 4px |  |
| `$050` | `0.5rem` | 8px |  |
| `$075` | `0.75rem` | 12px |  |
| `$round` | `9999px` | — |  |
