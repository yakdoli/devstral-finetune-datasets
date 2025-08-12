```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_583.jpeg
document_name: chart
page_number: 583
page_id: chart#page_583
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:22Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates creating and configuring a chart in a Windows Forms application using the Syncfusion WinForms API.
- Explains how to populate chart data and save the chart to an Excel file.

## Content

### Chart Creation and Export

```csharp
// Make the chart as active sheet.
chart.Activate();

// Save the Chart book.
chartBook.SaveAs(exportFileName);

chartBook.Close();
ExcelUtils.Close();

// Launches the file.
System.Diagnostics.Process.Start(exportFileName);
```

### Chart Creation in VB.NET

```vb
[VB.NET]

Dim exportFileName As String = Application.StartupPath & "\chartexport" & ".xls"

' A new workbook with a worksheet should be created.
Dim chartBook As IWorkbook = ExcelUtils.CreateWorkbook(1)
Dim sheet As IWorksheet = chartBook.Worksheets(0)

' Fill the worksheet with chart data.
For i As Integer = 1 To 5
    sheet.Range(i, 1).Number = Me.chartControl1.Series(0).Points(i - 1).X
    sheet.Range(i, 2).Number = Me.chartControl1.Series(0).Points(i - 1).YValues(0)
Next i

' Create a chart worksheet.
Dim chart As IChart = chartBook.Charts.Add("Essential Chart")
' Specify the title of the Chart.
chart.ChartTitle = "Essential Chart"

' Initialize a new series instance and add it to the series collection of the chart.
Dim series As IChartSerie = chart.Series.Add()

' Specify the chart type of the series.
series.SerieType = ExcelChartType.Column_Clustered

' Specify the name of the series. This will be displayed as the text of the legend.
series.Name = "Sample Series"
' Specify the value ranges for the series.
series.Values = sheet.Range("B1:B5")
' Specify the Category labels for the series.
```

<!-- tags: [chart, windows forms, essential chart, exporting to excel, chart control] keywords: [chart, essential chart, windows forms application, exporting, excel, vb.net, .xls] -->
```