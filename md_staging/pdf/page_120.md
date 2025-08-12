```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: pdf
page_number: 120
page_id: pdf#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:53Z
fidelity: lossless
-->

## Content

### QRBarcode Example

```csharp
//Draw the barcode on PdfPage.
QRBarcode.Draw(page, PointF.Empty);
```

#### [VB.NET]

```vb
'Create a QR Barcode.
Dim QRBarcode As New PdfQRBarcode()

'Set the dimension.
QRBarcode.XDimension = 8

'Set the input mode.
QRBarcode.InputMode = InputMode.BinaryMode

'Set the error correction level.
QRBarcode.ErrorCorrectionLevel = PdfErrorCorrectionLevel.High
QRBarcode.Text = "Syncfusion"

'Set the barcode version.
QRBarcode.Version = QRCodeVersion.Auto

'Draw the barcode on PdfPage.
QRBarcode.Draw(page, PointF.Empty)
```

### Pagination

**4.1.2.2.6 Pagination**

*Pagination* is the capability of the elements to span more than one page (to be shared by more than one page). The base class for all such elements is the `PdfLayoutElement` class. All the primitives that are derived from that class support page layouting in their own way. The following events are raised by this class.

| Name              | Description                                                        |
|-------------------|--------------------------------------------------------------------|
| BeginPageLayout   | This event is raised before the element is printed on the page.   |
| EndPageLayout     | This event is raised after the element is printed on the page.    |

## Page-level Navigation/TOC (if applicable)

This section describes basic interfacing concepts for a specific domain in control applications, notably pagination and barcode generation using VB.NET and C#.

<!-- tags: [pagination, barcode generation, VB.NET, C#, Syncfusion] keywords: [QRBarcode, PdfLayoutElement, BeginPageLayout, EndPageLayout, error correction level, text input, syncfusion] -->
```