---
title: "Accessibility Checklist"
description: "Overview of considerations, not comprehensive"
sourceUrl: "https://build.washingtonpost.com/resources/accessibility/accessibility-checklist"
---

# Accessibility Checklist

---

The following checklist is derived from the much more detailed [WCAG guidelines](https://www.w3.org/WAI/WCAG21/quickref/). This does not cover every possible accessibility issue but aims to cover the most prominent varieties. It’s meant to be an entry-level guide. For help with any part of the guide, or to request an addition to any of our docs, contact [accessibility@washpost.com](mailto:accessibility@washpost.com). We can also share copies of this checklist as .md files upon request.

**Important: Repeat all steps below on all screen sizes (mobile, tablet, desktop) to better evaluate accessibility across devices.**

**Many of the checklist items link out to more detailed instructions from [our accessibility docs](../accessibility.md) on how to test.**

We provide a [5-minute video tutorial](../tutorials/five-minute-accessibility-audit.md) going through a portion of the checklist.

Thanks for incorporating accessibility considerations into your work!

## 1. Screen reader & keyboard controls

It might seem complicated, but this testing often takes only a minute or two! Use the links below and reach out with any questions.

- **Navigate content with keyboard only**
 Press the `tab` key ([setup needed if using Firefox and Safari](./keyboard-accessibility.md#Setup)) and `shift` + `tab` to cycle forward and backward through the buttons, links, hoverable elements and any others the user should be able to interact with, ensuring (a) they each receive [appropriate focus styles](./keyboard-accessibility.md#Focus%20rings) and (b) they are clickable with the enter key (links and buttons) and/or space key (buttons). Each time you press `tab`, you should see something change on the page. If not, there is a missing focus style or tab index issue. See the [full list of keyboard controls](./keyboard-accessibility.md#How%20to%20navigate%20with%20a%20keyboard%20only) for details on other behavior, like what arrow keys and escape should do.
- **Test with screen reader linearly**
 Using a screen reader ([guidance on using screen readers](./screen-readers.md)), navigate the page from top to bottom. You can click with your mouse to position the screen reader, which is helpful for testing specific parts of a page. Ensure all visible text is read aloud with correct pronunciation and in a sensible order.
- **Test with screen reader rotor**
 Open [the screen reader rotor](./screen-readers.md#Using%20the%20VoiceOver%20rotor) (`caps lock` + `U` with VoiceOver) and ensure all links, buttons and other elements have appropriate names. Interactive elements [should not have generic names like "click here."](./semantic-html.md#Hyperlink%20text%20guidelines) You should be able to understand what each link or button does from the rotor menu without other context from the page.
- **Confirm heading order is correct**
 Check the page headers using a screen reader. Does the heading order make sense? There should be only one `h1`, the page title. From there, headings should be [ordered strictly by page hierarchy](./semantic-html.md#Heading%20order%20and%20page%20landmarks) (don't jump from `h2` to `h4`, don't use `h2` as a subhead of an `h3`, etc.).
- **Confirm page landmarks are present and have correct content**
 Are the [base page landmarks](./semantic-html.md#Page%20landmarks) (`main`, `nav`, `header`, `footer`) present? If there is complementary page content like a sidebar or right rail, is it in an `aside` tag? Are the landmarks accessible with a screen reader? They should contain the right content to help screen readers scan the page quickly.

---

## 2. Multimedia

- **Ensure all images have alt text**
 Follow the [guidance for writing alt text](./alt-text.md). If an image is purely decorative, make sure it still has `alt` or `alt=""` present in the HTML. Similarly, videos and gifs should have text descriptions for screen reader users.
- **Test with reduced motion settings turned on**
 Turn on [reduced motion](./audio-and-video.md#Animations%20and%20reduced%20motion), and ensure all non-essential animation and other moving content is eliminated upon page refresh. If not, then you should use [the prefers-reduced-motion media query](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) to modify behavior accordingly.
- **Hide useless content from screen readers**
 Just as you would put alt="" for purely decorative images to hide them from screen readers, you should add [aria-hidden="true"](./semantic-html.md#Hiding%20content%20from%20screen%20readers) for content on the page that is not screen reader friendly. An example might be an election map full of svgs and labels, etc. You can include [a table version](./semantic-html.md#Tables) of the data or some other alternative for accessibility, and then hide the map with aria-hidden.
- **Avoid auto-playing audio and video**
 Never auto-play audio. Auto-playing video, animations and other graphics (including gifs) are strongly discouraged. Ensure all audio and video instances have an accessible [pause, stop or hide button](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html).
- **Eliminate rapidly flashing content**
 Videos, gifs and animations must not include any instances of flashing or blinking more than 3 times within any one second, as this is a seizure risk.
- **Provide captions and transcripts**
 Anywhere there is audio, there should be a [transcript](./audio-and-video.md#Transcripts%20guidance) provided. Videos with audio should include [captions](./audio-and-video.md#Captions) in addition to transcripts. Both should include words spoken AND any other meaningful sounds from the audio (such as a sigh or laugh in conversation, or the chopping of a knife in cooking) as well.

---

## 3. Text, labels & zoom settings

- **Ensure text is readable and in plain language**
 Text should be [no smaller than 12px](./text-size-and-zoom.md#Text%20size) and written in [plain language](./plain-language-and-labeling.md) wherever possible. Is there any jargon or use of idioms? These should be avoided.
- **Ensure text decoration is not needed to understand meaning**
 Do you use underlined text (<u>example</u>) or struck-through text (example)? Text decorations like these are often not recognized by screen readers and are often confusing to other users, too, so they are generally not recommended. If you do use text decoration to convey meaning, then you must also provide [other ways for users to understand the meaning of decorated text](./plain-language-and-labeling.md#Text%20decoration).
- **Ensure non-English content is labeled as such**
 Content in non-English languages, such as Arabic or Spanish, must have the lang="CODE" attribute set, where CODE is the language code e.g. “ar” for Arabic or “es” for Spanish. There’s a [list of language codes](https://www.w3schools.com/tags/ref_language_codes.asp). This is essential [for non-English text to be read correctly by screen readers](./semantic-html.md#Non-English%20language%20support). Additionally, Arabic and some other languages are read right-to-left. In those cases, we need to set an additional attribute in the HTML, `dir="rtl`.
- **Clearly label interactive content**
 Meaning of icons, buttons and other elements should be [explicitly conveyed via text](./plain-language-and-labeling.md#Icons,%20emojis%20and%20ASCII%20art) whenever possible. In all cases, interactive elements should have appropriate [aria-labels](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label). See our [guidance on labeling for screen reader users](./semantic-html.md#Labeling%20interactive%20elements). Avoid user prompts or notices that disappear automatically. If the content includes a form, make sure that clear prompts and error messages are provided. See our [guidance on forms](./plain-language-and-labeling.md#Forms%20and%20user%20input).
- **Change page zoom level and browser zoom settings**
 Set [page zoom](./text-size-and-zoom.md#Page%20zoom) to 200% (on a Mac, press `command +` to zoom in). Does text scale correctly? Is it still readable (no overflow, overlap, etc.)? Then, Restore the page zoom to 100% and [increase the font size in your browser settings](./text-size-and-zoom.md#Scaling) to 200%. Does text scale correctly? Is it still readable?

---

## 4. Color

- **Confirm white text is never on a pure black background**
 White text on a pure black background causes a [fuzziness known as halation](https://medium.com/@h_locke/why-dark-mode-causes-more-accessibility-issues-than-it-solves-d2f8359bb46a) for many users with astigmatism. See [our guidance for avoiding halation](./color.md#Avoid%20white%20text%20on%20black%20backgrounds).
- **Confirm black text is never on a pure white background**
 Black text on a pure white background causes [eye strain among many users](https://uxmovement.com/content/why-you-should-never-use-pure-black-for-text-or-backgrounds/). See [our guidance for avoiding eye strain](./color.md#Avoid%20black%20text%20on%20white%20backgrounds).
- **Ensure color contrast meets the WCAG AA standard**
 All color combinations, especially for text and interactive elements, must meet at least the AA (preferably AAA) [color contrast](./color.md) standard [using the WebAIM tool](https://webaim.org/resources/contrastchecker/).
- **Check contrast for common forms of colorblindness**
 Ensure color combinations meet the AA color contrast standard for [colorblind users](./color.md#David%20Nichols'%20coloring%20for%20colorblindness%20tool) among at least the three most common forms of colorblindness.
- **View the page in dark and light mode**
 [Dark mode and light mode](./color.md#Dark%20mode%20vs.%20light%20mode%20settings) should both be supported. Does the page change to light or dark mode automatically per browser settings? Does the page pass color contrast thresholds in both modes? And does everything change color correctly upon toggling to light or dark? Are all links, buttons, fonts, etc. on the page still visible?

---

## 5. Automated testing (will not catch most issues)

If you are a developer, read [our documentation on automated testing](./automated-testing.md) for info about adding automated checks to your code.

- **Run the WAVE tests**
 Install the [WAVE Chrome extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh?hl=en-US) and then use it on the page ([guide to using WAVE](./automated-testing.md#WAVE%20Evaluation%20Tool%20(Google%20Chrome%20extension))). The tool is great for beginners, as it allows you to learn about different types of issues by clicking interactive labels that appear on the page. Fix any issues that are flagged.
- **Run the axe DevTools tests**
 Install the [axe DevTools Chrome Extension](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd?hl=en-US) and then use it on the page ([guide to using axe DevTools](./automated-testing.md#axe%20DevTools%20(Google%20Chrome%20extension))). Fix any issues that are flagged.
