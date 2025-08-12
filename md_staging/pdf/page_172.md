```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: pdf
page_number: 172
page_id: pdf#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:18Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Essential PDF now supports reading annotations from an existing PDF document.
- Demonstrates how to access and modify annotations in a PDF file using both C# and VB.NET.
- Provides details on 3D Annotations within PDF documents.

## Content

### Reading and Modifying Annotations

Essential PDF now supports reading annotations from the existing PDF document. The following code example illustrates this.

#### C# Code Example
```csharp
PdfLoadedDocument ldoc = new PdfLoadedDocument("Sample.pdf");
PdfPageBase lpage = ldoc.Pages[1];
PdfLoadedAttachmentAnnotation attAnnot = lpage.Annotations[0] as PdfLoadedAttachmentAnnotation;
attAnnot.Color = new PdfColor(Color.Red);
attAnnot.Text = "New Annotation";
attAnnot.Icon = PdfAttachmentIcon.PushPin;
```

#### VB.NET Code Example
```vb
Dim ldoc As PdfLoadedDocument = New PdfLoadedDocument("Sample.pdf")
Dim lpage As PdfPageBase = ldoc.Pages(1)
Dim attAnnot As PdfLoadedAttachmentAnnotation = TryCast(lpage.Annotations(0), PdfLoadedAttachmentAnnotation)
attAnnot.Color = New PdfColor(Color.Red)
attAnnot.Text = "New Annotation"
attAnnot.Icon = PdfAttachmentIcon.PushPin
```

### 3D Annotation

#### Overview
3D Annotations are the means by which 3D artwork is represented in a PDF document. Essential PDF can embed the 3D files (u3d) in PDF files. It provides a way to interact with the user by using the mouse and keyboard.

#### Controlling the Annotation
You can control the annotation with the help of the following classes.

- Pdf3DAnnotation
- Pdf3DView
- Pdf3DProjection
- Pdf3DActivation
- Pdf3DBackground
- Pdf3DRenderMode
- Pdf3DLighting
- Pdf3DCrossSection

#### Pdf3DAnnotation

### API Reference

#### Classes
- `Pdf3DAnnotation`
- `Pdf3DView`
- `Pdf3DProjection`
- `Pdf3DActivation`
- `Pdf3DBackground`
- `Pdf3DRenderMode`
- `Pdf3DLighting`
- `Pdf3DCrossSection`

#### Key Functionality
- Embeds 3D files (u3d) within PDF files.
- Enables interaction through mouse and keyboard.

## Code Examples

#### C# Example
```csharp
// Example of creating a 3D annotation
Pdf3DAnnotation annotation = new Pdf3DAnnotation(300, 300, 300, 300);
annotation.U3DFile.Add(new U3DFile(filename));
```

#### VB.NET Example
```vb
' Example of creating a 3D annotation
Dim annotation As Pdf3DAnnotation = New Pdf3DAnnotation(300, 300, 300, 300)
annotation.U3DFile.Add(New U3DFile(filename))
```

### Cross References
- For more information on working with annotations in PDFs, refer to the Annotations section in the Essential PDF documentation.

<!-- tags: [pdf, annotations, 3d, embedding, interaction] keywords: [essential pdf, pdf annotations, 3d artwork, 3D Annotations, user interaction, mouse, keyboard, embedding 3D files, u3d, annotations, designing, modification, interaction] -->
```