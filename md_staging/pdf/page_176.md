```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_176.jpeg
document_name: pdf
page_number: 176
page_id: pdf#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:37Z
fidelity: lossless
-->

### Setting Activation and Deactivation Modes

```csharp
annotation.Activation = activation
```

---

### Deactivation Mode Using Pdf3DDeactivationMode

**Note:** You can also set the deactivation mode by using the `Pdf3DDeactivationMode` class.

---

### Pdf3DBackground

Pdf3DBackground defines the background over which the 3D artwork is to be drawn. You can apply background color to the entire annotation by enabling the `ApplyToEntireAnnotation` property. If set to `False`, the background should apply only to the rectangle that is specified by the 3D view box of the annotation. Default value is `False`.

---

#### Code Example: Applying Background

##### C#

```csharp
PdfColor color = new PdfColor(Color.Silver);
Pdf3DBackground background = new Pdf3DBackground();
background.Color = color;
background.ApplyToEntireAnnotation = true;

// Setting Background color to current view.
view.Background = background;
```

##### VB.NET

```vb
Dim color As Syncfusion.Pdf.Graphics.PdfColor = New Syncfusion.Pdf.Graphics.PdfColor(color.Silver)

Dim background As Syncfusion.Pdf.Interactive.Pdf3DBackground = New Syncfusion.Pdf.Interactive.Pdf3DBackground()
background.Color = color
background.ApplyToEntireAnnotation = True

' Setting Background color to current view.
view.Background = background
```

---

### Pdf3DRenderMode

```markdown
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [pdf, background, deactivation, annotation, color, 3D, rendering, Syncfusion Winforms, Pdf3DBackground, Pdf3DRenderMode] keywords: [PdfColor, ApplyToEntireAnnotation, Pdf3DDeactivationMode, background color, default settings, 3D annotation, rendering mode, C#, VB.NET] -->
```