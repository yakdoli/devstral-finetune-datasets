```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_363.jpeg
document_name: pdf
page_number: 363
page_id: pdf#page_363
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:18Z
fidelity: lossless
-->

## Essential PDF

```csharp
pdfLightTable.Draw(pdfGraphics, xPos, yPos, width)
pdfLightTable.Draw(pdfPage, xPos, yPos, width)
pdfLightTable.Draw(pdfPage, xPos, yPos, width, pdfLightTableLayoutFormat)
```

```csharp
' Draw PdfGrid with specified width.
pdfGrid.Draw(pdfGraphics, PointF.Empty, width)
pdfGrid.Draw(pdfGraphics, xPos, yPos, width)
pdfGrid.Draw(pdfPage, xPos, yPos, width)
pdfGrid.Draw(pdfPage, xPos, yPos, width, pdfGridLayoutFormat)
```

### 5.1.2.10 How to specify bounds for Table during pagination?

When PdfLightTable or PdfGrid is paginated, by default it will occupy the entire client area of the PdfPage. But, it is possible to specify bounds for the additional pages using PaginateBounds property of PdfLightTableLayoutFormat or PdfGridLayoutFormat class.

```csharp
format.PaginateBounds = new RectangleF(50, 50, 500, 300);
```

```vb.net
format.PaginateBounds = New RectangleF(50, 50, 500, 300)
```

## 5.2 PDF Editing

This section shows some specific tasks that are supported in a PDF document editing.

### 5.2.1 How To Access Pages In an Existing Document?

Pages in the existing document are different from pages in the newly created document. PdfPageBase class is used to manipulate the existing page in a loaded document. The following code example illustrates how to access the existing page.

```csharp
PdfLoadedDocument lDoc = new PdfLoadedDocument(txtUrl.Text);
PdfPageBase lPage = lDoc.Pages[0];
```

## (Footer)
© 2013 Syncfusion. All rights reserved.  363 | Page
```

<!-- tags: [pdf, pdf table, pagination, pdf editing, accessed pages] keywords: [PdfLightTable, PdfGrid, Pagination, Bounds, PaginateBounds, pdfDocument, pdfPageBase, AccessPages, PdfLoadedDocument] -->
```