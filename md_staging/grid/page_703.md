```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_703.jpeg
document_name: grid
page_number: 703
page_id: grid#page_703
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Adding data groups and implementing simple grouping in the `Essential Grid` control.
- Grouping data by adding column names to the `TableDescriptor.GroupedColumns` property.
- Demonstrating how to group by the `Title` field and customize the grouping sort direction.

## Content

### Adding Data Groups

#### Simple Grouping

The data can be grouped by adding the column name to the `TableDescriptor.GroupedColumns` property.

```csharp
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Title");
```

```vb.net
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Title")
```

The below grid displays the data columns from the `Employees` Table grouped by the values of the `Title` field.

![Figure 277: ListSortDirection](figure277.png)

**Figure 277: ListSortDirection**

By default, the grouping of a column sorts the records in the ascending order of their `GroupedColumn` values. It is possible to specify the sort order while grouping. The code below arrange the data in the descending order of their `Title` field values.

```csharp
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Title",
```

<br>

---

### WinForms-specific conventions
- The example demonstrates how to group data by the `Title` column in both C# and VB.NET.
- The grid displays grouped data, showing collapsed groups and their respective counts.

## API Reference (if applicable)

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridGroupingControl
- **Property**: `TableDescriptor.GroupedColumns.Add`
  - Adds a column to the group.

## Code Examples (multi-language supported)

- **C#**
  ```csharp
  this.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Title");
  ```

- **VB.NET**
  ```vb.net
  Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Title")
  ```

## Page-level Navigation/TOC (if applicable)

- **Adding Data Groups**
  - Simple Grouping
  - Customizing Sort Direction

## Cross References

See also:
- [Grouping and Sorting in Essential Grid](#grouping-and-sorting-in-essential-grid)
- [Customizing Grid Appearance](#customizing-grid-appearance)

## RAG Annotations

<!-- tags: [WinForms, Grid, Grouping, Sorting, TableDescriptor] keywords: [Essential Grid, GroupedColumns, TableDescriptor.GroupedColumns, ListSortDirection, WinForms, C#, VB.NET, Employees Table, Title field, Grouped data, Sorting order] -->
```