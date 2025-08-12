```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_387.jpeg
document_name: XlsIO
page_number: 387
page_id: XlsIO#page_387
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:00Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page describes how to group and ungroup rows and columns in Excel using the `Group` and `Ungroup` methods provided by the `IRange` interface in Essential XlsIO.
- It includes examples demonstrating how to group by rows and columns, and how to expand or collapse groups.

## Content

### Grouping and Ungrouping in Essential XlsIO

Essential XlsIO provides support to group and ungroup rows and columns by using the `Group` and `Ungroup` methods of `IRange`. You can also collapse or expand groups through one of its overloads.

#### Figure: Grouping from Data Menu
![Grouping from Data Menu](https://i.imgur.com/G387.png)

**Figure 137: Grouping from Data Menu**

Understanding how to effectively manage your data by grouping and ungrouping rows and columns is crucial for data organization and presentation in Excel. Here's how you can perform these operations using Essential XlsIO in C#:

---

#### Code Examples

```csharp
// Grouping by Rows.
sheet.Range["A1:A3"].Group(ExcelGroupBy.ByRows, true);
sheet.Range["A4:A6"].Group(ExcelGroupBy.ByRows);

// Grouping by Columns.
sheet.Range["A1:B1"].Group(ExcelGroupBy.ByColumns, true);
sheet.Range["C1:F1"].Group(ExcelGroupBy.ByColumns);

// Ungroup by Rows
sheet.Range["A1:A3"].Ungroup(ExcelGroupBy.ByRows);
```

### Detailed Explanation
- **Grouping Rows**: The first two lines demonstrate how to group rows in the range `A1:A3`. The `true` parameter indicates that the group should be collapsed initially.
- **Grouping Columns**: Similarly, the next two lines show grouping of columns in the ranges `A1:B1` and `C1:F1`. The `true` parameter here also specifies collapsing the columns initially.
- **Ungrouping**: The last line shows how to ungroup the rows in the range `A1:A3`.

This functionality is particularly useful when dealing with large datasets, allowing for better organization and selective visibility of data subsets.

---

## API Reference

### Methods

#### Group
- **Syntax**: `Range.Group(ExcelGroupBy groupBy, bool collapse)`
  - **Parameters**:
    - `groupBy`: Specifies whether to group by rows or columns (`ExcelGroupBy.ByRows` or `ExcelGroupBy.ByColumns`).
    - `collapse`: A boolean indicating if the group should be collapsed initially.
  - **Returns**: `void`
  - **Description**: Groups the specified range based on the grouping type and collapse setting.

#### Ungroup
- **Syntax**: `Range.Ungroup(ExcelGroupBy groupBy)`
  - **Parameters**:
    - `groupBy`: Specifies whether to ungroup by rows or columns (`ExcelGroupBy.ByRows` or `ExcelGroupBy.ByColumns`).
  - **Returns**: `void`
  - **Description**: Ungroups the specified range based on the grouping type.

---

## Cross References
- For more information on using `IRange` and other functionalities in Essential XlsIO, refer to the full documentation.

---

<!-- tags: [xlsio, grouping, ungrouping, Excel, rows, columns, date-menu, group-outline, overloads, C#, Syncfusion] keywords: [group, ungroup, ExcelGroupBy, IRange, rows, columns, data organization] -->
```