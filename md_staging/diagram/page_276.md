```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_276.jpeg
document_name: diagram
page_number: 276
page_id: diagram#page_276
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:02Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Code Example

```vb
Dim diagramimage As System.Drawing.Image = New Bitmap(1, 1, PixelFormat.Format24bppRgb)
Dim grfx As Graphics = Graphics.FromImage(diagramimage)
Dim hdc As IntPtr = grfx.GetHdc()
Dim emf As Metafile = New Metafile(hdc, EmfType.EmfOnly)
Dim emfgrfx As Graphics = Graphics.FromImage(emf)
Me.diagram1.View.ExportDiagramToGraphics(emfgrfx, True)
gfx.ReleaseHdc(hdc)
grfx.Dispose()
emfgrfx.Dispose()
diagramimage.Dispose()
Dim document As WordDocument = New WordDocument()
```

#### Adding a new section to the document.
```vb
Dim section As IWSection = document.AddSection()
```

#### Adding a paragraph to the section.
```vb
Dim paragraph As IWParagraph = section.AddParagraph()
Dim mImage As WPicture = CType(paragraph.AppendPicture(emf), WPicture)
document.Save("Sample.doc", Syncfusion.DocIO.FormatType.Doc)
System.Diagnostics.Process.Start("Sample.doc")
```

## 5.17 How To Generate a Thumbnail Image Of a Diagram

To display a thumbnail image of the diagram, follow the below given steps.

1. Generate a Bitmap image of the diagram.
2. Use the `GetThumbnailImage` method of the `Image` class to generate a thumbnail, and set it as the image of the picture box in which you want to display the thumbnail.

The following code illustrates this.

### Code Example (C#)

```csharp
public bool ThumbnailCallback()
{
    return false;
}
```

#### Comment
```vb
//Generate Thumbnail and set it to be image of the PictureBox
```

## API Reference
- `GetThumbnailImage`: Method used to generate a thumbnail image.

## Code Examples
- Demonstrates how to generate a thumbnail image using the `GetThumbnailImage` method and set it as the image of a picture box.

## Cross References
- See also: [How To Generate a Thumbnail Image Of a Diagram](#generated-link-if-available)

### RAG Annotations
<!-- tags: [Syncfusion, WindowsForms, Diagram, ThumbnailImage, C#] keywords: [diagram, thumbnail image, Windows Forms, GetThumbnailImage] -->
```