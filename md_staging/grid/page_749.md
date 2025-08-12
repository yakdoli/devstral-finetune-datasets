```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_749.jpeg
document_name: grid
page_number: 749
page_id: grid#page_749
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Learn how to create more advanced summaries for a grid table.
- Understand different forms of summaries supported by the grid control.
- Explore how to define multiple summary rows for a single data table.
- Focus on defining summaries for groups and tables in nested table scenarios.

## Content

### 4.3.4.3.3.1 Exploring Summaries

In the previous chapter, we have learnt how to create simple summaries for a grid table. This chapter will explore the summaries into one more level to discuss the different forms of summaries. It is possible to have multiple summary rows for a single data table. We can define a summary for each group and also for each table when nested tables are used.

#### Multicolumn Summaries

A Summary Row can have any number of summary columns. To display summaries for more than one field, you must first create the summary columns for the desired fields. Then add those summary columns into a summary row. The code given below illustrates this.

```csharp
[C#]
GridSummaryColumnDescriptor scd1 = new GridSummaryColumnDescriptor("Wins", SummaryType.Int32Aggregate, "wins", "{Sum}");
scd1.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(192, 255, 162));

GridSummaryColumnDescriptor scd2 = new GridSummaryColumnDescriptor("Losses", SummaryType.Int32Aggregate, "losses", "{Sum}");
scd2.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.LavenderBlush);

GridSummaryRowDescriptor srd = new GridSummaryRowDescriptor();
srd.SummaryColumns.AddRange(new GridSummaryColumnDescriptor[] { scd1, scd2 });
srd.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(255, 231, 162));

this.gridGroupingControl1.TableDescriptor.SummaryRows.Add(srd);
```

```vb
[VB.NET]
Dim scd1 As GridSummaryColumnDescriptor = New GridSummaryColumnDescriptor("Wins", SummaryType.Int32Aggregate, "wins", "{Sum}")
scd1.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(192, 255, 162))

Dim scd2 As GridSummaryColumnDescriptor = New GridSummaryColumnDescriptor("Losses", SummaryType.Int32Aggregate, "losses", "{Sum}")
scd2.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.LavenderBlush)

Dim srd As GridSummaryRowDescriptor = New GridSummaryRowDescriptor()
srd.SummaryColumns.AddRange(New GridSummaryColumnDescriptor() { scd1, scd2 })
srd.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(255, 231, 162))

this.gridGroupingControl1.TableDescriptor.SummaryRows.Add(srd)
```

## API Reference

### `GridSummaryColumnDescriptor`
- **Namespace**:Syncfusion.Windows.Forms.Grid
- Represents a column to be used in summarizing grid data.
  
### `GridSummaryRowDescriptor`
- **Namespace**:Syncfusion.Windows.Forms.Grid
- Represents a row in the grid that displays summaries.

## Code Examples

The above code samples illustrate how to create and customize summary rows in a grid. It defines two summary columns, one for "Wins" and another for "Losses," and then adds these to a summary row with distinct background colors for visual differentiation.

## RAG Annotations
<!-- tags: [product, grid, summary, windows forms, version, 11.4.0.26] keywords: [syncfusion, gridsummarycolumndescriptor, gridsummaryrowdescriptor, summary rows, multi-column summaries, color customization, nested tables] -->
```