```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: XlsIO
page_number: 130
page_id: XlsIO#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:59Z
fidelity: lossless
-->

# Essential XlsIO

```cs
sheet.Range["B4"].CellStyle.Borders.LineStyle = ExcelLineStyle.Hair;
sheet.Range["B6"].CellStyle.Borders.LineStyle = ExcelLineStyle.Medium_dash_dot_dot;
```

```vb
' Accessing the first worksheet object in the worksheets collection.
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Setting Border Line Styles.
sheet.Range("A2").CellStyle.Borders.LineStyle = ExcelLineStyle.Medium
sheet.Range("A4").CellStyle.Borders.LineStyle = ExcelLineStyle.Double
sheet.Range("A6").CellStyle.Borders.LineStyle = ExcelLineStyle.Dash_dot
sheet.Range("A8").CellStyle.Borders.LineStyle = ExcelLineStyle.Thick
sheet.Range("A10").CellStyle.Borders.LineStyle = ExcelLineStyle.Thin
sheet.Range("A12").CellStyle.Borders.LineStyle = ExcelLineStyle.Medium_dashed
sheet.Range("B2").CellStyle.Borders.LineStyle = ExcelLineStyle.Slanted_dash_dot
sheet.Range("B4").CellStyle.Borders.LineStyle = ExcelLineStyle.Hair
sheet.Range("B6").CellStyle.Borders.LineStyle = ExcelLineStyle.Medium_dash_dot_dot

' Setting the Border Color for Cell "A2".
sheet.Range("A2").CellStyle.Borders(ExcelBordersIndex.DiagonalDown).Color = ExcelKnownColors.Blue
sheet.Range("A2").CellStyle.Borders(ExcelBordersIndex.DiagonalUp).Color = ExcelKnownColors.Blue
sheet.Range("A2").CellStyle.Borders(ExcelBordersIndex.EdgeBottom).Color = ExcelKnownColors.Blue
sheet.Range("A2").CellStyle.Borders(ExcelBordersIndex.EdgeLeft).Color = ExcelKnownColors.Blue
sheet.Range("A2").CellStyle.Borders(ExcelBordersIndex.EdgeRight).Color = ExcelKnownColors.Blue
```

## Copyright Information
© 2013 Syncfusion. All rights reserved.

<!-- tags: [XlsIO, border styles, line styles, border colors, Syncfusion Winforms] keywords: [border, line style, color, XlsIO, Syncfusion, worksheet, cell style, ExcelKnownColors, ExcelLineStyle] -->
```