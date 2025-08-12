```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_552.jpeg
document_name: grid
page_number: 552
page_id: grid#page_552
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
Dim myValue as Object = Me.GridDataBoundGrid1(row, col).CellValueget value at row, col
```

If you want to retrieve the values that are based on column names, use the methods in the `GridDataBoundGrid.Binder` object to switch the name for a column index.

### C#

```csharp
// Specify the field name.
int nField = this.gridDataBoundGrid1.Binder.NameToField("FirstName");

// Call Binder.FieldToColIndex method to retrieve the column index for the ColumnName specified.
int col = this.gridDataBoundGrid1.Binder.FieldToColIndex(nField);

// Get Value at (row, col).
object myValue = this.gridDataBoundGrid1[row, col].CellValue;
```

### VB.NET

```vb
' Specify the field name.
Dim nField As Integer = Me.gridDataBoundGrid1.Binder.NameToField("FirstName")

' Call Binder.FieldToColIndex method to retrieve the column index for the ColumnName specified.
Dim col As Integer = Me.gridDataBoundGrid1.Binder.FieldToColIndex(nField)

' Get Value at (row, col).
Dim myValue As Object = Me.gridDataBoundGrid1(row, col).CellValue
```

## 4.2.2.4 Using the CurrencyManager

Sometimes the grid itself will not contain all the data in the data table. For example, your data table may have 12 columns in it, but you are able to add only three `GridBoundColumns` to display exactly three of the twelve columns. In this case, the table has nine more columns than the grid. How do you get all the values in the columns that are not in the grid?

### 

### 
<!-- tags: [syncfusion, winforms, essential grid, currencymanager, gridboundcolumns, table Trafficking] keywords: [data retrieval, column indexing, gridboundcolumns, currencymanager, windows forms] -->
```