```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_814.jpeg
document_name: tools
page_number: 814
page_id: tools#page_814
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## E.1 API Reference

### Properties

| Property       | Description |
|----------------|-------------|
| **`BorderStyle`** | RaisedInner<br>Sunken (default)<br>SunkenOuter<br>SunkenInner<br>Etched<br>Bump<br>Adjust and<br>Flat. |
| **`BorderSides`** | Specifies the border sides. The options include<br>Left,<br>Top,<br>Right,<br>Bottom,<br>Middle and<br>All (default). |
| **`BorderColor`** | Specifies the color of the border when<br>BorderStyle is FixedSingle. |

## Code Examples

### C#

```csharp
this.currencyTextBox1.BorderStyle =
    System.Windows.Forms.FormBorderStyle.FixedSingle;
this.currencyTextBox1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.Flat;
this.currencyTextBox1.BorderColor =
    System.Drawing.Color.Magenta;
this.currencyTextBox1.BorderSides =
    System.Windows.Forms.Border3DSide.All;
```

### VB.NET

```vb
Me.currencyTextBox1.BorderStyle =
    System.Windows.Forms.FormBorderStyle.FixedSingle
Me.currencyTextBox1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.Flat
Me.currencyTextBox1.BorderColor =
    System.Drawing.Color.Magenta
```

## Page-level Navigation/TOC

This page provides detailed information about the styling and customization options for Windows Forms controls, specifically focusing on border styles and their properties. Code examples in both C# and VB.NET are included to demonstrate how to set these properties.

### Cross References

See also: [Other relevant sections or documents in the WinForms User Guide regarding control customization and design-time features.]

<!-- tags: [Microsoft.Windows.Forms, Border Styles, Control Customization, C#, VB.NET, Windows Forms] keywords: [BorderStyle, Border3DStyle, BorderColor, BorderSides, RaisedInner, Sunken, Flat, Single, Fixed, Multi-Language Support] -->
```