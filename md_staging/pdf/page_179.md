```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_179.jpeg
document_name: pdf
page_number: 179
page_id: pdf#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:10Z
fidelity: lossless
-->

# Essential PDF

```csharp
Pdf3DCrossSection csection = new Pdf3DCrossSection();
csection.IntersectionColor = color;
csection.IntersectionIsVisible = 50;
view.CrossSections = csection;
```

```vb.net
Dim csection As Syncfusion.Pdf.Interactive.Pdf3DCrossSection = New Syncfusion.Pdf.Interactive.Pdf3DCrossSection()
csection.IntersectionColor = color
csection.IntersectionIsVisible = 50
view.CrossSections = csection
```

## Hyperlinks for other external files

External files can be hyperlinked in a pdf document using the Annotation feature. An annotation can associate objects such as note, sound or a movie by specifying the corresponding object location in the document.

### Explanation

The external file can be linked to the document using the `PdfFileLinkAnnotation` class. This class allows you to create annotations that are associated with objects such as notes, sounds, or movies. By specifying the location of the object in the document, you can link the external file to the document.

### Code Example

```csharp
RectangleF flAnnotationRectangle = new RectangleF(0, 100, 80, 20);

// Create PdfFileLinkAnnotation to link external file
PdfFileLinkAnnotation flAnnotation = new PdfFileLinkAnnotation(flAnnotationRectangle, filename);

// Add the Annotation to the page
page.Annotations.Add(flAnnotation);
```

```vb.net
Dim flAnnotationRectangle As New RectangleF(0, 100, 80, 20)

' Create PdfFileLinkAnnotation to link external file
```

## Summary

This section explains how to create hyperlinks for external files in a PDF document using the `PdfFileLinkAnnotation` class. The process involves creating a `PdfFileLinkAnnotation` object and adding it to the document's annotations. The code examples demonstrate how to implement this functionality in both C# and VB.NET.

### Conclusion

By using the `PdfFileLinkAnnotation` class, you can easily hyperlink external files to your PDF documents, enhancing the interactivity and functionality of your documents. This feature is particularly useful for embedding various types of media and information within your PDFs.

## API Reference

### Namespaces and Classes
- `Syncfusion.Pdf.Interactive`
  - `PdfFileLinkAnnotation`

#### Parameters
- `RectangleF`: The rectangle that defines the boundaries of the annotation.
- `filename`: The path to the external file to be linked.

#### Methods
- `Add()`: Adds the annotation to the page.

## Code Examples

### C# Example

```csharp
RectangleF flAnnotationRectangle = new RectangleF(0, 100, 80, 20);

// Create PdfFileLinkAnnotation to link external file
PdfFileLinkAnnotation flAnnotation = new PdfFileLinkAnnotation(flAnnotationRectangle, filename);

// Add the Annotation to the page
page.Annotations.Add(flAnnotation);
```

### VB.NET Example

```vb.net
Dim flAnnotationRectangle As New RectangleF(0, 100, 80, 20)

' Create PdfFileLinkAnnotation to link external file

```

<!-- tags: [Essential PDF, Annotation, External File Link, PdfFileLinkAnnotation, Syncfusion Winforms, version: 11.4.0.26] keywords: [external files, hyperlink, annotation, PdfFileLinkAnnotation, document linking, interactivity] -->
```