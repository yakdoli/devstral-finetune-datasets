```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_348.jpeg
document_name: pdf
page_number: 348
page_id: pdf#page_348
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:14Z
fidelity: lossless
-->

# Essential PDF

## Content

### Setting up a PDF 3D Annotation

```vb
Syncfusion.Pdf.Interactive.Pdf3DProjection()
projection.ProjectionType = Pdf3DProjectionType.Perspective

projection.FieldOfView = 10
projection.ClipStyle = Pdf3DProjectionClipStyle.ExplicitNearFar
projection.NearClipDistance = 10

Dim activation As Syncfusion.Pdf.Interactive.Pdf3DActivation = New Syncfusion.Pdf.Interactive.Pdf3DActivation()
activation.ActivationMode = Pdf3DActivationMode.ExplicitActivation
activation.ShowToolbar = False
annot.Activation = activation

Dim background As Syncfusion.Pdf.Interactive.Pdf3DBackground = New Syncfusion.Pdf.Interactive.Pdf3DBackground()
background.Color = color

Dim rendermode As Syncfusion.Pdf.Interactive.Pdf3DRendormode = New Syncfusion.Pdf.Interactive.Pdf3DRendormode()
rendermode.Style = Pdf3DRenderStyle.Solid

Dim lighting As Syncfusion.Pdf.Interactive.Pdf3DLighting = New Syncfusion.Pdf.Interactive.Pdf3DLighting()
lighting.Style = Pdf3DLightingStyle.Headlamp

' Create the default view.
Dim projection1 As Syncfusion.Pdf.Interactive.Pdf3DProjection = New Syncfusion.Pdf.Interactive.Pdf3DProjection(Pdf3DProjectionType.Perspective)
projection1.FieldOfView = 50
projection1.ClipStyle = Pdf3DProjectionClipStyle.ExplicitNearFar
projection1.NearClipDistance = 10

Dim defaultValue As Syncfusion.Pdf.Interactive.Pdf3DView = CreateView("Default View", New Single() {-0.382684F, 0.92388F, -0.000000766026F, 0.18024F, 0.0746579F, 0.980785F, 0.906127F, 0.37533F, -0.19509F, -122.669F, -112.432F, 45.6829F}, 131.695F, background, projection, rendermode, lighting)

annot.Views.Add(defaultView)

' Add the pdf Annotation.
page.Annotations.Add(annot)
```

### 5.1.1.7 How To Embed Fonts?

You can embed fonts by using True type fonts. The following code example illustrates this.

## API Reference

### WinForms-specific conventions

This section describes the conventions and guidelines for working with WinForms-specific controls and namespaces in the Syncfusion framework.

### Code Examples

```vb
' Example of embedding fonts in a PDF document.
Dim pdfDocument As New PdfDocument()
Dim pdfSection As PdfSection = pdfDocument.Sections.Add()

Dim font As New PdfInstalledFont("Arial", True)
Dim embeddedFont As New PdfTrueTypeFont(font, True)

Dim fontSettings As New PdfFontSettings()
fontSettings.Font = embeddedFont

Dim content As New PdfContent()
content.BeginText()
content.SetFont(fontSettings)
content.SetFontColor(PdfColor.Black)
content.SetTextPosition(30, 715)
content.DrawString("Hello, World!")
content.EndText()

pdfSection.Contents.Add(content)

pdfDocument.Save("EmbeddedFont.pdf")
```

### Additional References

See also: [How to Create a PDF with Embedded Fonts](#how-to-create-a-pdf-with-embedded-fonts)

## Page-level Navigation/TOC

- [How To Embed Fonts?](#5.1.1.7)

```html
<!-- tags: [syncfusion, winforms, pdf, embed fonts, TrueType fonts, version: 11.4.0.26] keywords: [pdf, embed fonts, TrueType fonts, Syncfusion PDF, WinForms] -->
```