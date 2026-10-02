---
title: "Shadow"
description: "Shadow tokens are predefined box-shadow values."
sourceUrl: "https://build.washingtonpost.com/foundations/shadow"
---

# Shadow

When using shadow tokens in code, you can access them using `theme.shadows[tokenName]`

```jsx
return function Example() {
  const ShadowExample = styled("p", {
    padding: theme.space["100"],
    boxShadow: theme.shadows["300"], //Shadow example
    backgroundColor: theme.colors.secondary,
    color: theme.colors.onSecondary,
  });

  return <ShadowExample>Shadow Example</ShadowExample>;
}
```

| Name | Value | Description |
| --- | --- | --- |
| `$50` | `0px 2px 0px 0px #D5D5D5` | Shadow 1 - Card shadow |
| `$100` | `0px 1px 2px 0px rgba(0, 0, 0, 0.15)` | Shadow 2 - Extra small base shadow |
| `$200` | `0px 2px 4px 0px rgba(0, 0, 0, 0.15)` | Shadows 3 - Small |
| `$300` | `0px 4px 8px 0px rgba(0, 0, 0, 0.15)` | Shadows 4 - Medium |
| `$400` | `0px 8px 16px 0px rgba(0, 0, 0, 0.15)` | Shadows 5 - Large |
| `$500` | `0px 16px 32px 0px rgba(0, 0, 0, 0.15)` | Shadows 6 - Extra large |
