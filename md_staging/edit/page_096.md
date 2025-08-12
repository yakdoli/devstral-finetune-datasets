```html
<!--source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: edit
page_number: 096
page_id: edit#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:39Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Specifies styles and visibility settings for indentation block borders.

## Content

### Property Table

| Property | Description |
| --- | --- |
| IndentationBlockBorderStyle | Specifies style of indentation block border line. |
| ShowIndentationBlockBorders | Specifies whether indentation block borders should be drawn. |

### Code Examples

#### C#

```csharp
this.editControl.IndentLineColor = Color.OrangeRed;
this.editControl.IndentBlockHighlightingColor = Color.IndianRed;
this.editControl.IndentationBlockBackgroundBrush = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.SystemColors.Info, System.Drawing.Color.Khaki);
this.editControl.IndentationBlockBorderColor = System.Drawing.Color.Crimson;
this.editControl.IndentationBlockBorderStyle = Syncfusion.Windows.Forms.Edit.Enums.FrameBorderStyle.DashDot;
this.editControl.ShowIndentationBlockBorders = true;
```

#### VB.NET

```vb
Me.editControl.IndentLineColor = Color.OrangeRed
Me.editControl.IndentBlockHighlightingColor = Color.IndianRed
Me.editControl.IndentationBlockBackgroundBrush = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.SystemColors.Info, System.Drawing.Color.Khaki)
Me.editControl.IndentationBlockBorderColor = System.Drawing.Color.Crimson
Me.editControl.IndentationBlockBorderStyle = Syncfusion.Windows.Forms.Edit.Enums.FrameBorderStyle.DashDot
Me.editControl.ShowIndentationBlockBorders = True
```

### Public Form1 Implementation
```csharp
public Form1()
{
    // Required for Windows Form Designer support
    // 
    InitializeComponent();

    this.editControl1.LoadFile(@"..\..\Form1.cs");

    this.editControl1.IndentLineColor = Color.Khaki;
}
```

#### Figure 28: IndentLineColor = "OrangeRed"; IndentBlockHighlightingColor = "IndianRed"

### Positioning

---

<!-- tags: [indentation block border, style, visibility, Syncfusion Winforms, edit control, property, style setting] keywords: [IndentationBlockBorderStyle, ShowIndentationBlockBorders, IndentLineColor, IndentBlockHighlightingColor, IndentationBlockBackgroundBrush, IndentationBlockBorderColor] -->
```