---
title: "Input Text"
description: "A text field is an input that allows a user to write or edit text."
sourceUrl: "https://build.washingtonpost.com/components/input-text"
---

# Input Text

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/input-text/anatomy.svg)

*Note: Image is not  to scale*

1. Input value
2. Label/Placeholder
3. Border
4. Button Icon
5. Contextual Icon (non-actionable)
6. Optional Helper text

---

## Options

### Icon

Icon has two placements `left` or `right`.

```jsx
return function Example() {
  return (
    <Box css={{ display: "flex", flexDirection: "column", gap: "$050" }}>
      <InputText icon="right" label="Search">
        <Icon label="">
          <Search />
        </Icon>
      </InputText>
      <InputText icon="left" label="Email">
        <Icon label="">
          <Email />
        </Icon>
      </InputText>
      <InputText icon="right" label="Label"></InputText>
    </Box>
  );
}
```

### Types

Text input supports the following text inputs: `text` `search` `url` `tel` `email`.

```jsx
export default function Example() {
  return (
    <Box css={{ display: "flex", flexDirection: "column", gap: "$050" }}>
      <InputText defaultValue="Jane Doe" type="text" label="Name" />
      <InputText defaultValue="Apples" type="search" label="Search" />
      <InputText
        icon="left"
        type="email"
        defaultValue="Jane@mail.com"
        label="Email"
      >
        <Icon label="">
          <Email />
        </Icon>
      </InputText>
      <InputText
        icon="left"
        type="url"
        defaultValue="www.washingtonpost.com"
        label="Website"
      >
        <Icon label="">
          <Globe />
        </Icon>
      </InputText>
      <InputText
        icon="left"
        type="tel"
        defaultValue="123-456-7890"
        label="Phone"
      >
        <Icon label="">
          <Phone />
        </Icon>
      </InputText>
    </Box>
  );
}
```

### Helper Text

Input text supports an optional help text.

```jsx
export default function Example() {
  const HelperText = () => {
    return (
      <span>
        Not sure what to type in reach out to <a href="#">WPDS</a>
      </span>
    );
  };
  return (
    <InputText
      helperText={<HelperText />}
      icon="right"
      label="Label"
    ></InputText>
  );
}
```

---

## Behavior

### Focus

Click input text component to demostrate focus.

```jsx
export default function Example() {
  return <InputText label="Label"></InputText>;
}
```

### Error

```jsx
export default function Example() {
  return (
    <InputText
      type="email"
      icon="left"
      defaultValue="MyEmail@@mail.com"
      error
      errorMessage="Please use a valid email"
      label="Email"
    >
      <Icon label="">
        <Email />
      </Icon>
    </InputText>
  );
}
```

### Success

```jsx
export default function Example() {
  return <InputText success label="Label"></InputText>;
}
```

### Required

```jsx
export default function Example() {
  return <InputText label="Label" required></InputText>;
}
```

### Disabled

```jsx
export default function Example() {
  return <InputText disabled label="Label"></InputText>;
}
```

### Text Overflow

Overflow of the input value is indicated by an ellipse.

```jsx
export default function Example() {
  return (
    <InputText
      css={{ width: 160 }}
      defaultValue="A Very long input value shown here."
      label="Label"
    ></InputText>
  );
}
```

---

## Guidance

### Actionable inputs

Inputs that require user to take action and include an icon should have the icon be right. A left icon is meant for contextualizing the input.

```jsx
export default function Example() {
  // This code demonstrates a configuration against our reccomended guidance
  return (
    <InputText defaultValue="Apples" icon="left" label="Search">
      <Icon>
        <Search label="" />
      </Icon>
    </InputText>
  );
}
```

## API Reference

## Props

#### InputText
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `buttonIconText` | `string` | No | — | Accessible text for button icon, required for right icons |
| `icon` | `"left" \| "right" \| "none"` | No | none | The position of the icon in the input |
| `error` | `boolean` | No | — | Indicates there is an error |
| `success` | `boolean` | No | — | indicates there is a success |
| `disabled` | `boolean` | No | — | The underlying input element disabled attribute |
| `label` | `string` | Yes | — | The input's label text, required for accessibility |
| `name` | `string` | Yes | — | The name for the underlying input element |
| `placeholder` | `string` | No | — | placeholder text |
| `required` | `boolean` | No | — | The input elements required attribute |
| `type` | `"number" \| "text" \| "search" \| "email" \| "password" \| "tel" \| "url"` | No | text | Supported input element types |
| `value` | `string` | No | — | The input element value for controlled components |
| `onChange` | `(event: ChangeEvent<HTMLInputElement>) => void` | No | — | Callback executed when the input fires a change event |
| `defaultValue` | `string` | No | — | The initial input element value for uncontrolled components |
| `id` | `string` | Yes | — | The id for the underlying input element. Required for accessibility |
| `children` | `ReactNode` | No | — | Used to insert Icons in the input, only a single child is accepted |
| `onFocus` | `FocusEventHandler<HTMLInputElement>` | No | — | Callback executed when the input fires a focus event |
| `onBlur` | `FocusEventHandler<HTMLInputElement>` | No | — | Callback executed when the input fires a blur event |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `buttonIconType` | `"button" \| "reset" \| "submit"` | No | button | Explicit button icon typing for use in forms |
| `errorMessage` | `ReactNode` | No | — | Text displayed below the input to describe the cause of the error |
| `helperText` | `ReactNode` | No | — | Text displayed below the input to provide additional context |
| `onButtonIconClick` | `(event: MouseEvent<HTMLButtonElement, MouseEvent>) => void` | No | — | Callback executed when the button icon on the right is click to perform an action |
