```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_544.jpeg
document_name: grid
page_number: 544
page_id: grid#page_544
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.2.1.2 Through Code

### Overview
- Demonstrates how to create a DataTable and bind it to a GridDataBoundGrid using C#.
- Utilizes the GridDataBoundGrid.DataSource property to implement data binding.

### Content

#### Through Code
Here are some code samples that will create a DataTable and bind it to a Grid Data Bound Grid. Once you have a DataTable object populated, you can use the GridDataBoundGrid.DataSource property to implement the binding.

```csharp
[C#]

DataTable myDataTable = new DataTable("MyDataTable");

// Declare the Data Column and Data Row variables.
DataColumn myDataColumn;
DataRow myDataRow;

// Create a new Data Column, set the Data Type and Column Name and add to the Data Table.
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
this.GridDataBoundGrid1.DataSource = myDataTable;

// Size the columns.
this.GridDataBoundGrid1.Model.ColWidths[1] = 30;
this.GridDataBoundGrid1.Model.ColWidths[2] = 50;
```

#### [VB.NET]
Coming soon.

### API Reference
- Namespace: GridDataBoundGrid
- Member: DataSource
  - Type: Property
  - Description: Represents the data source for the grid. It can be set to bind the grid to a specific data source.

### Code Examples (C#)
- The provided code demonstrates creating a DataTable with two columns ("id" and "item") and adding 11 rows of data. It then binds this DataTable to the GridDataBoundGrid using the DataSource property. The column widths are adjusted for better visualization.

### Cross References
- Refer to the GridDataBoundGrid documentation for more information on data binding and customization.

<!-- tags: [Essential Grid, Windows Forms, DataTable, GridDataBoundGrid, DataSource] keywords: [DataTable, GridDataBoundGrid, DataColumn, DataRow, data binding, data source, column widths, programming example] -->
```