```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_364.jpeg
document_name: tools
page_number: 364
page_id: tools#page_364
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:20Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

| **Property**     | **Description**                                                                 |
|------------------|---------------------------------------------------------------------------------|
| **BorderStyle**  | Specifies the sides of the control which should have border.                   |
| **FlatStyle**    | Specifies the flat style to be applied to the ButtonEdit control.<br>Set `UseVisualStyle` property to `false` to make this setting effective. |
| **FlatBorderColor** | Specifies the border color for the control, when FlatStyle is set to "Flat".<br>This color setting can be reset by calling `ButtonEdit.ResetFlatBorderColor` method.                                          |

### Code Examples

#### C#
```csharp
this.buttonEdit3.UseVisualStyle = false;
this.buttonEdit3.FlatBorderColor = System.Drawing.Color.Red;
this.buttonEdit3.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
```

#### VB.NET
```vb
Me.buttonEdit3.UseVisualStyle = False
this.buttonEdit3.FlatBorderColor = System.Drawing.Color.Red;
this.buttonEdit3.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
```
<!-- tags: [Syncfusion Winforms, ButtonEdit, FlatStyle, FlatBorderColor, UseVisualStyle] keywords: [Essential Tools, Windows Forms, control styles, BorderStyle, FlatStyle] -->
```