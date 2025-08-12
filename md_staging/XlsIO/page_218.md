```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_218.jpeg
document_name: XlsIO
page_number: 218
page_id: XlsIO#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:55Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates embedding a chart in an Excel worksheet using XlsIO.
- Highlights the use of a pie chart to compare sales data across different categories.
- Shows how to create and format a sales report with totals and subtotals.

## Content

### Chart Worksheet

#### Sales Report
The image displays a sales report in an Excel worksheet, created using XlsIO. The report includes a table summarizing sales data across various categories, with columns for "Category Name," "Quantity," and "Amount." Below is the structure of the sales data:

| **Category Name**   | **Quantity** | **Amount** |
|---------------------|--------------|------------|
| Beverages          | 925          | $27,761.57 |
| Condiments          | 378          | $10,773.27 |
| Confections         | 880          | $22,877.18 |
| Dairy Products      | 581          | $13,685.32 |
| Grains/Cereals     | 189          | $3,325.40  |
| Meat/Poultry        | 92           | $4,083.66  |
| **Total**           | **3,045**    | **$82,506.41** |

#### Embedded Chart
The worksheet also includes a pie chart titled "Sales comparison," which visually represents the sales data by category. The chart's legend shows the breakdown as follows:
- Beverages: 925
- Condiments: 378
- Confections: 880
- Dairy Products: 581
- Grains/Cereals: 189
- Meat/Poultry: 92
- Total: 3,045

### Caption
**Figure 76: XlsIO with Embedded Chart**

## API Reference (if applicable)

### Code Examples
```csharp
// Example of creating a Sales Report with embedded chart using XlsIO
Workbook workbook = new Workbook();
IWorksheet worksheet = workbook.Worksheets[0];

// Populate sales data
worksheet.Range["A1"].Text = "Sales Report";
worksheet.Range["A3"].Text = "Category Name";
worksheet.Range["B3"].Text = "Quantity";
worksheet.Range["C3"].Text = "Amount";

// Add data rows
worksheet.Range["A4"].Text = "Beverages";
worksheet.Range["B4"].Text = "925";
worksheet.Range["C4"].Text = "$27,761.57";

// ... Add more categories and data rows as needed ...

// Create a pie chart
IPieChart pieChart = worksheet.Charts.AddPieChart();
pieChart.SetData(worksheet.Range["B4:B9"], worksheet.Range["C4:C9"]);
pieChart.ChartTitle.Text = "Sales comparison";
```

## Page-level Navigation/TOC (if applicable)
- 4.2.2.2 Chart Worksheet

## Cross References
- See also: XlsIO data manipulation and chart creation tutorials.

<!-- tags: [xlsio, excel, embedded chart, sales report, pie chart, winforms, syncfusion, version: 11.4.0.26] keywords: [xlsio, sales report, embedded chart, pie chart, data manipulation, worksheet, chart creation] -->
```