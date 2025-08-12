```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_200.jpeg
document_name: pdf
page_number: 200
page_id: pdf#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:06Z
fidelity: lossless
-->

# Essential PDF

'Add time stamp using the server URI and credentials.  
signature.TimeStampServer = New TimeStampServer(New Uri("http://digistamp.syncfusion.com"),"user", "123456")

### Multiple Signatures

You can add multiple signatures to the document with incremental updates by using standard signatures.

**Note:** Currently only self-created and third-party `.pfx` certificates are supported.

## 4.1.5 Standards for PDF/A-1 Compliance

PDF elements are standardized under ISO for several constituencies. This section deals with following standards that are supported by Essential PDF.

- PDF/A-This topic demonstrates PDF/A-1b standard, which is used for archiving in environments like corporate, government, and library.
- PDF/X-This topic discusses the PDF/X-1a standard that is mainly available for standardizing printing and graphics.

### 4.1.5.1 PDF/A-1b

### PDF/A

The PDF/A formats specified in the ISO 19005 standards strive to provide a mechanism for representing electronic documents. These documents are represented in a manner that preserves their visual appearance over time, independent of the tools and systems used for creating, storing, or rendering the files. A key element to this reproducibility is the requirement for PDF/A documents to be 100 percent self-contained.

All of the information necessary for displaying the document in the same manner every time is embedded in the file. This includes all visible content like text, raster images, vector graphics, fonts, and color information. The standard is based on PDF 1.4, and imposes some restrictions regarding the use of color, fonts, annotations, and other elements.

There are two types of PDF/A-1:

<!-- tags: [pdf, compliance, standards, pdf/a, pdf/x, pdf/a-1b, self-contained, electronic documents, iso 19005, Syncfusion Winforms, 11.4.0.26] keywords: [PDF/A, PDF/X-1a, PDF/A-1b, ISO 19005, electronic documents, self-contained, reproducibility, archiving, printing, graphics, synchronization, standards compliance] -->
```