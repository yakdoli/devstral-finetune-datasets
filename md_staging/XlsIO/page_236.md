<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_236.jpeg
document_name: XlsIO
page_number: 236
page_id: XlsIO#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:07Z
fidelity: lossless
-->

## Content

### Example: Creating and Populating an Excel Worksheet

The following example demonstrates how to create an Excel application object, instantiate a workbook, and populate a worksheet with data.

#### Code Example

```csharp
// Step 2: Instantiate the Excel application object.
IApplication application = excelEngine.Excel;
application.DefaultVersion = ExcelVersion.Excel2010;

// The first worksheet object in created.
IWorkbook workbook = application.Workbooks.Create(1);
IWorksheet sheet = workbook.Worksheets[0];

// Insert the data in sheet-1.
sheet.Range["B1"].Text = "Product-A";
sheet.Range["C1"].Text = "Product-B";
sheet.Range["D1"].Text = "Product-C";
sheet.Range["E1"].Text = "Product-D";
sheet.Range["A2"].Text = "Jan";
sheet.Range["A3"].Text = "Feb";
sheet.Range["A4"].Text = "Mar";
sheet.Range["A5"].Text = "Apr";
sheet.Range["A6"].Text = "May";
sheet.Range["B2"].Number = 25;
sheet.Range["B3"].Number = 20;
sheet.Range["B4"].Number = 35;
sheet.Range["B5"].Number = 67;
sheet.Range["B6"].Number = 23;
sheet.Range["C2"].Number = 35;
sheet.Range["C3"].Number = 25;
sheet.Range["C4"].Number = 14;
sheet.Range["C5"].Number = 78;
sheet.Range["C6"].Number = 45;
sheet.Range["D2"].Number = 40;
sheet.Range["D3"].Number = 55;
sheet.Range["D4"].Number = 51;
sheet.Range["D5"].Number = 89;
sheet.Range["D6"].Number = 64;
sheet.Range["E2"].Number = 67;
```

## API Reference

### Classes and Methods Used
- **`IApplication`**: Represents the Excel application object.
- **`Excel`**: Accesses the Excel engine.
- **`IWorkbook`**: Represents a workbook.
- **`Workbooks`**: Collection of workbooks.
- **`IWorksheet`**: Represents a worksheet.
- **`Worksheets`**: Collection of worksheets.
- **`Range`**: Represents a range of cells.
- **`Text`**: Sets the text value of a cell.
- **`Number`**: Sets the numeric value of a cell.

### Return Type
The example demonstrates how to populate an Excel worksheet, but it does not explicitly return any value. The focus is on setting the state of the worksheet by assigning text and numeric values to the cells.

## Code Examples

The provided code example illustrates the following:
1. Instantiating the Excel application object and setting its version.
2. Creating a workbook and accessing the first worksheet.
3. Assigning text and numeric values to specific cells of the worksheet.

## Cross References

For more detailed information on working with Excel using Syncfusion Winforms, refer to the official Syncfusion documentation:

- **Syncfusion XlsIO Documentation**: [https://help.syncfusion.com/xlsio/overview](https://help.syncfusion.com/xlsio/overview)

<!-- tags: [XlsIO, Excel, IApplication, IWorkbook, IWorksheet, Range, Text, Number, workbook creation, cell population, version setting] keywords: [Syncfusion, Winforms, XlsIO, Excel application, worksheet, range, text, number, assign, assign value, populate, cell, create, version, Excel 2010] -->