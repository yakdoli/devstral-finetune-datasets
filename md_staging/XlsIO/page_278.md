```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_278.jpeg
document_name: XlsIO
page_number: 278
page_id: XlsIO#page_278
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:56Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### Sample Code

```csharp
rowField.PivotFilters.Add(PivotFilterType.CaptionEqual, null, "East", null);

// Apply column field label based filter.
IPivotField colField = pivotTable.Fields[3];

colField.Items[0].Visible = false;
colField.Items[1].Visible = false;

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

### VB Example

```vb
' Step 1: Instantiate the spreadsheet creation engine.
Dim excelEngine As New ExcelEngine()
' Step 2: Instantiate the excel application object.
Dim application As IApplication = excelEngine.Excel

' Set the default version as Excel 2010.
```

### Purpose

This code snippet demonstrates how to work with pivot tables in an Excel workbook using the XlsIO library. It includes steps to apply filters to the pivot table fields, set a built-in style, activate the pivot sheet, save the workbook, and dispose of the ExcelEngine object properly.

### Summary

- **Filtering Pivot Fields:** The code applies a filter to show only rows where the label is equal to "East" in the specified pivot field.
- **Column Label Filtering:** It also hides specific items in a column field to refine the view.
- **Style Application:** A built-in style is applied to the pivot table for better presentation.
- **Workbook Management:** The workbook is saved, closed, and disposed of without throwing exceptions for unsaved changes.

## API Reference

### Namespace: Syncfusion.XlsIO

#### Classes

- **PivotFilterType:** Enum used for defining the type of pivot filter to apply.
  - **CaptionEqual:** Represents a filter that matches captions based on equality.
- **IPivotField:** Represents a pivot field in a pivot table.
  - **Items:** Collection of items in the pivot field.
    - **Visible:** Property to set the visibility of a specific item.
- **PivotBuiltInStyles:** Enum representing the built-in styles for pivot tables.
  - **PivotStyleMedium2:** A predefined style for pivot tables.
- **ExcelEngine:** Managing the Excel environment.
  - **Application:** Property providing access to the Excel application object.
  - **ThrowNotSavedOnDestroy:** Property to control whether an exception is thrown when disposing of an unsaved workbook.
  - **Dispose():** Method to release all the resources used by the ExcelEngine.

### Members

#### Methods

- **PivotFilters.Add(PivotFilterType type, null, String value, null):**
  - Applies a pivot filter based on the specified type, using the provided value.
  - **Parameters:**
    - `type`: Type of the pivot filter.
    - `value`: Value to match against for the filter.
  - **Returns:** An instance of the filter added.

#### Properties

- **PivotBuiltInStyle:** Assigns a built-in style to the pivot table.
- **Items.Visible:** Sets whether a specific pivot item is visible in the table.
- **ThrowNotSavedOnDestroy:** Gets or sets whether an exception should be thrown when disposing of unsaved workbooks.

## Code Examples

### C#

```csharp
IPivotField rowField = pivotTable.Fields[0];
rowField.PivotFilters.Add(PivotFilterType.CaptionEqual, null, "East", null);

IPivotField colField = pivotTable.Fields[3];
colField.Items[0].Visible = false;
colField.Items[1].Visible = false;

pivotTable.BuiltInStyle = PivotBuiltInStyles.PivotStyleMedium2;
pivotSheet.Activate();
workbook.SaveAs("PivotTable.xlsx");
workbook.Close();
excelEngine.ThrowNotSavedOnDestroy = false;
excelEngine.Dispose();
```

### VB

```vb
Dim rowField As IPivotField = pivotTable.Fields(0)
rowField.PivotFilters.Add(PivotFilterType.CaptionEqual, Nothing, "East", Nothing)

Dim colField As IPivotField = pivotTable.Fields(3)
colField.Items(0).Visible = False
colField.Items(1).Visible = False

pivotTable.BuiltInStyle = PivotBuiltInStyles.PivotStyleMedium2
pivotSheet.Activate()
workbook.SaveAs("PivotTable.xlsx")
workbook.Close()
excelEngine.ThrowNotSavedOnDestroy = False
excelEngine.Dispose()
```

## See also

- [Working with Pivot Tables](#working-with-pivot-tables)
- [Saving Excel Workbooks](#saving-excel-workbooks)
- [Managing Excel Resources](#managing-excel-resources)

<!-- tags: [xlsio, pivot tables, filters, built-in styles, workbook management] keywords: [pivot filters, column labels, visibility, built-in styles, worksheet activation, save, close, dispose, unsaved workbooks] -->
```