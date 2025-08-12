```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_289.jpeg
document_name: pdf
page_number: 289
page_id: pdf#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:28Z
fidelity: lossless
-->

# [VB.NET]

```vb
' Import all the pages to another document
doc2.ImportPageRange(doc2, 0, doc.Pages.Count)
```

**Note: To merge or append the document asynchronously for Windows Store apps, refer to the Asynchronous Support section.**

## 4.2.10.2 Import Pages As Templates

You can create a booklet or just place few pages onto a single one by converting the pages into a PdfTemplate object. This template can be scaled, rotated, placed at different coordinates, and so on. It enables you to customize the page representation as per your need.

The following code example illustrates how to import a page as a template.

### [C#]

```csharp
PdfPage page = doc1.Pages.Add();
PdfGraphics g = page.Graphics;

PdfPageBase lpage = doc2.Pages[0];
PdfTemplate template = lpage.CreateTemplate();

g.DrawPdfTemplate(template, PointF.Empty, page.GetClientSize());
```

### [VB.NET]

```vb
Dim doc As PdfLoadedDocument = New PdfLoadedDocument("../../../Data/sample.pdf")
Dim page As PdfPage = doc1.Pages.Add()
Dim g As PdfGraphics = page.Graphics

Dim lpage As PdfPageBase = doc2.Pages(0)
Dim template As PdfTemplate = lpage.CreateTemplate()

g.DrawPdfTemplate(template, PointF.Empty, page.GetClientSize())
```

## 4.2.10.3 Signature

<!-- tags: [syncfusion, winforms, pdf, template, pages, import, asynchronoussupport, document, merge, append, pdfloadeddocument, pdfpagetemplate, pdfgraphics, pointf, pdfpagebase] keywords: [pdf template, import pages, create template, draw template, pdfloadeddocument, asynchronous support, merge document, append document, coordinates, scale, rotate] -->
```