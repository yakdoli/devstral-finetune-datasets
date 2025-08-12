```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_474.jpeg
document_name: grid
page_number: 474
page_id: grid#page_474
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The GridControl.ColStyles and GridControl.RowStyles collections will allow you to programmatically set the default row or column style. This code will set the **backcolor** and the text color as well as set the font to bold for column two and row three.

## Note: RowStyles and ColStyles

<div style="text-align: center;">
<img src="clip_image002.jpg" alt="Icon" />
</div>

**Note:** RowStyles and ColStyles are not supported in a Grid Data Bound Grid. For that grid, you will need to use the GridBoundColumn.StyleInfo property to set column styles and you will need to use the grid.Model.QueryCellInfo event to set row styles.

## C#

```csharp
// Set Back Color, Text Color and Font Style of Column 2.
this.gridControl1.ColStyles[2].BackColor = Color.Red;
this.gridControl1.ColStyles[2].TextColor = Color.White;
this.gridControl1.ColStyles[2].Font.Bold = true;

// Set Back Color, Text Color and Font Style of Row 3.
this.gridControl1.RowStyle[3].BackColor = Color.Red;
this.gridControl1.RowStyle[3].TextColor = Color.White;
this.gridControl1.RowStyle[3].Font.Bold = true;
```

## VB.NET

```vb
' Set Back Color, Text Color and Font Style of Column 2.
Me.GridControl1.ColStyles(2).BackColor = Color.Red
Me.GridControl1.ColStyles(2).TextColor = Color.White
Me.GridControl1.ColStyles(2).Font.Bold = True

' Set Back Color, Text Color and Font Style of Row 3.
Me.GridControl1.RowStyle(3).BackColor = Color.Red
Me.GridControl1.RowStyle(3).TextColor = Color.White
Me.GridControl1.RowStyle(3).Font.Bold = True
```
<!-- tags: [GridControl, ColStyles, RowStyles, Syncfusion Winforms, 11.4.0.26] keywords: [GridControl, ColStyles, RowStyles, Default Row, Column Style, Backcolor, Text Color, Font Bold] -->
```