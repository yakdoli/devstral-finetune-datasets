<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_356.jpeg
document_name: pdf
page_number: 356
page_id: pdf#page_356
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:55Z
fidelity: lossless
-->

# Essential PDF

## Overview
- The following code example illustrates how to draw a borderless table.
- Demonstrates how to add an event handler to a table's cell layout.
- Shows how to insert an image into a specific cell of the table.

## Content

### Drawing a Borderless Table with an Image

#### C#

```csharp
// Adding the Event handler
table.BeginCellLayout += new BeginCellLayoutEventHandler(table_BeginCellLayout);

// Drawing an image in a cell
void table_BeginCellLayout(object sender, BeginCellLayoutEventArgs args)
{
    if (args.RowIndex == 0 && args.CellIndex == 0)
    {
        PdfImage img = new PdfBitmap(Image.FromFile(@"..\.Data\Image.png"));
        args.Graphics.DrawImage(img, args.Bounds);

        // To dispose the image
        (img as PdfBitmap).Dispose();
    }
}
```

#### VB.NET

```vb.net
' Adding the Event handler
Private table.BeginCellLayout += New BeginCellLayoutEventHandler(AddressOf table_BeginCellLayout)

' Drawing an image in a cell

Private Sub table_BeginCellLayout(ByVal sender As Object, ByVal args As BeginCellLayoutEventArgs)
    If args.RowIndex = 0 AndAlso args.CellIndex = 0 Then
        Dim img As PdfImage = New PdfBitmap(Image.FromFile("..\Data\Image.png"))
        args.Graphics.DrawImage(img, args.Bounds)

        ' To dispose the image
        TryCast(img, PdfBitmap).Dispose()
    End If
End Sub
```

### 5.1.2.3 How To Implement Column Span In PdfLightTable?

## RAG Annotations
<!-- tags: [pdf, drawing, borderless table, event handler, table, image, column span] keywords: [Syncfusion, Essential PDF, borderless table, cell layout, image insertion, column span, PdfLightTable] -->