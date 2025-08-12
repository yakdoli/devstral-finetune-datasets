```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_275.jpeg
document_name: diagram
page_number: 275
page_id: diagram#page_275
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:27Z
fidelity: lossless
-->

## Overview

- Explains how to export a diagram into a Word document.
- Involves saving the diagram in standard image formats and exporting them using Essential DocIO.

## Content

### 5.16 How To Export a Diagram Into a Word Document

To export a diagram into a Word document, follow the below given steps.

1. Save the diagram in any one of the standard image formats such as bitmaps, enhanced metafiles, SVG format files, and so forth.
2. Export the saved images to the Word document using Essential DocIO.

**Note**: To export the saved images to the Word document, you need to have Essential DocIO installed in your system.

#### Code Example: C#

```csharp
System.Drawing.Image diagramImage = new Bitmap(1, 1, PixelFormat.Format24bppRgb);
Graphics grfx = Graphics.FromImage(diagramImage);
IntPtr hdc = grfx.GetHdc();
Metafile emf = new Metafile(hdc, EmfType.EmfOnly);
Graphics emfGrfx = Graphics.FromImage(emf);
this.diagram1.View.ExportDiagramToGraphics(emfGrfx, true);
grfx.ReleaseHdc(hdc);
grfx.Dispose();
emfGrfx.Dispose();
diagramImage.Dispose();
WordDocument document = new WordDocument();

// Adding a new section to the document.
IWSection section = document.AddSection();

// Adding a paragraph to the section.
IWParagraph paragraph = section.AddParagraph();
WPicture mImage = (WPicture)paragraph.AppendPicture(emf);
document.Save("Sample.doc", Syncfusion.DocIO.FormatType.Doc);
System.Diagnostics.Process.Start("Sample.doc");
```

#### Code Example: VB.NET

```vb
' The VB.NET code block is not provided in the image. Please refer to the C# example for implementation details.
```

### Page-level Navigation/TOC (if applicable)

- How To Export a Diagram Into a Word Document

---

## API Reference (if applicable)

- **Namespace**: System.Drawing
  - Methods: Bitmap, Graphics.FromImage
- **Namespace**: Syncfusion.DocIO
  - Class: WordDocument
  - Methods: AddSection, AddParagraph, AppendPicture, Save

## Code Examples (multi-language supported)

- **C#**: Provided above.
- **VB.NET**: Not provided in this image.

## Cross References

- [unclear]

## RAG Annotations

<!-- tags: [Syncfusion, Diagram, WinForms, Export, WordDocument] keywords: [Diagram, Export, WordDocument, EssentialDocIO, Metafile, Bitmap, Graphics, ExportDiagramToGraphics, C#, VB.NET] -->
```