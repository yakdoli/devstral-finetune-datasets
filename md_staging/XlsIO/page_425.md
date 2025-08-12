<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_425.jpeg
document_name: XlsIO
page_number: 425
page_id: XlsIO#page_425
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:47Z
fidelity: lossless
-->

# Essential XlsIO

```vb
' Workbook is accessed.
Dim DestinationWorksheet As Syncfusion.XlsIO.IWorkbook = DestinationWorkbook.Worksheets(0)

' Assigning an object to the range of cells (90 rows) both for source and destination.
Dim source As Syncfusion.XlsIO.IRange = SourceWorksheet.Range(1, 1, 90, 100)
Dim des As Syncfusion.XlsIO.IRange = DestinationWorksheet.Range(1, 1, 90, 100)

' Copying (90 rows) from Source to Destination worksheet.
source.CopyTo(des)
```

## 5.1.4 How to ignore the green error marker in worksheets?

You can ignore the error marker that appears in cells, when there exists data that are of different formats. This can be done by using the ExcelIgnoreError enumerator that provides various options to ignore the error marker.

### C#

```csharp
// Ignore Error Options.
sheet.Range["B3"].IgnoreErrorOptions = ExcelIgnoreError.All;
```

### VB.NET

```vb
' Ignore Error Options.
sheet.Range("B3").IgnoreErrorOptions = ExcelIgnoreError.All
```

![Figure 163: To ignore error](attachment:Figure_163_Ignore_Error.png)

## Page-level Navigation/TOC (if applicable)
- **Section 5.1.4**: How to ignore the green error marker in worksheets?

## Cross References
- See also: Section 5.1.3: Working with error markers in Excel cells.

<!-- tags: [XlsIO, error markers, ExcelIgnoreError, C#, VB.NET, green error marker, Syncfusion Winforms, 11.4.0.26] keywords: [ignoring error markers, error checking options, workbook copy, cell range, ExcelIgnoreError, error marker, green error marker, source and destination worksheets] -->