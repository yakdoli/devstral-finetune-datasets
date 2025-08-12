```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_173.jpeg
document_name: pdf
page_number: 173
page_id: pdf#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:41Z
fidelity: lossless
-->

## Essential PDF

Pdf3DAnnotation specifies parameters to be applied to the virtual camera associated with a 3D annotation. These parameters include orientation and position of the camera, details regarding the projection of camera coordinates onto the target coordinate system of the annotation, and a description of the background on which the artwork is to be drawn.

The following code example illustrates how to embed a 3D file.

### Example: Embedding a 3D File

```csharp
// Pdf 3D Annotation
Pdf3DAnnotation annotation = new Pdf3DAnnotation(new RectangleF(10, 270, 270, 150), @"..\..\Data\box.u3d");
```

```vbnet
' Pdf 3D Annotation
Dim annotation As Syncfusion.Pdf.Interactive.Pdf3DAnnotation = New Syncfusion.Pdf.Interactive.Pdf3DAnnotation(New RectangleF(10, 270, 270, 150), "..\..\Data\box.u3d")
```

## Pdf3DView

Pdf3DView class specifies parameters to be applied to the virtual camera associated with a 3D annotation. These parameters include orientation and position of the camera, details regarding the projection of camera coordinates onto the target coordinate system of the annotation, and a description of the background on which the artwork is to be drawn.

### Example: Configuring a 3D View

```csharp
// Pdf 3D View
Pdf3DView view = new Pdf3DView();
view.ExternalName = "Default View";
```

```vbnet
' Pdf 3D View
Dim view As Syncfusion.Pdf.Interactive.Pdf3DView = New Syncfusion.Pdf.Interactive.Pdf3DView()
view.ExternalName = "Default View"
```

## Pdf3DProjection

<!-- tags: [Syncfusion Winforms, Essential PDF, 3D Annotations, Pdf3DAnnotation, Pdf3DView, Pdf3DProjection] keywords: [3D annotation, virtual camera, projection, background, 3D file embedding] -->
```