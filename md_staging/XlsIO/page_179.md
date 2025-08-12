```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_179.jpeg
document_name: XlsIO
page_number: 179
page_id: XlsIO#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:52Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Describes how to delete unwanted cells, rows, and columns in a spreadsheet using MS Excel and XlsIO.
- Explains the use of the `Clear` method in XlsIO for cell deletion.
- Lists options to delete rows and columns directly in Excel.

## Content

### Deleting Cells, Rows, and Columns in Excel
It is often necessary to delete unwanted cells, rows, and columns in a spreadsheet when you want to manipulate cells. MS Excel provides various options to delete cells, rows, and columns. You can delete a cell by right-clicking on it and selecting the **Delete** option from the context menu. On selecting the **Delete** option, the **Delete** dialog box prompts for an option to be selected, as shown in the following screenshot.

![Figure 59: Delete Dialog Box in Excel](https://example.com/image.png)

### Deleting Cells in XlsIO
To delete a cell in XlsIO, you can make use of the **Clear** method. The following code examples demonstrate this:

```csharp
[C#]
// Shifts cell left after deletion.
mySheet.Range["Al:E1"].Clear(ExcelMoveDirection.MoveLeft);

// Shifts cell up after deletion.
mySheet.Range["Al:A6"].Clear(ExcelMoveDirection.MoveUp);
```

```vb.net
[VB.NET]
' Shifts cell left after deletion.
mySheet.Range("Al:E1").Clear(ExcelMoveDirection.MoveLeft)

' Shifts cell up after deletion.
mySheet.Range("Al:A6").Clear(ExcelMoveDirection.MoveUp)
```

### Delete Rows and Columns
MS Excel allows you to delete rows and columns in a spreadsheet by selecting and deleting the rows or columns through the context menu that appears on right-clicking.

## API Reference

### Methods
- `Clear(ExcelMoveDirection.MoveLeft)`
- `Clear(ExcelMoveDirection.MoveUp)`

## Code Examples

### C#
```csharp
[C#]
// Example of shifting cells left after deletion.
mySheet.Range["Al:E1"].Clear(ExcelMoveDirection.MoveLeft);

// Example of shifting cells up after deletion.
mySheet.Range["Al:A6"].Clear(ExcelMoveDirection.MoveUp);
```

### VB.NET
```vb.net
[VB.NET]
' Example of shifting cells left after deletion.
mySheet.Range("Al:E1").Clear(ExcelMoveDirection.MoveLeft)

' Example of shifting cells up after deletion.
mySheet.Range("Al:A6").Clear(ExcelMoveDirection.MoveUp)
```

## Cross References
See also:  
- [Overview of Excel Operations in XlsIO](#overview-of-excel-operations-in-xlsio)
- [Managing Rows and Columns in Excel](#managing-rows-and-columns-in-excel)

<!-- tags: [XlsIO, MS Excel, cell deletion, row deletion, column deletion, Clear method, ExcelMoveDirection] keywords: [delete, cells, rows, columns, context menu, options, ExcelMoveDirection] -->
```