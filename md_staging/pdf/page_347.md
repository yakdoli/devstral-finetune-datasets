```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_347.jpeg
document_name: pdf
page_number: 347
page_id: pdf#page_347
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:23Z
fidelity: lossless
-->

# Essential PDF

```csharp
lighting.Style = Pdf3DLightingStyle.Headlamp;

// Create the default view.
Pdf3DProjection projection1 = new Pdf3DProjection(Pdf3DProjectionType.Perspective);
projection1.FieldOfView = 50;
projection1.ClipStyle = Pdf3DProjectionClipStyle.ExplicitNearFar;
projection1.NearClipDistance = 10;

Pdf3DView defaultView = CreateView("Default View", new float[] { -0.382684f,
0.92388f, -0.0000000766026f, 0.18024f, 0.0746579f, 0.980785f, 0.906127f,
0.37533f, -0.19509f, -122.669f, -112.432f, 45.6829f }, 131.695f, projection, rendermode, lighting);

annot.Views.Add(defaultView);

// Add the pdf Annotation.
page.Annotations.Add(annot);
```

## [VB.NET]

```vb.net
' Pdf 3D Annotation
Dim annot As Syncfusion.Pdf.Interactive.Pdf3DAnnotation = New Syncfusion.Pdf.Interactive.Pdf3DAnnotation(New RectangleF(10, 70, 150, 150), "..\..\Data\AQuick Example.u3d")

' Create font, font style and brush.
Dim f As Font = New Font("Calibri", 11, FontStyle.Regular)
Dim font As Syncfusion.Pdf.Graphics.PdfFont = New Syncfusion.Pdf.Graphics.PdfTrueTypeFont(f, False)
Dim brush As Syncfusion.Pdf.Graphics.PdfBrush = New Syncfusion.Pdf.Graphics.PdfSolidBrush(color.DarkBlue)
Dim bgbrush As Syncfusion.Pdf.Graphics.PdfBrush = New Syncfusion.Pdf.Graphics.PdfSolidBrush(color.WhiteSmoke)
Dim color As Syncfusion.Pdf.Graphics.PdfColor = New Syncfusion.Pdf.Graphics.PdfColor(color.Thistle)

page.Graphics.DrawRectangle(bgbrush, New RectangleF(10, 270, 150, 150))

' Pdf 3D Appearance
annot.Appearance = New PdfAppearance(annot)
annot.Appearance.Normal.Graphics.DrawString("Click to activate", font, brush, New PointF(40, 40))
annot.Appearance.Normal.Draw(page, New PointF(annot.Location.X, annot.Location.Y))

Dim projection As Syncfusion.Pdf.Interactive.Pdf3DProjection = New
```

<!-- tags: [Syncfusion Winforms, Essential PDF, Pdf3DAnnotation, Pdf3DProjection, Pdf3DView, VB.NET] keywords: [Pdf3DLightingStyle, perspective projection, font, brush, appearance, Annotation] -->
```