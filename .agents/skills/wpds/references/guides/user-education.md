---
title: "User Education Guide"
description: "This guide is an introduction to our user education framework. By the end of this document, you will have learned the following - Evaluate user education needs based on detail, engagement, and communication type. Apply best practices to select the right components and design effective user education experiences."
sourceUrl: "https://build.washingtonpost.com/resources/guides/user-education"
---

# User Education Guide

---

## The Framework

Our framework is grounded in the principle of thoughtful disruption—balancing the need to inform users versus their primary goal for coming to the Washington Post: Reading and engaging with our content.

- Consider these assumptions when using the user education framework:
- Users only internalize a small part of user education.
- Users are scanning, not reading.
- Users are also likely to dismiss a message before reading.
- Clarity begins on the feature level. User education is additive, but can't do all the work.
- The best messaging experiences are valuable, only when needed, and not overlapping. Be mindful of the greater messaging ecosystem. Are there several messages at this moment? Will if feel spammy?

### Using the framework

1. **Identify the Use Case**
  - Assess the detail required
  - Assess the level engagement level
  - Determine what type of communication
2. **Design and Implement**
  - Select the appropriate component: Use our matrix of components to help determine the correct pattern of user education for your specific use case.
  - Ensure consistency in design and messaging with other experiences.
  - Test the implementation to ensure clarity and effectiveness.

<!-- Box: interactive component, rendered on the official site only -->

High Detail

Low Detail

Passive Engagement

High Engagement

High Detail & Passive Engagmenet

Appropriate for information-dense content that doesn't demand immediate user action, but requires careful consideration (e.g., in-depth tooltips, instructional guides)

High Detail & Active Engagement

Best suited for content that requires active user interaction, and involves complex information (e.g., detailed onboarding flows, multi-step product tours).

Low Detail & Passive Engagmenet

Fits content that is simple and primarily informational without requiring much interaction (e.g., notifications, passive alerts).

Low Detail & Active Engagmenet

Ideal for interactive content that is easy to grasp, but still requires user participation (e.g., quick walkthroughs, feature discovery nudges).

---

## Assess the Level of Detail

The level of detail is determined by several factors, primarily based on the complexity of the information, the user's experience level, and how critical the information is to avoid frustration. Consider the following:

1. **Complexity of Information**
  - High Detail: Necessary for complex information involving multiple steps or requiring thorough understanding (e.g., detailed instructions, complex workflows).
  - Low Detail: Suitable for straightforward or simple information, like quick reminders (e.g., single-step instructions, brief notifications).
2. **User Experience Level**
  - High Detail: Required for users new to the application or feature who need comprehensive guidance.
  - Low Detail: Appropriate for experienced users who only need brief reminders or notifications.
3. **Criticality of Information**
  - High Detail: Essential if missing the information could lead to significant issues, errors, or user frustration.
  - Low Detail: Adequate when the information is helpful but not critical to the user's success or safety.

![](https://build.washingtonpost.com/img/resources/guides/user_education_detail.png)

---

## Assess the Level of Engagement

When designing user education content, consider the level of engagement needed based on user interaction requirements, learning goals, and the urgency of the communication. Here's how to approach it:

1. **User Interaction Requirement**
  - Active Engagement: Required if the communication encourages users to perform actions, make decisions, or interact with features (e.g., product tours, walkthroughs).
  - Passive Engagement: Suitable for informational content that doesn't require user action beyond reading or acknowledging (e.g., tooltips, system messages).
2. **Learning and Adoption Goals**
  - Active Engagement: Necessary when the objective is for users to learn and adopt new features or changes through hands-on interaction.
  - Passive Engagement: Appropriate if the goal is to inform users without requiring immediate engagement with the content.
3. **Frequency and Urgency**
  - Active Engagement: Ideal for messages that are urgent or infrequent and need immediate attention (e.g., critical alerts, onboarding).
  - Passive Engagement: Suitable for regular communications that serve as ongoing support or reminders.

![](https://build.washingtonpost.com/img/resources/guides/user_education_engagement.png)

---

## Determine the type of communication

It's crucial to identify the type of communication you need because it will guide decisions around language, messaging, UX, and more. We've categorized our user education into the following three buckets:

- **First Time User Experience**
- **Support**
- **Growth**

---

### First-Time User Experience (FTUX)

FTUX refers to a user's initial interaction with a product or feature. The experience should provide a smooth, engaging and informative introduction to the benefits and features. User education is often useful to show the value prop of our ever-evolving product offerings.

**Common FTUX experiences include:**

- Onboarding
- Product Tours
- New Feature Announcements
- Feature Walkthroughs

![](https://build.washingtonpost.com/img/resources/guides/user_education_ftux.png)

#### Considerations

**UX writing & content design**

- To create the most impactful experience, keep it as simple as possible, or consider if it's needed at all. If the goal is to teach a feature or interaction, make sure you're not leaning on the user education to fix unclear design.
- Many people close tutorials or similar without using them. The lengthier the tutorial, the more drop-off.
- If your user education has multiple steps, place them in order of importance to goals.
- Consider visuals or animation to improve comprehension and engagement.

---

### Support

Support provides users with contextual information and guidance, making it easier for them to understand and effectively use the product's features.

**Common support experiences include:**

- Added context (information tooltips)
- System communication (e.g. server timeout and errors, form errors, successful interactions)
- Account messaging (e.g. status of payment, changes to policies, and terms)

![](https://build.washingtonpost.com/img/resources/guides/user_education_support.png)

#### Considerations

**UX writing & content design**

- When providing system-level information (error, confirmation, info messages, etc.), be clear, concise and helpful.
- If it's an error, tell users what happened, why it happened, how to fix it and the next best option.
- Use information tooltips to add non-critical context that helps users or builds trust. For example, “Why is this AI feature here?”

**Semantic Color**

- Use our semantic colors for error, success, signal, and warning messages. These colors reinforce visual cues and help users quickly understand the context of the communication.

---

### Growth

Growth helps to expand a product's user base by encouraging user engagement, sharing, and retention through targeted messages and incentives.

**Common growth experiences include:**

- Upsell Visuals & Interactions
- Account/Subscription Upgrades
- Feature Adoption Campaigns

![](https://build.washingtonpost.com/img/resources/guides/user_education_growth.png)

#### Considerations

**UX writing & content design**

- User education can be useful to show our ever-evolving offering of features. Be thoughtful if the feature is actually cool and new in the user's mind. Consider if the user education will feel helpful or spammy.
- Make value proposition very clear.
- Understand this is an exchange. In exchange for my time, privacy or money, I will receive **___**.
- Keep it short.
- Keep it simple. In general, only ask the user to make one choice at a time.
- Have the button/CTA be the appropriate level of commitment for the step. For example, “See subscription options” might come before “Continue to payment.” [Example: See Google hotel booking case study](https://www.directyourbookings.com/blog/marketing/convert-better-with-ux-writing-hotel-case-study-by-google/)
- The text underneath a button is called “trigger text”. It's often used to help someone make a decision, for example “Cancel anytime.”

**Subscription Color**

- Use our designated subscription color whenever the communication specifically addresses subscription-related topics. This ensures visual consistency and reinforces the importance of subscription messaging.

---

## Selecting the Appropriate Component

We've aligned key components with their inherent interaction patterns within our framework for thoughtful disruption in user education. Each component offers different levels of support for handling complex details. Be sure to consult the component documentation for specific best practices.

![](https://build.washingtonpost.com/img/resources/guides/user_education_matrix.png)
