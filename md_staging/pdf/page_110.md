```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_110.jpeg
document_name: pdf
page_number: 110
page_id: pdf#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:09Z
fidelity: lossless
-->

## Main Content

### Drawing Codabar Barcode

#### Code Examples

- **C#**
  ```csharp
  // Drawing Codabar barcode
  PdfCodabarBarcode codabar = new PdfCodabarBarcode();
  codabar.Text = "0123";
  // Printing barcode on to the Pdf.
  codabar.Draw(page, new PointF(25, 400));
  ```

- **VB.NET**
  ```vbnet
  ' Drawing Codabar barcode
  Dim codabar As PdfCodabarBarcode = New PdfCodabarBarcode()
  codabar.Text = "0123"
  ' Printing barcode on to the Pdf.
  codabar.Draw(page, New PointF(25, 400))
  ```

### Code 32

**Summary:**
Code 32 is used primarily for encoding pharmaceuticals, cosmetics, and dietetic products. It is mainly used to encode pharmaceutical products in Italy, specifically the Italian Pharmacode. The structure of Code 32 is detailed as follows:

#### Structure of Code 32
- **'A' character (ASCII 65)**: Not encoded.
- **8 digits for Pharmacode**: Generally begins with or is prefixed by 0.
- **1 digit for Checksum module 10**: Automatically calculated by Barcode Professional.

#### Encoding Guidelines
The value to be encoded (passed to Barcode Professional) must consist of 8 digits of the pharmacode (prefixed with '0' if necessary). The 9th digit (the checksum) is automatically calculated by Barcode Professional.

#### Code Example

- **C#**
  ```csharp
  PdfCode32Barcode code32 = new PdfCode32Barcode();

  code32.Font = font;

  // Setting height of the barcode
  code32.BarHeight = 45;
  code32.Text = "01234567";
  code32.TextDisplayLocation = TextLocation.Bottom;
  code32.EnableCheckDigit = true;
  code32.ShowCheckDigit = true;
  ```

## Footer
© 2013 Syncfusion. All rights reserved.
``` 

<!-- tags: [barcode, codabar, code32, pdf] keywords: [codabar codec, code32 structure, barcode encoding,意大利药典码, 医药产品编码,化妆品编码, 饮食编码,医药产品, giản thuốc,编码, pdf barcode] -->
```