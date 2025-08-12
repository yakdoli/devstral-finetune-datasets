```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: pdf
page_number: 047
page_id: pdf#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:57Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Open MainPage.xaml of the application in the designer.
- Add assemblies as references: Syncfusion.Compression.Silverlight.dll and Syncfusion.Pdf.Silverlight.dll.

## Content

Essential PDF is now deployed in your Silverlight application.

### Create and add a PDF document with pages to the application

The following steps guide you to create and add a PDF document to this application:

1. **Create a PDF document using the following code.**

   **Note:** The PDF document represents the document that is created in the memory. It is only the memory representation of the PDF document that is written to the disk.

   ```csharp
   // Create a new PDF document. This object represents the PDF document.
   // This document has one page, by default. Additional pages have to be added.
   PdfDocument pdfDoc = new PdfDocument();
   ```

   ```vbnet
   ' Create a new PDF document. This object represents the PDF document.
   ' This document has one page, by default. Additional pages have to be added.
   Dim pdfDoc As Syncfusion.Pdf.PdfDocument = New Syncfusion.Pdf.PdfDocument()
   ```

   A new PDF document is created.

2. **Add a new page to the created document.**

   ```csharp
   // Add a page to the document
   PdfPage page = doc.Pages.Add();
   ```

   ```vbnet
   ' Add a page to the document
   Dim firstPage As Syncfusion.Pdf.PdfPage = doc.Pages.Add()
   ```

## API Reference (if applicable)
- Namespace: `Syncfusion.Pdf`
  - Class: `PdfDocument`
  - Members: 
    - `Add()`: Adds a new page to the document.

## Code Examples (multi-language supported)
- C#: 
  ```csharp
  // Create a new PDF document.
  PdfDocument pdfDoc = new PdfDocument();
  
  // Add a new page to the document.
  PdfPage page = doc.Pages.Add();
  ```

- VB.NET: 
  ```vbnet
  ' Create a new PDF document.
  Dim pdfDoc As Syncfusion.Pdf.PdfDocument = New Syncfusion.Pdf.PdfDocument()
  
  ' Add a new page to the document.
  Dim firstPage As Syncfusion.Pdf.PdfPage = doc.Pages.Add()
  ```

## Page-level Navigation/TOC (if applicable)
- Deploying Essential PDF in your application
- Creating and adding pages to a PDF document

## Cross References
- See also: [PDF Documentation in Syncfusion](#)

<!-- tags: [PDF, Silverlight, Syncfusion, PDF creation, page addition] keywords: [Essential PDF, PDF document, memory representation, Silverlight, Syncfusion.Pdf, Add page, C#, VB.NET] -->
```