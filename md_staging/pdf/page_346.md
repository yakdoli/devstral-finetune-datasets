```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_346.jpeg
document_name: pdf
page_number: 346
page_id: pdf#page_346
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:15Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Essential PDF provides support to embed collections of three-dimensional objects (such as those used by CAD software) in PDF files using the `Pdf3DAnnotation` class.
- Demonstrates how to embed a U3D file in a PDF document.

## Content

### Embedding a U3D File

The following code example illustrates how to embed a U3D file in a PDF document.

```csharp
[C#]

// Pdf 3D Annotation
Pdf3DAnnotation annot = new Pdf3DAnnotation(new RectangleF(10, 70, 150, 150), @"...\Data\AQuick Example.u3d");

// Create font, font style and brush.
Font f = new Font("Calibri", 11, FontStyle.Regular);
PdfFont font = new PdfTrueTypeFont(f, false);
PdfBrush brush = new PdfSolidBrush(Color.DarkBlue);
PdfBrush bbrush = new PdfSolidBrush(Color.WhiteSmoke);
PdfColor color = new PdfColor(Color.Thistle);

page.Graphics.DrawRectangle(bbrush, new RectangleF(10, 270, 150, 150));

// Pdf 3D Appearance
annot.Appearance = new PdfAppearance(annot);
annot.Appearance.Normal.Graphics.DrawString("Click to activate", font, brush, new PointF(40, 40));
annot.Appearance.Normal.Draw(page, new PointF(annot.Location.X, annot.Location.Y));

Pdf3DProjection projection = new Pdf3DProjection();
projection.ProjectionType = Pdf3DProjectionType.Perspective;

projection.FieldOfView = 10;
projection.ClipStyle = Pdf3DProjectionClipStyle.ExplicitNearFar;
projection.NearClipDistance = 10;

Pdf3DActivation activation = new Pdf3DActivation();
activation.ActivationMode = Pdf3DActivationMode.ExplicitActivation;
activation.ShowToolbar = false;
annot.Activation = activation;

Pdf3DBackground background = new Pdf3DBackground();
background.Color = color;

Pdf3DRendermode rendermode = new Pdf3DRendermode();
rendermode.Style = Pdf3DRenderStyle.Solid;

Pdf3DLighting lighting = new Pdf3DLighting();
```

## API Reference

### Classes
- **Pdf3DAnnotation**
  - Used to embed a 3D annotation.
- **PdfAppearance**
  - Defines the appearance of the 3D annotation.
- **Pdf3DProjection**
  - Specifies the projection settings for the 3D content.
- **Pdf3DActivation**
  - Configure the activation behavior of the 3D content.
- **Pdf3DBackground**
  - Sets the background color for the 3D content.
- **Pdf3DRendermode**
  - Defines the rendering style for the 3D content.
- **Pdf3DLighting**
  - Specifies the lighting settings for the 3D content.

### Parameters
- **RectangleF**: The location and size of the annotation.
- **Font**: Font settings for the text on the 3D annotation.
- **PdfActivationMode**: The mode for activating the 3D content.
- **PdfClipStyle**: The type of clipping for the 3D projection.
- **PdfRenderStyle**: The rendering style for the 3D content.

## Code Examples

The above code demonstrates how to:
1. Create a `Pdf3DAnnotation` object.
2. Define the appearance, projection, activation, background, rendering, and lighting styles for the 3D content.

## RAG Annotations

<!-- tags: [syncfusion, pdf, 3d annotation, u3d, winforms, 11.4.0.26] keywords: [Pdf3DAnnotation, PdfAppearance, Pdf3DProjection, Pdf3DActivation, Pdf3DBackground, Pdf3DRendermode, Pdf3DLighting, embedding 3D content, CAD objects, U3D file] -->
```