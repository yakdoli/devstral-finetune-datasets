```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_711.jpeg
document_name: grid
page_number: 711
page_id: grid#page_711
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Me.gridGroupingControl1.AddGroupDropArea("OrderDetails")
```

## Overview
- This section focuses on adding Group Drop Areas to the Grid control, specifically targeting child tables in the grid.
- It demonstrates how to customize the appearance and functionality of the GroupDropArea using various properties.
- A screenshot is provided to illustrate the GroupDropArea feature in action.

## Content

### Figure 286: Adding Group Drop Areas to the Child Tables (Product and OrderDetails)
The screenshot shows a Grid Grouping Control with GroupDropAreas added for the `Product` and `OrderDetails` tables. The GroupDropArea allows users to group data by dragging column headers into specified areas. The interface displays categories, products, and order details, highlighting the grouping functionality.

### 4.3.4.3.1.1.2 Customizing GroupDropArea
The Grid Group Drop Area consists of a collection of Grid controls packed within a panel named `GroupDropPanel`. A Splitter is used to provide runtime adjustability of the `Drop Panel` size in relation to the `Grid Table Panel`. When customizing the Group Drop Area, the user should consider the controls and their integration.

#### Properties affecting GroupDropArea
The properties listed below allow customization of the Grid Group Drop Area's look and feel.

| Property                    | Description                                |
|-----------------------------|--------------------------------------------|
| gridGroupingControl1.GridGroupDropArea | Lists the properties & events to customize the drop area. |

---

## API Reference (if applicable)
No specific API references are provided in the visible content.

## Code Examples (multi-language supported)
The VB.NET code snippet provided demonstrates the addition of a GroupDropArea to the `OrderDetails` table in a `GridGroupingControl`.

```vb
Me.gridGroupingControl1.AddGroupDropArea("OrderDetails")
```

## Page-level Navigation/TOC (if applicable)
- **4.3.4.3.1.1.2 Customizing GroupDropArea**
- **Properties affecting GroupDropArea**

## Cross References
- See also: GroupDropArea, GridGroupDropPanel, Splitter, Grid Table Panel, Drop Panel size.

<!-- tags: [Grid, GroupDropArea, WinForms, GridGroupingControl, Customization] keywords: [GroupDropArea, GroupDropPanel, Splitter, RuntimeAdjustment, ChildTables, Customization, LookAndFeel] -->
```