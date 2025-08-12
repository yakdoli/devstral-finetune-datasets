```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_577.jpeg
document_name: tools
page_number: 577
page_id: tools#page_577
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:51Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

|            | The options are,                                                                 |
|------------|---------------------------------------------------------------------------------|
|            | Left,                                                                           |
|            | Top,                                                                            |
|            | Right,                                                                          |
|            | Bottom,                                                                         |
|            | Middle and                                                                      |
|            | All. (Default)                                                                 |

| FlatStyle   | Specifies the Flat Style. The options are                                   |
|-------------|---------------------------------------------------------------------------------|
|             | Flat,                                                                           |
|             | Standard (Default) and                                                         |
|             | System.                                                                        |

| FlatBorderColor | Specifies the color with which flat border should                    |
|-----------------|---------------------------------------------------------------------------------|
|                 | be drawn. `FlatStyle` must be set to 'Flat' to get the color effect. |

## Code Examples

### C#

```csharp
this.comboBoxAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.Flat;
this.comboBoxAdv1.BorderSides = System.Windows.Forms.Border3DSide.All;
this.comboBoxAdv1.FlatStyle = Syncfusion.Windows.Forms.Tools.ComboFlatStyle.Flat;
this.comboBoxAdv1.FlatBorderColor = System.Drawing.Color.Blue;
```

### VB.NET

```vb
Me.comboBoxAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.Flat
Me.comboBoxAdv1.BorderSides = System.Windows.Forms.Border3DSide.All
Me.comboBoxAdv1.FlatStyle = Syncfusion.Windows.Forms.Tools.ComboFlatStyle.Flat
Me.comboBoxAdv1.FlatBorderColor = System.Drawing.Color.Blue
```

<!-- tags: [Syncfusion, Winforms, Border3DStyle, BorderSides, FlatStyle, FlatBorderColor] keywords: [WinForms, Border styles, Flat Style, Border color customization, .NET, C#, VB.NET, Syncfusion Advanced ComboBox] -->
```