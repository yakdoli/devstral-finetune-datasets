```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: pdf
page_number: 046
page_id: pdf#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:22Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This section discusses how PDF documents can be created, modified, and viewed in a WPF application.
- The procedure for creating a simple PDF document with "Hello world!" content is demonstrated.
- A sample PDF document is shown in Figure 22.
- The section also outlines how to deploy Essential PDF in a Silverlight application.

## Content

### PDF Document in WPF

PDF document will be closed after saving.

The sample pdf document created through the above procedure is shown below.

![Figure 22: PDF Document with pages](https://i.imgur.com/Figure22.png)
*Figure 22: PDF Document with pages*

**Description:**
A PDF document is created in the WPF application.

### 3.3.4 Silverlight

Now, you have created a Silverlight application (refer *Creating Platform Application*). This section covers the following:

- Deploying Essential PDF in a Silverlight Application
- Create and add a PDF document with pages to the application

#### Deploying Essential PDF in a Silverlight Application

The following steps will guide you to deploy Essential PDF:

---

## API Reference

#### Methods

- **Saving PDF Documents:**
 胤 PDF Document</li>
<liFizz PDF Document will be closed after saving.</li>
<br>

#### Creating a Sample PDF Document

The sample PDF document created through the above procedure is shown below.

#### Sample PDF Document Creation

![Sample PDF Document](https://i.imgur.com/SamplePDF.png)

**Description:**
A PDF document is created in the WPF application.

#### Deploying Essential PDF in a Silverlight Application

**Steps to Deploy:**
The following steps will guide you to deploy Essential PDF:

---

## Code Examples

#### Example: Creating a PDF Document in WPF

```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;
using Syncfusion.Pdf.DocIO;

namespace WpfApplication
{
    public class PDFDocumentExample
    {
        public void CreatePDFDocument()
        {
            // Create a new PDF document
            PdfDocument document = new PdfDocument();

            // Add a new page to the document
            PdfPage page = document.Pages.Add();

            // Draw text on the page
            PdfGraphics graphics = page.Graphics;
            PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 20);
            graphics.DrawString("Hello world!", font, PdfBrushes.Black, new PointF(10, 10));

            // Save the PDF document
            string filePath = "Sample.pdf";
            document.Save(filePath);

            // Close the document
            document.Close(true);
        }
    }
}
```

**Description:**
The above example demonstrates how to create a PDF document with the text "Hello world!" and save it as "Sample.pdf". The document is then closed after saving.

---

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Essential PDF, WPF, Silverlight] keywords: [PDF creation, WPF application, Silverlight application, PDF deployment] -->
```