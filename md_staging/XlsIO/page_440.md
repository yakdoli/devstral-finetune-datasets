```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_440.jpeg
document_name: XlsIO
page_number: 440
page_id: XlsIO#page_440
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:32Z
fidelity: lossless
-->

Essential XlsIO

```csharp
// Entering the data for the chart.
sheet.Range["A1"].Text = "Texas books Unit sales";
sheet.Range["A1:D1"].Merge();
sheet.Range["A1"].CellStyle.Font.Bold = true;

sheet.Range["B2"].Text = "Jan";
sheet.Range["C2"].Text = "Feb";
sheet.Range["D2"].Text = "Mar";

sheet.Range["A3"].Text = "Austin";
sheet.Range["A4"].Text = "Dallas";
sheet.Range["A5"].Text = "Houston";
sheet.Range["A6"].Text = "San Antonio";

sheet.Range["B3"].Number = 53.75;
sheet.Range["B4"].Number = 52.85;
sheet.Range["B5"].Number = 59.77;
sheet.Range["B6"].Number = 96.15;

sheet.Range["C3"].Number = 79.79;
sheet.Range["C4"].Number = 59.22;
sheet.Range["C5"].Number = 10.09;
sheet.Range["C6"].Number = 73.02;

sheet.Range["D3"].Number = 26.72;
sheet.Range["D4"].Number = 33.71;
sheet.Range["D5"].Number = 45.81;
sheet.Range["D6"].Number = 12.17;

sheet.Range["F1"].Number = 26.72;
sheet.Range["F2"].Number = 33.71;

sheet.Range["F3"].Number = 45.81;
sheet.Range["F4"].Number = 12.17;

// Discontinuous range.
IRanges rangesOne = sheet.CreateRangesCollection();
rangesOne.Add(sheet.Range["B3:B6"]);
rangesOne.Add(sheet.Range["F1:F2"]);

IRanges rangesTwo = sheet.CreateRangesCollection();
rangesTwo.Add(sheet.Range["D3:D6"]);
rangesTwo.Add(sheet.Range["F3:F4"]);

// Adding a New (Embedded chart)to the Worksheet.
IChartShape shape = sheet.Charts.Add();
```

<!-- tags: [syncfusion-sdk, XlsIO, WinForms, charts, embedded charts, data entry, ranges, chart creation] keywords: [Texas books Unit sales, Jan, Feb, Mar, Austin, Dallas, Houston, San Antonio, ranges collection, embedded charts, chart creation, number entry, bold font, cell merging] -->
```