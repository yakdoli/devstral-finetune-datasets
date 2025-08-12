```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: XlsIO
page_number: 116
page_id: XlsIO#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:34Z
fidelity: lossless
-->

### Text Alignment and Indentation in XlsIO

```csharp
// Text Alignment Setting (Horizontal Alignment).
sheet.Range["A2"].CellStyle.HorizontalAlignment = ExcelHAlign.HAlignCenter;
sheet.Range["A4"].CellStyle.HorizontalAlignment = ExcelHAlign.HAlignFill;
sheet.Range["A6"].CellStyle.HorizontalAlignment = ExcelHAlign.HAlignRight;
sheet.Range["A8"].CellStyle.HorizontalAlignment = ExcelHAlign.HAlignCenterAcrossSelection;

// Text Alignment Setting (Vertical Alignment).
sheet.Range["A2"].CellStyle.VerticalAlignment = ExcelVAlign.VAlignBottom;
sheet.Range["A4"].CellStyle.VerticalAlignment = ExcelVAlign.VAlignCenter;
sheet.Range["A6"].CellStyle.VerticalAlignment = ExcelVAlign.VAlignTop;
sheet.Range["A8"].CellStyle.VerticalAlignment = ExcelVAlign.VAlignDistributed;

// Text Indent Setting.
sheet.Range["B6"].CellStyle.IndentLevel = 6;
```

```vb.net
' Text Alignment Setting (Horizontal Alignment).
sheet.Range("A2").CellStyle.HorizontalAlignment = ExcelHAlign.HAlignCenter
sheet.Range("A4").CellStyle.HorizontalAlignment = ExcelHAlign.HAlignFill
sheet.Range("A6").CellStyle.HorizontalAlignment = ExcelHAlign.HAlignRight
sheet.Range("A8").CellStyle.HorizontalAlignment = ExcelHAlign.HAlignCenterAcrossSelection

' Text Alignment Setting (Vertical Alignment.
sheet.Range("A2").CellStyle.VerticalAlignment = ExcelVAlign.VAlignBottom
sheet.Range("A4").CellStyle.VerticalAlignment = ExcelVAlign.VAlignCenter
sheet.Range("A6").CellStyle.VerticalAlignment = ExcelVAlign.VAlignTop
sheet.Range("A8").CellStyle.VerticalAlignment = ExcelVAlign.VAlignDistributed

' Text Indent Setting.
sheet.Range("B6").CellStyle.IndentLevel = 6
```

### Text Control

The Text Control section provides three options: Wrap Text, Shrink To Fit, and Merge Cells.

## API Reference

- **Namespace**: `ExcelHAlign`
  - **Attributes**:
    - `HAlignCenter`: Aligns text to the center of the cell.
    - `HAlignFill`: Fills the cell with text as much as possible.
    - `HAlignRight`: Aligns text to the right edge of the cell.
    - `HAlignCenterAcrossSelection`: Centers text across selected cells.

- **Namespace**: `ExcelVAlign`
  - **Attributes**:
    - `VAlignBottom`: Aligns text to the bottom of the cell.
    - `VAlignCenter`: Aligns text to the center of the cell vertically.
    - `VAlignTop`: Aligns text to the top of the cell.
    - `VAlignDistributed`: Distributes text evenly across the cell vertically.

## Code Examples

The provided code snippets demonstrate how to set text alignment and indentation in an Excel sheet using both C# and VB.NET. These examples illustrate how to use the `ExcelHAlign` and `ExcelVAlign` enumerations to control horizontal and vertical alignment, respectively, as well as how to set the indentation level for specific cells.

## Summary

This section covers the functionality for setting text alignment and indentation in Excel sheets using the XlsIO library. It includes methods for horizontal and vertical alignment, as well as text indentation settings. The Text Control section provides options for wrapping text, shrinking text to fit, and merging cells, enhancing the formatting capabilities of the Excel sheet.

<!-- tags: [xlsio, text alignment, text control, winforms, version 11.4.0.26] keywords: [text alignment, horizontal alignment, vertical alignment, text indentation, wrap text, shrink to fit, merge cells, excelhalign, excelvalign] -->
```