```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_204.jpeg
document_name: pdf
page_number: 204
page_id: pdf#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:19Z
fidelity: lossless
-->

# Essential PDF

```vb.net
'Create the document.
Dim doc As New PdFDocument(PdfConformanceLevel.Pdf_X1A2001)

'Set the color space. Should be CMYK.
doc.ColorSpace = PdfColorSpace.CMYK

'Save and close the document.
doc.Save("sample.pdf")
```

## 4.1.6 Settings

This section demonstrates various document settings and compression settings available in Essential PDF.

- Document Settings - This topic provides details on setting various document properties and meta data writing.
- Compression - This topic explains how a document is compressed by using Essential PDF.

### 4.1.6.1 Document Settings

The Document settings help in storing information about the document. Extensible Metadata Platform (XMP) is a technology that enables to embed metadata.

> Metadata is the data that describes a file into the file itself.

It uses XML as the syntax for metadata description. XMP is provided with the following schemas:

- Basic Schema
- Dublin Core Schema
- Rights Management Schema
- Basic Job Ticket Schema
- Paged-Text Schema
- PDF Schema
```