```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_251.jpeg
document_name: pdf
page_number: 251
page_id: pdf#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:05Z
fidelity: lossless
-->

## Essential PDF

```csharp
PdfPageTemplateElement header = new PdfPageTemplateElement(rect);
PdfImage img = new PdfBitmap(@"..\..\Data\logo.png");

// Draw the image in the Header.
header.Graphics.DrawImage(img, imageLocation, imageSize);

// Add the header at the top
doc.Template.Top = header;

// Footer.
// Create a Template that can be used as a footer.
// Create a page template
PdfPageTemplateElement footer = new PdfPageTemplateElement(rect);

// Create page number field
PdfPageNumberField pageNumber = new PdfPageNumberField(font, brush);

// Create page count field
PdfPageCountField count = new PdfPageCountField(font, brush);

// Add the fields in composite fields
PdfCompositeField compositeField = new PdfCompositeField(font, brush, "Page {0} of {1}", pageNumber, count);
compositeField.Bounds = footer.Bounds;

// Draw the composite field in footer
compositeField.Draw(footer.Graphics, new PointF(470, 40));

// Add the footer template at the bottom
doc.Template.Bottom = footer;
```

### [VB.NET]

```vb
' Create a header and draw the image.
Dim rect As RectangleF = New RectangleF(0, 0, _
doc.Pages(0).GetClientSize().Width, 50)
Dim header As PdfPageTemplateElement = New PdfPageTemplateElement(rect)
Dim img As PdfImage = New PdfBitmap("..\..\Data\logo.png")

' Draw the image in the Header.
header.Graphics.DrawImage(img, imageLocation, imageSize)

' Add the header at the top
doc.Template.Top = header
```

<!-- tags: [syncfusion, pdf, template element, header, footer, page number field, page count field, composite field] keywords: [syncfusion pdf, template creation, image embedding, page header, page footer, page number field, page count field, composite field layout] -->
```