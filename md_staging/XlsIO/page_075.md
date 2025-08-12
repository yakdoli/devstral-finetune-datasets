```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: XlsIO
page_number: 075
page_id: XlsIO#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:57Z
fidelity: lossless
-->

# Overview

- This page provides a list of methods and their descriptions available for working with Excel worksheets using the XlsIO library in Syncfusion Winforms.
- Methods for autofitting columns and rows, clearing data, column width conversion, copying data to clipboard, deleting rows or columns, exporting data as a data table, and various other operations are detailed here.
- These methods allow for efficient manipulation and formatting of Excel data within applications.

## Content

### Methods and their Descriptions

| **Method**                    | **Description**                                                                                       |
|-------------------------------|-------------------------------------------------------------------------------------------------------|
| AutofitColumn                 | Autofits specified column.                                                                           |
| AutofitRow                    | Autofits specified row.                                                                              |
| Clear                         | Clears worksheet data. Removes all formatting and merges.                                            |
| ClearData                     | Clears worksheet. Only the data is removed from each cell.                                          |
| ColumnWidthToPixels           | Converts column width into pixels.                                                                   |
| CopyToClipboard               | Copies worksheet into the clipboard.                                                                 |
| CreateRangesCollection        | Creates new instance of IRanges and groups different ranges.                                        |
| CreateTemplateMarkersProcessor| Creates object that can be used for template markers processing.                                     |
| DeleteColumn                  | Removes specified column (with formulas update).                                                     |
| DeleteRow                     | Removes specified row (with formulas update).                                                        |
| ExportDataTable               | Exports sheet data as data table.                                                                    |
| FindAll                       | Finds all matching data.                                                                             |
| FindFirst                     | Finds the first data that matches the constraint.                                                   |
| GetBoolean                    | Gets bool value from the cell.                                                                       |
| GetColumnWidth                | Returns width from ColumnInfoRecord if there is corresponding ColumnInfoRecord or StandardWidth if not. |
| GetColumnWidthInPixels        | Returns width in pixels from ColumnInfoRecord if there is corresponding ColumnInfoRecord or StandardWidth if not. |
| GetDefaultColumnStyle         | Returns default column style.                                                                        |
| GetDefaultRowStyle            | Returns default row style.                                                                           |
| GetError                      | Gets error value from cell.                                                                          |

### Usage Example

The methods listed here can be utilized programmatically in C# to manipulate Excel worksheets efficiently. For example:

```csharp
using Syncfusion.XlsIO;

public void ExampleUsage()
{
    // Create a new workbook instance
    Workbook workbook = new Workbook();
    IWorksheet sheet = workbook.Worksheets[0];

    // Autofit a specified column
    sheet.AutoFitColumn(1);

    // Clear all data and formatting from the worksheet
    sheet.Clear();

    // Copy the worksheet to the clipboard
    sheet.CopyToClipboard();

    // Export sheet data as a data table
    DataTable dataTable = sheet.ExportDataTable();
}
```

### Cross References

- Refer to the [Syncfusion XlsIO Documentation](https://help.syncfusion.com/xlsio/overview) for more detailed information and examples.
- For additional methods and properties, see the [Syncfusion XlsIO API Reference](https://help.syncfusion.com/xlsio/api).

### Notes
- Ensure that the appropriate namespaces and assemblies are included when using these methods in your project.
- Always handle exceptions appropriately to manage potential errors during execution.

## RAG Annotations

<!-- tags: [xlsio, syncfusion winforms, worksheet manipulation, methods, data handling] keywords: [autofit, clear, export, delete, find, column width, row style, default styles, error handling, csharp example] -->
```