```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_984.jpeg
document_name: tools
page_number: 984
page_id: tools#page_984
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:22Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Demonstrates how to customize the text settings of the `RadioButtonAdv` control, including shadowing and wrapping text.
- Lists properties such as `TextShadow`, `ShadowColor`, `ShadowOffset`, and `WrapText` used for text customization.

### Content

#### Text Settings
This section focuses on the text settings of the `RadioButtonAdv` control.

**Text Customization in `RadioButtonAdv`:**
Text in the `RadioButtonAdv` can be shadowed and wrapped as illustrated below.

| `RadioButtonAdv` Properties      | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `TextShadow`                     | Determines if the text shadow is visible.                                 |
| `ShadowColor`                    | Specifies the color of the text shadow.                                   |
| `ShadowOffset`                   | Specifies the offset of the text shadow.                                  |
| `WrapText`                       | Determines if the text in the `CheckBoxAdv` is wrapped.                   |

**Example Code in C#**
```csharp
this.radioButtonAdv1.TextShadow = true;
this.radioButtonAdv1.ShadowColor = System.Drawing.Color.Gold;
this.radioButtonAdv1.ShadowOffset = new System.Drawing.Point(8, 8);
```

**Example Code in VB.NET**
```vb
Me.radioButtonAdv1.TextShadow = True
Me.radioButtonAdv1.ShadowColor = System.Drawing.Color.Gold
Me.radioButtonAdv1.ShadowOffset = New System.Drawing.Point(8, 8)
```

### See Also
- [RadioButtonAdv States, Image Settings](RadioButtonAdv States, Image Settings)

<!-- tags: [syncfusion, winforms, radiobuttonadv, text settings, shadowing, wrapping, csharp, vb.net] keywords: [TextShadow, ShadowColor, ShadowOffset, WrapText] -->
```