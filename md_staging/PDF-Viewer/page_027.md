```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: PDF Viewer
page_number: 027
page_id: PDF Viewer#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:26Z
fidelity: lossless
-->

## Essential PDF Viewer

### Load a specific page?

Navigation to a specific page, through code, is possible using the GoToPageAtIndex method.

```csharp
pdfViewer1.GoToPageAtIndex(2);
```

```vb
pdfViewer1.GoToPageAtIndex(2)
```

### Load PDF without Toolstrip in Viewer?

In order to view PDF without the toolbar, make use of the PdfDocumentView control instead of PdfViewerControl. Other features and options are similar to PdfViewerControl.

```csharp
PdfDocumentView pdfDocumentView1 = new PdfDocumentView();
pdfDocumentView1.Load(@"Template.pdf");
```

```vb
Dim pdfDocumentView1 As New PdfDocumentView()
pdfDocumentView1.Load("Template.pdf")
```

The following is the image of a PDF document viewed in PdfDocumentView.

---

Page © 2013 Syncfusion. All rights reserved.
```

<!-- tags: [Syncfusion Winforms, PDF Viewer, GoToPageAtIndex, PdfDocumentView] keywords: [navigation, specific page, toolstrip, features, options] -->
```