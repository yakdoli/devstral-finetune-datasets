```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: pdf
page_number: 105
page_id: pdf#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:29Z
fidelity: lossless
-->

## Overview

- The page discusses the properties of the `PdfMetafileLayoutFormat` class, their descriptions, and the supported color spaces for images in a PDF document.
- Includes code examples in C# and VB.NET for configuring `SplitImages` and `SplitTextLines` properties.
- Details the supported color spaces: RGB, CMYK, Grayscale, and Indexed.
- Briefly mentions the transparency feature provided by the `PdfMask` base class and introduces the `PdfImageMask`.

## Content

### Configuration Example

```csharp
format.SplitImages = false;
```

```vb
Dim format As New PdfMetafileLayoutFormat()
format.SplitTextLines = False
format.SplitImages = False
```

### Public Properties of `PdfMetafileLayoutFormat` Class

The following are the public properties of the `PdfMetafileLayoutFormat` class:

| Name               | Description                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------|
| Break              | Gets or sets break type of the element.                                                            |
| Layout             | Gets or sets layout type of the element.                                                           |
| PaginateBounds     | Gets or sets the bounds on the next page.                                                          |
| SplitImages        | Gets or sets the value indicating whether the images should be split between the pages or not.    |
| SplitTextLines     | Gets or sets the value indicating whether the text line should be split between the pages or not. |
| UsePaginateBounds  | Gets a value that indicates whether PaginateBounds should be used or not.                          |

---

### Color Spaces

Images retain their original color space. The supported color spaces are as follows.

- RGB - Images with 24-bit color space
- CMYK - Images with 48-bit color space
- Grayscale - Images with 8-bit color space
- Indexed - Images with 8-bit indexed color space

---

### Transparency

Transparency of `PdfBitmap` images are provided by the abstract `PdfMask` base class.

---

### PdfImageMask

  

<!-- tags: [Syncfusion Winforms, PdfMetafileLayoutFormat, color spaces, transparency, PdfImageMask] keywords: [PdfMetafileLayoutFormat, SplitImages, SplitTextLines, Break, Layout, PaginateBounds, UsePaginateBounds, RGB, CMYK, Grayscale, Indexed] -->
```