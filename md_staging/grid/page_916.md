```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_916.jpeg
document_name: grid
page_number: 916
page_id: grid#page_916
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of AlphaBlendSelectionColor property to highlight selected rows in the Grid.
- Explains Record Based Selection mechanism for grouping grids.
- Describes various methods for selecting records in a Grid Grouping control.

## Content

### AlphaBlendSelectionColor Example
The figure below illustrates a grouping grid where the AlphaBlendSelectionColor property is set to "Red".

![Figure 332: AlphaBlendSelectionColor = "Red"](image.png)

**Note:** For more details, refer to the following browser sample:
```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping Grid Options\Table Options Demo
```

#### Record Based Selection

**4.3.4.7.2 Record Based Selection**

This type of selection mechanism allows selection in terms of record. It is not cell based. This selection mode is specifically designed for a Grouping Grid and hence it is aware of nested tables, nested groups, and the like. Any selection that is record based affects the `Table.SelectedRecords` collection.

Grid Grouping control offers three types of record based selections which are together called as `ListBoxSelection Modes`. To enable record based selection, you need to set the `ListBoxSelectionMode` property to a value other than `None`. Once a listbox selection is enabled, it automatically turns off the model based selection by assigning `None` to the `AllowSelection` property.

**SelectionModes - One**

It allows you to select only one item (record).

### API Reference

- `AlphaBlendSelectionColor`: Property to set the color of the selection effect.
- `ListBoxSelectionMode`: Property to enable record based selection.
- `Table.SelectedRecords`: Collection to retrieve the selected records.

### Code Examples

```csharp
// Example of setting AlphaBlendSelectionColor
gridTableControl1.AlphaBlendSelectionColor = Color.Red;

// Enabling Record Based Selection
gridGroupingControl1.ListBoxSelectionMode = Syncfusion.Windows.Forms.Grid.GridSelectionMode.One;
```

## Cross References

- **Refer to additional samples and demos at:**  
  `<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\`

<!-- tags: Grid, Grouping, AlphaBlendSelectionColor, ListBoxSelectionMode, RecordBasedSelection, GridGroupingControl keywords: AlphaBlendSelectionColor, ListBoxSelectionMode, RecordBasedSelection, Grid Table Options, Grouping Grid, Syncfusion WinForms, Version 11.4.0.26 -->
```