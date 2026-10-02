---
title: "Input Password"
sourceUrl: "https://build.washingtonpost.com/components/input-password"
---

# Input Password

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/input-password/anatomy.svg)

*Note: Image is not  to scale*

1. Password value
2. Password Label
3. Input container
4. Button Icon

---

## Options

### Helper Text

Helper text can be added to the input.

```jsx
return function Example() {
  return (
    <InputPassword
      helperText={
        <Link href="#" css={{ textDecoration: "underline" }}>
          Forgot password
        </Link>
      }
    />
  );
}
```

---

## Behavior

### Hidden value

The password input by default renders the password hidden.

```jsx
export default function Example() {
  return <InputPassword />;
}
```

### Focus

Click password input to demostrate the focus state.

```jsx
export default function Example() {
  return <InputPassword />;
}
```

### Error

```jsx
export default function Example() {
  return (
    <InputPassword
      errorMessage="Sorry, that password does not match our records. Please check your username or password and try again."
      error={true}
    />
  );
}
```

### Disabled

```jsx
export default function Example() {
  return <InputPassword disabled />;
}
```

### Text Overflow

```jsx
export default function Example() {
  return (
    <InputPassword value="A really really really really really long password" />
  );
}
```

---

## Guidance

### Ensure the width of the field appropriately sized

Password lengths can vary based on user preference; ensure any reasonably long password will be fully visible within the input.

```jsx
export default function Example() {
  return <InputPassword css={{ width: "60px" }} defaultValue="123456789" />;
}
```

---

## API Reference

## Props

#### InputPassword

A pre-configured InputText that provides show/hide password interaction

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | `string` | No | Password | The input's label text, required for accessibility |
| `error` | `boolean` | No | — | Indicates there is an error |
| `success` | `boolean` | No | — | indicates there is a success |
| `disabled` | `boolean` | No | — | The underlying input element disabled attribute |
| `name` | `string` | Yes | — | The name for the underlying input element |
| `placeholder` | `string` | No | — | placeholder text |
| `required` | `boolean` | No | — | The input elements required attribute |
| `value` | `string` | No | — | The input element value for controlled components |
| `onChange` | `(event: ChangeEvent<HTMLInputElement>) => void` | No | — | Callback executed when the input fires a change event |
| `defaultValue` | `string` | No | — | The initial input element value for uncontrolled components |
| `id` | `string` | Yes | — | The id for the underlying input element. Required for accessibility |
| `onFocus` | `FocusEventHandler<HTMLInputElement>` | No | — | Callback executed when the input fires a focus event |
| `onBlur` | `FocusEventHandler<HTMLInputElement>` | No | — | Callback executed when the input fires a blur event |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `buttonIconType` | `"button" \| "reset" \| "submit"` | No | — | Explicit button icon typing for use in forms |
| `errorMessage` | `ReactNode` | No | — | Text displayed below the input to describe the cause of the error |
| `helperText` | `ReactNode` | No | — | Text displayed below the input to provide additional context |
| `hideButtonIconText` | `string` | No | Hide password text | Accessible text for the hide icon button |
| `showButtonIconText` | `string` | No | Show password text | Accessible text for the show icon button |
