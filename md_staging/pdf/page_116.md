```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: pdf
page_number: 116
page_id: pdf#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:39Z
fidelity: lossless
-->

## Overview

- Converts barcode to Image

## Content

The following code snippet illustrates how to draw a DataMatrix barcode:

### C#

```csharp
// Create a DataMatrix barcode.
PdfDataMatrixBarcode dataMatrix = new PdfDataMatrixBarcode("Syncfusion");

// Set the dimension.
dataMatrix.XDimension = 3;

// Set the encoding.
dataMatrix.Encoding = PdfDataMatrixEncoding.ASCII;

// Choose the matrix size.
dataMatrix.Size = PdfDataMatrixSize.Size12x12;

// Draw the barcode on PdfPage.
dataMatrix.Draw(page, PointF.Empty);
```

### VB.NET

```vbnet
' Create a DataMatrix barcode
Dim dataMatrix As New PdfDataMatrixBarcode("Syncfusion")

' Set the dimension
dataMatrix.XDimension = 3

' Set the encoding
dataMatrix.Encoding = PdfDataMatrixEncoding.ASCII

' Choose the matrix size
dataMatrix.Size = PdfDataMatrixSize.Size12x12
```

## API Reference

### Members

- **XDimension**: Sets the dimension of the DataMatrix barcode.
- **Encoding**: Specifies the encoding type (e.g., ASCII).
- **Size**: Determines the size of the DataMatrix matrix.
- **Draw**: Renders the barcode on a PDF page.

### Parameters

| Name       | Type                     | Description                                                                 | Default      | Required |
|------------|--------------------------|-----------------------------------------------------------------------------|--------------|----------|
| **page**   | `PdfPage`                | The PDF page on which the barcode will be drawn.                       | N/A          | Yes      |
| **location** | `PointF`            | The location on the PDF page where the barcode will be drawn.           | `PointF.Empty` | Yes      |

### Returns

- `void`: Renders the barcode on the specified PDF page.

### Exceptions

- **ArgumentException**: If the `page` or `location` is null or invalid.

```html
<!-- tags: [DataMatrix, barcode, PDF, Syncfusion, Winforms, version 11.4.0.26] keywords: [DataMatrixBarcode, PdfPage, XDimension, Encoding, Size, Draw] -->
```