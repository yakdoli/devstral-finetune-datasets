```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_283.jpeg
document_name: XlsIO
page_number: 283
page_id: XlsIO#page_283
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:13Z
fidelity: lossless
-->

## Overview
- This section explains how to create a PivotChart in Excel, detailing the dialog box settings and the placement of the PivotChart in a new worksheet.
- The process involves selecting the data range, modifying the range if necessary, and choosing the position for the PivotChart within the workbook.

## Content

### Figure Description

#### Figure 93: PivotChart Creation Dialog Box

The screenshot shows the **Create PivotTable with PivotChart** dialog box in Excel, where users can specify the data range for analysis and choose where to place the PivotTable and PivotChart. The key elements are:

- **Select the data that you want to analyze:**
  - The selected range is `Data!$A$1:$H$50`, and users can modify this if needed.
  - The option to use an external data source is also available but not selected.

- **Choose where you want the PivotTable and PivotChart to be placed:**
  - The default option is to place them in a **New Worksheet**, which is commonly used for PivotCharts.

#### Figure 94: New Sheet to Place the PivotTable and PivotChart

The second screenshot shows the setup for a **New Sheet** to hold the PivotTable and PivotChart. Key elements include:

- **PivotTable Field List:**
  - The green checkbox in the PivotField area indicates that fields are being selected for the PivotTable and PivotChart.

- **Chart 1:**
  - The chart is visually displayed with a sample bar chart.
  - Instructions guide users to build the PivotChart by choosing fields from the PivotTable Field List.

### Explanation

- By default, MS Excel selects the entire range of data in the table. Users can modify the range if specific data needs to be analyzed.
- The PivotChart is typically placed in a **New Worksheet**, making it easier to view and analyze without cluttering the original data sheet.

## WinForms-specific conventions
- The document uses Excel-specific terminology and features, such as PivotTables and PivotCharts, which are relevant for data analysis and visualization tasks in WinForms applications.

## API Reference (if applicable)
No specific APIs are referenced in this section, as the focus is on Excel functionality. However, similar data handling and pivot functionalities can be implemented in C# for WinForms applications using libraries such as `ExcelInterOp`.

## RAG Annotations
<!-- tags: [xlsio, ms-excel, pivot-table, pivot-chart, winforms] keywords: [ms-excel, pivottable, pivotchart, data-range, new-worksheet] -->
```