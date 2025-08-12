```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_857.jpeg
document_name: grid
page_number: 857
page_id: grid#page_857
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
BrushInfo(Color.White);
this.gridGroupingControl.Appearance.AnyGroupCell.Themed = false;
this.gridGroupingControl.Appearance.GroupCaptionCell.Borders.Bottom = GridBorder(GridBorderStyle.Solid, Color.FromArgb(157, 179, 200));
this.gridGroupingControl.Appearance.GroupCaptionRowHeaderCell.Interior = new BrushInfo(GradientStyle.BackwardDiagonal, SystemColors.Window, Color.DarkOrange);
this.gridGroupingControl.Appearance.GroupFooterSectionCell.Interior = new BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(192, 255, 192));
this.gridGroupingControl1.Appearance.GroupHeaderRowHeaderCell.Interior = new BrushInfo(GradientStyle.Vertical, SystemColors.Window, Color.LightPink);
this.gridGroupingControl1.Appearance.GroupHeaderSectionCell.Interior = new BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(255, 199, 190));
```

## [VB.NET]

```vb.net
gridGroupingControl1.Appearance.AnyGroupCell.Interior = New BrushInfo(Color.White)
gridGroupingControl1.Appearance.AnyGroupCell.Themed = False
gridGroupingControl1.Appearance.GroupCaptionCell.Borders.Bottom = GridBorder(GridBorderStyle.Solid, Color.FromArgb(157, 179, 200))
gridGroupingControl1.Appearance.GroupCaptionRowHeaderCell.Interior = New BrushInfo(GradientStyle.BackwardDiagonal, SystemColors.Window, Color.DarkOrange)
gridGroupingControl1.Appearance.GroupFooterSectionCell.Interior = New BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(192, 255, 192))
gridGroupingControl1.Appearance.GroupHeaderRowHeaderCell.Interior = New BrushInfo(GradientStyle.Vertical, SystemColors.Window, Color.LightPink)
gridGroupingControl1.Appearance.GroupHeaderSectionCell.Interior = New BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(255, 199, 190))
```

Here is a sample screen shot.
```