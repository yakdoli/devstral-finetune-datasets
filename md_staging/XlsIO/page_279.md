```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_279.jpeg
document_name: XlsIO
page_number: 279
page_id: XlsIO#page_279
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:56Z
fidelity: lossless
-->

## XlsIO

### Overview
- Demonstrates the creation and configuration of a PivotTable in an Excel worksheet.
- Illustrates how to access worksheets, select data for cache, and define PivotTable fields and axes.
- Explains the application of row and column field filters based on labels.

### Content

The following code snippet illustrates how to create a PivotTable in an Excel worksheet using the XlsIO library.

```csharp
application.DefaultVersion = ExcelVersion.Excel2010

Dim workbook As IWorkbook = application.Workbooks.Open("PivotCodeDate.xlsx")

'The first worksheet object in the worksheets collection is accessed.
Dim worksheet As IWorksheet = workbook.Worksheets(0)

'Access the worksheet to draw pivot table.
Dim pivotSheet As IWorksheet = workbook.Worksheets(1)

'Select the data to add in cache.
Dim cache As IPivotCache = workbook.PivotCaches.Add(worksheet("A1:H50"))

'Insert the pivot table.
Dim pivotTable As IPivotTable = pivotSheet.PivotTables.Add("PivotTable1", pivotSheet("A1"), cache)
pivotTable.Fields(4).Axis = PivotAxisTypes.Page
pivotTable.Fields(2).Axis = PivotAxisTypes.Row
pivotTable.Fields(6).Axis = PivotAxisTypes.Row
pivotTable.Fields(3).Axis = PivotAxisTypes.Column

Dim field As IPivotField = pivotSheet.PivotTables(0).Fields(5)
pivotTable.DataFields.Add(field, "Sum of Units", PivotSubtotalTypes.Sum)

'Apply row field filter.
Dim rowField As IPivotField = pivotTable.Fields(2)
'Applying Label based row field filter
rowField.PivotFilters.Add(PivotFilterType.CaptionEqual, Nothing, "East", Nothing)

'Apply column field label based filter.
Dim colField As IPivotField = pivotTable.Fields(3)
```

### API Reference

#### Classes and Interfaces
- `IWorkbook`
- `IWorksheet`
- `IPivotCache`
- `IPivotTable`
- `IPivotField`

#### Enumerations
- `PivotAxisTypes`
- `PivotFilterType`
- `PivotSubtotalTypes`

### Code Examples

The code above shows a complete example of creating a PivotTable, configuring its fields and axes, and applying filters to specific fields. This example uses the XlsIO library to manipulate Excel documents programmatically.

### Final Notes

This page provides a comprehensive guide on how to use the XlsIO library to create and configure PivotTables in Excel worksheets. It includes examples of selecting data for the cache, defining PivotTable fields, and applying filters based on specific labels.

### See also:
- XlsIO documentation for more advanced features and configuration options.
- Examples of other PivotTable functionalities.
```

<!-- tags: [xlsio, pivottable, pivottableconfig, filter, workbook, worksheet, xlsx, pivotfilter, pivotaxis, syncfusion, winforms, 11.4.0.26] keywords: [pivotcache, fields, axes, sumofunits, rowfilter, columnfilter, labelfilter, defaultversion, excel2010, page 279] -->
```