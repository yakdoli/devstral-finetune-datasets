```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_598.jpeg
document_name: grid
page_number: 598
page_id: grid#page_598
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:43Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to create a `DataTable` in C# and Visual Basic .NET by defining columns and adding rows.
- Uses `DataColumn` and `DataRow` objects to build a structured in-memory database.

## Content

### Creating a `DataTable` in C#

```csharp
// Create the Data Table.
myDataColumn = new DataColumn();
myDataColumn.DataType = System.Type.GetType("System.Int32");
myDataColumn.ColumnName = "id";
myDataTable.Columns.Add(myDataColumn);

// Create a second column.
myDataColumn = new DataColumn();
myDataColumn.DataType = Type.GetType("System.String");
myDataColumn.ColumnName = "item";
myDataTable.Columns.Add(myDataColumn);

// Create new Data Row objects and add to the Data Table.
for (int i = 0; i <= 10; i++)
{
    myDataRow = myDataTable.NewRow();
    myDataRow["id"] = i;
    myDataRow["item"] = "item " + i.ToString();
    myDataTable.Rows.Add(myDataRow);
}
```

### Creating a `DataTable` in VB.NET

```vb
Dim myDataTable As DataTable = New DataTable("MyDataTable")

' Declare the Data Column and Data Row variables.
Dim myDataColumn As DataColumn
Dim myDataRow As DataRow

' Create a new Data Column, set the Data Type and Column Name and add to the Data Table.
myDataColumn = New DataColumn()
myDataColumn.DataType = System.Type.GetType("System.Int32")
myDataColumn.ColumnName = "id"
myDataTable.Columns.Add(myDataColumn)

' Create a second column.
myDataColumn = New DataColumn()
myDataColumn.DataType = Type.GetType("System.String")
myDataColumn.ColumnName = "item"
myDataTable.Columns.Add(myDataColumn)

' Create new Data Row objects and add to the Data Table.
Dim i As Integer
For i = 0 To 10
    myDataRow = myDataTable.NewRow()
```

## API Reference

- **System.Data.DataTable**: Represents a set of data in tabular form. It forms a complete in-memory cache of data and necessary metadata.
  - **Columns**: Collection of `DataColumn` elements that define the table schema.
  - **Rows**: Collection of `DataRow` elements containing data for the table.

### DataColumn Class
- **Property**: `DataType`
  - **Type**: System.Type
  - **Description**: Specifies the data type of the column.
  - **Example Usage**: `myDataColumn.DataType = System.Type.GetType("System.Int32");`

### DataRow Class
- **Indexer**: `[String columnName]`
  - **Type**: Object
  - **Description**: Used to access and set values by column name.
  - **Example Usage**: `myDataRow["id"] = i;`

## Code Examples

### C#
```csharp
DataTable myDataTable = new DataTable();
DataColumn myDataColumn = new DataColumn();
myDataColumn.DataType = System.Type.GetType("System.Int32");
myDataColumn.ColumnName = "id";
myDataTable.Columns.Add(myDataColumn);

myDataColumn = new DataColumn();
myDataColumn.DataType = System.Type.GetType("System.String");
myDataColumn.ColumnName = "item";
myDataTable.Columns.Add(myDataColumn);

for (int i = 0; i <= 10; i++)
{
    DataRow myDataRow = myDataTable.NewRow();
    myDataRow["id"] = i;
    myDataRow["item"] = "item " + i.ToString();
    myDataTable.Rows.Add(myDataRow);
}
```

### VB.NET
```vb
Dim myDataTable As DataTable = New DataTable("MyDataTable")

Dim myDataColumn As DataColumn
myDataColumn = New DataColumn()
myDataColumn.DataType = System.Type.GetType("System.Int32")
myDataColumn.ColumnName = "id"
myDataTable.Columns.Add(myDataColumn)

myDataColumn = New DataColumn()
myDataColumn.DataType = Type.GetType("System.String")
myDataColumn.ColumnName = "item"
myDataTable.Columns.Add(myDataColumn)

Dim myDataRow As DataRow
For i = 0 To 10
    myDataRow = myDataTable.NewRow()
    myDataRow("id") = i
    myDataRow("item") = String.Concat("item ", i)
    myDataTable.Rows.Add(myDataRow)
Next
```

## Cross References
- Refer to the [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms/) for more detailed information on `DataTable`, `DataColumn`, and `DataRow`.

<!-- tags: [syncfusion, windowsforms, datatables, datarows, datacolumns] keywords: [System.Data.DataTable, DataColumn, DataRow, .NET, C#, VB.NET, in-memory database, tabular data, data type, schema, structured data] -->
```