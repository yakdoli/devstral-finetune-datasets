```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_718.jpeg
document_name: grid
page_number: 718
page_id: grid#page_718
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.gridGroupingControl.HierarchicalGroupDropArea = true;
```

```vb
Me.gridGroupingControl1.HierarchicalGroupDropArea = True
```

## Enabling Hierarchical GroupDropArea Features

To enable other features supported within the hierarchical GroupDropArea, the following properties can be used:

### Dynamic Removal of Grouped Columns

```csharp
// Support to dynamically remove the column from being grouped (adds support in default GroupDropArea too).
this.gridGroupingControl.GridGroupDropArea.AllowRemove = true;
```

### Tree Line Placement

```csharp
// Support to switch the tree line placement to the top and bottom between hierarchy levels.
this.gridGroupingControl.GridGroupDropArea.TreeLinePlacement = TreeLinePlacement.Bottom;
```

### Dynamic Resizing

```csharp
// Support to resize the GroupDropArea dynamically up to the last level of the hierarchy.
this.gridGroupingControl.GridGroupDropArea.DynamicResizing = true;
```

### Custom Tree Line Color

```csharp
// Support to set the tree lines to a desired color.
this.gridGroupingControl.GridGroupDropArea.TreeLineColor = Color.Red;
```

### Dynamic Removal of Grouped Columns (VB)

```vb
' Support to dynamically remove the column from being grouped (adds support in default GroupDropArea too).
Me.gridGroupingControl.GridGroupDropArea.AllowRemove = True
```

## API Reference

### Properties

- **HierarchicalGroupDropArea**: Controls whether the GroupDropArea supports hierarchical grouping.
- **AllowRemove**: Allows dynamically removing a column from being grouped.
- **TreeLinePlacement**: Controls the placement of tree lines.
- **DynamicResizing**: Enables dynamic resizing of the GroupDropArea.
- **TreeLineColor**: Sets the color of the tree lines.

## Code Examples

### C#

```csharp
this.gridGroupingControl.HierarchicalGroupDropArea = true;
this.gridGroupingControl.GridGroupDropArea.AllowRemove = true;
this.gridGroupingControl.GridGroupDropArea.TreeLinePlacement = TreeLinePlacement.Bottom;
this.gridGroupingControl.GridGroupDropArea.DynamicResizing = true;
this.gridGroupingControl.GridGroupDropArea.TreeLineColor = Color.Red;
```

### VB

```vb
Me.gridGroupingControl1.HierarchicalGroupDropArea = True
Me.gridGroupingControl.GridGroupDropArea.AllowRemove = True
Me.gridGroupingControl.GridGroupDropArea.TreeLinePlacement = TreeLinePlacement.Bottom
Me.gridGroupingControl.GridGroupDropArea.DynamicResizing = True
Me.gridGroupingControl.GridGroupDropArea.TreeLineColor = Color.Red
```

<!-- tags: [Syncfusion Winforms, GridGroupingControl, HierarchicalGroupDropArea, GroupDropArea, TreeLines, DynamicResizing] keywords: [HierarchicalGroupDropArea, AllowRemove, TreeLinePlacement, DynamicResizing, TreeLineColor, gridGroupingControl] -->
```