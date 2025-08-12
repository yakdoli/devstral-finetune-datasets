```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_099.jpeg
document_name: XlsIO
page_number: 099
page_id: XlsIO#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:48Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Demonstrates how to modify an existing spreadsheet and save the result to a new workbook using XlsIO.
- Illustrates inserting additional data into a worksheet.
- Highlights the process of saving the modified spreadsheet to disk and disposing of the Excel engine.

## Content

### Modifying and Saving a Workbook

The following code snippet demonstrates the process of modifying an existing spreadsheet, inserting additional data, saving the result to a new workbook, and disposing of the Excel engine.

```csharp
' Inserting some additional data.
sheet.Range("A1").Text = "New text that was not present in the template"

' Saving the workbook to disk. This spreadsheet is the result of opening and modifying
' an existing spreadsheet and then saving the result to a new workbook.
workbook.SaveAs("Sample.xls")

' Closing the workbook.
workbook.Close()

' Dispose the Excel engine
excelEngine.Dispose()
```

#### Figure 32: XlsIO with Spreadsheet from Template

![XlsIO with Spreadsheet from Template](https://i.imgur.com/ExampleFigure.png)

The figure shows a modified spreadsheet where the text "New text that was not present in the template" has been inserted into cell A1 of the spreadsheet.

### Reading a Workbook in Read-Only Mode

XlsIO enables opening a spreadsheet in Read-Only mode, even if the spreadsheet is already open in your machine. The following code example illustrates how to do this.

## API Reference

### Methods Used

- `sheet.Range("A1").Text`: Sets the text value of the specified range.
- `workbook.SaveAs`: Saves the workbook to a specific file location.
- `workbook.Close`: Closes the workbook.
- `excelEngine.Dispose`: Disposes of the Excel engine.

## Code Examples

### C# Example

```csharp
// Inserting new data
sheet.Range("A1").Text = "New text that was not present in the template";

// Save the modified workbook
workbook.SaveAs("Sample.xls");

// Close the workbook
workbook.Close();

// Dispose of the Excel engine
excelEngine.Dispose();
```

### VB.NET Example

```vb.net
' Inserting new data
sheet.Range("A1").Text = "New text that was not present in the template"

' Save the modified workbook
workbook.SaveAs("Sample.xls")

' Close the workbook
workbook.Close()

' Dispose of the Excel engine
excelEngine.Dispose()
```

## Cross References

See also:
- [Opening a Spreadsheet in Read-Only Mode](#opening-a-spreadsheet-in-read-only-mode)

### Useful Links

- [Syncfusion XlsIO Documentation](https://www.syncfusion.com/products/file-formats/xlsio)

## RAG Annotations

<!-- tags: [XlsIO, spreadsheet, template, read-only mode] keywords: [insert data, save workbook, dispose engine, open spreadsheet, modify worksheet] -->
```