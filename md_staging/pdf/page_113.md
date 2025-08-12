```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: pdf
page_number: 113
page_id: pdf#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:59Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Code Set A (or Chars Set A) includes all of the standard upper case U.S. alphanumeric keyboard characters and punctuation characters together with the control characters, (i.e. characters with ASCII values from 0 to 95 inclusive), and seven special characters.
- Code Set B (or Chars Set B) includes all of the standard upper case alphanumeric keyboard characters and punctuation characters together with the lower case alphabetic characters (i.e. characters with ASCII values from 32 to 127 inclusive), and seven special characters.
- Code Set C (or Chars Set C) includes the set of 100 digit pairs from 00 to 99 inclusive, as well as three special characters. This allows numeric data to be encoded as two data digits per symbol character, at effectively twice the density of standard data.

## Code 128 Special Characters
### Code 128 Special characters
The last seven characters of Code Sets A and B (character values 96 - 102) and the last three characters of Code Set C (character values 100 - 102) are special non-data characters with no ASCII character equivalents, which have particular significance to the bar code reading device.

### Note:
If you specify that the data must be encoded by using Char Set C, then the number of characters after it must be even.

## Code128A

### [C#]
```csharp
PdfCode128ABarcode barcode128A = new PdfCode128ABarcode();
// Setting height of the barcode
barcode128A.BarHeight = 45;
barcode128A.Text = "ABCD 12345";
barcode128A.EnableCheckDigit = true;
barcode128A.EncodeStartStopSymbols = true;
barcode128A.ShowCheckDigit = true;

//Printing barcode on to the Pdf.
barcode128A.Draw(page, new PointF(25, 135));
```

### [VB.NET]
```vbnet
Dim barcode128A As New PdfCode128ABarcode()
' Setting height of the barcode
barcode128A.BarHeight = 45
barcode128A.Text = "ABCD 12345"
barcode128A.EnableCheckDigit = True
barcode128A.EncodeStartStopSymbols = True
barcode128A.ShowCheckDigit = True
```

## Page-level Navigation/TOC
- **Code 128 Special characters**
- **Note**
- **Code128A**
- [C#] Code Example
- [VB.NET] Code Example

<!-- tags: [pdf, barcodes, code sets, character encoding, code 128, essential pdf, winforms, syncfusion] keywords: [ascii, control characters, data density, special characters, bar code reading device, enable check digit, encode start stop symbols, show check digit, barcode drawing] -->
```