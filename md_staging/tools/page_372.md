```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_372.jpeg
document_name: tools
page_number: 372
page_id: tools#page_372
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:46Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the visual style inheritance of child buttons from their parent ButtonEdit control.
- Explains how to focus child buttons at runtime, based on the `ChildButton.TabIndex` and `ChildButton.TabStop` properties.
- Describes displaying or hiding the focus rectangle for a focused button using the `ButtonEdit.KeepFocusRectangle` property.
- Covers replacing the default textbox within the ButtonEdit control with custom textboxes (e.g., PercentTextBox, IntegerTextBox).
- Provides details on properties of the embedded textbox within a ButtonEdit control.

## Content

### Note: Visual Styles of Child Buttons
> Visual style of a child buttons is inherited from the visual style of its parent (ButtonEdit) control. See **Style Settings** topic. You can override those settings using the above properties.

#### Focusing the Child Button at Runtime
The Child buttons can be focused based on the order of the `ChildButton.TabIndex` set for individual buttons. The `ChildButton.TabStop` property should be set to `true` to make this effective. While focusing the button, we can either display or don't display a focus rectangle, by using the `ButtonEdit.KeepFocusRectangle` property.

##### Code Example: Configuring `KeepFocusRectangle`

[C#]
```csharp
this.buttonEditChildButton3.KeepFocusRectangle = true;
```

[VB.NET]
```vb
Me.buttonEditChildButton3.KeepFocusRectangle = True
```

##### Focus Rectangle for Child Button
![Focus Rectangle for Child Button](image.png)
*Figure 181: Focus Rectangle for Child Button*

### See Also
- [How to hide a child button of a ButtonEdit control?](#)
- [3.5.2.2.3.3 TextBox Settings For ButtonEdit](#)

#### TextBox Settings For ButtonEdit
The default textbox within the ButtonEdit control can be replaced with any custom textbox like `PercentTextBox`, `IntegerTextBox`, and so on. The properties of the Embedded textbox of a ButtonEdit control are discussed below.

##### ButtonEdit Properties Table

| **ButtonEdit Properties**      | **Description**                                                                                   |
|---------------------------------|----------------------------------------------------------------------------------------------------|
| **ShowTextBox**                | Indicates whether the embedded TextBox is visible in the ButtonEdit control. This property setting can be reset to default by calling the `ResetShowTextBox` method. |
| **SelectionLength**            | Sets the selection length of the embedded TextBox. This property setting can be reset to default by calling the `ResetSelectionLength` method.                       |

---

## Page-level Navigation/TOC
- [Focusing the Child Button at Runtime](#focusing-the-child-button-at-runtime)
- [See Also](#see-also)
- [TextBox Settings For ButtonEdit](#text-box-settings-for-buttonedit)

## Cross References
- See **Style Settings** topic for more details on overriding visual styles.
- Refer to **How to hide a child button of a ButtonEdit control?** for instructions on hiding child buttons.

<!-- 
tags: [syncfusion, winforms, buttonedit, textbox, focus, visibility, selection] 
keywords: [visualstyle, childbuttons, tabindex, tabstop, keepfocusrectangle, embeddedtextbox, percenttextbox, integertextbox, resettextbox, selectionlength]
-->
```