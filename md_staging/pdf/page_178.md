```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_178.jpeg
document_name: pdf
page_number: 178
page_id: pdf#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:42Z
fidelity: lossless
-->

## Overview
- Explains the configuration of rendering modes and lighting effects for 3D PDF artwork using Syncfusion's `Pdf3DRendermode` and `Pdf3DLighting` classes.
- Demonstrates how to specify different lighting schemes and apply them to 3D artwork.
- Introduces the concept of 3D cross sections and provides an example for its implementation.

## Content

### Pdf3DRendermode

#### Overview
The `Pdf3DRendermode` class is used to define the rendering style for 3D artwork in PDFs. Below is an example in VB.NET demonstrating how to apply a solid rendering style.

```vb
Dim rendermode As Syncfusion.Pdf.Interactive.Pdf3DRendermode = New Syncfusion.Pdf.Interactive.Pdf3DRendermode()
rendermode.Style = Pdf3DRenderStyle.Solid
view.RenderMode = renderMode
```

### Pdf3DLighting

#### Overview
The `Pdf3DLighting` class specifies the lighting applied to the 3D artwork. Various lighting effects are supported, as listed below:

- Artwork
- None
- White
- Day
- Night
- Hard
- Primary
- Blue
- Red
- Cube
- CAD
- Headlamp

The following example demonstrates how to apply a CAD lighting style in both C# and VB.NET.

#### Example in C#

```csharp
Pdf3DLighting lighting = new Pdf3DLighting();
lighting.Style = Pdf3DLightingStyle.CAD;
view.LightingScheme = lightingScheme;
```

#### Example in VB.NET

```vb
Dim lighting As Syncfusion.Pdf.Interactive.Pdf3DLighting = New Syncfusion.Pdf.Interactive.Pdf3DLighting()
lighting.Style = Pdf3DLightingStyle.CAD
view.LightingScheme = lightingScheme
```

### Pdf3DCrossSection

#### Overview
The `Pdf3DCrossSection` class allows specifying how a portion of the 3D artwork is clipped to show cross sections. The following example illustrates this concept.

#### Code Example
A code example demonstrating the use of `Pdf3DCrossSection` is provided. Although the specific implementation is not detailed here, it involves specifying how a 3D object should be clipped for cross-sectional viewing.

#### Explanation
By configuring the `Pdf3DCrossSection`, users can define planes or other geometric entities to clip the 3D model, thereby exposing internal structures or specific sections of the artwork.

## Summary
This section focuses on configuring rendering styles, lighting effects, and cross-sectional views for 3D PDF artwork using Syncfusion's WinForms libraries. The provided examples showcase how to implement these features programmatically in both C# and VB.NET.

<!-- tags: [Syncfusion, WinForms, 3D PDF, Pdf3DLighting, Pdf3DRendermode, Pdf3DCrossSection, API, version 11.4.0.26] keywords: [Syncfusion, WinForms, 3D PDF, Pdf3DLighting, Pdf3DRendermode, Pdf3DCrossSection, rendering, lighting, cross section] -->
```