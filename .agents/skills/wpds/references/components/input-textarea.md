---
title: "Input Text Area"
description: "A text area lets users enter long form text which spans over multiple lines."
sourceUrl: "https://build.washingtonpost.com/components/input-textarea"
---

# Input Text Area

## Anatomy

![Note: Image is not  to scale](https://build.washingtonpost.com/img/components/input-textarea/anatomy.svg)

*Note: Image is not  to scale*

1. Label
2. Value
3. Border
4. Browser Default drag icon

---

## Options

### Resize

The text area can prevent reize by setting `canResize` to false.

```jsx
return function Example() {
  return (
    <Box css={{ display: "flex", flexDirection: "column", gap: "$050" }}>
      <InputTextarea canResize={false} label="Label" />
      <InputTextarea label="Label" />
    </Box>
  );
}
```

### Helper text

The text area has optional helper text.

```jsx
export default function Example() {
  return (
    <Box css={{ display: "flex", flexDirection: "column", gap: "$050" }}>
      <InputTextarea
        helperText={<p>Please keep your message brief</p>}
        label="Label"
      />
    </Box>
  );
}
```

---

## Behavior

### Default

The text area can resize by default.

```jsx
export default function Example() {
  return <InputTextarea label="Label" />;
}
```

### Error

```jsx
export default function Example() {
  return (
    <InputTextarea
      error
      errorMessage={<p>Please enter your message before submitting</p>}
      required
      label="Label"
    />
  );
}
```

### Success

```jsx
export default function Example() {
  const message =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut dignissim eros at velit iaculis accumsan. Praesent ullamcorper faucibus lobortis. Fusce accumsan tempus nisi, a pulvinar nunc pharetra ut. Integer mauris dui, sollicitudin a aliquam sed, aliquam sed sapien. Vivamus nibh arcu, laoreet nec aliquam sed, rutrum eget elit. Etiam et hendrerit lorem. Nunc ac nisi vel massa mollis pretium. Sed ac fermentum quam. Vivamus nulla libero, consequat sed efficitur vel, vulputate vel nunc. Proin purus nisl, vestibulum venenatis vulputate ac, tempor eget nunc. Integer tortor justo, viverra accumsan diam sed, laoreet mattis quam. Donec dapibus risus vitae urna suscipit ultrices. Vivamus dapibus tortor ligula, a feugiat eros fringilla a.";
  return <InputTextarea defaultValue={message} success={true} label="Label" />;
}
```

### Required

```jsx
export default function Example() {
  return <InputTextarea required label="Label" />;
}
```

---

## Guidance

### Do not use textarea for single or short inputs

Textarea are for multiline text such as a sentence or a paragraph.

```jsx
export default function Example() {
  return <InputTextarea defaultValue="John Doe" required label="Name" />;
}
```

## API Reference

## Props

#### InputTextarea
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | children |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `defaultValue` | `string` | No | — | The initial input element value for uncontrolled components |
| `disabled` | `boolean` | No | — | The underlying textarea element disabled attribute |
| `error` | `boolean` | No | — | if the element has an error |
| `errorMessage` | `ReactNode` | No | — | Text displayed below the input to describe the cause of the error |
| `helperText` | `ReactNode` | No | — | Text displayed below the input to provide additional context |
| `label` | `string` | Yes | — | Label (use instead of Placeholder) |
| `id` | `string` | Yes | — | An id attribute to allow the <InputTextarea> to be associated with a <label> element for accessibility purposes |
| `name` | `string` | Yes | — | A name attribute to set the name of the associated data point submitted to the server when the form is submitted. |
| `onBlur` | `FocusEventHandler<HTMLTextAreaElement>` | No | — | Callback executed when the input fires a blur event |
| `onChange` | `(event: ChangeEvent<HTMLTextAreaElement>) => void` | No | — | Callback executed when the input fires a change event |
| `onFocus` | `FocusEventHandler<HTMLTextAreaElement>` | No | — | Callback executed when the input fires a focus event |
| `placeholder` | `string` | No | — | placeholder text |
| `required` | `boolean` | No | — | The input elements required attribute |
| `value` | `string` | No | — | The input element value for controlled components |
| `canResize` | `boolean \| "false"` | No | — | Enable to allow for the text area to be resized by the user. |
