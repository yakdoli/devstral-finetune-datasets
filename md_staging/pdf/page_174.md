```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: pdf
page_number: 174
page_id: pdf#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:27Z
fidelity: lossless
-->

## Overview
- Pdf3DProjection defines the mapping of 3D camera coordinates onto the target coordinate system, specifying the type of projection (Orthographic or Perspective).
- Near and far plane clipping is supported to control object visibility based on distance from the camera.

## Content

### Pdf3DProjection

Pdf3DProjection defines the mapping of 3D camera coordinates onto the target coordinate system of the annotation. Using this class, you can specify the type of Projection, which determines how objects are projected onto the near plane and scaled. The possible values are **Orthographic** projection and **Perspective** projection.

Pdf3DProjection supports both near and far clipping. This type of clipping defines a near plane and a far plane. Objects or parts of objects that are beyond the far plane or closer to the camera than the near plane are not drawn.

#### Example: Setting 3D Projection Properties

**C#**
```csharp
Pdf3DView view = new Pdf3DView();

Pdf3DProjection projection = new Pdf3DProjection();
projection.ProjectionType = Pdf3DProjectionType.Perspective;
projection.FieldOfView = 10;
projection.ClipStyle = Pdf3DProjectionClipStyle.ExplicitNearFar;
projection.NearClipDistance = 10;

view.Projection = projection;
```

**VB.NET**
```vb
Dim view As Syncfusion.Pdf.Interactive.Pdf3DView = New Syncfusion.Pdf.Interactive.Pdf3DView()

Dim projection As Syncfusion.Pdf.Interactive.Pdf3DProjection = New Syncfusion.Pdf.Interactive.Pdf3DProjection()
projection.ProjectionType = Pdf3DProjectionType.Perspective
projection.FieldOfView = 10
projection.ClipStyle = Pdf3DProjectionClipStyle.ExplicitNearFar
projection.NearClipDistance = 10

view.Projection = projection
```

#### Note
You can set the near or far distance by using the `NearClipDistance` property. If you want to set the clipping distance explicitly, you have to set the `ClipStyle` property to `ExplicitNearFar`.

### Pdf3DActivation
```


<!-- tags: [syncfusion, winforms, pdf, projection, annotation, orthographic, perspective, near-far-clipping, explicit-clipping, view-settings, 3d-view, pdf3dprojection] keywords: [Pdf3DProjection, ProjectionType, PerspectiveProjection, NearClipDistance, ExplicitNearFar, Pdf3DView, FieldOfView, Clipping] -->
```