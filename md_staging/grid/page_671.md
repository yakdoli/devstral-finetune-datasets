```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_671.jpeg
document_name: grid
page_number: 671
page_id: grid#page_671
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:48Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Example

```vb
sender As Object, ByVal e As TableListChangedEventArgs)
Me.gridGroupingEmployee.OptimizeIListGroupingPeformance(sender, e)
End Sub
```

### Screenshot of Grid Grouping

The figure below shows the process of grouping data by dragging a column header.

**Figure 270: First Name Is Dragged to Add to Group.**

The screenshot displays a grid with the following features:

- **Header:** The grid header shows columns labeled `ID`, `Last Name`, and `First Name`.
- **Rows:** The grid rows contain data starting from `ID 0` to `ID 15`, with `Last` as the `Last Name` and `First 0` to `First 15` as the `First Name`.
- **Grouping:** The `First Name` column is being dragged, indicating the process of grouping the data by this column.
- **Title:** The title of the grid is labeled as `Binding Test`, and it indicates that there are `50000` items in the grid.

## Description

This example demonstrates how to use the grid's grouping functionality by dragging a column header to group the data. The code snippet provided demonstrates an event handler for optimizing the performance of the grouping process when the list of data changes.

---

<!-- tags: [Essential Grid, Windows Forms, grouping, performance optimization, data binding, VB.NET] keywords: [grid, grouping, drag and drop, performance, data binding, table list changed events] -->
```