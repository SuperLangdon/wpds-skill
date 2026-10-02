---
title: "How to use the WPDS Carousel component in your Figma design"
description: "WPDS Carousel is robust enough to support a variety of use-cases. In this guide, we’ll show you how to implement the component in your designs and get the most out of its many features. You’ll also learn how to configure the Carousel to enable custom elements such as your own button controls or custom content."
sourceUrl: "https://build.washingtonpost.com/resources/tutorials/carousel"
---

# How to use the WPDS Carousel component in your Figma design

## Getting Started

### What is a Carousel?

In simple terms, a carousel is a type of container that displays a sequence of items, which can be interacted with by clicking or swiping—much like a deck of cards or an old-fashioned slide projector – ie a “carousel”. Carousels are an extremely common UI pattern and it’s likely you’ve come across various instances of them across the web. Many websites make use of carousels— from news publishers and streaming platforms to e-commerce sites, recipe blogs and cloud-based tools.

![Some examples of carousels from across the web](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_1.png)

*Some examples of carousels from across the web*

### When Should I Use a Carousel?

Carousels are often a great choice for presenting individual cards or a collection of content in a format that is familiar to many users. Because they are interactive, carousels encourage discovery by permitting users to toggle the visibility of items in the sequence. The ability to navigate between previous and next items builds anticipation and gives users a sense of control.

In addition, using a carousel in your design can be an economical use of visual ‘real-estate’, as carousels typically don’t occupy much vertical space, but may display a continuous row of items, such as a series of articles. In contrast, a grid or photo gallery might occupy multiple rows or the whole page. This makes carousels convenient for use in scenarios in which free space is limited, such as on mobile screens.

### When Should I Avoid Using a Carousel?

In the browser, carousels can present challenges for users who rely on screen-readers or other assistive technology. Because carousels are inherently meant to hide or show individual items based on user-feedback, there’s a chance some content will be obscured from view, either visually or programmatically. This might result in important or essential information becoming hard to read or otherwise inaccessible to some screen-readers and users with visual impairments.

The WPDS Carousel is designed with modern accessibility best-practices in mind. The component supports reduced-motion and keyboard-enabled navigation and has been built to interoperate with screen reading technology. However, performance and functionality in these areas might be impacted when using rich media in your carousel (such as embedded audio or video). Ultimately it’s important to work closely with your engineering team to ensure that implementation of the carousel meets functional UX requirements and accessibility standards for your use-case.

Now that we’ve had a chance to understand Carousels as a UI pattern, let’s learn how to use the WPDS Carousel component in your Figma designs.

### But First – Component Docs!

Before delving further into this guide, we highly recommend taking the time to read our component documentation for WPDS Carousel, if you haven’t already done so. As a starting point, the Carousel component doc provides plenty of useful information regarding the component’s key technical features and functionality, including considerations for web-accessibility.

---

## Configuring the Carousel

### Figma’s Component Properties

WPDS Carousel takes advantage of **component properties**, a native feature in Figma. With component properties or ‘props’, we can build components that are flexible enough to configure according to your needs, while preserving reusability. A further benefit of this approach is that we can establish a direct relationship between the **design** component that lives in Figma and the **coded** component that lives in the browser, because they share the same properties. (Learn more about “connected components” in our [Zeplin resource guide](../guides/zeplin-guide.md)).

### Adding an Instance of the Carousel to your Figma Design

Like all of the components in our UI Kit Library, the Carousel component can be placed into your Figma file by dragging an instance of it from the **“Assets”** panel into your document.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_2.gif)

### Renaming the Carousel

In the design panel, you will see the `⬦Carousel` component instance, along with its configurable properties — including `🄵 title`.

By default, the text displayed at the top of the component is *“Carousel title”*. To alter this text, simply **click the input** field next to `🄵 title` to edit its value and press enter when done.

If you’d prefer not to display a title for your Carousel, you may **toggle the switch** next to `🄵 show title?`. (Toggling this setting hides the text layer in your `⬦Carousel` instance.)

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_3.gif)

### Positioning the controls

`⬦Carousel` ships with several options for placement of controls (e.g. prev / next buttons) and pagination — including the option to hide controls entirely.

To change where controls are placed, **click the dropdown menu** next to `🄵 controls` and select the option that’s most suitable to your design.

The available options are meant to serve a variety of use-cases and visual preferences while maintaining functionality and predictability for our website visitors. (For more guidance on custom controls, see section 4: Advanced Customization)

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_4.gif)

### Resizing the Carousel

To adjust the **width**, simply **drag the right or left edge** of the `⬦Carousel` frame. You may choose to make your instance of the component narrower or wider, depending on the space available in your design. Increasing the width will reveal additional content items nested within the component. (For more guidance on this, see section 3: Working with Content).

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_5.gif)

### Dynamic height with Auto layout

Using Figma’s Auto Layout feature, we can set the vertical dimension of `⬦Carousel` to “hug” its contents. This means the **height** of the carousel is determined by the content nested within it, and will adapt its height accordingly.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_6.png)

---

## Working with Carousel Content

### Selecting a content type

As previously discussed – Carousels can contain many kinds of content. The WPDS Carousel component ships with a number of content types to pick from when populating your instance (more on “content organisms” below).

To choose from the available options, **click the dropdown** menu next to `🄵 content type` and make a selection. Your selection will be applied to all nested **“Slot”** elements within your `⬦Carousel` instance.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_7.gif)

### Content Organisms

The options found under `🄵 content type` represent specific content patterns commonly found across washingtonpost.com. These “organisms” are in fact, unique sub-components that are maintained in their own dedicated Figma library (ie **Pattern Kit**), which lives outside of the core WPDS UI kit.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_8.gif)

### Editing Content via Component Properties

Each content type features its own, unique component properties. Once you’ve selected a content type, its properties can be modified directly in the Design panel. Any edits you make will be applied to your instance of `⬦Carousel`.

![The “Story card” (content organism) features several component properties.](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_9.gif)

*The “Story card” (content organism) features several component properties.*

---

## Advanced Customization

### Understanding Component Nesting in Figma

One of the most powerful aspects of designing with components in Figma is the ability to override *nested components*. (Read more about this technique in our guide, “[How to Use Slots](./how-to-use-slots.md)”).

Combined with Figma’s “swap instance” feature,`⬦Carousel` offers several methods to customize the appearance of key UI elements such as content and controls. Out of the box, the component ships with placeholder elements (eg, “slots”) that can be replaced with your own, unique designs— all without ever detaching the component from our component library.

To begin customizing your instance of `⬦Carousel`, **click the dropdown menu** next to `🄵 controls` and select **“Custom”**.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_10.png)

### Creating Your Own Button Controls

In order to swap the placeholder element with your own custom button — you’ll first have to create a custom button! Your button will then be used as a replacement for the placeholder (shown below).

![Placeholder for the “next” button shown in pink](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_11.png)

*Placeholder for the “next” button shown in pink*

Once you’ve designed the buttons you intend to use in your `⬦Carousel` instance, create a component of each button — one for *“previous”* one for *“next”*. Frame your selection and give it a name (such as “Custom Buttons”, shown below). Make note of where this frame lives in your Figma file in case you want to make adjustments later.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_12.png)

Now, in the instance panel, click the dropdown menu next to `🄵 prev button` or `🄵 next button`. In the search field, type the name of the frame where your custom buttons are located.

Choose the “previous” or “next” button that corresponds to the button you are swapping. Your selection will be applied to the `⬦Carousel`. Repeat the process for the other button and your buttons are now customized.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_13.gif)

![Carousel with custom “next” button applied.](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_14.png)

*Carousel with custom “next” button applied.*

### Using Your Own Content

As we saw earlier, Carousel ships with several common patterns to choose from for `🄵 content type`. However, what if none of these options are well-suited for your design or use-case?

Employing the same approach described above, we can replace the default “content” slots in the Carousel, with our own custom content by swapping instances.

![](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_15.png)

Just as before, you’ll design your own content card in Figma, create a component from it, and place it into a frame. Name the frame something easy to remember such as “Custom Content” (shown below).

![Custom content cards like this one can be swapped into the Carousel.](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_16.png)

*Custom content cards like this one can be swapped into the Carousel.*

Now let’s look at the instance panel once again and click the dropdown next to `🄵 content type`.

This time, rather than selecting from the default options under “Preferred” – we’ll choose “Local components”, find “Custom Content” and select the content card we designed earlier. Your instance of `⬦Carousel` is now populated with your own custom content!

![Choosing your custom content card from the instance panel](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_17.gif)

*Choosing your custom content card from the instance panel*

![Carousel with custom buttons and and custom content applied](https://build.washingtonpost.com/img/resources/tutorials/carousel/figure_18.gif)

*Carousel with custom buttons and and custom content applied*
