```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: PDF Viewer
page_number: 024
page_id: PDF Viewer#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:10Z
fidelity: lossless
-->

## Overview
- Explains how to convert PDF pages to EMF images using VB.NET and C#.
- Describes specifying a page range for conversion in the PDF Viewer control.
- Demonstrates text search and highlighting functionality in the Essential PDF Viewer.

## Content

### Code Examples for Exporting as EMF

#### VB.NET
```vb
Dim img As Metafile = pdfViewer1.ExportAsMetafile(0)

' Save the image
img.Save("Sample.emf", ImageFormat.Emf)
```

#### C#
```csharp
Metafile[] img = pdfViewer1.ExportAsMetafile(0, 3);
```

#### VB.NET
```vb
Dim img() As Metafile = pdfViewer1.ExportAsMetafile(0, 3)
```

### 4.1.5 Text Search

Essential PDF Viewer allows end users to search and highlight the text in the PDF document. The search box will appear when Ctrl+F is pressed and searches the text in the PDF document as shown in the following figure.

![Searching a PDF](image.png)

**Figure 10: Searching a PDF**

## API Reference

### Methods

- **ExportAsMetafile**: Converts a range of pages in the PDF into a Metafile.

### Parameters

- **startIndex**: The starting page index for conversion.
- **endIndex**: The ending page index for conversion.

### Returns

- An array of Metafiles containing the specified page range.

## Code Examples

#### VB.NET
```vb
Dim img As Metafile = pdfViewer1.ExportAsMetafile(0)
img.Save("Sample.emf", ImageFormat.Emf)
```

#### C#
```csharp
Metafile[] img = pdfViewer1.ExportAsMetafile(0, 3);
```

#### VB.NET
```vb
Dim img() As Metafile = pdfViewer1.ExportAsMetafile(0, 3)
```

## Cross References

- For more information on exporting PDF pages, see the complete documentation on PDF Viewer.

<!-- tags: [syncfusion, pdf viewer, essentials pdf, export as metafile, vb.net, c#, text search] keywords: [PDF Viewer, ExportAsMetafile, Ctrl+F, text highlighting, metafile, page range, search functionality] -->
```