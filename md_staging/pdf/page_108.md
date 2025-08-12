```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: pdf
page_number: 108
page_id: pdf#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:13Z
fidelity: lossless
-->

Essential PDF

```csharp
// Setting height of the barcode
barcode.BarHeight = 45;
barcode.Text = "CODE39$";

// Printing barcode on to the Pdf.
barcode.Draw(page, new PointF(25, 70 ));
```

### [VB.NET]

```vb
' Drawing Code39 barcode
Dim barcode As PdfCode39Barcode = New PdfCode39Barcode()

' Setting height of the barcode
barcode.BarHeight = 45
barcode.Text = "CODE39$"

' Printing barcode on to the Pdf.
barcode.Draw(page, New PointF(25, 70))
```

## ExtendedCode39

Code 39 Extended is an extended version of Code 39 that supports the ASCII character set. So with Code 39 Extended, you can also code the 26 lower letters (a-z) and the special characters you have on your keyboard.

### Code Example for Drawing Code39Extended Barcode

The following code example illustrates how to draw Code39Extended barcode.

### [C#]

```csharp
// Drawing Code39Extended barcode
PdfCode39ExtendedBarcode barcodeExt = new PdfCode39ExtendedBarcode();
barcodeExt.TextAlignment = PdfBarcodeTextAlignment.Left;
barcodeExt.Text = "CODE39Ext";
// Printing barcode on to the Pdf.
barcodeExt.Draw(page, new PointF(25, 200));
```

### [VB.NET]

```vb
' Drawing Code39Extended barcode
Dim barcodeExt As PdfCode39ExtendedBarcode = New PdfCode39ExtendedBarcode()
barcodeExt.TextAlignment = PdfBarcodeTextAlignment.Left
barcodeExt.Text = "CODE39Ext"
```

---
© 2013 Syncfusion. All rights reserved.
```