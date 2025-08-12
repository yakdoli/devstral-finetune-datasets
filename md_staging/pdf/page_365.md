```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_365.jpeg
document_name: pdf
page_number: 365
page_id: pdf#page_365
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:23Z
fidelity: lossless
-->

# Essential PDF

```vb
Dim g As PdfGraphics = lPage.Graphics
Dim state As PdfGraphicsState = g.Save()
    g.SetTransparency(0.25f)
    g.RotateTransform(-40)
    g.DrawString("Stamping text", font, PdfPens.Red, PdfBrushes.Red, New PointF(-150, 450))
Next
lDoc.Save("Sample.pdf")
```

## 5.2.3 How To Convert Units In PDF / What Are the Units Of the Elements In PDF?

Essential PDF uses the measure unit of "points" for the elements. A point is equal to 1/72 of an "inch". Points are represented in terms of float values. `PdfUnitConvertor` enables to convert different measure units.

The following code example illustrates how to convert pixels to points.

### [C#]

```csharp
//Converts inches to points
float height = con.ConvertUnits(800, PdfGraphicsUnit.Inch, PdfGraphicsUnit.Point);
float width = con.ConvertUnits(500, PdfGraphicsUnit.Inch, PdfGraphicsUnit.Point);
SizeF pageSize = new SizeF(width, height);
doc.PageSettings.Size = pageSize;
```

### [VB.NET]

```vb
'Converts inches to points
Dim height As Single = con.ConvertUnits(800, PdfGraphicsUnit.Inch, PdfGraphicsUnit.Point)
Dim width As Single = con.ConvertUnits(500, PdfGraphicsUnit.Inch, PdfGraphicsUnit.Point)
Dim pageSize As SizeF = New SizeF(width, height)
doc.PageSettings.Size = pageSize
```

## 5.2.4 How To Store And Retrieve a PDF Document From the Database?

<!-- tags: [pdf, document, units, conversion, database, store, retrieve, points, measure, synfusion] -->
```