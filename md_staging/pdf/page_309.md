```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_309.jpeg
document_name: pdf
page_number: 309
page_id: pdf#page_309
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:45Z
fidelity: lossless
-->

## Textbox Field Properties

### Overview

- This section describes the various properties and their functions related to a `TextBoxField` in a PDF document.
- Includes details on controlling the appearance and behavior of the text field, such as background and border colors, styles, alignment, and highlighting.

### Content

#### TextBoxField Properties Table

| **TextBoxField Property** | **Description**                                                                                                           |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| BackColor                 | Gets or sets the back color of the field.                                                                                |
| BorderColor               | Gets or sets the border color for the field.                                                                             |
| BorderStyle               | Gets or sets the border style for the field.                                                                             |
| Border                    | Gets or sets the width of the field border.                                                                              |
| ForeColor                 | Gets or sets the fore color for the field.                                                                              |
| HighlightMode             | Gets or sets the highlight mode of the field. It includes the following options:<br><ul><li>Invert</li><li>Outline</li><li>Push</li><li>NoHighlighting</li></ul> |
| TextAlignment             | Gets or sets the alignment of the text in the field. It includes the following options:<br><ul><li>Center</li><li>Left</li><li>Right</li><li"Justify"</li></ul> |

#### Code Example

[C#]

```csharp
PdfLoadedTextBoxField txt = frm.Fields[i] as PdfLoadedTextBoxField;
txt.BorderColor = Color.SteelBlue;
txt.BorderStyle = PdfBorderStyle.Solid;
txt.BorderWidth = 1;
txt.BackColor = new PdfColor(Color.AliceBlue);
txt.ForeColor = new PdfColor(Color.Navy);
txt.HighlightMode = PdfHighlightMode.Invert;
txt.TextAlignment = PdfTextAlignment.Right;
Font f = new Font("Arial", 18f);
PdfTrueTypeFont txtfnt = new PdfTrueTypeFont(f, false);
```

### API Reference

#### Properties
- **BackColor**: Gets or sets the back color of the field.
- **BorderColor**: Gets or sets the border color for the field.
- **BorderStyle**: Gets or sets the border style for the field.
- **Border**: Gets or sets the width of the field border.
- **ForeColor**: Gets or sets the fore color for the field.
- **HighlightMode**: Gets or sets the highlight mode of the field with options: `Invert`, `Outline`, `Push`, `NoHighlighting`.
- **TextAlignment**: Gets or sets the alignment of the text in the field with options: `Center`, `Left`, `Right`, `Justify`.

### Code Examples (C#)

Complete example demonstrating the use of `TextBoxField` properties:

```csharp
// Example: Configuring a TextBoxField
PdfLoadedTextBoxField txt = frm.Fields[i] as PdfLoadedTextBoxField;
txt.BorderColor = Color.SteelBlue;
txt.BorderStyle = PdfBorderStyle.Solid;
txt.BorderWidth = 1;
txt.BackColor = new PdfColor(Color.AliceBlue);
txt.ForeColor = new PdfColor(Color.Navy);
txt.HighlightMode = PdfHighlightMode.Invert;
txt.TextAlignment = PdfTextAlignment.Right;
Font f = new Font("Arial", 18f);
PdfTrueTypeFont txtfnt = new PdfTrueTypeFont(f, false);
```

### Cross References

- Refer to the `PdfLoadedTextBoxField` documentation for more advanced functionalities and properties relevant to the `TextBoxField`.

<!-- tags: [syncfusion, pdf, textboxfield, properties, highlightmode, textalignment] keywords: [syncfusion sdk, pdf loaded textboxfield, field properties, backcolor, bordercolor, borderstyle, borderwidth, forecolor, invert, outline, push, nohighlighting, center, left, right, justify, code example] -->
```