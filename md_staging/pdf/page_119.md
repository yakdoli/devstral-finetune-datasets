```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: pdf
page_number: 119
page_id: pdf#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:40Z
fidelity: lossless
-->

## Overview

- A detailed explanation of input modes and their supported character sets for QR code generation.
- Guidelines on selecting the appropriate error correction level for QR codes based on the required information.
- Instructions for integrating a QR Barcode into an application using the Syncfusion Winforms library.

## Content

### 4.1.2.2.5.6 Input mode

There are three modes for the input as defined in the table below. Each mode supports the specific set of input characters. The user may select the most suitable input mode. The default input mode is Binary Mode.

Table 4: Input Mode Table

| **Input Mode**         | **Possible characters**          |
|------------------------|-----------------------------------|
| **Numeric Mode**       | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9    |
| **Alphanumeric Mode**  | 0–9, A–Z (upper-case only), space, $, %, *, +, -., /, : |
| **Binary Mode**        | Shift JIS characters            |

### 4.1.2.2.5.7 Adding a QR Barcode to an application

[C#]
```csharp
//Create a QR Barcode.
PdfQRBarcode QRBarcode = new PdfQRBarcode();

//Set the dimension.
QRBarcode.XDimension = 8;

//Set the input mode.
QRBarcode.InputMode = InputMode.BinaryMode;

//Set the error correction level.
QRBarcode.ErrorCorrectionLevel = PdfErrorCorrectionLevel.High;
QRBarcode.Text = "Syncfusion";

//Set the barcode version.
QRBarcode.Version = QRCodeVersion.Auto;
```

## API Reference (if applicable)

None provided in the current text.

## Code Examples (multi-language supported)

- The above code snippet demonstrates how to create and configure a QR Barcode in a WinForms application using the Syncfusion library.

## Page-level Navigation/TOC (if applicable)

None provided in the current text.

## Cross References

None provided in the current text.

<!-- tags: [product, module, control, api, version?] keywords: [qr code, input mode, error correction level, barcode, winforms, syncfusion] -->
```