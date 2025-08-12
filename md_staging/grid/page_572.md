```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_572.jpeg
document_name: grid
page_number: 572
page_id: grid#page_572
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:54Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Implements nested drop-down grids for hierarchical data representation.
- Demonstrates multi-level data structure using the NorthWind database tables (Customers, Orders, and Order_Details).
- Highlights the use of the GridHierDataBoundGrid class for hierarchical data binding.

## Content

### Nested Drop-down Grids
Nested Drop-down grids are used to represent multi-level data in a grid. For example, if a bank wants to load all the accounts of an enrolled user in a grid control for a financial project, and some of the accounts have subaccounts with options to be selected under each subaccount, which need to be loaded/ shown as a subelement to that account, Nested Drop-down grids can be used to represent the data. The data can be distributed in parent (primary) grid, child grid, and so on. Grid Data Bound Grid control can display hierarchical data using Nested Drop-down grids.

### Example

In the code example below, the parent (primary) grid is the 'Customers' table from the NorthWind database. On clicking a row of this table, the 'Orders' table will be displayed in a new grid providing details on orders placed by the customers. On clicking any of the rows in Orders table, another grid named 'Order_Details' table is displayed providing details on the order details of the selected row in the Orders table.

This example has a derived GridDataBoundGrid class called the **GridHierDataBoundGrid** used for all the grids to be displayed. In the constructor for this class, the tables for parent and child are to be passed.

#### Code Example: C#
```csharp
// Parent table to Child table.
// Create the outermost grid for the customers table-uses
// GridHierDataBoundGrid class.
this.customerGrid1 = new GridHierDataBoundGrid(this,
this.dataSet11.Customers,
this.dataSet11.Orders, this.orderGrid2, new
QueryFilterStringEventHandler(ProvideOrdersFilterStrings),
new QueryFormatGridEventHandler(ProvideOrderFormat), true);
```

#### Code Example: VB.NET
```vbnet
' Parent table to Child table.
' Create the outermost grid for the customers table-uses
' GridHierDataBoundGrid class.
Me.customerGrid1 = New GridHierDataBoundGrid(Me,
Me.dataSet11.Customers, Me.dataSet11.Orders, Me.orderGrid2, New
QueryFilterStringEventHandler(AddressOf ProvideOrdersFilterStrings),
New QueryFormatGridEventHandler(AddressOf ProvideOrderFormat), True)
```

Finally, to specify a relationship between a parent table and a child table, an event handler must be passed for the **QueryFilterString** event. The event should specify the `FilterString` that defines the relationship between the parent table and the child table.

## API Reference
- **GridHierDataBoundGrid**: A derived class used for hierarchical data binding.
  - **Constructor**: Accepts parameters for the parent and child tables, along with event handlers for filtering and formatting.

## Code Examples
- The provided examples demonstrate the creation and configuration of GridHierDataBoundGrid, showing how to bind different tables and define relationships between them.

## Cross References
See also:  
- "Hierarchical Data Representation"
- "Grid Data Binding in WinForms"

<!-- tags: [syncfusion, windows forms, grid, hierarchical data, nested drop-down grids] keywords: [GridHierDataBoundGrid, NorthWind database, Customers, Orders, Order_Details, QueryFilterString, hierarchical data binding, multi-level data structure] -->
```
