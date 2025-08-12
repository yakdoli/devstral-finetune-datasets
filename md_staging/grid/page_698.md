```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_698.jpeg
document_name: grid
page_number: 698
page_id: grid#page_698
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:21Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Defining a Grouping Grid

```vb
' Define a Grouping Grid.
Private gridGroupingControl1 As Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl

Me.gridGroupingControl1 = New Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl()
Me.gridGroupingControl1.Size = New System.Drawing.Size(160, 200)
```

### Creating a Data Store

```vb
' Create a Data Store.
Dim dt As DataTable = New DataTable("MyTable")

Dim nCols As Integer = 2
Dim nRows As Integer = 5

Dim i As Integer = 0
Do While i < nCols
    dt.Columns.Add(New DataColumn(String.Format("Col{0}", i)))
    i += 1
Loop

i = 0
Do While i < nRows
    Dim dr As DataRow = dt.NewRow()
    Dim j As Integer = 0
    Do While j < nCols
        dr(j) = String.Format("row{0} col{1}", i, j)
        j += 1
    Loop
    dt.Rows.Add(dr)
    i += 1
Loop

' Bind the data source to the grouping grid.
Me.GridGroupingControl1.DataSource = dt
```

### Creating a FieldDescriptor

2. Create a FieldDescriptor that well describes your custom column and add it to the UnboundFieldDescriptor collection of the grouping grid.

```csharp
[C#]

FieldDescriptor unboundField = new FieldDescriptor("CheckboxCol", "", false, "");
unboundField.ReadOnly = false;
this.gridGroupingControl1.TableDescriptor.UnboundFields.Add(unboundField);
```

## API Reference

### Namespace: Syncfusion.Windows.Forms

#### Class: GridGroupingControl

##### Methods
- `GridGroupingControl()`: Constructor for the GridGroupingControl.
- `AddToUnboundFields(FieldDescriptor field)`: Adds a field descriptor to the unbound fields collection.

##### Properties
- `DataSource`: Gets or sets the data source for the GridGroupingControl.

## Code Examples

### VB.NET Example
```vb
' Define and configure the GridGroupingControl.
Private gridGroupingControl1 As New Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl()
gridGroupingControl1.Size = New System.Drawing.Size(160, 200)

' Create and configure the DataTable.
Dim dt As DataTable = New DataTable("MyTable")

Dim nCols As Integer = 2
Dim nRows As Integer = 5

Dim i As Integer = 0
Do While i < nCols
    dt.Columns.Add(New DataColumn(String.Format("Col{0}", i)))
    i += 1
Loop

i = 0
Do While i < nRows
    Dim dr As DataRow = dt.NewRow()
    Dim j As Integer = 0
    Do While j < nCols
        dr(j) = String.Format("row{0} col{1}", i, j)
        j += 1
    Loop
    dt.Rows.Add(dr)
    i += 1
Loop

' Bind the data source and configure unbound fields.
Me.GridGroupingControl1.DataSource = dt
Dim unboundField As FieldDescriptor = New FieldDescriptor("CheckboxCol", "", False, "")
unboundField.ReadOnly = False
Me.GridGroupingControl1.TableDescriptor.UnboundFields.Add(unboundField)
```

### C# Example
```csharp
// Define and configure the GridGroupingControl.
GridGroupingControl gridGroupingControl1 = new GridGroupingControl();
gridGroupingControl1.Size = new System.Drawing.Size(160, 200);

// Create and configure the DataTable.
DataTable dt = new DataTable("MyTable");

int nCols = 2;
int nRows = 5;

for (int i = 0; i < nCols; i++)
{
    dt.Columns.Add(new DataColumn(String.Format("Col{0}", i)));
}

for (int i = 0; i < nRows; i++)
{
    DataRow dr = dt.NewRow();
    for (int j = 0; j < nCols; j++)
    {
        dr[j] = String.Format("row{0} col{1}", i, j);
    }
    dt.Rows.Add(dr);
}

// Bind the data source and configure unbound fields.
this.GridGroupingControl1.DataSource = dt;
FieldDescriptor unboundField = new FieldDescriptor("CheckboxCol", "", false, "");
unboundField.ReadOnly = false;
this.GridGroupingControl1.TableDescriptor.UnboundFields.Add(unboundField);
```

## Summary

This guide demonstrates how to define and configure a `GridGroupingControl` in Windows Forms, create a data store, bind it to the grid, and add an unbound field descriptor for custom columns. The provided examples include both VB.NET and C# code for setting up the grid with a sample data source and custom configuration.

<!-- tags: [Syncfusion Winforms, GridGroupingControl, DataStore, FieldDescriptor, UnboundFields] keywords: [GridGroupingControl, DataTable, FieldDescriptor, UnboundFields, DataStore, Windows Forms, Syncfusion Grid, Custom Column, Data Binding] -->
```