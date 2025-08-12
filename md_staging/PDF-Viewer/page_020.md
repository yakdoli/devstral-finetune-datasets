```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: PDF Viewer
page_number: 020
page_id: PDF Viewer#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:57Z
fidelity: lossless
-->

# Essential PDF Viewer

| Method      | Description                                                                 | Parameters           | Returns | Result Type |
|-------------|-----------------------------------------------------------------------------|----------------------|---------|-------------|
| ZoomTo      | Magnifies the document displayed to the specified percentage.           | (int percentage)     | N/A     | Void        |

## 4.1.1.3 Events

### Table 3: Events Table

| Event               | Description                                                                 | Arguments | Type |
|---------------------|-----------------------------------------------------------------------------|----------|------|
| DocumentLoaded       | This event is triggered after the PDF is successfully loaded.             | N/A      | N/A  |
| HyperLinkMouseHover | This event is triggered when the mouse pointer is placed over the URL.    | N/A      | N/A  |
| HyperLinkMouseClicked | This event is triggered when the URL in the PDF document is clicked. | N/A      | N/A  |

## 4.1.2 Viewing PDF Files

A PDF can be loaded into the PDF Viewer either through the File Open dialog available in the toolbar or through the Load method. It also requests passwords to open encrypted documents.

```csharp
// Initialize PDF Viewer.
PdfViewerControl pdfViewer1 = new PdfViewerControl();

// Load the PDF.
pdfViewer1.Load("Template.pdf");
```

```vb.NET
```

<!-- tags: [Syncfusion Winforms, PDF Viewer, Events, Methods, Parameters, Returns, Loaded Files, Hyperlinks, Mouse Events, Loading PDF, Passwords] keywords: [Events Table, ZoomTo, DocumentLoaded, HyperLinkMouseHover, HyperLinkMouseClicked, Load method, File Open dialog, Encrypted documents, Initializing PDF Viewer, Loading PDF Files, GLC Functions, GLC PDF Viewer, API Reference, C#, VB.NET] -->
``` 
