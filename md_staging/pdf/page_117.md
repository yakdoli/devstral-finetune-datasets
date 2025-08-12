```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: pdf
page_number: 117
page_id: pdf#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:16Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Draws a barcode on a PDFPage using the `dataMatrix.Draw(page, PointF.Empty)` method.
- Converts a barcode generated using Essential PDF to an image.
- Describes QR Barcodes, including their structure, data encoding, and usage scenarios.

## Content

### Barcode as Image

Barcodes that are generated using Essential PDF are simultaneously converted to an image. The following code example illustrates this.

```csharp
[![C#](https://www.syncfusion.com/file-net-core/assets/content/images/CSharp.png)]()  
Image img = barcode.ToImage();  
img.Save("Code38Barcode.png", ImageFormat.Png);
```

```vb.net
[![VB.NET](https://www.syncfusion.com/file-net-core/assets/content/images/VBNet.png)]()  
Private img As Image = barcode.ToImage()  
img.Save("Code38Barcode.png", ImageFormat.Png)
```

#### 4.1.2.2.5 QR Barcode

**Overview**:  
A QR Barcode is a two-dimensional barcode consisting of a grid of dark and light dots or blocks forming a square. The data encoded can be numeric, alphanumeric, or JIS8 characters. The `PdfQRBarcode` class in the `Syncfusion.Pdf.Barcode` namespace sets the suitable version, error correction level, and size for the input data. These settings can also be adjusted using properties.

##### 4.1.2.2.5.1 Use Case Scenarios

QR Barcodes are widely used in printed media such as labels and letters. They can be easily read by barcode readers and mobile phones.

##### 4.1.2.2.5.2 Properties

| Property  | Description                   | Data Type |
|-----------|--------------------------------|-----------|
| Text      | Gets or sets the data.        | String    |

<!-- tags: [Essential PDF, barcode, QR Barcode, Image, PdfQRBarcode, Syncfusion.Winforms, version: 11.4.0.26] keywords: [barcode, image, QR Barcode, PdfQRBarcode, barcode reader, mobile phone] -->
```