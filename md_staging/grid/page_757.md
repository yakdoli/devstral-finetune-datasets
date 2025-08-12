```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_757.jpeg
document_name: grid
page_number: 757
page_id: grid#page_757
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Final steps to format caption rows for enhanced visual appeal.
- Code examples provided in both C# and VB.NET for formatting caption cells.

## Content

### Formatting Caption Rows

4. Finally, format the caption rows to improve the look and feel.

#### C# Code Example
```csharp
// Providing a good look and enabling Caption Summary Cells as Record Field Cells.
this.gridGroupingControl1.Appearance.GroupCaptionCell.BackColor = this.gridGroupingControl1.Appearance.RecordFieldCell.BackColor;
this.gridGroupingControl1.Appearance.GroupCaptionCell.Borders.Top = new GridBorder(GridBorderStyle.Standard);
this.gridGroupingControl1.Appearance.GroupCaptionCell.CellType = "Static";
```

#### VB.NET Code Example
```vb
' Providing a good look and enabling Caption Summary Cells as Record Field Cells.
Me.gridGroupingControl1.Appearance.GroupCaptionCell.BackColor = Me.gridGroupingControl1.Appearance.RecordFieldCell.BackColor
Me.gridGroupingControl1.Appearance.GroupCaptionCell.Borders.Top = New GridBorder(GridBorderStyle.Standard)
Me.gridGroupingControl1.Appearance.GroupCaptionCell.CellType = "Static"
```

### Example Grid Output

5. When you run the sample, your grid will look similar to this.

![Example Grid with Group Summary in Caption and Table Summary](https://via.placeholder.com/600x400?text=Example+Grid+Screenshot)

The image demonstrates:
- **Group Summary in Caption**: Summaries shown in the header row.
- **Table Summary**: Total values displayed at the bottom of the grid.

## Page-level Navigation/TOC (if applicable)

- [Overview]
- [Formatting Caption Rows]
- [Example Grid Output]

### Cross References

See also:

- "GridGrouping Control Overview"
- "Caption and Summary Cells Configuration"
- "Advanced Grid Formatting Techniques"

<!-- tags: [Syncfusion Winforms, GridGroupingControl, Caption Summary, Formatting, Version 11.4.0.26] keywords: [grid, caption cells, summary cells, formatting, look and feel, group summary, table summary, C#, VB.NET] -->
```