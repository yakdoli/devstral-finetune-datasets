```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_632.jpeg
document_name: tools
page_number: 632
page_id: tools#page_632
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the event handling mechanism for `PopupControlContainer` in Windows Forms.
- Focuses on discussing commonly used events before and after the `Popup` is shown.

## Content

### WinForms-specific conventions

#### Event Handling
**PopupControlContainer handles events before and after the Popup is shown. The most commonly used events are discussed below.**

| Event       | Description                                                                                                                                                |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Popup**   | It occurs after the Popup has been dropped down and made visible. The event handler receives an argument of type EventArgs. <br><br> This event can be handled to get focus on the PopupControlContainer. |
| **BeforePopup** | It occurs when the Popup is about to be shown. The event handler receives an argument of type CancelEventArgs. The event property associated with the CancelEventArgs is as follows. <br><br> **Cancel - Gets/Sets a value indicating whether the event should be canceled.** <br><br> This event can be handled to resize the PopupControlContainer. |
| **CloseUp** | It occurs when a Popup is closed. The event handler receives an argument of type PopupClosedEventArgs. The event property associated with the PopupClosedEventArgs is as follows. <br><br> **PopupCloseType - Returns the** |

---

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: PopupControlContainer
- **Events**:
  - Popup
  - BeforePopup
  - CloseUp

## Code Examples (multi-language supported)
```csharp
// Example handling the Popup event
private void PopupControlContainer_Popup(object sender, EventArgs e)
{
    // Code to handle the event when the Popup is shown
}

// Example handling the BeforePopup event
private void PopupControlContainer_BeforePopup(object sender, CancelEventArgs e)
{
    e.Cancel = true; // Example of canceling the Popup event
}

// Example handling the CloseUp event
private void PopupControlContainer_CloseUp(object sender, PopupClosedEventArgs e)
{
    // Code to handle the event when the Popup is closed
}
```

## Page-level Navigation/TOC (if applicable)
- **3.5.6.1.4 Event Handling**
  - Overview of event handling for `PopupControlContainer`.
  - Detailed description of events: `Popup`, `BeforePopup`, and `CloseUp`.

## Cross References
- **See also**: Related documentation or topics in the same user guide, such as:
  - ControlContainers
  - Event Handling in Syncfusion WinForms
  - Understanding the Popup feature

<!-- tags: [PopupControlContainer, EventHandling, WinForms, Syncfusion, tools] keywords: [Popup, BeforePopup, CloseUp, EventArgs, CancelEventArgs, PopupClosedEventArgs] -->
```