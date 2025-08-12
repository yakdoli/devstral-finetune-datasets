```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_177.jpeg
document_name: pdf
page_number: 177
page_id: pdf#page_177
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:55Z
fidelity: lossless
-->

# Essential PDF

You can specify the rendering style for the 3D artwork by using the Pdf3DRenderMode class. For example, surfaces may be filled with opaque colors, they may be stroked as a "wireframe", or the artwork may be rendered with special lighting effects.

The following are the rendering styles supported by the Pdf3DRenderMode class.

- Solid
- SolidWireframe
- Transparent
- TransparentWireframe
- BoundingBox
- TransparentBoundingBox
- TransparentBoundingBoxOutline
- Wireframe
- ShadedWireframe
- HiddenWireframe
- Vertices
- ShadedVertices
- Illustration
- SolidOutline
- ShadedIllustration

Apart from using the Style property, you can also change the rendering style by using the following properties.

- **AuxiliaryColor**: PdfColor name that specifies the auxiliary color to be used when rendering the 3D image. The first entry in the array is a color space; the subsequent entries are values specifying color values in that color space.
- **FaceColor**: PdfColor name that specifies the face color to be used when rendering the 3D image. This entry is relevant only when the Style property is set to Illustration.
- **Opacity**: Number specifying the opacity of the added transparency applied by some render modes using a standard additive blend. Default value is **0.5**.
- **CreaseValue**: Number specifying the angle in degrees to be used as the crease value while determining silhouette edges. Default value is **45**.

The following code example illustrates this.

```csharp
Pdf3DRendermode rendermode = new Pdf3DRendermode();
rendermode.Style = Pdf3DRenderStyle.Solid;
view.RenderMode = renderMode;
```

## API Reference

### Pdf3DRenderMode

#### Properties
- **Style**: The rendering style of the 3D object. Default is `Pdf3DRenderStyle.Solid`.

#### Methods
- **SetAuxiliaryColor**: Sets the auxiliary color for rendering.
- **SetFaceColor**: Sets the face color for rendering.

## Code Examples

### C#

```csharp
Pdf3DRendermode rendermode = new Pdf3DRendermode();
rendermode.Style = Pdf3DRenderStyle.Solid;
view.RenderMode = renderMode;
```

### VB.NET

```vb
Dim rendermode As Pdf3DRendermode = New Pdf3DRendermode()
rendermode.Style = Pdf3DRenderStyle.Solid
view.RenderMode = renderMode
```

### Remarks

You can customize the rendering style of 3D objects by setting the `Style` property of the `Pdf3DRenderMode` class. Additionally, properties like `AuxiliaryColor`, `FaceColor`, `Opacity`, and `CreaseValue` allow for more fine-grained control over the appearance and behavior of the rendered 3D objects.

<!-- tags: [pdf, 3d, render, style, opacity, wireframe, transparent, solid, shaded] keywords: [Pdf3DRenderMode, style, opacity, wireframe, transparent, facecolor, auxiliarycolor, creasevalue, pdf3DRenderStyle, illustrate] -->
```