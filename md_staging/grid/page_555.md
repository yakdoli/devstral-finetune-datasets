```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_555.jpeg
document_name: grid
page_number: 555
page_id: grid#page_555
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to filter grid data using a `DataView` and `RowFilter`.
- Shows how to add a Grid Filter Bar to simplify filtering in a Grid Data Bound Grid.

## Content

### Using RowFilter for Filtering Grid Data

The following code examples demonstrate how to use `RowFilter` to filter rows in a grid bound to a `DataTable`. The filter will display only rows where the `FirstName` starts with 's'.

```csharp
// Assuming the grid is bound to a Data Table.
DataView dv =
  ((DataTable)this.gridDataBoundGrid1.DataSource).DefaultView;
dv.RowFilter = "FirstName LIKE 's*'";
```

```vb.net
' Assuming the grid is bound to a Data Table.
Dim dv As DataView = CType(Me.gridDataBoundGrid1.DataSource, 
DataTable).DefaultView
dv.RowFilter = "FirstName LIKE 's*'"
```

### Adding a Grid Filter Bar

You can use the Essential Grid's `GridFilterBar` class to automatically add a row of drop-down cells at the top of a simple (non-hierarchical) Grid Data Bound Grid. These drop-down cells can be used to filter the grid to display only rows that match values from the drop-down.

For example, if one of your columns is `City` and you want to see all the rows where the `City` is 'Boston', you can drop the combo box at the top of the `City` column, select 'Boston', and the grid will then display only those rows.

Adding a Grid Filter Bar requires only two lines of code.

```csharp
// Add a Filter Bar to the data bound grid.
GridFilterBar filterBar = new
  Syncfusion.Windows.Forms.Grid.GridFilterBar();
filterBar.WireGrid(gridDataBoundGrid1);
```

```vb.net
' Add a Filter Bar to the data bound grid.
Dim filterBar As GridFilterBar = New
  Syncfusion.Windows.Forms.Grid.GridFilterBar()
filterBar.WireGrid(GridDataBoundGrid1)
```

## API Reference

### `GridFilterBar`

- **Namespace:** `Syncfusion.Windows.Forms.Grid`
- **Usage:** Adds a filter bar to a Grid Data Bound Grid to facilitate filtering rows based on drop-down selections.

### Methods

- **`WireGrid(IGrid grid)`**
  - **Description:** Connects the Grid Filter Bar to a specific grid, enabling filtering functionality.

## Code Examples

### Example: Adding a Grid Filter Bar

Below is a complete example showing how to add a Grid Filter Bar to a Grid Data Bound Grid:

```csharp
using Syncfusion.Windows.Forms.Grid;

// Assuming gridDataBoundGrid1 is the Grid Data Bound Grid
GridFilterBar filterBar = new GridFilterBar();
filterBar.WireGrid(gridDataBoundGrid1);
```

### Example: Using RowFilter

Here is an example of using `RowFilter` to filter rows:

```csharp
DataView dv =
  ((DataTable)this.gridDataBoundGrid1.DataSource).DefaultView;
dv.RowFilter = "FirstName LIKE 's*'";
```

## Page-level Navigation/TOC

- [Using RowFilter for Filtering Grid Data](#using-rowfilter-for-filtering-grid-data)
- [Adding a Grid Filter Bar](#adding-a-grid-filter-bar)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

<!-- tags: [Essential Grid, WinForms, GridFilterBar, RowFilter, DataGrid] keywords: [syncfusion, windows forms, data filtering, grid control, filter bar, rowfilter, drop-down filtering] -->
```
