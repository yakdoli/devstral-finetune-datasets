```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_366.jpeg
document_name: XlsIO
page_number: 366
page_id: XlsIO#page_366
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:03Z
fidelity: lossless
-->

# Importing and Exporting Data Tables

## Overview
- Demonstrates the functionality of exporting and importing DataTables using the `ImportDataTable` and `ExportDataTable` methods.
- Shows how to handle scenarios where no DataTable is available for export.

## Content

### C# Code Example

```csharp
sheet.ImportDataTable((DataTable)this.dataGrid1.DataSource, true, 1, 1, -1, -1);
}
else
{
    MessageBox.Show("There is no datatable to export, Please import a datatable first", "Error");
    return;
}
}
```

### VB.NET Code Example

```vb
' Read data from the spreadsheet.
Dim customersTable As DataTable =
sheet.ExportDataTable(sheet.UsedRange, ExcelExportDataTableOptions.ColumnNames)
Me.dataGrid1.DataSource = customersTable

' Export DataTable.
If Not Me.dataGrid1.DataSource Is Nothing Then
    sheet.ImportDataTable(CType(Me.dataGrid1.DataSource, DataTable), True, 1, 1, -1, -1)
Else
    MessageBox.Show("There is no datatable to export, Please import a datatable first", "Error")
    Return
End If
```

### ImportDataTable Customization

The `ImportDataTable` method has several overloads that can be used to enable customization options such as:

- Importing data from named ranges.
- Showing or hiding field names in the columns.
- Importing only a specific range of records.
- Preserving data types in the data table.

For more details, see the XlsIO class reference in the [Online documentation](Online documentation).

## API Reference

- `ImportDataTable(DataTable table, Boolean showHeaders, Int32 startRow, Int32 startColumn, Int32 endRow, Int32 endColumn)`
- `ExportDataTable(Range range, ExcelExportDataTableOptions options)`

## Code Examples

Both C# and VB.NET examples are provided above to illustrate the use of the `ImportDataTable` and `ExportDataTable` methods.

## Page-level Navigation/TOC (if applicable)

- Summary of DataTable Import and Export
- C# Code Example
- VB.NET Code Example
- ImportDataTable Customization

## Cross References

See also:
- [Online documentation](Online documentation) for XlsIO class reference.

<!-- tags: [product, syncfusion winforms, xlsio, datatable, import, export] keywords: [importdatatable, exportdatatable, datatables, named ranges, field names, data types, customization, online documentation] -->
```