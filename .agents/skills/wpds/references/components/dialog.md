---
title: "Dialog"
description: "A dialog is an overlay used to display important content or request input from the user. It is layered on top of the primary screen and typically requires the user to take action before continuing."
sourceUrl: "https://build.washingtonpost.com/components/dialog"
---

# Dialog

Note: Dialogs are designed to be attention-grabbing and prominent to ensure that the user sees and interacts with them, therefore, they should only be used to display critical information. For less critical information and tasks, consider using our [drawer component](./drawer.md) or [popover component](./popover.md) for actionable UI and our [tooltip component](./tooltip.md) for non-actionable UI.

---

## Anatomy

<!-- Box: interactive component, rendered on the official site only -->

1. Container
2. Close button icon (optional)
3. Scrim
4. Footer (optional)

---

## Options

### Width

Dialog width can be defined. The default width of the dialog is 500px.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content width="500px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Dialog width</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description>This dialog is 500px wide.</Dialog.Description>
      </Dialog.Body>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Height

Dialog height can be defined. The default height of the dialog is 300px.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content height="300px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Dialog height</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description>This dialog is 300px tall.</Dialog.Description>
      </Dialog.Body>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Optional footer

The footer is optional when using the dialog. It provides recommended positioning and padding for buttons and links on a dialog for both inline (side-by-side) elements and stacked (vertical) elements.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content height="225px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Dialog with footer</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description css={{ marginBlockEnd: 0 }}>
          {`This dialog has a footer with inline elements, or buttons that are
          placed side-by-side.`}
        </Dialog.Description>
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content width="310px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Dialog with footer</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description css={{ marginBlockEnd: 0 }}>
          {`This dialog has a footer with stacked elements, or buttons placed
          vertically above and below each other.`}
        </Dialog.Description>
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Optional close

The dialog close button can be optional. By default, the close button renders in the top right of the dialog content. The button's `asChild` property can be used to give any child button the ability to close the dialog.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content height="117px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Dialog with close</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description css={{ marginBlockEnd: 0 }}>
          {`This dialog has a close button.`}
        </Dialog.Description>
      </Dialog.Body>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Custom scrim color

The scrim color can be changed by defining the color using one of our tokens.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay backgroundColor={"$green500"} />
    <Dialog.Content height="117px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Scrim color</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description css={{ marginBlockEnd: 0 }}>
          {`This example uses $green500 as the scrim color.`}
        </Dialog.Description>
      </Dialog.Body>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Custom container color

The container color can be changed by defining the color using one our tokens.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content height="117px" backgroundColor={"$blue500"}>
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Container color</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description css={{ marginBlockEnd: 0 }}>
          {`This example uses $blue500 as the container color.`}
        </Dialog.Description>
      </Dialog.Body>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

---

## Behavior

### Closing

When the close button is rendered, the dialog can be closed by clicking the scrim, the close button, or the cancel button if one is present.

Note: If the user is required to take action in order to dismiss the dialog, the dialog can be set to open and will remain open even if the scrim is clicked on. The user must then interact with the content in the dialog to close it.

On hover, a circular background color appears behind the close icon.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content height="224px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Closing</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description>
          {`This dialog can be closed by clicking the scrim, the close button, or the Cancel button.`}
        </Dialog.Description>
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Content overflow

Content will overflow, both vertically and horizontally, in the dialog by default. Users can scroll within a dialog. See our guidance on complex and interactive content in dialogs.

Note: If a dialog has vertical overflow, the content in the scrollable area should flow behind the footer. In other words, the footer should be sticky so that the user can always see the action buttons available to them.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content>
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Content overflow</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description
          css={{ marginBottom: "$350" }}
        >{`This dialog is scrollable.`}</Dialog.Description>
        <InputText
          label="Input label"
          name="input-1"
          id="input-1"
          css={{ marginBottom: "$100" }}
        />
        <InputText label="Input label" name="input-2" id="input-2" />
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

---

## Guidance

### Content should be accessible

Make sure color contrasts comply with [WCAG accessible contrast requirements](https://webaim.org/articles/contrast/).

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Content height="204px">
      <Dialog.Close css={{ opacity: 0.25 }} />
      <Dialog.Header>
        <Dialog.Title css={{ color: "$faint" }}>
          Inaccessible text color
        </Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description
          css={{ color: "$faint", marginBlockEnd: 0 }}
        >{`The color of the text and buttons on this dialog is not accessible.`}</Dialog.Description>
      </Dialog.Body>
      <Dialog.Footer css={{ opacity: 0.25 }}>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Buttons and links should be placed at the bottom of the container

Buttons should typically be placed at the bottom right of the container or in the center of the container at full-width. If using text links, they should typically be placed at the bottom-center of the dialog along with any buttons. Dialogs should include a maximum of two buttons.

Confirming buttons should be aligned to the end of the screen. See the example below for reference, where the confirming button is on the right and the dismissing button is to its left.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Content height="204px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Button placement</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description css={{ marginBlockEnd: 0 }}>
          {`Buttons are placed at the bottom right of this dialog.`}
        </Dialog.Description>
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Avoid overly complex or interactive content in dialogs

Be careful with the level of interactivity and complexity of content inside of a dialog. Avoid using scrollbars in dialogs.

Make sure that the dialog contains only the essential information and actions. Consider other options, such as a separate page, for content that takes up a lot of space or requires several actions.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Content height="500px" width="900px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Complex dialog</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Box css={{ marginBlockEnd: "$100" }}>
          <RadioGroup
            legend="Label"
            name="horizontal"
            orientation="horizontal"
            variant="primary"
          >
            <RadioButton label="Option" value="opt1" id="opt1" />
            <RadioButton label="Option" value="opt2" id="opt2" />
            <RadioButton label="Option" value="opt3" id="opt3" />
            <RadioButton label="Option" value="opt4" id="opt4" />
            <RadioButton label="Option" value="opt5" id="opt5" />
            <RadioButton label="Option" value="opt6" id="opt6" />
          </RadioGroup>
        </Box>
        <Box css={{ marginBlockEnd: "$100", display: "flex", gap: "$100" }}>
          <Box css={{ flex: 1 }}>
            <Select.Root>
              <Select.Trigger aria-label="Select options">
                <Select.Label>Label/Placeholder</Select.Label>
                <Select.Value />
              </Select.Trigger>
              <Select.Content css={{ zIndex: "$offer" }}>
                <Select.Item value="op1">Option</Select.Item>
                <Select.Item value="op2">Option</Select.Item>
                <Select.Item value="op3">Option</Select.Item>
                <Select.Item value="op4">Option</Select.Item>
                <Select.Item value="op5">Option</Select.Item>
              </Select.Content>
            </Select.Root>
          </Box>
          <Box css={{ flex: 1 }}>
            <Select.Root>
              <Select.Trigger aria-label="Select options">
                <Select.Label>Label/Placeholder</Select.Label>
                <Select.Value />
              </Select.Trigger>
              <Select.Content css={{ zIndex: "$offer" }}>
                <Select.Item value="op1">Option</Select.Item>
                <Select.Item value="op2">Option</Select.Item>
                <Select.Item value="op3">Option</Select.Item>
                <Select.Item value="op4">Option</Select.Item>
                <Select.Item value="op5">Option</Select.Item>
              </Select.Content>
            </Select.Root>
          </Box>
        </Box>
        <Carousel.Root>
          <Carousel.Header>
            <Carousel.HeaderContent>
              <Carousel.Title
                css={{
                  fontFamily: "$meta",
                  fontWeight: "$bold",
                  fontSize: "$150",
                }}
              >
                Carousel
              </Carousel.Title>
            </Carousel.HeaderContent>
            <Carousel.HeaderActions>
              <Carousel.PreviousButton />
              <Carousel.NextButton />
            </Carousel.HeaderActions>
          </Carousel.Header>
          <Carousel.Content>
            {[...new Array(5)].map((item, i) => (
              <Carousel.Item key={item}>
                <Card
                  css={{
                    width: "300px",
                    height: "250px",
                    marginInlineEnd: "$100",
                    backgroundColor: "$subtle",
                  }}
                />
              </Carousel.Item>
            ))}
          </Carousel.Content>
          <Carousel.Footer>
            <Carousel.Dots />
          </Carousel.Footer>
        </Carousel.Root>
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Dialog should be used with a scrim

Using a scrim with the dialog helps distinguish it from the primary screen in the background. It will help users understand that the dialog is layered above the parent page, shifting the user’s focus appropriately and aligning with best practices for accessibility.

When designing in Figma, pull in the scrim component from the WPDS UI kit to use it in your design.

```jsx
return function Example() {
  const [container, setContainer] = useState();
  return (
    <Box
      css={{
        backgroundImage: "url('/img/components/dialog/article-image.png')",
        width: "100vw",
        height: "calc(100vh - 70px)",
        marginBlockStart: "70px",
        position: "relative",
      }}
      ref={setContainer}
    >
      <Dialog.Root open>
        <Dialog.Portal container={container}>
          <Dialog.Overlay css={{ position: "absolute" }} />
          <Dialog.Content
            css={{ position: "absolute" }}
            width="450px"
            height="307px"
          >
            <Dialog.Header css={{ color: "$accessible", fontSize: "$087" }}>
              {`Subscribe to continue reading. Already a subscriber? `}
              <u>Sign in</u>
            </Dialog.Header>
            <Dialog.Body
              css={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "end",
              }}
            >
              <Box
                css={{
                  display: "flex",
                  border: "1px solid black",
                  fontSize: "$025",
                  textTransform: "uppercase",
                }}
              >
                <Box
                  as="strong"
                  css={{
                    borderInlineEnd: "1px solid black",
                    paddingInline: "$050",
                  }}
                >
                  Limited time offer
                </Box>
                <Box css={{ paddingInline: "$050" }}>2 Days only</Box>
              </Box>
              <Box
                as="h2"
                css={{
                  fontFamily: "$headline",
                  fontWeight: "$bold",
                  fontSize: "$250",
                  marginBlockStart: "$100",
                  marginBlockEnd: "$200",
                }}
              >
                Get one year for $30
              </Box>
              <Box css={{ fontSize: "$125" }}>
                You can <strong>cancel anytime</strong>.
              </Box>
            </Dialog.Body>
            <Dialog.Footer css={{ justifyContent: "center" }}>
              <Button variant="cta" css={{ paddingInline: "$300" }}>
                Subscribe
              </Button>
            </Dialog.Footer>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </Box>
  );
}
```

### Consider screen size when determining the appropriate size for the dialog

Avoid fullscreen dialogs on desktop. On desktop, a dialog should only take up a portion of the screen, with visibility of the primary screen behind it. Ideally, it shouldn’t take up more than 25% of the screen on large screens and desktop.

On tablets and mobile, dialogs may take up a larger portion of the screen, typically 50% to 100%, as the screen size will be smaller.

Note that these percentages are not exact rules but provide general guidelines to follow.

```jsx
export default function Example() {
  const [container, setContainer] = useState();
  return (
    <Box
      css={{
        width: "100vw",
        height: "calc(100vh - 70px)",
        marginBlockStart: "70px",
        position: "relative",
      }}
      ref={setContainer}
    >
      <Dialog.Root open>
        <Dialog.Portal container={container}>
          <Dialog.Overlay css={{ position: "absolute" }} />
          <Dialog.Content
            css={{ position: "absolute" }}
            width="100vw"
            height="100%"
          >
            <Dialog.Close />
            <Dialog.Header>
              <Dialog.Title>Fullscreen dialog</Dialog.Title>
            </Dialog.Header>
            <Dialog.Body>
              <Dialog.Description>
                {`Avoid using fullscreen dialogs on desktop.`}
              </Dialog.Description>
            </Dialog.Body>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </Box>
  );
}
```

```jsx
export default function Example() {
  const [partialContainer, setPartialContainer] = useState();
  const [fullContainer, setFullContainer] = useState();
  return (
    <>
      <Box
        css={{
          marginInlineEnd: "23px",
          width: "375px",
          height: "812px",
          position: "relative",
        }}
        ref={setPartialContainer}
      >
        <Dialog.Root open>
          <Dialog.Portal container={partialContainer}>
            <Dialog.Overlay css={{ position: "absolute" }} />
            <Dialog.Content
              css={{ position: "absolute" }}
              width="311px"
              height="248px"
            >
              <Dialog.Close />
              <Dialog.Header>
                <Dialog.Title>Partial screen dialog</Dialog.Title>
              </Dialog.Header>
              <Dialog.Body>
                <Dialog.Description>
                  {`This is a partial screen mobile dialog.`}
                </Dialog.Description>
              </Dialog.Body>
              <Dialog.Footer>
                <Dialog.Close asChild>
                  <Button>Cancel</Button>
                </Dialog.Close>
                <Button variant="primary">Confirm</Button>
              </Dialog.Footer>
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
      </Box>
      <Box
        css={{
          marginInlineStart: "23px",
          width: "375px",
          height: "812px",
          position: "relative",
        }}
        ref={setFullContainer}
      >
        <Dialog.Root open>
          <Dialog.Portal container={fullContainer}>
            <Dialog.Overlay css={{ position: "absolute" }} />
            <Dialog.Content
              css={{ position: "absolute" }}
              width="100%"
              height="100%"
            >
              <Dialog.Close />
              <Dialog.Header>
                <Dialog.Title>Fullscreen dialog</Dialog.Title>
              </Dialog.Header>
              <Dialog.Body>
                <Dialog.Description>
                  {`This is a fullscreen mobile dialog.`}
                </Dialog.Description>
              </Dialog.Body>
              <Dialog.Footer>
                <Dialog.Close asChild>
                  <Button>Cancel</Button>
                </Dialog.Close>
                <Button variant="primary">Confirm</Button>
              </Dialog.Footer>
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
      </Box>
    </>
  );
}
```

### Ensure that the most critical information goes on the topmost layer

The most critical information should be on the topmost layer, regarding Z-index/layering of the dialog on the page.

```jsx
export default function Example() {
  const [container, setContainer] = useState();
  return (
    <Box
      css={{
        width: "100vw",
        height: "calc(100vh - 70px)",
        marginBlockStart: "70px",
        position: "relative",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: "$050",
      }}
      ref={setContainer}
    >
      <Drawer.Root id="drawer" defaultOpen>
        <Drawer.Trigger>Open Drawer</Drawer.Trigger>
        <Drawer.Content height="200px">
          <Drawer.Close />
          Non-critical information in a drawer.
        </Drawer.Content>
      </Drawer.Root>
      <Dialog.Root defaultOpen>
        <Dialog.Trigger asChild>
          <Button>Open Dialog</Button>
        </Dialog.Trigger>
        <Dialog.Portal container={container}>
          <Dialog.Overlay css={{ position: "absolute" }} />
          <Dialog.Content css={{ position: "absolute" }} height="204px">
            <Dialog.Close />
            <Dialog.Header>
              <Dialog.Title>Critical information</Dialog.Title>
            </Dialog.Header>
            <Dialog.Body>
              <Dialog.Description>
                {`This dialog contains critical information.`}
              </Dialog.Description>
            </Dialog.Body>
            <Dialog.Footer>
              <Dialog.Close asChild>
                <Button>Cancel</Button>
              </Dialog.Close>
              <Button variant="primary">Confirm</Button>
            </Dialog.Footer>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </Box>
  );
}
```

### Do not use nested dialogs

Using a nested dialog creates visual complexity. Multiple layers of information and actions can be confusing to users.

```jsx
export default function Example() {
  const [container, setContainer] = useState();
  const [open, setOpen] = useState(true);
  return (
    <Box
      css={{
        width: "100vw",
        height: "calc(100vh - 70px)",
        marginBlockStart: "70px",
        position: "relative",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: "$050",
      }}
      ref={setContainer}
    >
      <Dialog.Root defaultOpen>
        <Dialog.Trigger asChild>
          <Button>Open Dialog</Button>
        </Dialog.Trigger>
        <Dialog.Portal container={container}>
          <Dialog.Content css={{ position: "absolute" }}>
            <Dialog.Close />
            <Dialog.Header>
              <Dialog.Title>Dialog header</Dialog.Title>
            </Dialog.Header>
            <Dialog.Body>
              <Dialog.Description>
                {`This is sample text that would go inside the dialog component. 
A dialog sits on top of the screen and is used to display content or request input from user`}
              </Dialog.Description>
            </Dialog.Body>
            <Dialog.Footer>
              <Dialog.Close asChild>
                <Button>Cancel</Button>
              </Dialog.Close>
              <Button variant="primary" onClick={() => setOpen(true)}>
                Confirm
              </Button>
            </Dialog.Footer>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
      <Dialog.Root open={open} onOpenChange={(isOpen) => setOpen(isOpen)}>
        <Dialog.Portal container={container}>
          <Dialog.Overlay css={{ position: "absolute" }} />
          <Dialog.Content
            css={{ position: "absolute" }}
            width="400px"
            height="204px"
          >
            <Dialog.Close />
            <Dialog.Header>
              <Dialog.Title>Nested dialog</Dialog.Title>
            </Dialog.Header>
            <Dialog.Body>
              <Dialog.Description>
                {`Do not use nested dialogs.`}
              </Dialog.Description>
            </Dialog.Body>
            <Dialog.Footer>
              <Dialog.Close asChild>
                <Button>Cancel</Button>
              </Dialog.Close>
              <Button variant="primary">Confirm</Button>
            </Dialog.Footer>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </Box>
  );
}
```

### Use clear, consistent language in dialogs

Dialog content should be as concise as possible while still effectively communicating its message to users.

When writing headers and buttons, use explicit button text that indicates exactly what will happen and match headers to corresponding buttons. For example, for a dialog labeled “Save your changes,” instead of using buttons labeled “Yes” and “No,” use wording that is more direct and actionable such as “Save” and “Discard.”

```jsx
export default function Example() {
  const [container, setContainer] = useState();
  return (
    <Box
      css={{
        width: "100vw",
        height: "calc(100vh - 70px)",
        marginBlockStart: "70px",
        position: "relative",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: "$050",
      }}
      ref={setContainer}
    >
      <Dialog.Root defaultOpen>
        <Dialog.Trigger asChild>
          <Button>Open Dialog</Button>
        </Dialog.Trigger>
        <Dialog.Portal container={container}>
          <Dialog.Overlay css={{ position: "absolute" }} />
          <Dialog.Content css={{ position: "absolute" }} height="204px">
            <Dialog.Close />
            <Dialog.Header>
              <Dialog.Title>Save your changes</Dialog.Title>
            </Dialog.Header>
            <Dialog.Body>
              <Dialog.Description>
                {`Would you like to save your changes before exiting?`}
              </Dialog.Description>
            </Dialog.Body>
            <Dialog.Footer>
              <Dialog.Close asChild>
                <Button>Discard</Button>
              </Dialog.Close>
              <Button variant="primary">Save</Button>
            </Dialog.Footer>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </Box>
  );
}
```

---

## Accessibility

### Keyboard interaction

The dialog component is accessible via keyboard interaction. When the dialog trigger or close buttons are focused, the “space” key will open and close a dialog. The "tab" key can be used to navigate focus on the next interactive element contained in the dialog. Pressing “shift + tab” can be used to navigate focus on the previous interactive element contained in the dialog. The element currently in focus is denoted by an outline, using the CSS outline property. Pressing the "enter" ("return") key will trigger or commit the action of the focused element. Pressing the “escape” key closes the dialog.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content height="224px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Keyboard interaction</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description>
          {`Try out keyboard interactions with this dialog by following the instructions above.`}
        </Dialog.Description>
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Include a title and description

An accessible title and optional accessible description should be included to be announced by screen readers when the dialog is opened. Take a look at the code to see the title and description for this example dialog.

```jsx
<Dialog.Root defaultOpen>
  <Dialog.Trigger asChild>
    <Button>Open Dialog</Button>
  </Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content height="244px">
      <Dialog.Close />
      <Dialog.Header>
        <Dialog.Title>Title and description</Dialog.Title>
      </Dialog.Header>
      <Dialog.Body>
        <Dialog.Description>
          {`This is sample text that would go inside the dialog component. 
A dialog sits on top of the screen and is used to display content or request input from user.`}
        </Dialog.Description>
      </Dialog.Body>
      <Dialog.Footer>
        <Dialog.Close asChild>
          <Button>Cancel</Button>
        </Dialog.Close>
        <Button variant="primary">Confirm</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

---

## API Reference

## Props

#### DialogRoot
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `open` | `boolean` | No | — |  |
| `defaultOpen` | `boolean` | No | — |  |
| `onOpenChange` | `(open: boolean) => void` | No | — |  |
| `modal` | `boolean` | No | — |  |

#### DialogContent
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `backgroundColor` | `Color \| Token<"background", string, "colors", "wpds"> \| Token<"outline", string, "colors", "wpds"> \| Token<"errorContainer", string, "colors", "wpds"> \| ... 302 more ... \| Token<...>` | No | $gray700 | Css background color of content |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `width` | `string` | No | 500px | Width in any valid css string |
| `height` | `string` | No | 300px | Height in any valid css string |
| `zIndex` | `ZIndex \| Token<"page", string, "zIndices", "wpds"> \| Token<"offer", string, "zIndices", "wpds"> \| Token<"shell", string, "zIndices", "wpds"> \| Token<...>` | No | 400 | Css z-index |
| `forceMount` | `true` | No | true | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |
| `asChild` | `boolean` | No | — |  |
| `onEscapeKeyDown` | `(event: KeyboardEvent) => void` | No | — | Event handler called when the escape key is down. Can be prevented. |
| `onPointerDownOutside` | `(event: PointerDownOutsideEvent) => void` | No | — | Event handler called when the a `pointerdown` event happens outside of the `DismissableLayer`. Can be prevented. |
| `onFocusOutside` | `(event: FocusOutsideEvent) => void` | No | — | Event handler called when the focus moves outside of the `DismissableLayer`. Can be prevented. |
| `onInteractOutside` | `(event: PointerDownOutsideEvent \| FocusOutsideEvent) => void` | No | — | Event handler called when an interaction happens outside the `DismissableLayer`. Specifically, when a `pointerdown` event happens outside or focus moves outside of it. Can be prevented. |
| `onOpenAutoFocus` | `(event: Event) => void` | No | — | Event handler called when auto-focusing on open. Can be prevented. |
| `onCloseAutoFocus` | `(event: Event) => void` | No | — | Event handler called when auto-focusing on close. Can be prevented. |

#### DialogTrigger
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `asChild` | `boolean` | No | — |  |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |

#### DialogPortal
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `container` | `Element \| DocumentFragment` | No | — | Specify a container element to portal the content into. |
| `forceMount` | `true` | No | true | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |

#### DialogOverlay
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `backgroundColor` | `Color \| Token<"background", string, "colors", "wpds"> \| Token<"outline", string, "colors", "wpds"> \| Token<"errorContainer", string, "colors", "wpds"> \| ... 302 more ... \| Token<...>` | No | rgba(0, 0, 0, .50) | Css background color of overlay |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `zIndex` | `ZIndex \| Token<"page", string, "zIndices", "wpds"> \| Token<"offer", string, "zIndices", "wpds"> \| Token<"shell", string, "zIndices", "wpds"> \| Token<...>` | No | 400 | Css z-index of overlay |
| `forceMount` | `true` | No | true | Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries. |
| `asChild` | `boolean` | No | — |  |

#### DialogTitle
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

#### DialogDescription
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `asChild` | `boolean` | No | — |  |

#### DialogClose
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `asChild` | `boolean` | No | — |  |
| `css` | `CSS` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |

#### DialogHeader
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `css` | `{} & { alignContent?: AlignContent \| ScaleValue \| Globals \| Index; alignItems?: AlignItems \| ScaleValue \| Globals \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |

#### DialogBody
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `css` | `{} & { alignContent?: AlignContent \| ScaleValue \| Globals \| Index; alignItems?: AlignItems \| ScaleValue \| Globals \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |
| `isOverflow` | `boolean \| "true"` | No | — |  |

#### DialogFooter
| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `children` | `ReactNode` | No | — | Any React node may be used as a child |
| `css` | `{} & { alignContent?: AlignContent \| ScaleValue \| Globals \| Index; alignItems?: AlignItems \| ScaleValue \| Globals \| Index; ... 426 more ...; vectorEffect?: VectorEffect \| ... 2 more ... \| Index; } & ... 7 more ... & { ...; }` | No | — | WPDS provides a css prop for overriding styles easily. It’s like the style attribute, but it supports tokens, media queries, nesting and token-aware values. All WPDS Components include a css prop. Use it to pass in overrides. |

```jsx
``
```
