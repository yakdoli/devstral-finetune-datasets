```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: diagram
page_number: 068
page_id: diagram#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:05Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### NudgeRight

| Property Name | Description |
| --- | --- |
| `NudgeRight` | Nudge the selected components to the right by `Syncfusion.Windows.Forms.Diagram.Controls.Diagram.NudgeIncrement` units. |

```csharp
diagram1.NudgeRight();
```

### Text Formatting Tool

The following screen shot illustrates the Text Formatting tools.

**Figure 40: Text Formatting Tools**

| Tool Name | Description | Code Snippet |
| --- | --- | --- |
| **Font Family** | The `FamilyName` property is used to get or set the font family name. | ```csharp string strFamilyName = this.comboBoxBarItemFamilyName.ListBox.SelectedItem.ToString(); if (this.diagram1.Controller.TextEditor.FamilyName != strFamilyName) this.diagram1.Controller.TextEdit or.FamilyName = strFamilyName; ``` |
| **Font Size** | Gets or sets the size of the point. | ```csharp int ptSize = 10; this.diagram1.Controller.TextEdit or.PointSize = ptSize; ``` |
| **Bold** | Gets or sets a value indicating whether the **Syncfusion.Windows.Forms.Diagram.TextEditor** is bold. | ```csharp bool newValue = !(this.diagram1.Controller.TextEdit or.Bold); this.diagram1.Controller.TextEdit or.Bold = newValue; ``` |
| **Italic** | Gets or sets a value indicating whether the **Syncfusion.Windows.Forms.Diagram.TextEditor** is italic. | ```csharp bool newValue = !(this.diagram1.Controller.TextEdit or.Italic); this.diagram1.Controller.TextEdit or.Italic = newValue; ``` |
| **Underline** | Gets or sets a value indicating whether the **Syncfusion.Windows.Forms.Diagram.TextEditor** is underline. | ```csharp bool newValue = !(this.diagram1.Controller.TextEdit or.Underline); this.diagram1.Controller.TextEdit or.Underline = newValue; ``` |
| **StrikeOut** | Gets or sets a value indicating whether the **Syncfusion.Windows.Forms.Diagram.TextEditor** is strikeout. | ```csharp bool newValue = !(this.diagram1.Controller.TextEdit or.StrikeOut); ``` |

## Footer

© 2013 Syncfusion. All rights reserved. Page 68

<!-- tags: [Syncfusion WinForms, Diagram Control, Text Formatting Tools, Font Family, Font Size, Bold, Italic, Underline, StrikeOut] keywords: [nakฏทNormalization, C#", namespace, class, types, design-time, runtime, WinForms, application-specific UI elements, diagram control, text formatting, bold, italic, underline, strikeout] -->
```