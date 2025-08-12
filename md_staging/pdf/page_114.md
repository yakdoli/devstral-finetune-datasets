```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_114.jpeg
document_name: pdf
page_number: 114
page_id: pdf#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:23Z
fidelity: lossless
-->

# Essential PDF

```csharp
' Printing barcode on to the Pdf.
barcode128A.Draw(page, New PointF(25, 135))
```

## Code128B

### C#
```csharp
PdfCode128BBarcode barcode128B = new PdfCode128BBarcode();
// Setting height of the barcode
barcode128B.BarHeight = 45;
barcode128B.Text = "12345 abcd";
barcode128B.EnableCheckDigit = true;
barcode128B.EncodeStartStopSymbols = true;
barcode128B.ShowCheckDigit = true;
```

### VB.NET
```vb.net
Dim barcode128B As New PdfCode128BBarcode()
' Setting height of the barcode
barcode128B.BarHeight = 45
barcode128B.Text = "12345 abcd"
barcode128B.EnableCheckDigit = True
barcode128B.EncodeStartStopSymbols = True
barcode128B.ShowCheckDigit = True
```

## Code128C

### C#
```csharp
PdfCode128CBarcode barcode128C = new PdfCode128CBarcode();
// Setting height of the barcode
barcode128C.BarHeight = 45;
barcode128C.Text = "001122334455";
barcode128C.EnableCheckDigit = true;
barcode128C.EncodeStartStopSymbols = true;
barcode128C.ShowCheckDigit = true;
```

### VB.NET
```vb.net
Dim barcode128C As New PdfCode128CBarcode()
' Setting height of the barcode
```

<!-- tags: [pdf, barcode, essential-pdf, winforms, syncfusion, code128] keywords: [PdfCode128BBarcode, PdfCode128CBarcode, barcode128A, barcode128B, barcode128C, BarHeight, Text, EnableCheckDigit, EncodeStartStopSymbols, ShowCheckDigit] -->
```