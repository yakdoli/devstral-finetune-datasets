```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_274.jpeg
document_name: XlsIO
page_number: 274
page_id: XlsIO#page_274
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:42Z
fidelity: lossless
-->

## Applying Built-In Styles and Saving Workbooks

### C#

```csharp
// Apply built-in style.
pivotTable.BuiltInStyle = PivotBuiltInStyles.PivotStyleMedium2;

// Activate the pivot worksheet.
pivotSheet.Activate();

// Save the workbook to disk.
workbook.SaveAs("PivotTable.xlsx");

// Close the workbook.
workbook.Close();

// No exception will be thrown if there are unsaved workbooks.
excelEngine.ThrowNotSavedOnDestroy = false;
excelEngine.Dispose();
```

### VB

```vb
' Step 1: Instantiate the spreadsheet creation engine.
Dim excelEngine As New ExcelEngine()

' Step 2: Instantiate the excel application object.
Dim application As IApplication = excelEngine.Excel

' Set the default version as Excel 2010.
application.DefaultVersion = ExcelVersion.Excel2010

' Get the path of input file.
Dim workbook As IWorkbook = application.Workbooks.Open("PivotCodeDate.xlsx")

' The first worksheet object in the worksheets collection is accessed.
Dim worksheet As IWorksheet = workbook.Worksheets(0)
```

## Code Examples

The above code snippets demonstrate how to:

1. **Apply a Built-In Style to a Pivot Table:**
   - Includes setting the built-in style.
2. **Activate the Pivot Worksheet:**
   - Focuses on activating the pivot worksheet tab.
3. **Save the Workbook:**
   - Shows saving the workbook to disk.
4. **Close and Dispose of the Excel Engine:**
   - Ensures proper cleanup and handling of unsaved workbooks.

## Summary

This section provides examples of how to apply styles to pivot tables, manage workbook files, and ensure proper disposal of ExcelEngine objects to avoid exceptions when working with Syncfusion's XlsIO API for Excel manipulation.

<!-- tags: [Syncfusion, Winforms, XlsIO, Excel, ExcelEngine, PivotTable, BuiltInStyle, WorkbookHandling, CodeExamples] keywords: [XlsIO, Excel, BuiltInStyle, PivotTable, Dispose, Save, Close] -->
```