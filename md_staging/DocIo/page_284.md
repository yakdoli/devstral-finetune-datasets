```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_284.jpeg
document_name: DocIo
page_number: 284
page_id: DocIo#page_284
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:59Z
fidelity: lossless
-->

# Essential DocIO

DocIO provides support to convert a Word document into an image of type Bitmap or EMF. It enables to easily convert a single specified page, group of pages or a whole document into image format.

## Overview

- DocIO provides support for converting Word documents into images.
- The RenderAsImages method is used to convert Word documents into images.
- It supports the conversion of individual pages or the entire document into various image formats.

## Content

The following overloads of the RenderAsImages method that can be used to convert a Word document into an image:

- **WordDocument.RenderAsImages(imageType):** This is used to convert the whole document into an image.
- **WordDocument.RenderAsImages(pageIndex, imageFormat):** This is used to render/convert a particular page of the document into an image; it returns the resultant image of type Stream.
- **WordDocument.RenderAsImages(pageIndex, imageType):** This is used to render/convert a particular page of the document into an image; it returns the resultant image of type Image.
- **WordDocument.RenderAsImages(pageIndex, noOfPages, imageType):** This is used to render/convert multiple number of pages in the document, starting from the specified page index. It returns the resultant image of type `Image[]` array.

### Code Examples

```csharp
[C#]

Image[] images = document.RenderAsImages(ImageType.Metafile);
Stream stream = document.RenderAsImages(0, ImageFormat.Emf);
Image image = document.RenderAsImages(5, ImageType.Metafile);

// This converts pages 2,3,4 in the document into images.
Image[] images = document.RenderAsImages(1, 3, ImageType.Metafile);
```

```vb
[VB]

Dim images() As Image = document.RenderAsImages(ImageType.Metafile)
Dim stream As Stream = document.RenderAsImages(0, ImageFormat.Emf)
Dim image As Image = document.RenderAsImages(5, ImageType.Metafile)

' This converts pages 2,3,4 in the document into images.
Dim images() As Image = document.RenderAsImages(1, 3, ImageType.Metafile)
```

## Note

- **Parameter "pageIndex" is a zero-based index.**
- **Layouting of pages in DocIO is not the same as layouting of pages in Word. The total number of pages and layouting of the elements tend to vary.**
- **Currently Doc to Image conversion is not supported in Silverlight application.**

<!-- tags: [DocIO, WordDocument, RenderAsImages, Bitmap, EMF, ImageConversion, Syncfusion Winforms, version: 11.4.0.26] keywords: [DocIO, RenderAsImages, Word document, image conversion, multiple pages, specific pages, image format, Stream, Image, Silverlight, C#, VB] -->
```