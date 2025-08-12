```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_727.jpeg
document_name: grid
page_number: 727
page_id: grid#page_727
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Adjusting colors for different sections of the grid group control.
- Setting the interior color for various grid cells such as AddNewRecordFieldCell, GroupCaptionCell, and GroupIndentCell.
- Demonstrating the use of `Color.Pink`, `Color.FromArgb`, and `SystemColors.Control` for styling.

## Content

### Code Examples

#### C#
```csharp
new BrushInfo(Color.Pink);
this.gridGroupingControl.Appearance.GroupHeaderSectionCell.Interior = new BrushInfo(Color.Pink);
this.gridGroupingControl.Appearance.GroupIndentCell.Interior = new BrushInfo(Color.FromArgb(192, 192, 255));
this.gridGroupingControl.Appearance.GroupPreviewCell.Interior = new BrushInfo(Color.FromArgb(192, 255, 192));
```

#### VB.NET
```vb
Me.gridGroupingControl1.Appearance.AddNewRecordFieldCell.Interior = New BrushInfo(Color.FromArgb(255, 255, 192))
Me.gridGroupingControl1.Appearance.GroupCaptionCell.Interior = New BrushInfo(SystemColors.Control)
Me.gridGroupingControl1.Appearance.GroupCaptionCell.TextColor = Color.FromArgb(192, 64, 0)
Me.gridGroupingControl1.Appearance.GroupFooterSectionCell.Interior = New BrushInfo(Color.Pink)
Me.gridGroupingControl1.Appearance.GroupHeaderSectionCell.Interior = New BrushInfo(Color.Pink)
Me.gridGroupingControl1.Appearance.GroupIndentCell.Interior = New BrushInfo(Color.FromArgb(192, 192, 255))
Me.gridGroupingControl1.Appearance.GroupPreviewCell.Interior = New BrushInfo(Color.FromArgb(192, 255, 192))
```

### Instructions
9. Run the sample and group the table against any data column. Here is a sample screen shot that shows the grouped grid against 'Sport' column.

## Page-level Navigation/TOC (if applicable)
- This page provides detailed code examples for customizing the appearance of the grid group control.
- Includes both C# and VB.NET code snippets for setting the interior colors of various grid cells.

<!-- tags: [grid, groupcontrol, appearance, colors, windowsforms] keywords: [grid, group, control, custom, appearance, colors, windows forms] -->
``` 
