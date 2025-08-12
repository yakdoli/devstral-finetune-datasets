```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_854.jpeg
document_name: grid
page_number: 854
page_id: grid#page_854
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:55Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Examples

```csharp
// Row Header Cell styles.
this.gridGroupingControl1.Appearance.RowHeaderCell.Interior = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal,
SystemColors.Window, Color.FromArgb(206, 213, 231));
this.gridGroupingControl1.Appearance.RowHeaderCell.Themed = false;

// Top Left Header Cell style.
this.gridGroupingControl1.Appearance.TopLeftHeaderCell.Interior = new
BrushInfo(GradientStyle.PathRectangle, SystemColors.Window,
Color.FromArgb(255, 228, 221));
```

```vb.net
' Column Header Cell styles.
Me.gridGroupingControl1.Appearance.ColumnHeaderCell.CellTipText = "ColumnHeader"
Me.gridGroupingControl1.Appearance.ColumnHeaderCell.Interior = new
BrushInfo(GradientStyle.Vertical, Color.FromArgb(214, 220, 232), Color.FromArgb(106, 111, 151))
Me.gridGroupingControl1.Appearance.ColumnHeaderCell.TextColor = Color.White

' Record Field Cell style.
Me.gridGroupingControl1.Appearance.RecordFieldCell.Interior = new
BrushInfo(Color.Lavender)

' Row Header Cell styles.
Me.gridGroupingControl1.Appearance.RowHeaderCell.Interior = new
BrushInfo(GradientStyle.Horizontal, SystemColors.Window, Color.FromArgb(206, 213, 231))
Me.gridGroupingControl1.Appearance.RowHeaderCell.Themed = false

' Top Left Header Cell style.
Me.gridGroupingControl1.Appearance.TopLeftHeaderCell.Interior = new
BrushInfo(GradientStyle.PathRectangle, SystemColors.Window, Color.FromArgb(255, 228, 221))
```

### Apply styles to the Child Table

```csharp
GridTableDescriptor gtd =
this.gridGroupingControl.GetTableDescriptor("Orders");

// Record Field Cell styles.
gtd.Appearance.AnyRecordFieldCell.BackColor = Color.FromArgb(223, 247, 252);
```

<!-- tags: [Syncfusion, WinForms, Essential Grid, GridTableDescriptor, RowHeader, ColumnHeader, RecordField] keywords: [grid, row header, column header, record field cell, GradientStyle, BrushInfo, themed, color customization, vertical gradient, horizontal gradient, PathRectangle gradient, any record field cell] -->
```