```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_364.jpeg
document_name: pdf
page_number: 364
page_id: pdf#page_364
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:26Z
fidelity: lossless
-->

## Overview

- Demonstrates how to write text on a loaded page in a PDF document.
- Explains how to add watermarks or stamps in an existing document.
- Provides sample C# and VB.NET code for manipulating a PDF document.

## Content

### Chapter 5: Essential PDF

#### 5.2.2 How To Add Watermarks Or Stamps In an Existing Document?

You can add watermarks or stamps in an existing document by adding transparent images or text on the pages. The following code example illustrates this.

##### C#

```csharp
PdfGraphics g = lPage.Graphics;
g.DrawString("Writing text in loaded page", font, PdfPens.Red, PdfBrushes.Red, new PointF(-150, 450));
lDoc.Save("Sample.pdf");
```

##### VB.NET

```vbnet
Dim lDoc As PdfLoadedDocument = New PdfLoadedDocument(txtUrl.Text)
Dim lPage As PdfPageBase = lDoc.Pages(0)
Dim g As PdfGraphics = lPage.Graphics
g.DrawString("Writing text in loaded page", font, PdfPens.Red, PdfBrushes.Red, New PointF(-150, 450))
lDoc.Save("Sample.pdf")
```

##### C#

```csharp
PdfLoadedDocument lDoc = new PdfLoadedDocument(txtUrl.Text);
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 36f);

foreach (PdfPageBase lPage in lDoc.Pages)
{
    PdfGraphics g = lPage.Graphics;
    PdfGraphicsState state = g.Save();
    g.SetTransparency(0.25f);
    g.RotateTransform(-40);
    g.DrawString("Stamping text", font, PdfPens.Red, PdfBrushes.Red, new PointF(-150, 450));
    }
lDoc.Save("Sample.pdf");
```

##### VB.NET

```vbnet
Dim lDoc As PdfLoadedDocument = New PdfLoadedDocument(txtUrl.Text)
Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, 36.0F)

Dim lPage As PdfPageBase
For Each lPage In lDoc.Pages
```

## References

For more information on Syncfusion PDF functionalities, refer to the official documentation.

## RAG Annotations

This section includes examples and explanations on how to manipulate PDF documents using Syncfusion's PDF library. It demonstrates adding text and creating watermarks or stamps.

<!-- tags: [PDF, Syncfusion, watermark, stamp, loaded document] keywords: [Write text, add stamp, modify PDF,_ASYNC_API, Syncfusion PDF library] -->
```