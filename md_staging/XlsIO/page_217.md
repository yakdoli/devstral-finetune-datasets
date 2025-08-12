```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: XlsIO
page_number: 217
page_id: XlsIO#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:11Z
fidelity: lossless
-->

## Adding Embeded Chart with Sales Data

### Code Example

```csharp
sheet.Range("A5").Text = "Apr"
sheet.Range("A6").Text = "May"

' Random Data.
Dim r As Random = New Random
For i As Integer = 2 To 6
    For j As Integer = 2 To 3
        sheet.Range(i, j).Number = r.Next(0, 500)
    Next j
Next i

' Embedded Chart.
Dim chart As IChartShape = sheet.Charts.Add()

' Setting chart type.
chart.ChartType = ExcelChartType.Line

' Setting Chart Title.
chart.ChartTitle = "Product Sales comparison"

' Product A.
Dim productA As IChartSerie = chart.Series.Add("ProductA")
productA.Values = sheet.Range("B2:B6")
productA.CategoryLabels = sheet.Range("A2:A6")

' Product B.
Dim productB As IChartSerie = chart.Series.Add("ProductB")
productB.Values = sheet.Range("C2:C6")
productB.CategoryLabels = sheet.Range("A2:A6")
```
```html

<!-- tags: [xlsio, embedded chart, sales data, random data, product sales comparison, line chart, series, chart title] keywords: [xlsio, embedded, chart, sales, data, random, product, comparison, line, series, title] -->
```