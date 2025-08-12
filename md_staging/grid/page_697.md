```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_697.jpeg
document_name: grid
page_number: 697
page_id: grid#page_697
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

This section demonstrates how to add custom columns to a grouping grid. The `TableDescriptor.UnboundFields.Add()` method will allow you to add unbound fields to the grouping grid. The unbound values can be provided in QueryValue event and any changes in the values can be stored back to the data store by handling SaveValue event. Additionally, you can handle QueryCellStyleInfo event to customize the unbound cells individually.

The values must be saved somewhere because the grouping grid does not maintain any data structure to store the cell values. Since the values are unbound, they cannot be stored into the bound data source too. In this example, a HashTable is used to save the values of the unbound column.

The example displays an unbound CheckBox column along with other bound columns using a grouping grid.

## Steps to Create a Grid Grouping Control and Bind It to a Data Store

1. **Create a Grid Grouping control and bind it to a data store.**

```csharp
[C#]

private Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl gridGroupingControl;

// Define a Grouping Grid.
this.gridGroupingControl = new
Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl();
this.gridGroupingControl.Size = new System.Drawing.Size(160, 200 );

// Create a Data Store.
DataTable dt = new DataTable("MyTable");
int nCols = 2;
int nRows = 5;
for(int i = 0; i < nCols; i++)
dt.Columns.Add(new DataColumn(string.Format("Col{0}", i)));
for(int i = 0; i < nRows; ++i)
{
    DataRow dr = dt.NewRow();
    for(int j = 0; j < nCols; j++)
    dr[j] = string.Format("row{0} col{1}", i, j);
    dt.Rows.Add(dr);
}

// Bind the data source to the grouping grid.
this.gridGroupingControl.DataSource = dt;
```

```vbnet
[VB.NET]
```

## API Reference

- **Namespace:** `Syncfusion.Windows.Forms.Grid.Grouping`
- **Class:** `GridGroupingControl`
- **Methods:**
  - `TableDescriptor.UnboundFields.Add()`
- **Events:**
  - `QueryValue`
  - `SaveValue`
  - `QueryCellStyleInfo`
- **Properties:**
  - `Size`

## Code Examples

### C#
```csharp
private Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl gridGroupingControl;

// Define a Grouping Grid.
this.gridGroupingControl = new
Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl();
this.gridGroupingControl.Size = new System.Drawing.Size(160, 200 );

// Create a Data Store.
DataTable dt = new DataTable("MyTable");
int nCols = 2;
int nRows = 5;
for(int i = 0; i < nCols; i++)
dt.Columns.Add(new DataColumn(string.Format("Col{0}", i)));
for(int i = 0; i < nRows; ++i)
{
    DataRow dr = dt.NewRow();
    for(int j = 0; j < nCols; j++)
    dr[j] = string.Format("row{0} col{1}", i, j);
    dt.Rows.Add(dr);
}

// Bind the data source to the grouping grid.
this.gridGroupingControl.DataSource = dt;
```

### VB.NET
```vbnet
[VB.NET]
```

## Page-level Navigation/TOC

- [Overview]
- [Steps to Create a Grid Grouping Control and Bind It to a Data Store]
- [API Reference]
- [Code Examples]

<!-- tags: [product, module, control, api, version?] keywords: [Essential Grid, GridGroupingControl, Syncfusion, unbound fields, grouping grid, data binding, QueryValue, SaveValue, QueryCellStyleInfo] -->
```