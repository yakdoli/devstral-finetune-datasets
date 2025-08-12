```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_719.jpeg
document_name: grid
page_number: 719
page_id: grid#page_719
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the `GridGroupDropArea` functionality in `GridGroupingControl`.
- Demonstrates how to customize tree line placement, dynamic resizing, and tree line color using properties.
- Introduces `GroupByOptions` to control the behavior of groups in the grid.

## Content

### Customizing GridGroupDropArea

Support to switch the tree line placement to the top and bottom between hierarchy levels.

```vb
Me.gridGroupingControl1.GridGroupDropArea.TreeLinePlacement = TreeLinePlacement.Bottom
```

Support to resize the `GroupDropArea` dynamically up to the last level of the hierarchy.

```vb
Me.gridGroupingControl1.GridGroupDropArea.DynamicResizing = True
```

Support to set the tree lines to a desired color.

```vb
Me.gridGroupingControl1.GridGroupDropArea.TreeLineColor = Color.Red
```

#### Hierarchical GroupDropArea

![Hierarchical GroupDropArea](https://example.com/image_url)  
*Figure 288: Hierarchical GroupDropArea*

### GroupByOptions

#### Grid Grouping Control Options

Grid Grouping control provides a number of options that allows you to control the look and behavior of the groups. You can control the caption text, where and if `AddNew` row will be displayed, and whether captions, headers, footers, preview rows, and summaries will be displayed.

#### The GridGroupOptionsStyleInfo class

The `GridGroupOptionsStyleInfo` class is used to define the visual and behavior aspects of grouped rows, including their captions, headers, footers, and summary rows.

---

```vb
<!-- tags: [grid, gridgroupingcontrol, gridgroupdroparea, groupbyoptions, treelineplacement, dynamicresizing, treelinecolor, gridgroupoptionsstyleinfo] -->
``` 
```