```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en  
source_filename: page_145.jpeg  
document_name: pdf  
page_number: 145  
page_id: pdf#page_145  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T07:33:00Z  
fidelity: lossless  
-->  

## Overview

- Bounds (read-only): Bounds of the row on the page
- BeginCellLayout event detailed explanation with event arguments.
- Illustrated example of drawing graphics elements within a cell using C# and VB.NET code samples.

## Content

### BeginCellLayout

#### Overview

This event is raised when cell layout starts. The arguments of this event are as follows:

- **RowIndex (read-only)**: Index of the current row.
- **CellIndex (read-only)**: Index of the current cell within the row.
- **Value (read-only)**: Text value of the cell.
- **Bounds (read-only)**: Bounds of the cell.
- **Graphics**: Graphics on which the cell should be drawn.
- **Skip**: Indicates if the cell should be skipped.

#### Example: Drawing the Graphics Elements Inside the Cell

The following code example illustrates how to draw the graphics elements inside the cell.

##### C#

```csharp
// Subscribing the event
pdfLightTable.BeginCellLayout += new BeginCellLayoutEventHandler(pdfLightTable_BeginCellLayout);

// Drawing ellipse inside the cell
void pdfLightTable_BeginCellLayout(object sender, BeginCellLayoutEventArgs args)
{
    if (args.RowIndex == 0 && args.CellIndex == 2)
    {
        args.Graphics.DrawEllipse(PdfBrushes.Red, args.Bounds);
    }
}
```

##### VB.NET

```vb
' Subscribing the event
Private pdfLightTable.BeginCellLayout += New BeginCellLayoutEventHandler(pdfLightTable_BeginCellLayout)

' Drawing ellipse inside the cell
Private Sub pdfLightTable_BeginCellLayout(ByVal sender As Object, ByVal args As BeginCellLayoutEventArgs)
    If args.RowIndex = 0 AndAlso args.CellIndex = 2 Then
        args.Graphics.DrawEllipse(PdfBrushes.Red, args.Bounds)
    End If
End Sub
```

## RAG Annotations

<!-- tags: [syncfusion, winforms, cell layout, graphics drawing, pdf] keywords: [BeginCellLayout, RowIndex, CellIndex, Bounds, Graphics, Skip, ellipse, C#, VB.NET] -->
```