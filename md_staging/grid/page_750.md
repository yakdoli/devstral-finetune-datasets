```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_750.jpeg
document_name: grid
page_number: 750
page_id: grid#page_750
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:40Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Summary Column Descriptor Example

```csharp
GridSummaryColumnDescriptor("Losses", SummaryType.Int32Aggregate, "losses", "{Sum}")
scd2.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.LavenderBlush)
```

### Summary Row Descriptor Example

```csharp
Dim srd As GridSummaryRowDescriptor = New GridSummaryRowDescriptor()
srd.SummaryColumns.AddRange(New GridSummaryColumnDescriptor() {scd1, scd2})
srd.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(255, 231, 162))
Me.gridGroupingControl1.TableDescriptor.SummaryRows.Add(srd)
```

Here is a sample screenshot displaying the summaries for the columns **wins** and **losses**.

![Figure 300: Multi Column Summaries](https://i.imgur.com/MultiColumnSummaries.png)
*Figure 300: Multi Column Summaries*

### Multi Row Summaries

#### Grouping Grid

Grouping Grid allows you to have summaries for more than one row. It is achieved by defining a required number of summary row descriptors. Each of the summary rows can have its own format for calculating the summaries. Here is an example that shows how to add two different summary rows for a grid table.

#### C#

```csharp
GridSummaryColumnDescriptor scd1 = new GridSummaryColumnDescriptor("Wins", SummaryType.Int32Aggregate, "wins", "{Sum}");
scd1.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(192, 255, 162));

GridSummaryColumnDescriptor scd2 = new
```

## API Reference

- **Namespace**: Inherits from `GridSummaryRowDescriptor`
- **Properties**:
  - `SummaryType`: Type of summary to calculate (e.g., `Int32Aggregate`).
  - `Formatter`: String format for summary display (e.g., `{Sum}`).
  - `Appearance`: Custom appearance settings for the summary row (e.g., `Interior` color).

## Code Examples

### Example 1: Configuring Summary Columns

```csharp
GridSummaryColumnDescriptor scd1 = new GridSummaryColumnDescriptor("Wins", SummaryType.Int32Aggregate, "wins", "{Sum}");
scd1.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(192, 255, 162));

GridSummaryColumnDescriptor scd2 = new GridSummaryColumnDescriptor("Losses", SummaryType.Int32Aggregate, "losses", "{Sum}");
scd2.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.LavenderBlush);
```

### Example 2: Adding Summary Rows

```csharp
Dim srd As GridSummaryRowDescriptor = New GridSummaryRowDescriptor()
srd.SummaryColumns.AddRange(New GridSummaryColumnDescriptor() {scd1, scd2})
srd.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(255, 231, 162))
Me.gridGroupingControl1.TableDescriptor.SummaryRows.Add(srd)
```

## See also

- [GridSummaryRowDescriptor](link-to-documentation)
- [GridSummaryColumnDescriptor](link-to-documentation)
- [Appearance Customization](link-to-documentation)

<!-- tags: [syncfusion, windowsforms, grid, summaryrow, multirowsummaries] keywords: [gridsummaryrowdescriptor, gridsummarycolumndescriptor, summarytype, appearance, cellinterior, multirowsummaries, aggregatefunctions] -->
```