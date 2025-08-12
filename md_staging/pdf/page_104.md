```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: pdf
page_number: 104
page_id: pdf#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:57Z
fidelity: lossless
-->

## Overview
- PdfImage as well as graphics elements support laying out multiple pages (see Pagination).

- Properties can specify image dimensions, resolutions, and quality.

- Bitmaps use PdfBitmap class for functionality with support for masks and channels.

- Metafiles can be rendered with support for various types and features including RTF and multi-page layouts.

## Content

### Base Properties

- **Height**: Specifies image height in pixels.
- **Width**: Specifies image width in pixels.
- **HorizontalResolution**: Specifies horizontal image resolution, also known as DpiX.
- **VerticalResolution**: Specifies vertical image resolution, also known as DpiY.
- **PhysicalDimension**: Specifies image dimension in points.
- **Quality**: Gets or sets the quality.

**Note:** Image quality is 100 by default, which increases the resultant file size and quality. Reducing the quality will reduce the file size.

### Bitmaps

The **PdfBitmap** class provides functionality for raster images, including support for masks and alpha channels. There are two types of masks:

- **Color mask**: Implemented by the **PdfColorMask** class.
- **Image mask**: Implemented by the **PdfImageMask** class.

Masks are set using the **Mask** property of the **PdfBitmap** object.

For multiframe images (e.g., GIF, TIFF), the active frame is chosen based on the **FrameCount** and **ActiveFrame** properties.

### Metafiles

All three types of Windows metafiles are supported by Essential PDF through the **PdfMetafile** class. Additionally, RTF is supported through the **PdfMetafile** class.

- **PdfMetafile** supports multipage layout and graphic elements.
- It allows splitting text lines across page breaks when shared by pages.

The **PdfMetafileLayoutFormat** should be used to handle this feature when calling the **Draw** method.

If metafiles contain images and text spanning multiple pages, the images and text may not split across page breaks unless the **SplitTextLines** and **SplitImages** properties are disabled in the **PdfMetafileLayoutFormat** class.

#### Code Example

```csharp
PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat();
format.SplitTextLines = false;
```

## Page-level Navigation/TOC (if applicable)
- No TOC elements present on this page.

## Cross References
See also: Pagination.

### RAG Annotations
<!-- tags: [syncfusion, winforms, pdf, metafiles, images, masks, multi-page layouts] keywords: [PdfBitmap, PdfMetafile, DpiX, DpiY, FrameCount, ActiveFrame, PdfImageMask, PdfColorMask, Page breaks, SplitTextLines, SplitImages] -->
```