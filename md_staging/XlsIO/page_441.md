```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_441.jpeg
document_name: XlsIO
page_number: 441
page_id: XlsIO#page_441
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:39Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
shape.PrimaryCategoryAxis.Title = "City";
shape.PrimaryValueAxis.Title = "Sales (in Dollars)";
shape.ChartTitle = "Texas Books Unit Sales";

// Setting the Series Names in a Legend.
IChartSerie serieOne = shape.Series.Add();
serieOne.Name = "Jan";
serieOne.Values = rangesOne;

IChartSerie serietwo = shape.Series.Add();
serietwo.Name = "March";
serietwo.Values = rangesTwo;

// Setting the(Rows & Columns)Property for the Embedded chart.
shape.BottomRow = 40;
shape.TopRow = 10;
shape.LeftColumn = 3;
shape.RightColumn = 15;
```

### [VB.NET]

```vb
' Entering the data for the chart.
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
```

<!-- tags: [XlsIO, Syncfusion Winforms, 11.4.0.26, chart, property, sheet, range] keywords: [chart, series, property, range, text, number, bold, font, add, series, add, embedded chart, top row, bottom row, left column, right column, data entry] -->
```