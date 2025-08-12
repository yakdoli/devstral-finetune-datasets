```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_389.jpeg
document_name: XlsIO
page_number: 389
page_id: XlsIO#page_389
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:12Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates rows/column manipulations using grouping in XlsIO.
- Explains customization options for grouping settings in MS Excel.
- Shows how to configure summary details for grouped data through the Settings dialog.

## Content

### Rows/Column Manipulations in Excel

The image illustrates the use of grouping features in XlsIO within an Excel spreadsheet. The table shown compares data for different countries under two categories: "Current Month" and "Last Month." Each category has sub-columns for Quantity and Amount, and the grouped data is displayed with a summary row for France as an example.

#### Data Table Example

| **Country Name** | **Current Month**        | **Last Month**         | **Loss/Gain** |
|------------------|--------------------------|------------------------|---------------|
| **Quantity**     | **Amount**               | **Quantity**           | **Amount**    |
| Belgium          | 192                      | $3,558.70             | 158           | $4,049.50 |
| Brazil           | 334                      | $20,360.40            | 506           | $9,617.28 |
| Canada           | 289                      | $8,626.33             | 0             | $0.00     |
| Denmark          | 140                      | $3,343.50             | 0             | $0.00     |
| Finland          | 0                        | $0.00                 | 82            | $1,401.00 |
| France           | 251                      | $8,026.04             | 172           | $3,864.83 |
| Germany          | 601                      | $10,294.23            | 327           | $24,378.54 |
| Ireland          | 79                       | $2,023.38             | 216           | $17,035.79 |
| Italy            | 83                       | $1,307.50             | 34            | $663.10   |
| Japan            | 0                        | $0.00                 | 0             | $0.00     |
| Mevirn           | **92**                   | **$514.40**           | **57**        | **$539.50** |

**Figure 138: Grouping in XlsIO**

### Customizing Grouping Settings

Excel provides options to customize the Grouping settings via the Settings dialog box. Users can adjust the display of summary details rows or columns by selecting relevant options in the dialog.

#### Grouping Settings Dialog Box

The dialog box below allows users to specify the direction of the summary details:

| **Settings**       |
|---------------------|
| **Direction**      |
| - Summary rows below detail |
| - Summary columns to right of detail |
| - Automatic styles |
| **Create**         |
| **Apply Styles**   |
| **OK**             |
| **Cancel**         |

**Figure 139: Grouping Settings Dialog in MS Excel**

## API Reference

This section is not explicitly detailed in the image, but based on the context, it might include references to methods or properties related to grouping, summary settings, and styling in XlsIO.

## Code Examples

The image doesn't contain any code examples, but as part of the documentation, code snippets could demonstrate how to programmatically set up grouping and summary rows in an Excel worksheet.

```csharp
// Example code: Setting up grouping in XlsIO
using Syncfusion.XlsIO;

// Create a new Excel file
IExcelEngine engine = new ExcelEngine();
IApplication application = engine.Excel;
IWorkbook workbook = application.Workbooks.Create(1);
IWorksheet worksheet = workbook.Worksheets[0];

// Populate data and set up grouping
worksheet.Range["A1"].Text = "Country Name";
worksheet.Range["B1"].Text = "Current Month Quantity";
worksheet.Range["C1"].Text = "Current Month Amount";
// ...additional data population and grouping setup

// Apply styles and save the workbook
workbook.Save("GroupedData.xlsx", ExcelVersion.Excel2013);
workbook.Close();
engine.ThrowOnException = false;
engine.Dispose();
```

## Page-level Navigation/TOC
This page focuses on rows/column manipulations in XlsIO, highlighting the use of grouping and customization options available for summarizing data.

### Cross References
- See also: "Using Data Manipulation Techniques in XlsIO" for more advanced examples.

<!-- tags: [XlsIO, grouping, rows/column manipulations, data summaries, MS Excel] keywords: [data manipulation, summary details, grouping settings] -->
```