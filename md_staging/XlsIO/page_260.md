```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_260.jpeg
document_name: XlsIO
page_number: 260
page_id: XlsIO#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:56Z
fidelity: lossless
-->

# PivotTable in Excel Using XlsIO

## Overview
- Demonstrates how to create and configure a PivotTable in an Excel sheet using the XlsIO library.
- Explains the process of adding fields to the PivotTable and organizing them into specific areas: Report Filter, Column Labels, Row Labels, and Values.
- Guides users through the steps of building a report using the PivotTable Field List.

## Content

### Creating a New Sheet for the PivotTable

To place the PivotTable, a new sheet must be created within the workbook. This sheet allows the PivotTable to be added and customized without affecting other data or worksheets. The figure below provides an example of a new sheet setup for the PivotTable.

#### Figure: New Sheet for the PivotTable

![New Sheet to place the Pivot Table](#)
**Figure 90: New Sheet to place the Pivot Table**

### Building the PivotTable Report

Once you select a field, the PivotTable appears in the specified location. The next step is to populate the PivotTable with the necessary data fields, which are available in the PivotTable Field List on the right-hand side of the Excel interface. The fields can be dragged into specific areas of the PivotTable grid to define how the data is presented.

#### Procedures for Populating the PivotTable

1. **Select Fields from the PivotTable Field List:** Click on the fields you want to include in your report. These fields will be used to create the report.
   
2. **Drag Fields to Defined Areas:**
   - **Report Filter:** Use this area to filter the data displayed in the PivotTable based on specific criteria.
   - **Column Labels:** Drag fields here to define the columns in the PivotTable.
   - **Row Labels:** Drag fields here to define the rows in the PivotTable.
   - **Values:** Drag fields here to specify the values to be summarized or displayed in the PivotTable.

3. **Update the PivotTable:** After dragging the fields to the appropriate areas, click the "Update" button to refresh the PivotTable with the selected fields and their arrangement.

#### Example of Fields in the PivotTable Field List

The following list shows some of the fields typically available for selection in the PivotTable Field List:
- Date
- Weekday
- Region
- Employee
- Item
- Units
- Unit Cost
- Total

These fields can be dragged to the appropriate areas as per the desired report configuration.

## API Reference

- **Class:** `PivotTable`
  - **Methods:**
    - `AddFieldToReportFilter(field)`
    - `AddFieldToColumnLabels(field)`
    - `AddFieldToRowLabels(field)`
    - `AddFieldToValues(field)`
  - **Properties:**
    - `FieldList`
    - `ReportFilterArea`
    - `ColumnLabelsArea`
    - `RowLabelsArea`
    - `ValuesArea`

## Code Examples

### Example: Creating and Configuring a PivotTable

```csharp
using Syncfusion.XlsIO;

// Create a new Excel engine instance
ExcelEngine engine = new ExcelEngine();
IApplication application = engine.Excel;

// Create a new workbook and worksheet
IWorkbook workbook = application.Workbooks.Create();
IWorksheet worksheet = workbook.Worksheets[0];

// Create a new PivotTable
IPivotTable pivotTable = worksheet.PivotTables.Add("A1", "A3", "A5", "A10");

// Add fields to the PivotTable areas
pivotTable.Fields.AddToReportFilter("Date");
pivotTable.Fields.AddToColumnLabels("Region");
pivotTable.Fields.AddToRowLabels("Employee");
pivotTable.Fields.AddToValues("Total");

// Update the PivotTable to reflect changes
pivotTable.Update();

// Save the workbook
workbook.Save("PivotTableExample.xlsx");

// Close the workbook and engine
workbook.Close();
engine.Dispose();
```

## Page-level Navigation/TOC
- [Overview](#overview)
- [Content](#content)
  - [Creating a New Sheet for the PivotTable](#creating-a-new-sheet-for-the-pivottable)
  - [Building the PivotTable Report](#building-the-pivottable-report)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

## Cross References
- See also: [Working with PivotTables in Excel](#working-with-pivottables-in-excel)

<!-- tags: [XlsIO, Excel, PivotTable, Winforms, Control, Configuration, FieldList, ReportBuilding] keywords: [PivotTable, ReportFilter, ColumnLabels, RowLabels, Values, PivotTable Field List, Drag and Drop, Update] -->
```