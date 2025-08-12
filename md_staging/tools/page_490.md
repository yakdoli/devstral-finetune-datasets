```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_490.jpeg
document_name: tools
page_number: 490
page_id: tools#page_490
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the creation and manipulation of a dataset in a Windows Forms application.
- Explains how to bind the dataset to a DataGrid control and a DateTimePickerAdv control.

## Content

### Creating a Dataset, Table, and Rows

```csharp
table = dataSet.Tables.Add("Table");

table.Columns.Add("DateTimeColumn", typeof(DateTime));

table.Columns[0].AllowDBNull = true;

table.Rows.Add(new object[] { DateTime.Now - TimeSpan.FromDays(60) });
table.Rows.Add(new object[] { DateTime.Now });
table.Rows.Add(new object[] { DBNull.Value });
```

```vbnet
' Creating DataSet, Table and rows.
Private dataSet As DataSet = Nothing
Private table As DataTable = Nothing

Private dataSet = New DataSet()
Private table = dataSet.Tables.Add("Table")

table.Columns.Add("DateTimeColumn", GetType(DateTime))

Private table.Columns(0).AllowDBNull = True

table.Rows.Add(New Object() { DateTime.Now - TimeSpan.FromDays(60) })
table.Rows.Add(New Object() { DateTime.Now })
table.Rows.Add(New Object() { DBNull.Value })
```

### Binding the Dataset to a DataGrid Control

1. **Assign the dataset to the DataGrid control using its `DataSource` property.**
2. **Set the control's `DataMember` property to the member that must be bound.**

#### Code Example

```csharp
dataGrid1.DataSource = dataSet;
dataGrid1.DataMember = "Table";
```

```vbnet
Private dataGrid1.DataSource = dataSet
Private dataGrid1.DataMember = "Table"
```

### Binding the Datasource with the DateTimePickerAdv Control

1. **Bind the datasource with the DateTimePickerAdv control.**

#### Code Example

```csharp
// [C#]
```

## API Reference

### Methods
- `AddRow(object[] values)`
  - Parameters: 
    - `values`: An array of objects representing the row's data.
  - Returns: None.
  - Description: Adds a new row to the table with the specified values.

### Properties
- `AllowDBNull`
  - Type: `bool`
  - Description: Indicates whether `DBNull.Value` is accepted in the column.

## Code Examples

#### C#

```csharp
dataSet = new DataSet();
table = dataSet.Tables.Add("Table");

table.Columns.Add("DateTimeColumn", typeof(DateTime));
table.Columns["DateTimeColumn"].AllowDBNull = true;

table.Rows.Add(DateTime.Now - TimeSpan.FromDays(60));
table.Rows.Add(DateTime.Now);
table.Rows.Add(DBNull.Value);

dataGrid1.DataSource = dataSet;
dataGrid1.DataMember = "Table";
```

#### VB.NET

```vbnet
Private dataSet As DataSet = New DataSet
Private table As DataTable = New DataTable

dataSet.Tables.Add("Table")
table.Columns.Add("DateTimeColumn", GetType(DateTime))
table.Columns("DateTimeColumn").AllowDBNull = True

table.Rows.Add(DateTime.Now - TimeSpan.FromDays(60))
table.Rows.Add(DateTime.Now)
table.Rows.Add(DBNull.Value)

dataGrid1.DataSource = dataSet
dataGrid1.DataMember = "Table"
```

## Page-level Navigation/TOC

- **Creating a Dataset, Table, and Rows**
- **Binding the Dataset to a DataGrid Control**
- **Binding the Datasource with the DateTimePickerAdv Control**

<!-- tags: [product, dataset, windows-forms, datagrid, datetimepickeradv, data-binding] keywords: [dataset, table, rows, datagrid, datetimepicker, data-binding, windows forms] -->
```