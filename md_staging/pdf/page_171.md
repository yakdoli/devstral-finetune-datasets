```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: pdf
page_number: 171
page_id: pdf#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:31Z
fidelity: lossless
-->

## Overview
- This page demonstrates how to work with annotations in PDF documents using the Syncfusion Pdf library. It covers creating and configuring various types of annotations such as pop-up annotations, URI annotations, and document link annotations.

## Content

### Adding Annotations to a PDF Document

#### C# Example
```csharp
documentAnnotation.Color = new PdfColor(Color.Navy);
documentAnnotation.Border.Width = 3;
documentAnnotation.Border.HorizontalRadius = 25;
documentAnnotation.AnnotationFlags = AnnotationFlags.NoRotate;
PdfPage page2 = document.Pages.Add();
documentAnnotation.Destination = new PdfDestination(page2);
documentAnnotation.Destination.Location = new Point(0, 0);
documentAnnotation.Destination.Zoom = 5;
page.Annotations.Add(documentAnnotation);
```

#### VB.NET Example
```vb
Dim popupAnnotationRectangle As RectangleF = New RectangleF(0, 50, 50, 50)
Dim popupAnnotation As Syncfusion.Pdf.Interactive.PdfPopupAnnotation = New Syncfusion.Pdf.Interactive.PdfPopupAnnotation(popupAnnotationRectangle, "Test popup annotation")
popupAnnotation.Border.Width = 4
popupAnnotation.Icon = PopupIcon.NewParagraph
page.Annotations.Add(popupAnnotation)

Dim uriAnnotationRectangle As RectangleF = New RectangleF(0, 100, 80, 20)
Dim uriAnnotation As Syncfusion.Pdf.Interactive.PdfUriAnnotation = New Syncfusion.Pdf.Interactive.PdfUriAnnotation(uriAnnotationRectangle, "http://www.google.com")
page.Annotations.Add(uriAnnotation)

Dim docLinkAnnotationRectangle As RectangleF = New RectangleF(0, 200, 80, 20)
Dim documentAnnotation As Syncfusion.Pdf.Interactive.PdfDocumentLinkAnnotation = New Syncfusion.Pdf.Interactive.PdfDocumentLinkAnnotation(docLinkAnnotationRectangle)
documentAnnotation.Text = "Document link annotation"
documentAnnotation.Color = New PdfColor(Color.Navy)
documentAnnotation.Border.Width = 3
documentAnnotation.Border.HorizontalRadius = 25
documentAnnotation.AnnotationFlags = AnnotationFlags.NoRotate
Dim page2 As Syncfusion.Pdf.PdfPage = document.Pages.Add()
documentAnnotation.Destination = New PdfDestination(page2)
documentAnnotation.Destination.Location = New Point(0, 0)
documentAnnotation.Destination.Zoom = 5
page.Annotations.Add(documentAnnotation)
```

### Getting Annotation from existing PDF Document

## API Reference

### Namespace: Syncfusion.Pdf.Interactive

#### Classes
- `PdfPopupAnnotation`
- `PdfUriAnnotation`
- `PdfDocumentLinkAnnotation`
- `PdfDestination`
- `PdfColor`
- `Point`

#### Methods/Properties
- `Color`: Gets or sets the color of the annotation.
- `Border.Width`: Gets or sets the width of the border.
- `Border.HorizontalRadius`: Gets or sets the horizontal radius of the border.
- `AnnotationFlags`: Gets or sets the annotation flags.
- `Destination`: Gets or sets the destination of the annotation.
- `Destination.Location`: Gets or sets the location of the destination.
- `Destination.Zoom`: Gets or sets the zoom level of the destination.

## Code Examples

### C# Example for Adding Annotations
This example demonstrates how to add annotations to a PDF document using the SyncfusionPdf library.

### VB.NET Example for Adding Annotations
This example shows how to work with pop-up annotations, URI annotations, and document link annotations in a PDF document using VB.NET.

## Page-level Navigation/TOC (if applicable)
This page provides a structured approach to adding and configuring annotations in a PDF document, including examples in both C# and VB.NET.

## Cross References
See also:
- [Unclear] Additional PDF functionality in the Syncfusion documentation.
- [Unclear] Related features and methods in the Syncfusion.Pdf.Interactive namespace.

<!-- tags: [Syncfusion, Winforms, PDF, Annotations] keywords: [PdfAnnotation, PdfPopupAnnotation, PdfUriAnnotation, PdfDocumentLinkAnnotation, PdfDestination, Color, Border, Destination, Zoom, Annotations] -->
```