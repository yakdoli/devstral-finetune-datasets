```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: pdf
page_number: 118
page_id: pdf#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:37Z
fidelity: lossless
-->

## Properties and Methods of QRCode

### Properties

| Property       | Description                             | Type                |
|----------------|-----------------------------------------|---------------------|
| Version        | Gets or sets the QR barcode version.   | QRCodeVersion      |
| ErrorCorrectionLevel | Gets or sets the error correction level. | PdfErrorCorrectionLevel |
| InputMode      | Gets or sets the mode of the input text. | InputMode           |
| XDimension     | Gets or sets the dimension of the blocks. | Float              |

### Methods

#### 4.1.2.2.5.3 Methods

**Table 4: Methods Table**

| Method       | Description                             | Parameters         | Return Type |
|--------------|-----------------------------------------|--------------------|-------------|
| Draw         | Draws barcode in PdfPage.              | (PdfPage, PointF)  | Void        |
| ToImage      | Converts barcode to image.             | None               | Image       |

#### 4.1.2.2.5.4 Version

The QR Barcode uses version levels numbered from 1 to 40. Version 1 measures 21 modules x 21 modules, Version 2 measures 25 modules x 25 modules, and so on. The number of modules increases in steps of 4 modules per side up to Version 40, which measures 177 modules x 177 modules. Each version has its own capacity. By default the QR Version is Auto, which will automatically set the version according to the length of the input text.

#### 4.1.2.2.5.5 Error correction level

The QR Barcode employs error correction to generate a series of error correction codewords which are added to the data codeword sequence. This enables the symbol to withstand damage without loss of data. There are four user-selectable levels of error correction, as shown in the table, offering the capability of recovery from the following amounts of damage. By default, the Error correction level is Low (L).

### Error Correction Level Table

**Table 3: Error Correction Level Table**

| Error Correction Level | Recovery Capacity % (approx.) |
|-------------------------|-----------------------------|
| Error Correction Level | Recovery Capacity % (approx.) |

### Footer

© 2013 Syncfusion. All rights reserved. | 118 Page
```

<!-- tags: [qr code, version, error correction level, input mode, dimension, barcode, pdf, image, draw] keywords: [qr code version, error correction, input mode, block dimension, pdf page, barcode drawing, image conversion, recovery capacity] -->
```