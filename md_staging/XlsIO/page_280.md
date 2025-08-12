```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_280.jpeg
document_name: XlsIO
page_number: 280
page_id: XlsIO#page_280
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:14Z
fidelity: lossless
-->

## Essential XlsIO

```csharp
colField.Items(0).Visible = False
colField.Items(1).Visible = False

'Apply built-in style.
pivotTable.BuiltInStyle = PivotBuiltInStyles.PivotStyleMedium2

'Activate the pivot worksheet.
pivotSheet.Activate()

'Save the workbook to disk.
workbook.SaveAs("PivotTable.xlsx")

'Close the workbook.
workbook.Close()

'No exception will be thrown if there are unsaved workbooks.
excelEngine.ThrowNotSavedOnDestroy = False
excelEngine.Dispose()
```

### WinForms-specific conventions
- The code snippet above demonstrates basic operations within a WinForms application using the ExcelEngine API from Syncfusion.
- It involves hiding specific items, applying styles, activating sheets, saving the workbook, closing the workbook, and disposing of the engine. This sequence is typical for managing Excel interactivity and file handling in a WinForms environment.

## API Reference
- **ExcelEngine**
  - Properties:
    - `ThrowNotSavedOnDestroy`: A boolean property that determines whether an exception will be thrown for unsaved workbooks upon disposal.
  - Methods:
    - `Dispose()`: Releases all resources used by the ExcelEngine.

## Code Examples

### Example: Managing a PivotTable in Excel

#### C#

```csharp
// Assuming colField, pivotTable, pivotSheet, and workbook are properly initialized
colField.Items(0).Visible = False;
colField.Items(1).Visible = False;

// Apply a built-in style to the pivot table
pivotTable.BuiltInStyle = PivotBuiltInStyles.PivotStyleMedium2;

// Activate the pivot worksheet
pivotSheet.Activate();

// Save the workbook to disk
workbook.SaveAs("PivotTable.xlsx");

// Close the workbook
workbook.Close();

// Prevent an exception for unsaved workbooks during disposal
excelEngine.ThrowNotSavedOnDestroy = False;

// Dispose of the ExcelEngine resources
excelEngine.Dispose();
```

#### VB.NET

```vb
' Assuming colField, pivotTable, pivotSheet, and workbook are properly initialized
colField.Items(0).Visible = False
colField.Items(1).Visible = False

' Apply a built-in style to the pivot table
pivotTable.BuiltInStyle = PivotBuiltInStyles.PivotStyleMedium2

' Activate the pivot worksheet
pivotSheet.Activate()

' Save the workbook to disk
workbook.SaveAs("PivotTable.xlsx")

' Close the workbook
workbook.Close()

' Prevent an exception for unsaved workbooks during disposal
excelEngine.ThrowNotSavedOnDestroy = False

' Dispose of the ExcelEngine resources
excelEngine.Dispose()
```

## RAG Annotations
<!-- tags: [ExcelEngine, PivotTable, WinForms, XlsIO, SaveAs, Dispose] keywords: [Unsaved workbooks, Exception handling, Built-in styles, Pivot worksheet activation, Workbook save, Resource disposal, C#, VB.NET] -->
```