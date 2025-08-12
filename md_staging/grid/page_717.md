```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_717.jpeg
document_name: grid
page_number: 717
page_id: grid#page_717
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:43Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains the feature to display items in the GroupDropArea in a hierarchical order.
- It covers interactive features enabled by hierarchical grouping in the GridGrouping control.
- Lists properties related to hierarchical grouping and their descriptions.

## Display GroupDropArea in Hierarchy

### Overview
This feature allows users to display items in the GroupDropArea in a hierarchical order. The items will follow a stacked order.

### Hierarchical Grouping Features
Hierarchical grouping enables the following interactive features in the GridGrouping control:
- Dynamically remove columns from the grouping area.
- Switch the tree line placement between the top and bottom of hierarchy levels.
- Resize the group drop area dynamically up to the last level of the hierarchy.
- Set the tree lines with the desired color.

## Properties

| Property                                      | Description                                                                 | Type      | Data Type    |
|-----------------------------------------------|-----------------------------------------------------------------------------|-----------|--------------|
| HierarchicalGroupDropArea                      | Gets or sets a value to enable the GroupDropArea hierarchy in the grid.     | Boolean    | Boolean, true/false |
| GridGroupDropArea.AllowRemove                 | Gets or sets whether the GroupDropArea should support removal of groups dynamically. | Boolean    | Boolean, true/false |
| GridGroupDropArea.TreeLinePlacement            | Gets or sets the location for the tree line which will be drawn between the hierarchy items. | Enum      | enumeration   |
| GridGroupDropArea.DynamicResizing             | Gets or sets the value to resize the GroupDropArea dynamically.              | Boolean    | Boolean, true/false |
| GridGroupDropArea.TreeLineColor                | Gets or sets the color of the tree lines.                                  | Color      | Color        |

### Sample Link
```plaintext
{installed
drive}\AppData\Local\Syncfusion\EssentialStudio\{version}\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping\GroupingDemo
```

### Adding Hierarchical GroupDropArea to an Application
To enable this feature, the HierarchicalGroupDropArea property must be set to `true`.

---

```html
<!-- tags: [essential grid, windows forms, groupdroparea, hierarchical grouping, gridgrouping, syncfusion, version 11.4.0.26] keywords: [groupdroparea, hierarchical grouping, gridgrouping, tree lines, dynamic resizing, interactive features, syncfusion windows forms] -->
``` 
```