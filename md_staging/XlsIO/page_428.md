```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_428.jpeg
document_name: XlsIO
page_number: 428
page_id: XlsIO#page_428
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:50Z
fidelity: lossless
-->

# Essential XlsIO

However, there is often a need to protect only certain cells in a worksheet. In this scenario, you need to protect a worksheet, and set the `IsLocked` property to `false` for the cells that need to be made editable.

## Protecting Specific Cells

[C#]

```csharp
// Sample data
sheetOne.Range["A1:K20"].Text = "Locked";

// A1:A10 will not be protected.
sheetOne.Range["A1:A10"].CellStyle.Locked = false;
sheetOne.Range["A1:A10"].Text = "UnLocked";
sheetOne.Protect("syncfusion", ExcelSheetProtection.FormattingColumns);
```

[VB.NET]

```vb
' Sample data
Private sheetOne.Range("A1:K20").Text = "Locked"

' A1:A10 will not be protected.
Private sheetOne.Range("A1:A10").CellStyle.Locked = False
Private sheetOne.Range("A1:A10").Text = "UnLocked"
sheetOne.Protect("syncfusion", ExcelSheetProtection.FormattingColumns)
```

>Note: Locking/Unlocking cells in an unprotected worksheet has no effect.

## 5.1.9 How to save a file to stream?

XlsIO provides support to save a spreadsheet to a .NET stream. The following code example illustrates this.

[C#]

```csharp
// Save the workbook to stream.
FileStream fs = new FileStream("FileStreamSample.xls", FileMode.Create,
 FileAccess.ReadWrite, FileShare.ReadWrite);
workbook.SaveAs(fs);
workbook.Close();
```

[VB.NET]

```vb
' Sample data
Private sheetOne.Range("A1:K20").Text = "Locked"

' A1:A10 will not be protected.
Private sheetOne.Range("A1:A10").CellStyle.Locked = False
Private sheetOne.Range("A1:A10").Text = "UnLocked"
sheetOne.Protect("syncfusion", ExcelSheetProtection.FormattingColumns)
```

```html
<!-- tags: [XlsIO, protecting cells, saving to stream] keywords: [cells, lock, unlock, worksheet, stream, Syncfusion, XlsIO, workbook, saveas, filestream] -->
```