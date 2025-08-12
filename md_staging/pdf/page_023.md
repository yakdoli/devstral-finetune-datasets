```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_023.jpeg
document_name: pdf
page_number: 023
page_id: pdf#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:04Z
fidelity: lossless
-->

## Overview
- This page demonstrates how to use the WPF Sample Browser to explore examples and samples for `Essential DocIO` and `Essential PDF` libraries.

## Content

### WPF Sample Browser

#### Essential DocIO Overview
- **Essential DocIO**: A .NET library for reading and writing Microsoft Word files.
  - Compatible with Microsoft Office COM libraries.
  - Built using C# and does not require Microsoft Word installation.

#### Featured Samples (Essential DocIO)
- **Sales Invoice**: Example of creating or manipulating a sales invoice.
- **Table Insertion**: Inserting tables into Word documents.
- **Table of Contents**: Generating a content table structure.
- **Employee Report**: Demonstrating employee details representation.
- **Forms**: Handling form insertions.
- **Clone and Merge**: Cloning or merging different Word document elements.
- **Update Fields**: Updating fields within Word documents.

#### WPF Sample Browser Interface
- **Navigation Pane**: Located on the left side for easy browsing.
- **Sample Display**: Various sample images shown for quick access.

**Figure 10: WPF Sample Browser**

#### Exploring PDF Samples

1. **Accessing PDF Samples**
   - **Step**: Click `Pdf` from the bottom-left pane to view PDF-related samples.

2. **PDF Samples Overview**
   - **Essential PDF**: A .NET library for manipulating Adobe PDF files.
   - Features include:
     - Full-featured object model for creating PDF files.
     - No external library dependencies.
     - Built in C# from scratch.

#### Featured Samples (Essential PDF)
- **Digital Signature**: Demonstrating digital signature functionality in PDFs.
- **Merge Documents**: Merging multiple PDF documents.
- **Overlay Documents**: Overlaying content on PDF documents.
- **Form Fill**: Filling out PDF forms.
- **Northwind Report**: Example of generating reports using PDF.

**Figure 11: PDF Samples for WPF**

1. **List of Samples**
   - A list of samples will be displayed on the left pane.

## API Reference

- Essential DocIO:
  - **Object model**: Similar to Microsoft Office COM libraries.
  - **languages**: .NET
  - **Framework**: Built in C#

- Essential PDF:
  - **Object model**: Full-featured for creating and manipulating PDF files.
  - **Dependencies**: None (built from scratch in C#).

## Code Examples

### Example: Creating a PDF Document

```csharp
// Import the necessary namespaces
using System;
using System.IO;
using Syncfusion.Pdf;

public class PdfExample {
    public static void CreatePdfDocument(string filePath) {
        // Create a new PDF document
        using (PdfDocument doc = new PdfDocument()) {
            // Add a new page
            PdfPage page = doc.Pages.Add();
            // Instantiate the PDF graphics for the page
            PdfGraphics graphics = page.Graphics;
            
            // Create a text element
            PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 15);
            PdfBrush brush = new PdfSolidBrush(PdfColor.Black);
            string text = "Hello, PDF!";
            
            // Draw text on the PDF page
            graphics.DrawString(text, font, brush, new PointF(100, 100));
            
            // Save the PDF document
            doc.Save(filePath);
        }
    }

    public static void Main() {
        string filePath = @"..\..\output.pdf";
        CreatePdfDocument(filePath);
    }
}
```

### Example: Manipulating Existing PDFs

```csharp
using System;
using System.IO;
using Syncfusion.Pdf;

public class PdfEditExample {
    public static void ModifyPdfDocument(string inputFilePath, string outputFilePath) {
        // Load an existing PDF document
        using (PdfDocument doc = new PdfDocument(inputFilePath)) {
            // Modify the document (e.g., add a stamp)
            foreach (PdfPage page in doc.Pages) {
                PdfGraphics graphics = page.Graphics;
                PdfBrush brush = new PdfSolidBrush(PdfColor.Red);
                
                // Add a stamp to the page
                graphics.DrawString("Confidential", 
                    new PdfStandardFont(PdfFontFamily.Arial, 12, PdfFontStyle.Bold),
                    brush, new PointF(100, 100));
            }
            
            // Save the modified PDF
            doc.Save(outputFilePath);
        }
    }

    public static void Main() {
        string inputFilePath = @"..\..\input.pdf";
        string outputFilePath = @"..\..\output_modified.pdf";
        ModifyPdfDocument(inputFilePath, outputFilePath);
    }
}
```

## Page-level Navigation/TOC (if applicable)

- WPF Sample Browser
  - Essential DocIO
    - Sales Invoice
    - Table Insertion
    - Table of Contents
    - Employee Report
    - Forms
    - Clone and Merge
    - Update Fields
  - Essential PDF
    - Digital Signature
    - Merge Documents
    - Overlay Documents
    - Form Fill
    - Northwind Report

## Cross References

- See also: [Additional documentation for Essential DocIO](#)
- See also: [Additional documentation for Essential PDF](#)

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Essential DocIO, Essential PDF, WPF Samples, PDF Manipulation, Word Document Processing] keywords: [DocIO, PDF, WPF, Sales Invoice, Table Insertion, Table of Contents, Employee Report, Forms, Clone and Merge, Update Fields, Digital Signature, Merge Documents, Overlay Documents, Form Fill, Northwind Report, Word Files, PDF Files, PDF Libraries, C#, .NET] -->
```
