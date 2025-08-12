```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: pdf
page_number: 217
page_id: pdf#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:21Z
fidelity: lossless
-->

## WinForms RTF as Image

### Overview
- Demonstrates how to draw RTF content as images by converting it into either a metafile or a bitmap.
- Allows pagination of RTF content without breaking at page breaks.

## Content

### Drawing RTF as Metafile

The following code snippet shows how to convert RTF content into a metafile and draw it without breaking the text at page breaks:

#### C#
```csharp
// Draw RTF as metafile
PdfMetafile metafile = (PdfMetafile)PdfImage.FromRtf(text, bounds.Width, PdfImageType.Metafile);
PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat();

// Allow pagination without any breaks at page breaks.
format.SplitTextLines = false;

// Draw the image.
metafile.Draw(page, 0, 0, format);
```

#### VB.NET
```vb.net
' Convert it as metafile image.
Dim metafile As PdfMetafile = CType(PdfImage.FromRtf(text, bounds.Width, PdfImageType.Metafile), PdfMetafile)
Dim format As PdfMetafileLayoutFormat = New PdfMetafileLayoutFormat()

' Allow the text to flow multiple pages without any breaks.
format.SplitTextLines = False

' Draw the image.
metafile.Draw(page, 0, 0, format)
```

### Drawing RTF as Bitmap

The following code snippet shows how to convert RTF content into a bitmap and draw it:

#### C#
```csharp
// Draw RTF as Bitmap
bitmap = PdfImage.FromRtf(text, bounds.Width, PdfImageType.Bitmap);
bitmap.Draw(page, 0, 0, format)
```

#### VB.NET
```vb.net
' Draw RTF as Bitmap
Dim bitmap As PdfImage = PdfImage.FromRtf(text, bounds.Width, PdfImageType.Bitmap)
bitmap.Draw(page, 0, 0, format)
```

## API Reference

### Methods
- **FromRtf**: Converts RTF content into a PDF image.
  - **Parameters**:
    - `text`: The RTF content to be converted.
    - `width`: The width of the output image.
    - `type`: The type of image to return (`PdfImageType.Metafile` or `PdfImageType.Bitmap`).
  - **Returns**: A `PdfImage` object.

- **Draw**: Draws the image on a specified page.
  - **Parameters**:
    - `page`: The page to draw the image on.
    - `x`: The x-coordinate for the top-left corner of the image.
    - `y`: The y-coordinate for the top-left corner of the image.
    - `format`: The layout format for the image.

### Properties
- **SplitTextLines**: A boolean property that determines whether text is split across pages.

## Code Examples

The code examples above demonstrate how to:
- Render RTF content as a metafile or bitmap.
- Configure the rendering to prevent text breaks at page breaks.

## Cross References

For more information on:
- **RTF to Image Conversion**: See the section on PDF image rendering.
- **Pagination Control**: Refer to the documentation on PDF layout control.

<!-- tags: [Syncfusion, WinForms, RTF, PDF, Image, Metafile, Bitmap, Pagination] keywords: [C#, VB.NET, PdfMetafile, PdfMetafileLayoutFormat, PdfImage, FromRtf, Draw, SplitTextLines, RTF, Bitmap, Metafile, Pagebreak] -->
```