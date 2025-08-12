```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_343.jpeg
document_name: pdf
page_number: 343
page_id: pdf#page_343
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:05Z
fidelity: lossless 
 -->

# Essential PDF

## 5.1.1.2 How To Compress a PDF Document?

Compression is used for reducing the size of the created PDF document. Essential PDF controls the compression level of the document by using the `PdfCompressionLevel` class with the help of the LZW and zlib/deflate compression algorithms. Both LZW and Flate methods compress either binary data or ASCII text, but always produce binary data, even if the original data is text.

### Supported Compression Levels

The following compression levels are supported by Essential PDF:

- Best
- BestSpeed
- BelowNormal
- AboveNormal
- None

### Example Code for Compression

#### [C#]

```csharp
// Compressing PDF document
doc.Compression = PdfCompressionLevel.Normal;
```

#### [VB.NET]

```vbnet
' Compressing PDF document
doc.Compression = PdfCompressionLevel.Normal
```

## 5.1.1.3 How To Create a Borderless Table?

You can create a borderless table by making use of the `Style` property of the `PdfLightTable` class. This is achieved by setting the border color of the table to `Transparent`. The following code example illustrates this.

```csharp
// Creating Border with transparent color.
PdfPen borderPen = new PdfPen(Color.Transparent);
borderPen.Width = 1.0f;

// Assigning the border pen to table cell.
PdfCellStyle defStyle = new PdfCellStyle();
defStyle.Font = font;
defStyle.BorderPen = borderPen;
table.Style.DefaultStyle = defStyle;
```

## API Reference

### Classes and Methods

- **`PdfCompressionLevel`**: Controls the compression level of the PDF document.
  - **Properties**:
    - `Best`: Best compression.
    - `BestSpeed`: Best compression speed.
    - `BelowNormal`: Below normal compression.
    - `AboveNormal`: Above normal compression.
    - `None`: No compression.
  - **`PdfPen`**: Represents a pen used for drawing lines in the document.
  - **`PdfCellStyle`**: Represents the style of a table cell.
  - **`PdfLightTable`**: Represents a lightweight table in the document.

---

### Code Examples

#### Compressing a PDF Document

```csharp
// Example using C#
doc.Compression = PdfCompressionLevel.Normal;

// Example using VB.NET
doc.Compression = PdfCompressionLevel.Normal
```

#### Creating a Borderless Table

```csharp
// Example using C#
PdfPen borderPen = new PdfPen(Color.Transparent);
borderPen.Width = 1.0f;

PdfCellStyle defStyle = new PdfCellStyle();
defStyle.Font = font;
defStyle.BorderPen = borderPen;
table.Style.DefaultStyle = defStyle;
```

### See also

- [Essential PDF Documentation](https://www.syncfusion.com/documentation)
- [PdfCompressionLevel](https://www.syncfusion.com/documentation/pdf/compression-level)
- [PdfLightTable](https://www.syncfusion.com/documentation/pdf/light-table)

<!-- tags: [Essential PDF, compression, borderless table, PdfCompressionLevel, PdfLightTable] keywords: [compression level, borderless, tables, transparency, control, document, size reduction] -->
```