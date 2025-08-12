```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: XlsIO
page_number: 067
page_id: XlsIO#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:20Z
fidelity: lossless
-->

# Essential XlsIO

| Property                  | Description                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PathSeparator             | Returns the path separator character ("\\"). It is a Read-Only property.                                                                                                                                                                                                                                                  |
| Range                     | Returns a Range object that represents a cell or a range of cells.                                                                                                                                                                                                                                                         |
| RowSeparator             | Gets/sets row separator for array parsing.                                                                                                                                                                                                                                                                                 |
| SheetsInNewWorkbook      | Returns or sets the number of sheets that Microsoft Excel automatically inserts into new workbooks.                                                                                                                                                                                                                       |
| StandardFont              | Returns or sets the name of the standard font.                                                                                                                                                                                                                                                                             |
| StandardFontSize         | Returns or sets the standard font size, in points.                                                                                                                                                                                                                                                                         |
| StandardHeight            | Returns or sets the standard (default) height of all the rows in the worksheet, in points. This value is used only for newly created worksheets.                                                                                                                                                                          |
| StandardHeightFlag       | Returns or sets the standard (default) height option flag, which defines that standard (default) row height and book default font height do not match. This value is used only for newly created worksheets.                                                                                                                |
| StandardWidth            | Returns or sets the standard (default) width of all the columns in the worksheet. This value is used only for newly created worksheets.                                                                                                                                                                                     |
| ThousandsSeparator        | Sets or returns the character used for the thousands separator as a String.                                                                                                                                                                                                                                               |
| UseNativeOptimization     | Indicates to use unsafe code.                                                                                                                                                                                                                                                                                              |
| UseNativeStorage          | Indicates whether we should use native storage (standard windows COM object) or .NET implementation to open Excel 97-2003 files. This .NET storage doesn't depend on windows APIs and are developed with fully managed code. By default, it is set to true [uses native storage]. |
| UserName                  | Returns or sets the name of the current user.                                                                                                                                                                                                                                                                             |

## API Reference
- **Namespace**: `Syncfusion.XlsIO`
- **Class**: `XlsIO`
- **Properties**:
  - `PathSeparator`: Returns the path separator character.
  - `Range`: Returns a `Range` object representing a cell or a range of cells.
  - `RowSeparator`: Gets/sets the row separator for array parsing.
  - `SheetsInNewWorkbook`: Returns or sets the number of sheets in a new workbook.
  - `StandardFont`: Returns or sets the name of the standard font.
  - `StandardFontSize`: Returns or sets the standard font size.
  - `StandardHeight`: Returns or sets the standard height of rows.
  - `StandardHeightFlag`: Returns or sets the flag indicating if default row height and font height match.
  - `StandardWidth`: Returns or sets the standard width of columns.
  - `ThousandsSeparator`: Returns or sets the character for the thousands separator.
  - `UseNativeOptimization`: Indicates whether to use unsafe code.
  - `UseNativeStorage`: Indicates whether to use native storage or .NET implementation for Excel 97-2003 files.
  - `UserName`: Returns or sets the name of the current user.

<!-- tags: [XlsIO, API Reference, WinForms, Excel, Data Handling] keywords: [PathSeparator, Range, RowSeparator, SheetsInNewWorkbook, StandardFont, StandardFontSize, StandardHeight, StandardHeightFlag, StandardWidth, ThousandsSeparator, UseNativeOptimization, UseNativeStorage, UserName] -->
```