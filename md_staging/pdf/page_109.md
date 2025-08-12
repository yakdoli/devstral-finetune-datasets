```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: pdf
page_number: 109
page_id: pdf#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:43Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Printing barcode on to the Pdf.
- barcodeExt.Draw(page, New PointF(25, 200))

## Content

### Code 11

Code 11 is used primarily for labeling telecommunications equipment. The character set includes the digits 0 to 9, a dash (-), and a start / stop code. Each character is encoded with three bars and two spaces. Of these five elements, there may be two wide and three narrow elements, or one wide and four narrow elements.

The following code example illustrates how to draw Code 11 Barcode.

```csharp
[C#]
// Drawing Code 11 barcode
PdfCode11Barcode barcode11 = new PdfCode11Barcode();
barcode11.Text = "012345678";
barcode11.EncodeStartStopSymbols = true;
// Printing barcode on to the Pdf.
barcode11.Draw(page, new PointF(25, 300));
```

```vb
[VB.NET]
' Drawing Code 11 barcode
Dim barcode11 As PdfCode11Barcode = New PdfCode11Barcode()
barcode11.Text = "012345678"
barcode11.EncodeStartStopSymbols = True
' Printing barcode on to the Pdf.
barcode11.Draw(page, New PointF(25, 300))
```

### CodaBar

CodaBar is a variable length symbology that performs encoding of the following 20 characters:

`0123456789-$:/.+ABCD`

CodaBar uses the characters, A, B, C and D, only as start and stop characters. CodaBar is used in libraries, blood banks, the overnight package delivery industry, and a variety of other information processing applications.

The following code example illustrates how to draw CodaBar barcode.

## API Reference (if applicable)

None specified in the given text.

## Code Examples (multi-language supported)

The code examples are provided in the sections above.

## Page-level Navigation/TOC (if applicable)

None specified in the given text.

## Cross References

None specified in the given text.

## RAG Annotations

<!-- tags: pdf, code11, codabar, barcode, telecommunications, labeling, equipment, digits, character set, encoding, narrow elements, wide elements, libraries, blood banks, overnight package delivery, information processing applications keywords: code11, codabar, barcode, telecommunications, labeling, equipment, digits, character set, encoding, narrow elements, wide elements, libraries, blood banks, overnight package delivery, information processing applications -->
```