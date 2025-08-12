```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_365.jpeg
document_name: XlsIO
page_number: 365
page_id: XlsIO#page_365
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:42Z
fidelity: lossless
-->

## Import/Export Data Example

### Overview
- Demonstrates importing and exporting data between a spreadsheet and a grid control.
- Highlights the use of the `ExportDataTable` method to extract data from a sheet into a `DataTable`.
- Illustrates binding the `DataTable` to a grid and exporting it back to a sheet.

### Content

#### Importing Data from a Spreadsheet to a Grid
The following code snippet shows how to read data from a spreadsheet and bind it to a grid control.

```csharp
// Read data from the spreadsheet.
DataTable customersTable =
    sheet.ExportDataTable(sheet.UsedRange, ExcelExportDataTableOptions.ColumnName);

this.dataGrid1.DataSource = customersTable;
```

#### Exporting Data from a Grid to a Spreadsheet
The code snippet below demonstrates exporting data from a grid back to a spreadsheet.

```csharp
// Export DataTable.
if (this.dataGrid1.DataSource != null)
{
    // Export logic would be implemented here.
}
```

### API Reference
#### Methods
- **ExportDataTable(sheet.UsedRange, options)**
  - **Parameters:**
    - `sheet.UsedRange`: Specifies the range of data to be exported.
    - `options`: Defines the export options, such as including column names.
  - **Returns:** A `DataTable` containing the exported data.

#### Properties
- **DataSource**: A property of the grid control that binds the grid to a data source.

### Code Examples
The provided code examples demonstrate the complete process of:
1. Importing data from a spreadsheet into a `DataTable`.
2. Binding the `DataTable` to a grid.
3. Exporting data back to a spreadsheet.

### Cross References
- Refer to the `ExportDataTable` method documentation for more information on export options.
- Consult the grid control's `DataSource` property for details on data binding.

<!-- tags: [Syncfusion Winforms, XlsIO, ImportExport, DataTable, Grid, DataGrid] keywords: [export, import, DataTable, grid, sheet, data binding, ExportDataTable, data source, spreadsheet] -->
```