```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: XlsIO
page_number: 199
page_id: XlsIO#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:17Z
fidelity: lossless
-->

## XlsIO

### Overview
- Demonstrates how to manipulate worksheets in Excel documents using XlsIO.
- Includes opening, copying, saving, and closing Excel workbooks.
- Explanation of methods to move worksheets within a workbook.

### Content

#### Copying a Worksheet

```csharp
// Close the workbook.
destinationWorkbook.Close();
```

```vb
' Open the Source WorkBook.
Dim sourceWorkbook As IWorkbook = 
application.Workbooks.Open("...\\...\\...\\Data\\SourceWorkbookTemplate.xls")

' Open the Destination WorkBook.
Dim destinationWorkbook As IWorkbook = 
application.Workbooks.Open("...\\...\\...\\Data\\DestinationWorkbookTemplate.xls")

' Copy the first worksheet from the Source workbook to the destination
' workbook with data validations.
destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets(0), 
ExcelWorksheetCopyFlags.CopyDataValidations)

' Activate the newly added worksheet in the destination workbook.
destinationWorkbook.ActiveSheetIndex = 1

' Saving the workbook to disk.
destinationWorkbook.SaveAs("Sample.xls")

' Close the workbook.
destinationWorkbook.Close()
```

You can also copy a worksheet before and after a particular worksheet by using the `AddCopyBefore` and `AddCopyAfter` methods respectively.

#### Moving a Worksheet

XlsIO also allows moving worksheets from one position to another. This is similar to dragging a worksheet in MS Excel. This can be performed by using the `Move` method. Following code example illustrates how a worksheet is moved to the 2nd position.

```csharp
sheet.Move(2);
```

```vb
[VB.NET]
```

### API Reference

- **Methods**: `Open`, `AddCopy`, `SaveAs`, `Close`
- **Flags**: `ExcelWorksheetCopyFlags.CopyDataValidations`
- **Properties**: `ActiveSheetIndex`

### Code Examples

C# Example:
```csharp
destinationWorkbook.Close();
```

VB.NET Example:
```vb
' Open the Source WorkBook.
Dim sourceWorkbook As IWorkbook = 
application.Workbooks.Open("...\\...\\...\\Data\\SourceWorkbookTemplate.xls")
```

### Page-level Navigation/TOC (if applicable)
- [unclear]

### Cross References
See also: Excel worksheet manipulation, data validations, workbook management.

<!-- tags: XlsIO, Excel, worksheet manipulation, data validations, workbook management keywords: copy, move, worksheet, Excel, workbook -->
```