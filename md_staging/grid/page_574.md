```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_574.jpeg
document_name: grid
page_number: 574
page_id: grid#page_574
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Explores the use of multiple nested relations in the Syncfusion Grid Data Bound Grid control.
- Demonstrates how to set up hierarchical data display in the Grid using the Grid.Binder.AddRelation function.
- Provides examples in both C# and VB.NET for handling nested relations in a dataset.

## Content

### 4.2.2.12.2 Multiple Nested Relations

The Grid Data Bound Grid control supports multiple nested relations. A relation can be added in the data source, and the data source can be set to the Grid Data Bound Grid. Then, the name of the relation can be passed through the `Grid.Binder.AddRelation` function to show a hierarchical pattern.

#### Example:

This following code example illustrates the display of a DataSet with multiple nested relations. The sample displays the NorthWind's 'Category', 'Products', and the 'Orders_Details' table, and allows you to expand and collapse the order details for each order and the products for each category. After adding a relation in the dataset and setting the DataSource to the grid, the name of the relation is passed through the Grid.Binder.AddRelation function in order to show a hierarchical pattern.

```csharp
GridHierarchyLevel hlCategory_Products = 
gridBinder.AddRelation("Category_Products"); 
GridHierarchyLevel hlProducts_OrderDetails = 
gridBinder.AddRelation("Products_OrderDetails");
```

```vbnet
Dim hlCategory_Products As GridHierarchyLevel = 
gridBinder.AddRelation("Category_Products") 
Dim hlProducts_OrderDetails As GridHierarchyLevel = 
gridBinder.AddRelation("Products_OrderDetails")
```

## API Reference

### Methods
- **AddRelation(string relationName): GridHierarchyLevel**
  - Adds a relation to the grid using the specified relation name.
  - **Parameters**
    - `relationName`: The name of the relation to be added.
  - **Returns**: A `GridHierarchyLevel` object representing the hierarchy level for the added relation.

## RAG Annotations
- Links: `Grid.Binder.AddRelation`, `GridHierarchyLevel`
<!-- tags: [Syncfusion, Grid, Data Bound Grid, Nested Relations, C#, VB.NET] keywords: [multiple nested relations, hierarchical data display, Grid.Binder.AddRelation, GridHierarchyLevel, NorthWind database, Category, Products, Orders_Details, expand, collapse, relationName] -->
```