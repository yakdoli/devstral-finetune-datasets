```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_394.jpeg
document_name: XlsIO
page_number: 394
page_id: XlsIO#page_394
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:59Z
fidelity: lossless
-->

## Reading and Styling Rich Text Comments

### Overview
- Demonstrates how to read rich text comments from a spreadsheet.
- Illustrates the process of filling comments with various types of gradients using the `IFill` interface.

### Content

#### Reading Comments

The following code examples show how to read both plain text and rich text comments from a spreadsheet:

```csharp
// Read Rich Text Comment.
this.richTextBox1.Rtf = sheet.Range["A2"].Comment.RichText.RtfText;
```

```vb.net
' Read plain text comment.
Me.txtPlainTextBox.Text = sheet.Range("A1").Comment.Text

' Read Rich Text Comment.
Me.richTextBox1.Rtf = sheet.Range("A2").Comment.RichText.RtfText
```

**Figure 143: Reading Rich Text Comments**

![Reading Rich Text Comments](https://i.imgur.com/image123.png)

*Figure 143: Reading Rich Text Comments*

#### Styling Comments with Gradients

You can fill the comments with various types of fills by using the `IFill` interface. The following code example illustrates how to fill the comment shape with a TwoColor gradient:

```csharp
shape.Fill.TwoColorGradient();
shape.Fill.GradientStyle = ExcelGradientStyle.Horizontal;
shape.Fill.GradientColorType = ExcelGradientColor.TwoColor;
shape.Fill.ForeColorIndex = ExcelKnownColors.Red;
shape.Fill.BackColorIndex = ExcelKnownColors.White;
```

```vb.net
shape.Fill.TwoColorGradient()
```

### Summary

This section explains how to handle rich text comments and style them with gradients, providing both C# and VB.NET code examples.

## API Reference

### Methods
- `TwoColorGradient()`: Applies a two-color gradient to the shape fill.
- `GradientStyle`: Property to set the gradient style (e.g., horizontal).
- `GradientColorType`: Property to set the type of gradient color (e.g., two-color).
- `ForeColorIndex`: Property to set the foreground color index.
- `BackColorIndex`: Property to set the background color index.

## Code Examples

### C#
```csharp
shape.Fill.TwoColorGradient();
shape.Fill.GradientStyle = ExcelGradientStyle.Horizontal;
shape.Fill.GradientColorType = ExcelGradientColor.TwoColor;
shape.Fill.ForeColorIndex = ExcelKnownColors.Red;
shape.Fill.BackColorIndex = ExcelKnownColors.White;
```

### VB.NET
```vb.net
shape.Fill.TwoColorGradient()
```

## Cross References

See also:
- `ExcelGradientStyle`
- `ExcelGradientColor`
- `ExcelKnownColors`

<!-- tags: [Syncfusion Winforms, XlsIO, Rich Text Comments, Gradients] keywords: [read comment, style gradient, TwoColorGradient, ExcelGradientStyle, ExcelGradientColor, ExcelKnownColors] -->
```