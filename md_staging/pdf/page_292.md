```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_292.jpeg
document_name: pdf
page_number: 292
page_id: pdf#page_292
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:35Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Creates PDF documents with signatures.
- Demonstrates adding images and textual information to PDF pages.
- Handles document saving and loading functionality.

## Content

### Code Example 1: Adding Signatures to a PDF Document

```vb
    Dim pen As PdfPen = New PdfPen(Brush, 1)
    Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Courier, 12, PdfFontStyle.Regular)
    Dim g As PdfGraphics = signature.Appearence.Normal.Graphics
    g.DrawImage(bmp, 0, 0)
    g.Drawstring(validfrom, font, pen, brush, 10, 30)
    g.Drawstring(validto, font, pen, brush, 10, 10)
    
    ' Storing the document
    doc.Save("Sample.pdf")
    doc.Close(True)
```

### Code Example 2: Loading and Adding Another Signature to a PDF Document

```vb
    ' Load the signed document
    Dim document As PdfLoadedDocument = New PdfLoadedDocument("Sample.pdf")
    page = document.Pages.Add()
    
    ' Adding a signature
    Dim signature1 As PdfSignature = New PdfSignature(document, page, pfdCert, "Signature 2")
    Dim bmp1 As PdfBitmap = New PdfBitmap("..\\Image.jpg")
    signature1.Bounds = New RectangleF(New PointF(5,5), bmp1.PhysicalDimension)
    signature1.ContactInfo = "Roase@owned.us"
    signature1.LocationInfo = "London, UAE"
    signature1.Reason = "I am second author of this document."
    validto = "Valid To: " & signature1.Certificate.ValidTo.ToString()
    validfrom = "Valid From: " & signature1.Certificate.ValidFrom.ToString()
    
    brush = New PdfSolidBrush(New PdfColor(1, 1, 255))
    pen = New PdfPen(brush, 1)
    font = New PdfStandardFont(PdfFontFamily.Courier, 12, PdfFontStyle.Regular)
    g = signature1.Appearence.Normal.Graphics
    g.DrawImage(bmp1, 100,400)
    g.Drawstring(validfrom, font, pen, brush, 10, 30)
    g.Drawstring(validto, font, pen, brush, 10, 10)
    
    ' Store the document
    document.Save("Sample1.pdf")
```

### 4.3 PDF Form

In the previous sections, we have seen the procedure to create a pdf document, its properties and various editing options of the loaded document. In this section, we will see how to create and work with forms by using Essential PDF under the following topics.
<!-- tags: [pdf, signatures, forms, essentialpdf, documentcreation, documentediting, user/guide, syncfusion-winforms, 11.4.0.26] keywords: [essentialpdf, pdf creation, pdf editing, pdf signatures, forms, document storage, document loading, document saving, pdfloadeddocument, pdfsignature, pdffont, pdfpen, pdfbitmap, document properties, document editing options, user guide, documentation] -->
```