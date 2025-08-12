```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_284.jpeg
document_name: edit
page_number: 284
page_id: edit#page_284
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:04Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
' Converting the VirtualPoints to ParsePoints.
Dim startParsePoint As New ParsePoint(startVirtualPoint.Y, 
startVirtualPoint.X, 0)
Dim endParsePoint As New ParsePoint(endVirtualPoint.Y, endVirtualPoint.X, 0)

' Creating the associated CoordinatePoints that indicate the text range.
Dim startCoordinatePoint As New 
CoordinatePoint(TryCast(Me.editControl1.Parser, ILexemParser), 
startParsePoint, startVirtualPoint.Y, startVirtualPoint.X, True)
Dim endCoordinatePoint As New CoordinatePoint(TryCast(Me.editControl1.Parser, 
ILexemParser), endParsePoint, endVirtualPoint.Y, endVirtualPoint.X, True)
```

## 5.5 How To Data Bind an Edit Control To a Datasource

The following code snippet illustrates how an Edit Control can be data-bound to a table in a DataSet.

```csharp
[C#]

// Create a new DataSet.
this.dataset = new DataSet("MyDataSet");

// Create a new DataTable.
this.table = new DataTable("MyDataTable");

// Create a new DataColumn and add it to the DataTable.
this.datacolumn = new DataColumn("Code", 
System.Type.GetType("System.String"));
this.table.Columns.Add(this.datacolumn);

// Create a new DataRow, and assign it to the specific column.
// Assign a string value 'program' to that DataRow-DataColumn field.
this.datarow = this.table.NewRow();
this.datarow[this.datacolumn] = program;

// Add this DataRow to the DataTable.
this.table.Rows.Add(this.datarow);

// Add this DataTable to the DataSet.
this.dataset.Tables.Add(this.table);

// Databinding EditControl.Text to the DataColumn "Code",
// where "Code" contains the program to be displayed in the EditControl.
```

## Page-level Navigation/TOC (if applicable)

This page demonstrates how to bind an edit control to a datasource in Windows Forms using Syncfusion components. It provides example code in C# for creating a dataset, data table, and data column, as well as adding data and performing data binding.

### Overview
- **1.** Understanding the process of data binding an edit control to a data source.
- **2.** Creating a dataset, table, and column in C#.
- **3.** Demonstrating how to assign data and bind it to an edit control.

### WinForms-specific conventions
- **Namespace:** `TabPage` is used for handling edit controls.
- **EditControl** class handling text editing and binding.
- **Data Handling:** Utilizes `DataSet`, `DataTable`, and `DataColumn` for data binding.

### API Reference (if applicable)
- **Methods:** `Add`, `NewRow`, `GetType`, `TryCast`.

### Code Examples (multi-language supported)
The code above demonstrates the use of C# for creating a dataset, handling data columns and rows, and binding them to edit controls.

### Cross References
- **See also:** Data binding and handling in Windows Forms controls.
  
### RAG Annotations
<!-- tags: [Windows Forms, Data Binding, Syncfusion, edit control, DataSet, DataTable, DataColumn] keywords: [data binding, edit control, dataset, table, column, C#, DataRow, WinForms] -->
```