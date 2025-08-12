```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: pdf
page_number: 115
page_id: pdf#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:25Z
fidelity: lossless
-->

# Essential PDF

```csharp
barcode128C.BarHeight = 45
barcode128C.Text = "001122334455"
barcode128C.EnableCheckDigit = True
barcode128C.EncodeStartStopSymbols = True
barcode128C.ShowCheckDigit = True
```

## 2D Barcode

### DataMatrix Barcode

DataMatrix barcode is a two-dimensional barcode that consists of a grid of dark and light dots or blocks forming square or rectangular symbols. The data encoded in the barcode can either be numeric or alphanumeric. The `PdfDataMatrixBarcode` class available in `Syncfusion.Pdf.Barcode` namespace sets the suitable encoding type and size for the input data. However, the size, encoding type, and dimension of individual blocks can also be set using the properties.

---

**Note:** By default, the width of the quiet zone on all four sides of the barcode is equal to the dimension of the blocks.

## Use case scenario

The DataMatrix barcodes are widely used in printed media such as labels and letters. It can be read easily by a barcode reader and also by mobile phones.

## Properties, Methods and Events

### Properties

**Table 1: Properties Table**

| **Property**   | **Description**                                  | **Data Type**                |
|-----------------|--------------------------------------------------|-------------------------------|
| Encoding       | Gets or sets the encoding type.                 | `PdfDataMatrixEncoding`      |
| Size           | Gets or sets the size of the symbol.            | `PdfDataMatrixSize`          |
| Text           | Gets or sets the data.                          | `String`                     |
| XDimension     | Gets or sets the dimension of the blocks       | `float`                      |

### Methods

**Table 2: Methods Table**

| **Method**  | **Description**                     | **Parameters**        | **Return Type** |
|-------------|---------------------------------------|------------------------|------------------|
| Draw        | Draws barcode in `PdfPage`          | `(PdfPage, PointF)`   | `Void`          |
```

<!-- tags: [syncfusion, pdf, barcode, datamatrixbarocode, properties, methods, events] keywords: [DataMatrixBarcode, PdfDataMatrixBarcode, barcode, encoding, size, dimension, quietzone, printed media, labels, letters, mobile phones, barcode reader] -->
```