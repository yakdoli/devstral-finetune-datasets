```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_354.jpeg
document_name: pdf
page_number: 354
page_id: pdf#page_354
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:48Z
fidelity: lossless
-->

# Essential PDF

```csharp
PdfDocument document = new PdfDocument();
document.ViewerPreferences.PageMode = PdfPageMode.UseAttachments;
```

```vb
Dim document As New PdfDocument()
document.ViewerPreferences.PageMode = PdfPageMode.UseAttachments
```

![Sample.pdf - Adobe Reader](https://i.imgur.com/3EZJ8SM.png)
*Figure 66: PDF with default view*

## 5.1.2 Advanced

This section shows some advanced tasks in a PDF Generator.

---

## API Reference

### Namespaces

- `Syncfusion.Pdf`
- `Syncfusion.Pdf.Graphics`
- `Syncfusion.Pdf.Interactive`
- `Syncfusion.Pdf.Security`

### Classes

- **PdfDocument**
  - Manages the document-level properties and methods.
  - Includes methods for reading, writing, and manipulating PDF documents.

### Members

- **Properties**
  - `Version`: Returns the PDF version.
  - `IsOpened`: Indicates whether the document is currently open.
  - `ViewerPreferences`: Manages viewer-related preferences like page mode and zoom level.

- **Methods**
  - `Save(string fileName)`: Saves the document to the specified file.
  - `Open(string fileName)`: Opens an existing PDF file.
  - `AddPage(int width, int height)`: Adds a new page to the document.

- **Events**
  - `DocumentSaving`: Triggered before saving the document.
  - `DocumentOpened`: Triggered after a document is successfully opened.

---

## Code Examples

### C#

```csharp
using Syncfusion.Pdf;

// Create a new PDF document
PdfDocument document = new PdfDocument();

// Set viewer preferences
document.ViewerPreferences.PageMode = PdfPageMode.UseAttachments;

// Add an attachment to the document
document.Attachments.Add("business.jpg", File.ReadAllBytes("business.jpg"));
document.Attachments.Add("logo.png", File.ReadAllBytes("logo.png"));
document.Attachments.Add("mouse.jpg", File.ReadAllBytes("mouse.jpg"));
document.Attachments.Add("simple.txt", File.ReadAllBytes("simple.txt"));

// Save the document
document.Save("Sample.pdf");

// Clean up resources
document.Close();
```

### VB.NET

```vb
Imports Syncfusion.Pdf

Dim document As New PdfDocument()

document.ViewerPreferences.PageMode = PdfPageMode.UseAttachments

document.Attachments.Add("business.jpg", File.ReadAllBytes("business.jpg"))
document.Attachments.Add("logo.png", File.ReadAllBytes("logo.png"))
document.Attachments.Add("mouse.jpg", File.ReadAllBytes("mouse.jpg"))
document.Attachments.Add("simple.txt", File.ReadAllBytes("simple.txt"))

document.Save("Sample.pdf")
document.Close()
```

---

<!-- tags: [Syncfusion, Winforms, PDF, Essential PDF, viewer preferences, attachments, advanced tasks] keywords: [PdfDocument, ViewerPreferences, UseAttachments, attachment, document saving] -->
```