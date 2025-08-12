```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: XlsIO
page_number: 210
page_id: XlsIO#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:10Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how XlsIO renders images from an XLS file in a Panel.
- Explains the use of XlsIO's Chart APIs for creating and modifying Excel charts.
- Highlights options for embedding charts inside a worksheet or creating a separate chart worksheet.

## Content

### 4.2.2 Charts

This section explains the usage of the Essential XlsIO's Chart APIs.

**Charts** can convey much more than numbers and makes it easier to see the meaning behind the numbers. Essential XlsIO has advanced support for creating and modifying Excel charts inside a workbook. There is an option to choose between creating an **Embedded Chart** (chart is embedded inside a worksheet) or a **Chart Worksheet** (chart is a separate worksheet).

#### 4.2.2.1 Embedded Chart

傣

Figure 75: Image from an xls file read by XlsIO and rendered in a Panel
![Figure 75](https://i.imgur.com/abstract_image.png)

### Related Information
- **Chart Rendering**: Learn how XlsIO handles the rendering of charts within Excel files.
- **Chart Customization**: Discover how to customize the appearance and data of charts using XlsIO's Chart APIs.

### API Reference
- **Namespace**: Syncfusion.XlsIO
- **Class**: Workbook
- **Methods**:
  - `CreateChartSheet`: Creates a new ChartSheet.
  - `CreateChart`: Creates a new chart in the specified sheet.
  
### Code Examples

```csharp
// Example: Creating an embedded chart
using (ExcelEngine excelEngine = new ExcelEngine())
{
    IApplication application = excelEngine.Excel;
    application.DefaultVersion = ExcelVersion.Excel2016;
    IWorkbook workbook = application.Workbooks.Create(1);
    IWorksheet worksheet = workbook.Worksheets[0];

    // Add data to the worksheet
    worksheet.Range["A1"].Text = "Category";
    worksheet.Range["A2"].Text = "Sales";
    worksheet.Range["A3"].Text = "Profit";
    worksheet.Range["B1"].Text = "2010";
    worksheet.Range["B2"].Text = "1000";
    worksheet.Range["B3"].Text = "500";

    // Create an embedded chart
    IChart chart = worksheet.Charts.Add();

    // Set the type of the chart
    chart.ChartType = ChartType.Column;

    // Select the data range for the chart
    chart.SeriesCollection.Add(worksheet.Range["A2:A3"], worksheet.Range["B2:B3"]);
}
```

## RAG Annotations
<!-- tags: [XlsIO, Chart, Embedded, ChartSheet, Excel, Workbook, API, version: 11.4.0.26] keywords: [Essential XlsIO, Chart API, Embedded Chart, Chart Worksheet, ExcelChart, Workbook, Chart Rendering, Chart Customization, XlsIO] -->
```