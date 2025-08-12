```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_140.jpeg
document_name: XlsIO
page_number: 140
page_id: XlsIO#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:25Z
fidelity: lossless
-->


## Style Customization in XlsIO

### C# Sample

```csharp
workbook.SetPaletteColor(9, Color.FromArgb(239, 243, 247)); 
bodyStyle.Color = Color.FromArgb(239, 243, 247); 
bodyStyle.Borders[ExcelBordersIndex.EdgeLeft].LineStyle = ExcelLineStyle.Thin; 
bodyStyle.Borders[ExcelBordersIndex.EdgeRight].LineStyle = ExcelLineStyle.Thin; 
bodyStyle.EndUpdate(); 

// Apply the defined styles. 
// Apply Body Style. 
sheet.UsedRange.CellStyleName = "BodyStyle"; 

// Apply Header style. 
sheet.Rows[0].CellStyleName = "HeaderStyle";
```

### VB.NET Sample

```vb
' Formatting

' Global styles should be used when the same style needs to be applied to
' more than 
' one cell. This usage of a global style reduces memory usage.

' Header Style
Dim headerStyle As IStyle = workbook.Styles.Add("Header Style")

' Add custom colors to the palette.
headerStyle.BeginUpdate()
workbook.SetPaletteColor(8, Color.FromArgb(255, 174, 33))
headerStyle.Color = Color.FromArgb(255, 174, 33)
headerStyle.Font.Bold = True
headerStyle.Borders(ExcelBordersIndex.EdgeLeft).LineStyle = ExcelLineStyle.Thin
headerStyle.Borders(ExcelBordersIndex.EdgeRight).LineStyle = ExcelLineStyle.Thin
headerStyle.Borders(ExcelBordersIndex.EdgeTop).LineStyle = ExcelLineStyle.Thin
headerStyle.Borders(ExcelBordersIndex.EdgeBottom).LineStyle = ExcelLineStyle.Thin
headerStyle.EndUpdate()

' Body Style
Dim bodyStyle As IStyle = workbook.Styles.Add("BodyStyle")

' Add custom colors to the palette.
bodyStyle.BeginUpdate()
```

<!-- tags: [xlsio, styles, formatting, global style, header style, body style, color palette, borders, thin line, VB.NET, C#] keywords: [workbook, setpalettecolor, color, font, bold, borders, linestyle, usedrange, cellstylename, beginupdate, endupdate] -->
```