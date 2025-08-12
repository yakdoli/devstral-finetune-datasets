```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_755.jpeg
document_name: grid
page_number: 755
page_id: grid#page_755
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Grid grouping control provides options to display group summaries for columns in GroupCaptions.
- Built-in options avoid creating distinct rows for summaries.
- Requires a few property settings accessible through the GroupOptions.

## Content

### GridGrouping Control Properties for Summaries

| Property Name                | Description                                          |
|------------------------------|------------------------------------------------------|
| ShowCaptionSummaryCells      | Controls whether GroupCaptionCells can display summaries. |
| ShowSummaries                | Indicates visibility of summaries.                 |
| CaptionSummaryRow            | Specifies a summary row to display when Summary cells are enabled. |
| CaptionText                  | Allows customization of the caption text displayed. |

### Steps to create Caption Summaries

1. First, define a summary for the grid table. Then group the table against a data column.

#### C#

```csharp
// Adding Summaries.
GridSummaryColumnDescriptor scd = new
    GridSummaryColumnDescriptor("Sum", SummaryType.DoubleAggregate,
    "Freight", "{Sum:#}");
GridSummaryRowDescriptor srd = new GridSummaryRowDescriptor("Sum", "$",
    scd);
srd.Appearance.AnyCell.HorizontalAlignment =
    GridHorizontalAlignment.Right;
srd.Appearance.AnyCell.BackColor =
    Color.Cornsilk;
this.gridGroupingControl1.GetTableDescriptor("Orders").SummaryRows.Add(
    srd);

this.gridGroupingControl1.ShowGroupDropArea = true;
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("RequiredDate");
```

#### VB.NET

```vb
' Adding Summaries.
Dim scd As GridSummaryColumnDescriptor = New
    GridSummaryColumnDescriptor("Sum", SummaryType.DoubleAggregate,
    "Freight", "{Sum:#}")
Dim srd As GridSummaryRowDescriptor = New
```

## API Reference

### Properties of GridGroupingControl
- **ShowGroupDropArea**: Boolean property to display or hide the group drop area.
- **TableDescriptor**: Property to access table-specific settings.
- **GroupedColumns**: Collection property to specify which columns are grouped.
- **SummaryRows**: Collection property to add or manage summary rows.

### Methods of GridGroupingControl
- **GetTableDescriptor(string tableName)**: Returns the table descriptor for a specified table.

## Code Examples

The provided code examples illustrate how to:
1. Define a summary descriptor for a specific column.
2. Create a summary row that references the summary descriptor.
3. Set visual properties (e.g., alignment and background color) for the summary row.
4. Assign the summary row to a table and enable group summaries.

### Miscellaneous HTML Element Separator

---

### Rights Information
© 2013 Syncfusion. All rights reserved.

## Page-level Navigation/TOC (if applicable)
- [ ] This page does not contain a local Table of Contents.

## Cross References
- Refer to additional grid customization options in the [Syncfusion WinForms documentation](https://www.syncfusion.com/documentation/windows-forms/grid).

<!-- tags: grid, winforms, group summaries, grid grouping, summaries, captions, essential grid, syncfusion, winforms controls keywords: group captions, summary cells, summary visibility, alignment, caption text, grid summary, custom captions -->
```