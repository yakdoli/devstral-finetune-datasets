```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: pdf
page_number: 111
page_id: pdf#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:11Z
fidelity: lossless
-->

## Essential PDF

### Example: Printing Barcode to PDF

```csharp
// Printing barcode on to the Pdf.
code32.Draw(page, new PointF(25, 500));
```

#### VB.NET

```vb
Dim code32 As New PdfCode32Barcode()

code32.Font = font

' Setting height of the barcode
code32.BarHeight = 45
code32.Text = "01234567"
code32.TextDisplayLocation = TextLocation.Bottom
code32.EnableCheckDigit = True
code32.ShowCheckDigit = True

' Printing barcode on to the Pdf.
code32.Draw(page, New PointF(25, 500))
```

### Code93

**Introduction**

Code 93 was designed to complement and improve upon Code 39. It can represent the full ASCII character set by using combinations of 2 characters. Code 93 is a continuous, variable-length symbology and produces denser code.

#### Features

- **The Standard Mode (default implementation)** can encode uppercase letters (A through Z), digits (0 through 9), and special characters like the `*`, `-`, `$`, `%`, `(Space)`, `.`, `/`, and `+`.
- **The Full ASCII Mode or Extended Version** can encode all 128 ASCII characters.

**Note:** The asterisk (*) is not a true encodable character, but is the start and stop 'symbol' for Code 93.

#### Code Example: C#

```csharp
PdfCode93Barcode code93 = new PdfCode93Barcode();
// Setting height of the barcode
code93.BarHeight = 45;
code93.Text = "ABC 123456789";
// Printing barcode on to the Pdf.
code93.Draw(page, new PointF(25, 600));
```

---

<!-- tags: [Syncfusion Winforms, Essential PDF, Code32Barcode, Code93Barcode, Printing, VB.NET, C#] keywords: [barcode, pdf, barcode printing, Code32, Code93, ASCII encoding, asterisk, barcode symbology, synchronized, fonts , encodable characters, height settings] -->
```