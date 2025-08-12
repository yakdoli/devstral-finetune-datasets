```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_462.jpeg
document_name: grid
page_number: 462
page_id: grid#page_462
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates handling the Draw Cell event in a grid control.
- Provides examples in C# and VB.NET for applying custom styles to grid cells.
- Utilizes gradient brushes to achieve styled effects in grid rows and columns.

## Content

The following code examples illustrate handling the Draw Cell event.

### 1. Using C#

```csharp
[C#]

// DrawCell event is used to apply styles to the grid.
private void gridControl1_DrawCell(object sender, GridDrawCellEventArgs e)
{
    if (e.RowIndex == 0)
    {
        e.Style.Interior = new BrushInfo(GradientStyle.Vertical, Color.FromArgb(255, 229, 201), Color.FromArgb(255, 153, 52));
    }
    else if (e.ColIndex == 0)
    {
        e.Style.Interior = new BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(102, 110, 152));
    }
    else if (e.RowIndex % 2 == 0)
    {
        e.Style.Interior = new BrushInfo(GradientStyle.BackwardDiagonal, Color.FromArgb(51, 51, 101), Color.White);
    }
}
```

### 2. Using VB.NET

```vb
[VB.NET]

' DrawCell event is used to apply styles to the grid.
Private Sub gridControl1_DrawCell(ByVal sender As Object, ByVal e As GridDrawCellEventArgs)
    If e.RowIndex = 0 Then
        e.Style.Interior = New BrushInfo(GradientStyle.Vertical, Color.FromArgb(255, 229, 201), Color.FromArgb(255, 153, 52))
    ElseIf e.ColIndex = 0 Then
        e.Style.Interior = New BrushInfo(GradientStyle.Horizontal, Color.White, Color.FromArgb(102, 110, 152))
    ElseIf e.RowIndex Mod 2 = 0 Then
        e.Style.Interior = New BrushInfo(GradientStyle.BackwardDiagonal, Color.FromArgb(51, 51, 101), Color.White)
    End If
End Sub
```

## Code Examples

The above examples showcase how to apply different gradient styles to grid cells based on their position (row or column index). This allows for creating visually distinct grid sections or patterns.

## Page-level Navigation/TOC (if applicable)
- **Using C#**
- **Using VB.NET**

## Cross References
- See also: Grid control properties for more styling options.
- See also: Event handling in Windows Forms for general event handling techniques.

<!-- tags: [essential-grid, windows-forms, c#, vb.net, draw-cell-event, gradient-styles, custom-styling, grid-control] keywords: [grid, draw cell, gradient brushes, C#, VB.NET, row indexing, column indexing, event handling, windows forms] -->
```