---
title: "Space"
sourceUrl: "https://build.washingtonpost.com/foundations/space"
---

# Space

Space tokens are relative to the [baseSize](./base.md). Use space tokens to define padding or margin when designing a component or layout. When using space tokens in code, you can access them using `theme.space.[tokenName]`

```jsx
return function Example() {
  const SpaceExample = styled("div", {
    padding: theme.space["300"], // Space example
    marginRight: theme.space["200"], // Space example
    backgroundColor: theme.colors.primary,
    color: theme.colors.onPrimary,
  });
  return (
    <>
      <SpaceExample>Item 1</SpaceExample>
      <SpaceExample>Item 2</SpaceExample>
    </>
  );
}
```

| Name | Value | Calculated | Description |
| --- | --- | --- | --- |
| `$100` | `1rem` | 16px |  |
| `$125` | `1.25rem` | 20px |  |
| `$150` | `1.5rem` | 24px |  |
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
| `$025` | `0.25rem` | 4px |  |
| `$050` | `0.5rem` | 8px |  |
| `$075` | `0.75rem` | 12px |  |
