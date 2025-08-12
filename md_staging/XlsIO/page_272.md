```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_272.jpeg
document_name: XlsIO
page_number: 272
page_id: XlsIO#page_272
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:44Z
fidelity: lossless
-->

## Overview
- This page provides an example of applying filters to pivot tables using the XlsIO library. It demonstrates how to dynamically manipulate pivot table filters and access pivot table values programmatically.

## Content

```csharp
filter.Value1 = "East"
pivotTable.Fields(1).Axis = PivotAxisTypes.Row
pivotTable.Fields(3).Axis = PivotAxisTypes.Column

Dim field As IPivotField = pivotTable.Fields(2)
pivotTable.DataFields.Add(field, "sum", PivotSubtotalTypes.Sum)
'The following code sample must be included to XlsIO layout the pivot
table 'like MS Excel.

pivotTable.Layout()
```

### Supported Elements:
1. **Apply filter value to page filter of the pivot table.**
2. **Pivot table values can be accessed dynamically.**

### Apply Filter to Pivot Table
In Microsoft Excel, filtered data of a pivot table displays only the subset of data that meet the criteria we specified. The Excel has drop-down filter arrows for report/page filter fields, row fields, and column fields. This can be achieved in **XlsIO** using the `IPivotFilters` interface.

#### Page Field Filter
The page field filter filters the pivot table based on page field items. The following code example illustrates how to apply multiple filters to the page field items.

```csharp
//Step 1: Instantiate the spreadsheet creation engine.
ExcelEngine excelEngine = new ExcelEngine();
//Step 2: Instantiate the excel application object.
IApplication application = excelEngine.Excel;

//Set the default version as Excel 2010.
application.DefaultVersion = ExcelVersion.Excel2010;

IWorkbook workbook = application.Workbooks.Open("PivotCodeDate.xlsx");
```

### Page-level Navigation/TOC (if applicable)

## Code Examples (multi-language supported)

```csharp
void ApplyPivotTableFilter()
{
    //Step 1: Instantiate the spreadsheet creation engine.
    ExcelEngine excelEngine = new ExcelEngine();
    //Step 2: Instantiate the excel application object.
    IApplication application = excelEngine.Excel;

    //Set the default version as Excel 2010.
    application.DefaultVersion = ExcelVersion.Excel2010;

    IWorkbook workbook = application.Workbooks.Open("PivotCodeDate.xlsx");

    // Apply filter to the pivot table
    IPivotTable pivotTable = workbook.Worksheets["PivotTableSheet"].PivotTables["PivotTable1"];

    // Example of applying a filter
    IPivotFilter filter = pivotTable.PageFields[1].Filters.Add();
    filter.Value1 = "East";
    
    // Layout the pivot table
    pivotTable.Layout();
    
    // Save the workbook
    workbook.Save("FilteredPivotTable.xlsx");
    workbook.Close();

    // Dispose the objects
    excelEngine.Dispose();
}
```

### Cross References
- See also: **PivotTableInterface** and **IPivotFilters** for more details on pivot table operations.

<!-- tags: [XlsIO, pivot table, filters, IPivotFilters, IPivotFields, ExcelIO, Winforms] keywords: [pivot table, filters, Excel, XlsIO, filtering, IPivotFields, IPivotFilters, ExcelIO, C#, programmatic filtering] -->
```