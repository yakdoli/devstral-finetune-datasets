```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_220.jpeg
document_name: XlsIO
page_number: 220
page_id: XlsIO#page_220
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:42Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
IChartSerie seriethree = chart.Series[2];
seriethree.Name = "March";
```

## Overview
- Adding data to a chart.
- Configuring chart properties.
- Setting series names for a legend.

## Content

### Setup Chart Data

Here is an example of setting up a chart in a worksheet with data entry and configuration.

#### Setting Data for the Chart
```vb.net
' Entering the Data for the chart.
sheet.Range("A1").Text = "Texas books Unit sales"
sheet.Range("A1:D1").Merge()
sheet.Range("A1").CellStyle.Font.Bold = True

sheet.Range("B2").Text = "Jan"
sheet.Range("C2").Text = "Feb"
sheet.Range("D2").Text = "Mar"

sheet.Range("A3").Text = "Austin"
sheet.Range("A4").Text = "Dallas"
sheet.Range("A5").Text = "Houston"
sheet.Range("A6").Text = "San Antonio"

sheet.Range("B3").Number = 53.75
sheet.Range("B4").Number = 52.85
sheet.Range("B5").Number = 59.77
sheet.Range("B6").Number = 96.15

sheet.Range("C3").Number = 79.79
sheet.Range("C4").Number = 59.22
sheet.Range("C5").Number = 10.09
sheet.Range("C6").Number = 73.02

sheet.Range("D3").Number = 26.72
sheet.Range("D4").Number = 33.71
sheet.Range("D5").Number = 45.81
sheet.Range("D6").Number = 12.17
```

#### Adding a New Chart to the Existing Worksheet
```vb.net
' Adding a New chart to the Existing Worksheet.
Dim chart As IChart = workbook.Charts.Add()
chart.DataRange = sheet.Range("B3:D6")
chart.Name = "ChartWorksheet"
chart.PrimaryCategoryAxis.Title = "City"
chart.PrimaryValueAxis.Title = "Sales (in Dollars)"
chart.ChartTitle = "Texas Books Unit Sales"
```

#### Setting the Series Names in a Legend
```vb.net
' Setting the Serie Names in a Legend.
Dim seriethree As IChartSerie = chart.Series[2]
seriethree.Name = "March"
```

## Code Examples

### Adding Series to a Chart

```vb.net
Dim chart As IChart = workbook.Charts.Add()
chart.DataRange = sheet.Range("B3:D6")
chart.Name = "ChartWorksheet"
chart.PrimaryCategoryAxis.Title = "City"
chart.PrimaryValueAxis.Title = "Sales (in Dollars)"
chart.ChartTitle = "Texas Books Unit Sales"

Dim serietwo As IChartSerie = chart.Series[1]
serietwo.Name = "Feb"

Dim seriethree As IChartSerie = chart.Series[2]
seriethree.Name = "March"
```

## Page-level Navigation/TOC (if applicable)
- Overview
- Content
  - Setup Chart Data
  - Adding Series to a Chart

## RAG Annotations

```html
<!-- tags: [chart, series, legend, worksheet, data range, workbook, chart title] keywords: [chart, series, legend, worksheet, data range, workbook, chart title, texas books unit sales, city, sales in dollars, austin, dallas, houston, san antonio, june, march] -->
```
```