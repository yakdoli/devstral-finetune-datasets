```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_112.jpeg
document_name: pdf
page_number: 112
page_id: pdf#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:25Z
fidelity: lossless
-->

# Essential PDF

```vb.net
Dim code93 As New PdfCode93Barcode()
' Setting height of the barcode
code93.BarHeight = 45
code93.Text = "ABC 123456789"
' Printing barcode on to the Pdf.
code93.Draw(page, New PointF(25, 600))
```

## Code93Extended

### C#

```csharp
PdfCode93ExtendedBarcode code93ext = new PdfCode93ExtendedBarcode();
// Setting height of the barcode
code93ext.BarHeight = 45;
code93ext.EncodeStartStopSymbols = true;
code93ext.Text = "(abc) 123456789";

// Printing barcode on to the Pdf.
page = doc.Pages.Add();
code93ext.Draw(page, new PointF(25, 50));
```

### VB.NET

```vb.net
Dim code93ext As New PdfCode93ExtendedBarcode()
' Setting height of the barcode
code93ext.BarHeight = 45
code93ext.EncodeStartStopSymbols = True
code93ext.Text = "(abc) 123456789"

' Printing barcode on to the Pdf.
page = doc.Pages.Add()
code93ext.Draw(page, New PointF(25, 50))
```

## Code128

Code 128 is a variable length, high density, alphanumeric, linear bar code symbology, capable of encoding the full 128-character ASCII character set and extended character sets. This Symbology includes a checksum digit for verification, and the barcode may also be verified character-by-character verifying the parity of each data byte.

### Code 128 Code Sets

---

<!-- tags: [syncfusion-sdk, pdf, barcode, code93, code93extended, code128, winforms] keywords: [barcode generation, code93, code93extended, code128, variable length, high density, alphanumeric, linear bar code, ascii character set, checksum digit] -->
```