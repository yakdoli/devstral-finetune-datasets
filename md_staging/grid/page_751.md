```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_751.jpeg
document_name: grid
page_number: 751
page_id: grid#page_751
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:48Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Describes how to summarize data in the `Essential Grid` for Windows Forms, focusing on aggregate functions and row appearance customization.
- Demonstrates setting up summary rows and columns with aggregates like "Sum" and "Count".
- Shows how to style summary rows using colors for better visual distinction.

## Content

The following code examples illustrate how to configure summary rows and columns in the `GridGroupingControl`.

### C#

```csharp
GridSummaryColumnDescriptor scd1 = new GridSummaryColumnDescriptor("Wins", SummaryType.Int32Aggregate, "wins", "{Sum}");
scd1.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(192, 255, 162));

GridSummaryColumnDescriptor scd2 = new GridSummaryColumnDescriptor("Losses", SummaryType.Int32Aggregate, "losses", "{Sum}");
scd2.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.LavenderBlush);

GridSummaryRowDescriptor srd = new GridSummaryRowDescriptor();
srd.SummaryColumns.AddRange(new GridSummaryColumnDescriptor[] { scd1, scd2 });
srd.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(255, 231, 162));

GridSummaryColumnDescriptor scd3 = new GridSummaryColumnDescriptor("Total", SummaryType.Count, "{Count} Records.");
GridSummaryRowDescriptor srd2 = new GridSummaryRowDescriptor("Row2", scd3);
srd2.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(255, 231, 162));

this.gridGroupingControl1.TableDescriptor.SummaryRows.AddRange(new GridSummaryRowDescriptor[] { srd, srd2 });
```

### VB.NET

```vb
Dim scd1 As GridSummaryColumnDescriptor = New GridSummaryColumnDescriptor("Wins", SummaryType.Int32Aggregate, "wins", "{Sum}")
scd1.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(192, 255, 162))

Dim scd2 As GridSummaryColumnDescriptor = New GridSummaryColumnDescriptor("Losses", SummaryType.Int32Aggregate, "losses", "{Sum}")
scd2.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.LavenderBlush)

Dim srd1 As GridSummaryRowDescriptor = New GridSummaryRowDescriptor()
srd1.SummaryColumns.AddRange(New GridSummaryColumnDescriptor() { scd1, scd2 })
srd1.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(255, 231, 162))

Dim scd3 As GridSummaryColumnDescriptor = New GridSummaryColumnDescriptor("Total", SummaryType.Count, "{Count} Records.")
Dim srd2 As GridSummaryRowDescriptor = New GridSummaryRowDescriptor("Row2", scd3)
srd2.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(255, 231, 162))
```

### Explanation

- **Summary Columns and Rows**:
  - `GridSummaryColumnDescriptor` is used to define columns for aggregate functions (e.g., sum, count).
  - `GridSummaryRowDescriptor` is used to define rows that display summary data.
  - The `SummaryType.Int32Aggregate` is used for aggregate functions like summing integers.
  - The `SummaryType.Count` is used to count records.

- **Appearance Customization**:
  - The `Appearance.AnySummaryCell.Interior` property is used to set the background color for summary cells.

### Key Points

- The code configurations demonstrate how to:
  - Add summary columns for "Wins" and "Losses" with aggregate sums.
  - Add a summary row for the total count of records.
  - Style summary cells using custom background colors.

## API Reference

### GridSummaryColumnDescriptor
- **SummaryType.Int32Aggregate**:
  - Used for aggregate functions like summing integer values.
  - Parameters:
    - `ColumnName`: The name of the column being summarized.
    - `AggregateFunction`: The aggregate function to apply (e.g., sum).
    - `AggregateField`: The data source field to use for aggregation.
    - `AggregateFormatString`: The format string for the aggregate result.

- **SummaryType.Count**:
  - Used to count the number of records.
  - Parameters:
    - `ColumnName`: The name of the column being summarized.
    - `AggregateField`: The data source field to use for counting.

## Code Examples

The provided examples show how to:

1. Create summary columns with aggregate functions.
2. Create summary rows to display aggregated data.
3. Style summary cells to enhance visual distinction.

## Cross References

See also:
- Documentation on `GridGroupingControl` for more details on data binding and grid management.
- Examples of other aggregate functions like average, minimum, and maximum.

<!-- tags: [Syncfusion, Essential Grid, Windows Forms, Summary Rows, Aggregate Functions] keywords: [GridGroupingControl, GridSummaryColumnDescriptor, GridSummaryRowDescriptor, SummaryType, Aggregate Functions, Row Appearance] -->
```
