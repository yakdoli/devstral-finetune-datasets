```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_710.jpeg
document_name: grid
page_number: 710
page_id: grid#page_710
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- GroupDropArea allows grouping data in tables by dragging column headers.
- Support for adding GroupDropArea dynamically to nested tables.
- Demonstrates enabling and adding GroupDropArea for parent and child tables in a hierarchical dataset.

## Content

### GroupDropArea with Multiple Column Headers

[![](https://example.com/image710.png)](https://example.com/image710.png)

**Figure 285: GroupDropArea with Multiple Column Headers**

#### See Also

* **4.3.4.3.1.1.1 Adding GroupDropArea**

The **ShowGroupDropArea** property enables the GroupDropArea only for the top-level table. For nested tables, drop areas for child tables need to be added at runtime. This is achieved by calling the **AddGroupDropArea** method, specifying the respective child table name as the parameter.

In this example, the grid is bound to a hierarchical dataset containing three tables: **Categories**, **Products**, and **OrderDetails**. The following code examples illustrate how to add the group drop area for the child tables **Products** and **OrderDetails**.

#### C#

```csharp
// ShowGroupDropArea adds Group Drop Area for the parent Categories table.
this.gridGroupingControl1.ShowGroupDropArea = true;

// Adding Group Drop Areas for nested tables.
this.groupingGrid1.AddGroupDropArea("Products");
this.groupingGrid1.AddGroupDropArea("OrderDetails");
```

#### VB.NET

```vb
' ShowGroupDropArea adds Group Drop Area for the parent Categories table.
Me.gridGroupingControl1.ShowGroupDropArea = True

' Adding Group Drop Areas for nested tables.
Me.gridGroupingControl1.AddGroupDropArea("Products")
```

## API Reference

### Methods
- **AddGroupDropArea(string tableName)**

  Adds a group drop area for the specified child table.

  - **Parameters**
    - **tableName**: The name of the child table.
  
  - **Description**: Dynamically adds GroupDropArea for the specified nested table.

### Properties
- **ShowGroupDropArea**

  - **Type**: Boolean
  - **Description**: Enables or disables the GroupDropArea for the top-level table.

## Code Examples

### Example 1: Enabling GroupDropArea for Parent and Child Tables

#### C#

```csharp
// Enable GroupDropArea for the parent table.
this.gridGroupingControl1.ShowGroupDropArea = true;

// Add GroupDropArea for child tables.
this.groupingGrid1.AddGroupDropArea("Products");
this.groupingGrid1.AddGroupDropArea("OrderDetails");
```

#### VB.NET

```vb
' Enable GroupDropArea for the parent table.
Me.gridGroupingControl1.ShowGroupDropArea = True

' Add GroupDropArea for child tables.
Me.gridGroupingControl1.AddGroupDropArea("Products")
```

<!-- tags: [grouping, grid, GroupDropArea, Syncfusion Winforms, 11.4.0.26] keywords: [GroupDropArea, nested tables, hierarchical dataset, C#, VB.NET, top-level table, child table] -->
```