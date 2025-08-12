```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_973.jpeg
document_name: grid
page_number: 973
page_id: grid#page_973
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:08Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Grouping

### Overview
- Provides full drag-and-drop capability for grouping records.
- Allows grouping records by dragging a column header to the GroupDropArea.
- Enables grouping across multiple nested tables.

---

### Detailed Explanation

The Designer provides full drag-and-drop capability, enabling users to group records by dragging a column header and dropping it into the GroupDropArea. This functionality is enabled by setting the `ShowGroupDropArea` property to `true`. Users can group data against any number of columns across tables when multiple nested tables are used.

---

### Visual Demonstration

#### Figure 364: Dragging a column header to group grid by that Column

![Dragging a column header to group grid by that Column](https://example.com/image1.png)

This figure illustrates the process of dragging a column header to the GroupDropArea to group the grid by that column.

#### Figure 365: Grouped Grid

![Grouped Grid](https://example.com/image2.png)

This figure shows the grouped grid after the operation has been completed, demonstrating the hierarchical structure created by the grouping.

---

### API Reference

- **Property:** `ShowGroupDropArea`
  - **Type:** Boolean
  - **Description:** Enables or disables the GroupDropArea for drag-and-drop grouping.
  - **Default:** `false`

---

### Code Examples

```csharp
// Enable the GroupDropArea
gridGroupingControl1.ShowGroupDropArea = true;
```

---

### Cross References
- See also: [Drag-and-Drop Functionality](#drag-and-drop-functionality)
- See also: [Nested Tables in Grid](#nested-tables-in-grid)

---

<!-- tags: [essential-grid, windows-forms, grouping, drag-and-drop, grid-drop-area, nested-tables] keywords: [grouping, drag-and-drop, gridGroupingControl, ShowGroupDropArea] -->
```