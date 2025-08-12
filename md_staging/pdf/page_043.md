```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_043.jpeg
document_name: pdf
page_number: 043
page_id: pdf#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:38Z
fidelity: lossless
-->

## Essential PDF

### Overview
- Guide to setting up references in the application.
- Detailed steps to create and add PDF documents to the application.

### Content

1. Go to **Solution Explorer** of the application you have created. Right-click the **Reference** folder and then click **Add References**.
2. Add the following assemblies as references in the application:
   - Syncfusion.Core.dll
   - Syncfusion.Compression.Base.dll
   - Syncfusion.Pdf.Base.dll

**Note:** For detailed documentation on Windows Application deployment, see: [http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf](http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf).

**Essential PDF** is deployed in the Windows application.

#### Create and add a PDF document with pages to the application

The following steps will guide you to create and add a PDF document to this application:

3. Create a PDF document using the following code.

**Note:** The PDF document represents the document that is created in the memory. It is only the memory representation of the PDF document that is written to the disk.

#### Code Examples

[C#]
```csharp
// Create a new PDF document. This object represents the PDF document.
// This document has one page, by default. Additional pages have to be added.
PdfDocument pdfDoc = new PdfDocument();
```

[VB.NET]
```vb
' Create a new PDF document. This object represents the PDF document.
' This document has one page, by default. Additional pages have to be added.
Dim pdfDoc As Syncfusion.Pdf.PdfDocument = New Syncfusion.Pdf.PdfDocument()
```

A new PDF document is created.

### Add a new page to the created document

[C#]
```csharp
// Add a page to the document
PdfPage page = doc.Pages.Add();
```

## API Reference (if applicable)

- **Namespace:** Syncfusion.Pdf
- **Class:** PdfDocument, PdfPage

## Code Examples

- **Creating a new PDF document**:
  - C# Example: `PdfDocument pdfDoc = new PdfDocument();`
  - VB.NET Example: `Dim pdfDoc As Syncfusion.Pdf.PdfDocument = New Syncfusion.Pdf.PdfDocument()`

- **Adding a new page to the document**:
  - C# Example: `PdfPage page = doc.Pages.Add();`

### See also:
- [Deploying Windows Application Guide](http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf)

<!-- tags: [Syncfusion, WinForms, PDF, Reference, Document Creation, Page Addition] keywords: [Syncfusion.Pdf.PdfDocument, Syncfusion.Pdf.PdfPage, Solution Explorer, Add References, Memory Representation, Windows Application Deployment] -->
```