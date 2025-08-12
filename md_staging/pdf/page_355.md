```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_355.jpeg
document_name: pdf
page_number: 355
page_id: pdf#page_355
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:56Z
fidelity: lossless
-->

## 5.1.2.1 How To Add the Tables One After Another?

You can draw the table relative to the position of the previous table by using the `PdfLayoutResult` class. This class stores the boundary values of the table that is drawn. By using the boundary values, you can set the starting position of the table relative to the height of the previous table. The following code example illustrates this.

### C#

```csharp
// Drawing first table.
PdfLightTable table = new PdfLightTable();
table.DataSource = dt;
table.Style.ShowHeader = true;
PdfLayoutResult result = table.Draw(page, new PointF(0, 20));

// Calculating Second table position.
RectangleF bounds = result.Bounds;
PointF location = new PointF(bounds.Left, bounds.Bottom + 30);

// Drawing the second table.
table.Draw(page, location);
```

### VB.NET

```vbnet
' Drawing first table.
Dim table As PdfLightTable = New PdfLightTable()
table.DataSource = dt
table.Style.ShowHeader = True
Dim result As PdfLayoutResult = table.Draw(page, New PointF(0, 20))

' Calculating Second table position.
Dim bounds As RectangleF = result.Bounds
Dim location As PointF = New PointF(bounds.Left, bounds.Bottom + 30)

' Drawing the second table.
table.Draw(page, location)
```

## 5.1.2.2 How To Draw an Image In a Table Cell?

You can draw an image in a particular table cell by using the `BeginCellLayout` event handler and its arguments. This is done by using the Graphics object in the event handler.
```