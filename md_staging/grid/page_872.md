```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_872.jpeg
document_name: grid
page_number: 872
page_id: grid#page_872
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the application of dynamic formatting to the Grid Grouping Control.
- Explains how to merge cells dynamically based on cell values in the grid.

## Content

### Example of Dynamic Formatting

#### Figure 339: Dynamic Formatting applied to the Grid Grouping Control

![Figure 339: Dynamic Formatting applied to the Grid Grouping Control](#)

**Note:** For more details, refer the following browser sample:  
**<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Appearance\Dynamic Formatting Demo**

### 4.3.4.5.5 Merge Cells Dynamically

Merging can be applied to the cells dynamically based on the cell values. The merged state will be preserved after any dynamic change such as sorting or grouping.

By default, when merging is applied in the cells, the Grid's bounds will be drawn with respect to the `MergeCellsMode` applied in the Grid. In the case of the GridGrouping control, when the Grid's view layout is changed, the merged state becomes invalid as the Grid still has its initial state bounds.

To preserve this merging after the dynamic change in the grid's layout, the existing `MergeCellsMode` is modified to update the grid bounds after they change, and provides additional support to query the user whether to always update the range of cells to merge.

### Properties

| Property               | Description                                           | Type           | Data Type    |
|------------------------|-------------------------------------------------------|----------------|--------------|
| **MergeCellsLayout**   | Sets the range of cells to merge in the grid.        | **Enum**       | enumeration   |

### Sample Link

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

See also: Grid Grouping, Dynamic Formatting, Merge Cells, Cell Merging, Grid Layout, Sorting, Grouping, Dynamic State Preservation.

## RAG Annotations

<!-- tags: [syncfusion, grid, windows forms, grouping, dynamic formatting, cell merging, version: 11.4.0.26] keywords: [dynamic formatting, grid grouping control, merge cells, cell values, merged state, sorting, grouping, bounds, MergeCellsMode, properties, layout changes, user query, enumeration] -->
```