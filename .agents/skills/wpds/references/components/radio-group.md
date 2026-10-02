---
title: "Radio Group"
description: "Use radio buttons when you have a group of mutually exclusive choices and only one selection from the group is allowed."
sourceUrl: "https://build.washingtonpost.com/components/radio-group"
---

# Radio Group

## Anatomy

![Image is not to scale for informative purposes only](https://build.washingtonpost.com/img/components/radio-group/anatomy.svg)

*Image is not to scale for informative purposes only*

1. Radio container
2. Border
3. Filled container

---

## Options

### Variants

There are three variants `primary` `secondary` and `cta`

```jsx
return function Example() {
  return (
    <>
      <RadioGroup
        legend="Primary"
        name="primary"
        defaultValue={"opt1"}
        css={{ marginRight: "$050" }}
        variant="primary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
        <RadioButton label="Option 3" value="opt3" id="opt3" />
      </RadioGroup>
      <RadioGroup
        legend="Secondary"
        name="secondary"
        defaultValue={"opt1"}
        css={{ marginRight: "$050" }}
        variant="secondary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt4" />
        <RadioButton label="Option 2" value="opt2" id="opt5" />
        <RadioButton label="Option 3" value="opt3" id="opt6" />
      </RadioGroup>
      <RadioGroup legend="CTA" name="cta" defaultValue={"opt1"} variant="cta">
        <RadioButton label="Option 1" value="opt1" id="opt7" />
        <RadioButton label="Option 2" value="opt2" id="opt8" />
        <RadioButton label="Option 3" value="opt3" id="opt9" />
      </RadioGroup>
    </>
  );
}
```

---

## Options

### isOutline

```jsx
export default function Example() {
  return (
    <>
      <RadioGroup
        legend="Primary"
        name="primary"
        isOutline
        defaultValue={"opt1"}
        css={{ marginRight: "$050" }}
        variant="primary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
        <RadioButton label="Option 3" value="opt3" id="opt3" />
      </RadioGroup>
      <RadioGroup
        legend="Secondary"
        name="secondary"
        isOutline={"true"}
        defaultValue={"opt1"}
        css={{ marginRight: "$050" }}
        variant="secondary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt4" />
        <RadioButton label="Option 2" value="opt2" id="opt5" />
        <RadioButton label="Option 3" value="opt3" id="opt6" />
      </RadioGroup>
      <RadioGroup
        legend="CTA"
        name="cta"
        isOutline={"true"}
        defaultValue={"opt1"}
        variant="cta"
      >
        <RadioButton label="Option 1" value="opt1" id="opt7" />
        <RadioButton label="Option 2" value="opt2" id="opt8" />
        <RadioButton label="Option 3" value="opt3" id="opt9" />
      </RadioGroup>
    </>
  );
}
```

### Default value

Radio buttons can be preselected or not depending on the situation.

```jsx
export default function Example() {
  return (
    <>
      <RadioGroup
        legend="Select an option"
        name="default-value"
        defaultValue={"opt1"}
        variant="primary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
      </RadioGroup>
    </>
  );
}
```

### Orientation

Radio groups can be either horizontal or vertical. By default, radio groups are vertical.

```jsx
export default function Example() {
  return (
    <Box css={{ display: "flex", gap: "$050" }}>
      <RadioGroup legend="Select an option" name="vertical" variant="primary">
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
        <RadioButton label="Option 3" value="opt3" id="opt3" />
      </RadioGroup>

      <RadioGroup
        legend="Select an option"
        name="horizontal"
        orientation="horizontal"
        variant="primary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
        <RadioButton label="Option 3" value="opt3" id="opt3" />
      </RadioGroup>
    </Box>
  );
}
```

---

## Behaviors

### Disabled

```jsx
export default function Example() {
  return (
    <>
      <RadioGroup
        legend="Select an option"
        disabled
        defaultValue={"opt1"}
        variant="primary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
      </RadioGroup>
    </>
  );
}
```

### Focus

```jsx
export default function Example() {
  return (
    <>
      <Fieldset>
        <b> Radio group example</b>
        <RadioGroup defaultValue={"opt1"} variant="primary">
          <RadioButton label="Click to see focus" value="opt1" id="opt1" />
          <RadioButton label="Click to see focus" value="opt2" id="opt2" />
        </RadioGroup>
      </Fieldset>
    </>
  );
}
```

### Error

```jsx
export default function Example() {
  return (
    <>
      <Fieldset>
        <b> Radio group example</b>
        <RadioGroup
          error
          errorMessage="Optional error message"
          defaultValue={"opt1"}
          variant="primary"
        >
          <RadioButton label="Click to see focus" value="opt1" id="opt1" />
          <RadioButton label="Click to see focus" value="opt2" id="opt2" />
        </RadioGroup>
      </Fieldset>
    </>
  );
}
```

### Text Overflow

```jsx
export default function Example() {
  return (
    <>
      <Fieldset css={{ maxWidth: 150 }}>
        <b> Radio group example</b>
        <RadioGroup defaultValue={"opt1"} variant="primary">
          <RadioButton
            label="Choice 1 demonstrates how this text wraps to two line"
            value="opt1"
            id="opt1"
          />
          <RadioButton label="Click to see focus" value="opt2" id="opt2" />
        </RadioGroup>
      </Fieldset>
    </>
  );
}
```

---

## Guidance

### When error should be shown

Error should only occur if the options were not pre-selected and user tries to continue without selecting an option. Required radio groups should be indicated in the label with a * in the error token color. Suplementary error message should be shown below the group.

```jsx
export default function Example() {
  return (
    <>
      <RadioGroup
        legend="Select an option"
        error
        errorMessage="Please select an option"
        variant="primary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
        <RadioButton label="Option 3" value="opt3" id="opt3" />
        <RadioButton label="Option 4" value="opt4" id="opt4" />
      </RadioGroup>
    </>
  );
}
```

### Required

When radio button selection is required it should be reflected in the fieldset label.

```jsx
export default function Example() {
  return (
    <>
      <RadioGroup
        legend="Select an option"
        required
        error
        errorMessage="Please select an option"
        variant="primary"
      >
        <RadioButton label="Option 1" value="opt1" id="opt1" />
        <RadioButton label="Option 2" value="opt2" id="opt2" />
        <RadioButton label="Option 3" value="opt3" id="opt3" />
        <RadioButton label="Option 4" value="opt4" id="opt4" />
      </RadioGroup>
    </>
  );
}
```

### Avoid using radio buttons for a binary choice

The toggle or checkbox is most often used for settings and allows the user to choose between yes/no options or on/off.

```jsx
export default function Example() {
  return (
    <>
      <RadioGroup legend="Select an option" variant="primary">
        <RadioButton label="Yes" value="opt1" id="opt1" />
        <RadioButton label="No" value="opt2" id="opt2" />
      </RadioGroup>
    </>
  );
}
```

---

## API Reference

## Props

#### RadioGroup
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `buttonsWrapperCss` | `CSS` | No | — | CSS passed to RadioButtons parent element |
| `defaultValue` | `string & (string \| number \| readonly string[])` | No | — |  |
| `dir` | `"ltr" \| "rtl"` | No | — |  |
| `loop` | `boolean` | No | — |  |
| `name` | `string` | Yes | — | Shared name of group radios |
| `onValueChange` | `(value: string) => void` | No | — |  |
| `orientation` | `"horizontal" \| "vertical"` | No | — |  |
| `required` | `boolean` | No | — |  |
| `value` | `string` | No | — |  |
| `legend` | `ReactNode` | Yes | — | Legend text labelling entire group |
| `disabled` | `boolean` | No | — | Inputs are disabled, changing appearance and preventing input |
| `error` | `boolean` | No | — | If there is an error with the fields |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `errorMessage` | `ReactNode` | No | — | Description of error |
| `isOutline` | `boolean` | No | false | Only the radio button's outline is displayed |
| `variant` | `"cta" \| "secondary" \| "primary"` | No | primary | Color variants |

#### RadioButton
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `required` | `boolean` | No | — |  |
| `value` | `string` | Yes | — | underlying value for input |
| `label` | `string` | Yes | — | label text displayed next to button |
| `id` | `string` | Yes | — | id of input |
| `asChild` | `boolean` | No | — |  |
| `error` | `boolean` | No | — | displays error state with colored border |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `isOutline` | `boolean \| "true"` | No | — |  |
| `checked` | `boolean` | No | — |  |
| `variant` | `"cta" \| "secondary" \| "primary"` | No | primary |  |
| `isInvalid` | `boolean \| "true"` | No | — |  |
