```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: pdf
page_number: 079
page_id: pdf#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:04Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Discusses the RightToLeft property and its impact on text alignment and printing.
- Explains the use of CJK Fonts in Essential PDF and their additional requirements.
- Introduces the MeasureString method for text size calculation.
- Outlines the attributes and functionalities covered in the "Drawing" section.

### Note
- **RightToLeft property**: Does not change the text alignment. It enables the RTL engine and prints text in RTL order. Use the Alignment property of PdfStringFormat to set the horizontal alignment of the text.
- **RTL Support**: Do not enable RTL support if it is not needed, as it reduces text printing speed.

### CJK Fonts
A set of standard PDF fonts supports Chinese, Japanese, and Korean characters. These fonts are supported through the `PdfCjkStandardFont` class. In addition to the families supported by `PdfStandardFont`, the following families are required:

- HanyangSystemsGothicMedium
- HanyangSystemsShinMyeongJoMedium
- HeiseiKakuGothicW5
- HeiseiMinchoW3
- MonotypeHeiMedium
- MonotypeSungLight
- SinoTypeSongLight

### Text Measuring
The `MeasureString` method of the `PdfFont` class calculates the size of the text, the number of lines that fit in the bounds, and the number of characters in the text.

---

## 4.1.2 Drawing

### Overview
This section explains how various drawing elements are drawn using Essential PDF. It includes the following topics:

- **Text**: Describes various text drawing methods of Essential PDF.
- **Graphics**: Demonstrates various graphic elements in PDF.
- **Tables**: Explains table creation and formatting by using the Essential PDF light table model.
- **PDF Grid**: Describes PdfGrid, which is based on the cell model. It provides support for cell formatting, row and column spanning, and drawing nested tables in the PDF document.
- **Lists**: Describes how various lists can be drawn by using Essential PDF.

## Cross References
See also:
- [PdfStringFormat](#pdfstringformat)
- [PdfCjkStandardFont](#pdfcjkstandardfont)
- [.MeasureString](#measurestring)

### Metadata
- Copyright: © 2013 Syncfusion. All rights reserved.
- Page Number: 79

<!-- tags: [essential pdf, right to left, cjk fonts, text measuring, drawing, tables, pdf grid, lists] keywords: [rtl, pdfcjkstandardfont, measurestring, text alignment, font families, table formatting, cell model, list drawing] -->
```