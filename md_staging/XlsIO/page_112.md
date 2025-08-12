```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_112.jpeg
document_name: XlsIO
page_number: 112
page_id: XlsIO#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:10Z
fidelity: lossless
-->

# XlsIO

## Overview
- Demonstrates setting various font properties using the `XlsIO` library.
- Includes font attributes such as font type, style, size, effects, underline types, and color.
- Examples are provided in both C# and VB.NET.

## Content

### Font Configuration

#### C#

```csharp
sheet.Range["A2"].CellStyle.Font.FontName = "Arial Black";
sheet.Range["A4"].CellStyle.Font.FontName = "Castellar";

// Setting Font Styles.
sheet.Range["A6"].CellStyle.Font.Bold = true;
sheet.Range["A8"].CellStyle.Font.Italic = true;

// Setting Font Size.
sheet.Range["A10"].CellStyle.Font.Size = 18;

// Setting Font Effects.
sheet.Range["A12"].CellStyle.Font.Strikethrough = true;
sheet.Range["B10"].CellStyle.Font.Subscript = true;
sheet.Range["B12"].CellStyle.Font.Superscript = true;

// Setting UnderLine Types.
sheet.Range["B2"].CellStyle.Font.Underline = ExcelUnderline.Double;
sheet.Range["B4"].CellStyle.Font.Underline = ExcelUnderline.DoubleAccounting;
sheet.Range["B6"].CellStyle.Font.Underline = ExcelUnderline.Single;
sheet.Range["B8"].CellStyle.Font.Underline = ExcelUnderline.SingleAccounting;

// Setting Font Color.
sheet.Range["C2"].CellStyle.Font.Color = ExcelKnownColors.Lavender;
sheet.Range["C4"].CellStyle.Font.Color = ExcelKnownColors.Light_blue;
sheet.Range["C6"].CellStyle.Font.Color = ExcelKnownColors.Indigo;
```

#### VB.NET

```vb
' Setting Font Type.
sheet.Range("A2").CellStyle.Font.FontName = "Arial Black"
sheet.Range("A4").CellStyle.Font.FontName = "Castellar"

' Setting Font Styles.
sheet.Range("A6").CellStyle.Font.Bold = True
sheet.Range("A8").CellStyle.Font.Italic = True

' Setting Font Size.
sheet.Range("A10").CellStyle.Font.Size = 18

' Setting Font Effects.
sheet.Range("A12").CellStyle.Font.Strikethrough = True
sheet.Range("B10").CellStyle.Font.Subscript = True
sheet.Range("B12").CellStyle.Font.Superscript = True

' Setting UnderLine Types.
sheet.Range("B2").CellStyle.Font.Underline = ExcelUnderline.Double
sheet.Range("B4").CellStyle.Font.Underline = ExcelUnderline.DoubleAccounting
sheet.Range("B6").CellStyle.Font.Underline = ExcelUnderline.Single
sheet.Range("B8").CellStyle.Font.Underline = ExcelUnderline.SingleAccounting

' Setting Font Color.
sheet.Range("C2").CellStyle.Font.Color = ExcelKnownColors.Lavender
```

## API Reference

### CellStyle.Font
- **FontName**: Sets the font face name.
- **Bold**: Boolean property to set bold style.
- **Italic**: Boolean property to set italic style.
- **Size**: Numeric property to set font size.
- **Strikethrough**: Boolean property to apply strikethrough effect.
- **Subscript**: Boolean property to apply subscript effect.
- **Superscript**: Boolean property to apply superscript effect.
- **Underline**: Enum property for underline types (e.g., `ExcelUnderline.Double`, `ExcelUnderline.Single`).
- **Color**: Property to set the font color using predefined ExcelKnownColors.

## Code Examples

The above code snippets demonstrate how to configure different font properties using the `XlsIO` library. These examples illustrate setting font types, styles, sizes, effects, underline types, and colors in Excel cells.

## Cross References

For more detailed examples and additional font properties, refer to the documentation on cell formatting in the `XlsIO` library.

<!-- tags: [XlsIO, CellStyle, Font Properties, C#, VB.NET] keywords: [font name, bold, italic, size, strikethrough, subscript, superscript, underline, font color, ExcelUnderline] -->
```