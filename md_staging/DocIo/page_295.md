```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_295.jpeg
document_name: DocIo
page_number: 295
page_id: DocIo#page_295
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:00Z
fidelity: lossless
-->

## Essential DocIO

### Overview
- `Essential DocIO` provides a robust tool for PDF conversion from DOC and DOCX files.
- The table style in Word documents can be converted to PDF with light shading for improved readability.
- Table styles for Word 97–2003 documents are not supported.

### Content

#### Known Limitations: Table styles for Word 97–2003 documents are not supported
The table styles in Word documents from the versions 97–2003 will not be supported in the generated PDF.

#### Breaks
The columns, section, line, and page breaks are fully-supported in the generated PDF document.

#### OLEObject
The OLEObjects are partially supported. Specifically, the image which represents a particular document will be available in the generated PDF document. However, the object associated with the OLEObject will not be converted into the generated document.

#### Text box
The text value present in the text box will be rendered as text at its actual position in the generated PDF document. Text directions are also supported.

### Code Examples
```csharp
// Example of using Syncfusion's DocIO component for PDF conversion
using Syncfusion.DocIO;
using Syncfusion.Pdf;

// Load the DOCX document
WordDocument document = new WordDocument("input.docx");

// Convert the DOCX to PDF
PdfDocument pdfDocument = document.ExportToPdf();

// Save the generated PDF
pdfDocument.Save("output.pdf");
```

### RAG Annotations
Each section is summarized as follows:
- **Known Limitations**: Highlights restrictions for older versions of Word documents.
- **Breaks**: Confirms support for various document breaks.
- **OLEObject**: Describes partial support for OLEObjects.
- **Text box**: Explains direct rendering of text boxes in PDF output.

#### Figure: Converted PDF with Table Style – Light Shading
![Figure 84: Converted PDF with Table Style – Light Shading](DoctoPDF.pdf#page=2 "Northwind Suppliers Table in PDF")

<!-- tags: [Essential DocIO, pdf conversion, table styles, breaks, OLEObjects, text box] keywords: [Essential DocIO, table style conversion, Word document limitation, section break, line break, page break, OLEObject, text rendering, text box] -->
```