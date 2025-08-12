```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: XlsIO
page_number: 065
page_id: XlsIO#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:39Z
fidelity: lossless
-->

# 3.6 Spreadsheet

A spreadsheet is a grid that organizes data into columns and rows. Spreadsheets make it easy to display information, and people can insert formulas to work with the data. This section covers the following topics:

## 3.6.1 Excel Engine

ExcelEngine class provides access to IApplication interface that represents an Excel application. This class has the Dispose method, which is responsible for disposing of the objects after closing the workbook.

### Public Properties

The following table lists the public properties and their corresponding descriptions of ExcelEngine class:

| Properties            | Description                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Excel                 | Interface to the XlsIO Application which gives access to all supported functions.                                                                                                                                                                                                                                                                                           |
| ThrowNotSavedOnDestroy | Dispose will throw an ExcelWorkbookNotSaved exception when the workbook is not saved and this property is set to True. Default value is False.                                                                                                                                                                                                                                  |
| ActiveCell            | Returns a range object that represents the active cell in the active window (the window on top) or in the specified window. If the window isn't displaying a worksheet, this property fails. It is a Read-Only property.                                                                                                                    |
| ActiveSheet           | Returns an object that represents the active sheet (the sheet on top) in the active workbook or in the specified window or workbook. Returns nothing if no sheet is active. It is a Read-Only property.                                                                                                         |

## API Reference (if applicable)

### Summary
- **Excel**: Interface to the XlsIO Application, providing access to all supported functions.
- **ThrowNotSavedOnDestroy**: Property to control whether Dispose throws an ExcelWorkbookNotSaved exception when the workbook is not saved.
- **ActiveCell**: A Read-Only property that returns the active cell in the current window or specified window.
- **ActiveSheet**: A Read-Only property that returns the active sheet in the current workbook or specified window.

### Cross References
- For more information on Dispose method and exception handling, see the documentation for ExcelWorkbookNotSaved.

<!-- tags: [XlsIO, ExcelEngine, IApplication, Dispose, Public Properties, Excel, ThrowNotSavedOnDestroy, ActiveCell, ActiveSheet] keywords: [spreadsheet, grid, columns, rows, formulas, Excel, ActiveWindow, ActiveWorkbook, properties, read-only, Dispose method, exception handling] -->
```