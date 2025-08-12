```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_196.jpeg
document_name: XlsIO
page_number: 196
page_id: XlsIO#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:56Z
fidelity: lossless
-->

# Essential XlsIO

## Sheet Organization

Excel has options to consolidate data from different worksheets, or move a sheet to another workbook, or insert a sheet in between the worksheets. Also, the sheet tab color can be formatted, and the sheets can be named as per the users' needs. This section explains how sheets can be organized. Below sections explain the XlsIO's ability to organize sheets.

- **Copy/Move Worksheet**  
  This section explains how a worksheet can be copied from another worksheet with or without certain formatting.
- **Sheet Format**  
  This section explains various formats that can be applied to a sheet.

### 4.1.3.3.1 Copy/Move Worksheet

When you copy/move rows and columns, Microsoft Excel copies or moves all the data that it contains, including formulas and their resulting values, comments, cell formats, and hidden cells.

#### Copying Worksheets

Copying worksheets can be internal or external. XlsIO provides support for copying a worksheet within a workbook, and also from one workbook to another. This feature can be used to merge together several workbooks. Following code example illustrates how to copy a sheet with its entire contents to another sheet.

```csharp
[C#]

// Open the Source WorkBook.
IWorkbook sourceWorkbook =
    application.Workbooks.Open(@"...\.resources\Data\SourceWorkbookTemplate.xls");

// Open the Destination WorkBook.
IWorkbook destinationWorkbook =
    application.Workbooks.Open(@"...\.resources\Data\DestinationWorkbookTemplate.xls");

// Copy the first worksheet from the Source workbook to the destination workbook.
destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets[0]);

// Activate the newly added worksheet in the destination workbook.
destinationWorkbook.ActiveSheetIndex = 1;
```

## Page-level Navigation/TOC (if applicable)
- This page provides documentation on organizing sheets in Excel using XlsIO, covering:
  - Copying and moving worksheets within or between workbooks.
  - Formatting options for sheets.

### WinForms-specific conventions
- This section specifically uses C# language syntax for code examples, adhering to Syncfusion conventions for formatting and structuring.

<!-- tags: [XlsIO, Sheet Organization, Copy/Move Worksheet, Sheet Format, Microsoft Excel, Syncfusion, C#] keywords: [XlsIO, Excel, Workbooks, Sheets, Copy Move, Formatting, Integration, Documentation, Programming, C#] -->
```