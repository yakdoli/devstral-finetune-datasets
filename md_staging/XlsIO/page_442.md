```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_442.jpeg
document_name: XlsIO
page_number: 442
page_id: XlsIO#page_442
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:59Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.Range("D3").Number = 26.72
sheet.Range("D4").Number = 33.71
sheet.Range("D5").Number = 45.81
sheet.Range("D6").Number = 12.17

sheet.Range("F1").Number = 26.72
sheet.Range("F2").Number = 33.71

sheet.Range("F3").Number = 45.81
sheet.Range("F4").Number = 12.17

' Discontiguous range.
Dim rangesOne As Syncfusion.XlsIO.IRanges = sheet.CreateRangesCollection()
rangesOne.Add(sheet.Range("B3:B6"))
rangesOne.Add(sheet.Range("F1:F2"))

Dim rangesTwo As Syncfusion.XlsIO.IRanges = sheet.CreateRangesCollection()
rangesTwo.Add(sheet.Range("D3:D6"))
rangesTwo.Add(sheet.Range("F3:F4"))

' Adding a New(Embedded chart)to the Worksheet.
Dim shape As Syncfusion.XlsIO.IChartShape = sheet.Charts.Add()
shape.PrimaryCategoryAxis.Title = "City"
shape.PrimaryValueAxis.Title = "Sales (in Dollars)"
shape.ChartTitle = "Texas Books Unit Sales"

' Setting the Series Names in a Legend.
Dim serieOne As Syncfusion.XlsIO.IChartSerie = shape.Series.Add()
serieOne.Name = "Jan"
serieOne.Values = rangesOne

Dim serieTwo As Syncfusion.XlsIO.IChartSerie = shape.Series.Add()
serieTwo.Name = "March"
serieTwo.Values = rangesTwo

' Setting the (Rows & Columns)Property for the Embedded chart.
shape.BottomRow = 40
shape.TopRow = 10
shape.LeftColumn = 3
shape.RightColumn = 15
```

## How to define discontinuous ranges?

<!-- tags: [syncfusion, winforms, xlsio, discontinuous ranges, chart series, embedded charts] keywords: [discontinuous ranges, embedded chart, series legend, chart properties, worksheet, sales data] -->
```