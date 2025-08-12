```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_029.jpeg
document_name: pdf
page_number: 029
page_id: pdf#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:34Z
fidelity: lossless
-->

# Essential PDF

## Overview
- A detailed structure of PDF document classes and their hierarchy, including key components such as Actions, Attachments, Bookmarks, Pages, and Form sections.
- Highlights the various elements that can be manipulated or accessed in a PDF document, such as annotations, tables, and transitions.
- Emphasizes the distinction between PDFDocument and PdfLoadedDocument to handle different scenarios of document creation and editing.

## Content

### PDFDocument Class Structure
The `PDFDocument` class serves as the primary interface for creating and modifying PDF documents. It provides access to various properties and methods that help in managing different aspects of a PDF document.

#### Main Components
- **Actions**
- **Attachments**
  - `PdfAttachment`
- **BookMarks**
  - `PdfBookmark`
- **ColorSpace**
- **Template**
  - `PdfPageTemplateElement`
- **Pages**
  - **PdfPage**
    - Inherits from `PdfPageBase`
    - Contains `Sections`, `PageSettings`, and `Transition`
    - **Sections**
      - `PdfSection`
    - **Annotations**
      - Inherits from `PdfAnnotation`
    - **Signature**
      - `Appearance`
        - `PdfAppearance`
      - `Certificate`
        - `PdfCertificate`
- **Form**
  - Contains `Fields`
  - `PdfField`
  - `PdfLoadedField`
- **Security**
  - `PdfSecurity`
- **Signature**

### Abstract Classes and Subclasses
- **PdfPageBase**
  - **Sections**
    - `Section`
  - **Annotations**
    - `PdfAnnotation`
  - **Signature**
    - `Appearance`
      - `PdfAppearance`
    - `Certificate`
      - `PdfCertificate`

- **PdfGraphics**
  - **Table**
  - **PdfLightTable**
    - `Columns`
      - `PdfColumn`
    - `Rows`
      - `PdfRow`

### PdfLoadedDocument
- Similar to `PdfDocument` but designed for handling existing documents.
- Contains:
  - **BookMarks**
    - `PdfBookmark`
  - **ColorSpace**
  - **Form**
    - `PdfLoadedForm`
      - Contains `Fields`
        - `PdfLoadedField`
  - **Pages**
    - `PdfLoadedPage`
      - Inherits from `PdfPageBase`
  - **Security**
    - `PdfSecurity`
  - **Signature**

## API Reference
- **Namespace**: Syncfusion.Pdf
- **Key Classes**:
  - `PdfDocument`
  - `PdfPageBase`
  - `PdfAnnotation`
  - `PdfAppearance`
  - `PdfCertificate`
  - `PdfField`
  - `PdfLoadedField`

### Class Descriptions
- **PdfDocument**: The main class for creating and manipulating PDF documents.
- **PdfPageBase**: Abstract base class for page-related functionalities.
- **PdfAnnotation**: Abstract class for handling annotations.
- **PdfAppearance**: Class representing signatures and their appearance.
- **PdfCertificate**: Class for managing digital certificates.
- **PdfField**: Base class for handling form fields.
- **PdfLoadedField**: Class for handling fields in an existing PDF document.

## Code Examples

### Example: Creating a Basic PDF Document
```csharp
using Syncfusion.Pdf;

// Create a new PDF document
PdfDocument document = new PdfDocument();

// Add a blank page
PdfPage page = document.Pages.Add();

// Draw some text on the page
PdfGraphics graphics = page.Graphics;
float x = 50;
float y = 50;
graphics.DrawString("Hello, World!", new PdfStandardFont(PdfFontFamily.Helvetica, 20), PdfBrushes.Black, x, y);

// Save the document
document.Save("Output.pdf");
document.Close(true);
```

### Example: Adding Bookmarks
```csharp
using Syncfusion.Pdf;

// Create a new PDF document
PdfDocument document = new PdfDocument();

// Add multiple pages with content
for (int i = 0; i < 5; i++)
{
    PdfPage page = document.Pages.Add();
    // Draw content on each page
}

// Add bookmarks
PdfBookmark bookmark = new PdfBookmark();
bookmark.Text = "Chapter 1";
bookmark.Open();
{
    PdfBookmark subBookmark = new PdfBookmark();
    subBookmark.Text = "Section 1.1";
    subBookmark.Page = document.Pages[0];
    subBookmark.PageIndex = 0;
    bookmark.Add(subBookmark);
}

// Save and close the document
document.Bookmarks.Add(bookmark);
document.Save("BookmarkedPDF.pdf");
document.Close(true);
```

## Cross References
- See also: Official Syncfusion documentation for more detailed examples and API references.
- [Syncfusion PDF Documentation](https://help.syncfusion.com/documentprocessing/net/pdf/getting-started)

## RAG Annotations
<!-- tags: pdf, document, structure, actions, annotations, bookmarks, form fields, security, transition, signing keywords: pdfdocument, pdfpagebase, pdfannotation, pdfappearance, pdfcertificate, pdfsecurity, signature -->
```