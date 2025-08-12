```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_959.jpeg
document_name: tools
page_number: 959
page_id: tools#page_959
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:50Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Form Fields
This section demonstrates how to set various properties of a CheckBoxAdv control using VB.NET.

#### CheckBoxAdv State Properties Example
The following VB.NET code snippet demonstrates setting different states and property values for a CheckBoxAdv control:

```vb
[VB.NET]

Me.checkBoxAdv1.CheckedInt = 3
Me.checkBoxAdv1.CheckedString = "CheckBoxAdv is Checked"
Me.checkBoxAdv1.IndeterminateInt = 5
Me.checkBoxAdv1.IndeterminateString = "CheckBoxAdv is Indeterminate"
Me.checkBoxAdv1.UncheckedInt = 3
Me.checkBoxAdv1.UncheckedString = "CheckBoxAdv is Unchecked"
Me.checkBoxAdv1.StringValue = "String"
Me.checkBoxAdv1.IntValue = 5
Me.checkBoxAdv1.BoolValue = True
```

### Text Settings for CheckBoxAdv

#### Overview
This section discusses the text settings of the CheckBoxAdv control, including shadowing and wrapping.

#### Text Shadowing and Wrapping
Text in the CheckBoxAdv can be styled with shadows and wrapping as illustrated below:

| CheckBoxAdv Properties | Description |
|------------------------|-------------|
| TextShadow            | Determines if the text shadow is visible. |
| ShadowColor           | The color of the text shadow.          |
| ShadowOffset          | The offset of the text shadow.         |
| WrapText              | Determines if the text in the CheckBoxAdv is wrapped. |

#### Code Examples

##### C# Implementation
The following C# code snippet demonstrates how to set text shadow and wrapping properties for a CheckBoxAdv control:

```csharp
this.checkBoxAdv1.TextShadow = true;
this.checkBoxAdv1.ShadowColor = System.Drawing.Color.BurlyWood;
this.checkBoxAdv1.ShadowOffset = new System.Drawing.Point(8, 8);
this.checkBoxAdv1.WrapText = true;
```

##### VB.NET Implementation
The following VB.NET code snippet demonstrates setting the `TextShadow` property for a CheckBoxAdv control:

```vb
[VB.NET]

Me.checkBoxAdv1.TextShadow = True
```

### See Also
- **CheckBoxAdv States, Image Settings**
- **3.5.11.1.3.2 Text Settings**

This section covers the text settings of the CheckBoxAdv, including shadowing and text wrapping, allowing for enhanced visual customization.

---

<!-- tags: [Syncfusion, Windows Forms, CheckBoxAdv, Text Settings, Shadowing, Wrapping] keywords: [CheckBoxAdv, text shadow, shadow color, shadow offset, text wrapping, visual customization, WinForms] -->
```