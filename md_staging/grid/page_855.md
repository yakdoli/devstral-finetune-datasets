```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_855.jpeg
document_name: grid
page_number: 855
page_id: grid#page_855
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:12Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the customization of grid cell styles for record, column header, and group caption cells.
- Provides examples in both C# and VB.NET for altering the appearance of grid elements.

## Content

The following code snippet shows how to modify the appearance of record, column header, and group caption cells in a `GridTableDescriptor` using C#.

### Example in C#

```csharp
gtd.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 229, 201);

// Column Header Cell styles.
gtd.Appearance.ColumnHeaderCell.Interior = new BrushInfo(GradientStyle.Vertical, Color.FromArgb(203, 201, 202), Color.FromArgb(253, 247, 215));
gtd.Appearance.ColumnHeaderCell.TextColor = Color.Black;

// Group Caption Cell styles.
gtd.Appearance.GroupCaptionCell.Interior = new BrushInfo(Color.FromArgb(255, 238, 220));
gtd.Appearance.GroupCaptionCell.Borders.Bottom = new GridBorder(GridBorderStyle.Solid, Color.FromArgb(242, 158, 32), GridBorderWeight.Medium);
```

### Example in VB.NET

```vb
Dim gtd As GridTableDescriptor = Me.gridGroupingControl1.GetTableDescriptor("Orders")

' Record Field Cell styles.
gtd.Appearance.AnyRecordFieldCell.BackColor = Color.FromArgb(223, 247, 252)
gtd.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 229, 201)

' Column Header Cell styles.
gtd.Appearance.ColumnHeaderCell.Interior = New BrushInfo(GradientStyle.Vertical, Color.FromArgb(203, 201, 202), Color.FromArgb(253, 247, 215))
gtd.Appearance.ColumnHeaderCell.TextColor = Color.Black

' Group Caption Cell styles.
gtd.Appearance.GroupCaptionCell.Interior = New BrushInfo(Color.FromArgb(255, 238, 220))
gtd.Appearance.GroupCaptionCell.Borders.Bottom = New GridBorder(GridBorderStyle.Solid, Color.FromArgb(242, 158, 32), GridBorderWeight.Medium)
```

## Sample Screenshot
Here is a sample screenshot showcasing the customized styles applied to the grid.

**Note:** The screenshot is not included in the text and must be referenced separately.

<!-- tags: [grid, styling, record, column header, group caption, appearance, brush info, border styles] keywords: [gridtabledescriptor, alternaterecordfieldcell, anyrecordfieldcell, columnheadercell, groupcaptioncell, color, gradientstyle, borders] -->
```