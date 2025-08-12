```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_107.jpeg
document_name: pdf
page_number: 107
page_id: pdf#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:54Z
fidelity: lossless
-->

## Overview

- Bar codes offer a simple and cost-effective way to encode text information for easy reading by inexpensive electronic readers.
- Essential PDF supports both 1D linear barcodes and 2D barcodes.
- The detailed structure of 1D linear barcodes is explained, including the character sets and examples for each type.

## Content

### 4.1.2.2.4 Barcode

Bar codes provide a simple and inexpensive method of encoding text information that is easily read by inexpensive electronic readers. A bar code consists of a series of parallel, adjacent bars and spaces. Predefined bar and space patterns or "symbologies" are used to encode small strings of character data into a printed symbol.

The basic structure of a bar code consists of a leading and trailing quiet zone, a start pattern, one or more data characters, optionally one or two check characters, and a stop pattern. Essential PDF supports 1D / linear barcodes and 2D barcode.

#### 1D / Linear Barcodes

Following codes are the 1D / linear barcodes. This section also includes details of each code with coding examples.

- Code39
- Code39Extended
- Code11
- Codabar
- Code32
- Code93
- Code93Extended
- Code128
- Code128A
- Code128B
- Code128C

#### Code39

The Code 39 character set includes the digits 0-9, the letters A-Z (upper case only), and the following symbols: space, minus (-), plus (+), period (.), dollar sign ($), slash (/), and percent (%). A special start / stop character is placed at the beginning and end of each barcode. The barcode may be of any length, although more than 25 characters really begin to push the bounds. Code 39 is just about the only type of barcode in common use that does not require a checksum.

The following code example illustrates how to draw Code39 Barcode.

```csharp
[code#]
// Drawing Code39 barcode
PdfCode39Barcode barcode = new PdfCode39Barcode();
```

## API Reference (if applicable)
- The API section would detail the PdfCode39Barcode class and its methods.

## Code Examples (multi-language supported)
- The provided C# example demonstrates the creation of a Code39 barcode.

## Page-level Navigation/TOC (if applicable)
- Local table of contents or navigation elements specific to this page are not present.

## Cross References
- See also related sections or references if explicitly mentioned.

<!-- tags: [barcode, essentialpdf, pdf, winforms, code39, syncfusion, version:11.4.0.26] keywords: [code39, bar code, symbologies, quiet zone, start pattern, stop pattern, check characters, PdfCode39Barcode, electronic readers] -->
```