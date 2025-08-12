```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: PDF Viewer
page_number: 026
page_id: PDF Viewer#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:26Z
fidelity: lossless
-->

## 5 How To

This section will help you find answers to common questions regarding Essential Pdf Viewer.

### 5.1 View the PDF stream in viewer?

PDF files as stream can be viewed in Essential Pdf Viewer using the overload available in the Load method. Following are the code snippets.

```csharp
[C#]
FileStream stream = new FileStream("Template.pdf", FileMode.Open);
//Initialize PDF Viewer
PdfViewerControl pdfViewer1 = new PdfViewerControl();
  
//Load the PDF
pdfViewer1.Load(stream);
```

```vb.net
[VB.NET]
Dim stream As New FileStream("Template.pdf", FileMode.Open)

' Initialize PDF Viewer
Dim pdfViewer1 As New PdfViewerControl()

' Load the PDF
pdfViewer1.Load(stream)
```

### 5.2 Get page count?

The number of pages as viewed in the PDF Viewer can be found by using PageCount property.

```csharp
[C#]
int count = pdfViewer1.PageCount;
```

<!-- tags: [PDF Viewer, Essential PDF Viewer, Page Count, Stream, Load Method, C#, VB.NET] keywords: [PDF, viewer, stream, load, PageCount, essential] -->
```