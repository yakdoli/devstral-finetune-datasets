```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_368.jpeg
document_name: tools
page_number: 368
page_id: tools#page_368
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Describes how to set the border style for BorderEdit Child buttons.
- Explains the settings applicable for specific Office and Windows styles.
- Highlights the properties available to control the appearance and behavior of ButtonEdit Child buttons.

## Content

### Note: Border Style Settings

This setting is effective only for Office2003, OfficeXP, and WindowsXP styles set through the `ButtonEdit.ButtonStyle` property. See Style Settings. We can also set border style for `ButtonEdit` controls without enabling visual styles.

#### Sample Code in C#

```csharp
// Sample code for setting "Bump" Border Style for BorderEdit Child Button
this.buttonEditChildButton4.BorderStyleAdv =
    Syncfusion.Windows.Forms.ButtonAdvBorderStyle.Bump;
```

#### Sample Code in VB.NET

```vb
' Sample code for setting "Bump" Border Style for BorderEdit Child Button
Me.buttonEditChildButton4.BorderStyleAdv =
    Syncfusion.Windows.Forms.ButtonAdvBorderStyle.Bump
```

#### Figure 177: Border Styles set for Child Buttons

![Figure 177: Border Styles set for Child Buttons](https://user-images.githubusercontent.com/88478798/130848067-3d604c4f-515b-4f56-babc-9a8c7e4127f6.png)

**Figure 177:** Border Styles set for Child Buttons

### See Also

- Style Settings
- How to set tooltip for `ButtonEdit` Child buttons?

#### Properties

The properties which control the appearance and behavior of the `ButtonEdit` Child Buttons are listed below with their description.

##### Button Alignment

Placement of the child buttons inside the `ButtonEdit` control is set through the following property:

| Property        | Description                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------|
| `ButtonAlign`   | Specifies whether the child button should be aligned to the left or right of the `ButtonEdit` control. |

## API Reference

This page provides an overview of the properties and their descriptions related to `ButtonEdit` Child Buttons.

## Code Examples

The section provides examples in both C# and VB.NET to demonstrate how to set the border styles and align the child buttons.

### Related Links

- **Style Settings**
- **How to set tooltip for `ButtonEdit` Child buttons?**

## Page-level Navigation/TOC

- **Note: Border Style Settings**
- **Sample Code in C#**
- **Sample Code in VB.NET**
- **Figure 177**
- **See Also**
- **Properties**
- **Button Alignment**
- **API Reference**
- **Code Examples**
- **Related Links**

<!-- tags: [Syncfusion, Winforms, ButtonEdit, ChildButtons, BorderStyle, ButtonAlign] keywords: [SIF, Winforms, ButtonEdit, ChildButtons, borders, alignment, style] -->
```