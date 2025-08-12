```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_957.jpeg
document_name: tools
page_number: 957
page_id: tools#page_957
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section describes the properties and their usage in the context of CheckBox controls in Syncfusion Winforms.
- Covers the different states (Unchecked, Checked, and Indeterminate) of a CheckBox control.
- Provides examples for setting and getting the Checked state of a CheckBox in C# and VB.NET.

## Content

### Properties of CheckBox Control

| Property Name | Description |
|----------------|-------------|
| CheckState | Unchecked, <br> Checked and <br> Indeterminate. |
| Checked | Gets / sets the checked state of the CheckBox. |

#### Example Code: Setting Checked State

##### C#
```csharp
this.checkBoxAdv1.CheckState = System.Windows.Forms.CheckState.Checked;
this.checkBoxAdv1.Checked = true;
```

##### VB.NET
```vb
Me.checkBoxAdv1.CheckState = System.Windows.Forms.CheckState.Checked
Me.checkBoxAdv1.Checked = True
```

#### Figure: CheckBox States

![Figure 615: CheckBoxAdv States](#)

**Figure 615: CheckBoxAdv States**

#### Figure: Checked Property Displaying States

![Figure 616: "Checked" property displaying the Checked States](#)

**Figure 616: "Checked" property displaying the Checked States**

## See Also
- [CheckBoxAdv Control Overview](#)
- [Properties of CheckBoxAdv](#)
- [Events of CheckBoxAdv](#)

## Page-level Navigation/TOC (if applicable)
- References to other parts of the document can be added here if needed.

<!-- tags: [WinForms, CheckBox, Checked, Indeterminate, Unchecked, C#, VB.NET, CheckState] keywords: [CheckBox, Checked, Indeterminate, Unchecked, CheckState, states, C#, VB.NET, example] -->
```