```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: pdf
page_number: 102
page_id: pdf#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:39Z
fidelity: lossless
-->

# Essential PDF

```csharp
brush2 = New PdfSolidBrush(color7)
rect = New RectangleF(180, 110, 30, 30)

' Draw using the PdfBrush
g.DrawRectangle(brush2, rect)
```

> **Note:** This property will not convert the entire document into different color spaces. Also, it will not have any impact on pages that have been created before the property value has changed. It just chooses the color space for the pages created after the alteration.

## Graphics Level

The **PdfGraphics** class has its own **ColorSpace** property, which chooses the color space for the objects that will be drawn next. This property alternates the document settings and enables to change the color space as many times as you wish. **Save** and **Restore** methods save and restore the color space, along with other graphics state parameters respectively.

### C#

```csharp
PdfPen pen = new PdfPen(Color.Red);
PdfBrush brush = new PdfSolidBrush(Color.Blue);

// Default color space.
graphics.DrawRectangle(pen, brush, rectangle);

graphics.Save();

// GrayScale color space.
graphics.ColorSpace = PdfColorSpace.GrayScale;
graphics.DrawRectangle(pen, brush, rectangle);

// CMYK color space.
graphics.ColorSpace = PdfColorSpace.CMYK;
graphics.DrawRectangle(pen, brush, rectangle);
graphics.Restore();

// Default color space.
graphics.DrawRectangle(pen, brush, rectangle);
```

### VB.NET

```vbnet
Dim pen As Syncfusion.Pdf.Graphics.PdfPen = New Syncfusion.Pdf.Graphics.PdfPen(Color.Red)
```

## Footer
© 2013 Syncfusion. All rights reserved. | Page 102

<!-- tags: [syncfusion sdk, pdf, color space, graphics, pdfGraphics, colorSpace property, save, restore, C#, VB.NET] keywords: [Syncfusion Winforms, Essential PDF, PdfGraphics, ColorSpace, color spaces, document settings, PdfPen, PdfSolidBrush] -->
```