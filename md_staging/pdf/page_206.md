```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_206.jpeg
document_name: pdf
page_number: 206
page_id: pdf#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:29Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates the Document Properties window.
- Explains the use of Custom Metadata in PDF documents.
- Describes how to add custom metadata fields beyond predefined ones.

## Content

### Document Properties

#### Figure: Document Properties

The Document Properties dialog shows detailed information about a PDF document. Here are the key details displayed:

- **File**: DocumentSettings
- **Title**: Document Properties Information
- **Author**: Syncfusion
- **Subject**: PDF demo
- **Keywords**: PDF
- **Created**: 8/17/2007 2:58:33 PM
- **Modified**: (Not specified)
- **Application**: (Not specified)

**Advanced Properties**:
- **PDF Producer**: Syncfusion Software
- **PDF Version**: 1.5 (Acrobat 6.x)
- **Location**: C:\Users\Administrator\Desktop\PDFScreenshots\
- **File Size**: 2.03 KB (2,083 Bytes)
- **Page Size**: 8.26 x 11.69 in
- **Number of Pages**: 1
- **Tagged PDF**: No
- **Fast Web View**: No

### 4.1.6.2 Custom Metadata

#### Overview
Essential PDF allows you to add required metadata (custom metadata) to a PDF document. Custom metadata can include information about the document that cannot fit within the predefined metadata fields. For example, if a metadata field "Link" is available, you can primarily provide a link there. However, Essential PDF enables you to add additional information such as the author, date of creation, etc., about the link.

#### Feature Details
This feature enables you to add as many metadata fields as you want. Only new metadata fields can be added; you cannot modify or add fields under the predefined metadata fields.

## API Reference

- **Namespace**: Syncfusion
- **Class**: DocumentProperties
- **Functionality**: Allows modification of document properties and metadata.

## Code Examples

### Example: Adding Custom Metadata

```csharp
// Sample code to add custom metadata fields in PDF
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;
using System;

class Program
{
    static void Main()
    {
        // Create a new PDF document
        PdfDocument document = new PdfDocument();
        
        // Add a new page
        PdfPage page = document.Pages.Add();
        
        // Create PDF graphics for drawing
        PdfGraphics graphics = page.Graphics;
        
        // Define a font
        PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 12);
        // Add a drawing
        graphics.DrawString("Custom Metadata Example", font, 
        PdfBrushes.Black, new RectangleF(0, 0, page.Width, page.Height));
        
        // Set custom metadata fields
        document.DocumentInformation.AdditionalInformation.Add("Author", "John Doe");
        document.DocumentInformation.AdditionalInformation.Add("Created", DateTime.Now.ToString());
        document.DocumentInformation.AdditionalInformation.Add("Custom Field", "Additional Information");
        
        // Save the PDF document
        document.Save("CustomMetadataExample.pdf");
        
        // Close the PDF document
        document.Close(true);
    }
}
```

## Page-level Navigation/TOC
- **Document Properties**
- **Custom Metadata**

### Additional Notes
The document demonstrates how to use the `AddAdditionalInformation` method to add custom metadata fields to a PDF document.

<!-- tags: [pdf, document properties, custom metadata, syncfusion] keywords: [Essential PDF, metadata, PDF document, custom metadata, metadata fields, Document Properties, Syncfusion] -->
```