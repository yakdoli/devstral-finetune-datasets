```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_213.jpeg
document_name: pdf
page_number: 213
page_id: pdf#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:05Z
fidelity: lossless
-->

# Essential PDF

## Content

### 4.1.7.1.2 Text Pagination

**Overview**

- Explains how text can flow across multiple pages in a PDF document.
- Describes using the PDFStringFormat class to specify custom formats for text elements.
- Provides a code snippet demonstrating the process of drawing text with custom formats.

### Text in a PDF Document

Text in a PDF document can flow through multiple pages. You can specify different formats for the text element using the PDFStringFormat class of Essential PDF. The following code snippet illustrates how to draw the text element of a PDF document with custom formats.

```csharp
// Create a new PDF document.
PdfDocument doc = new PdfDocument();

// Add a page to the document.
PdfPage page = doc.Pages.Add();
```

## References

Figure 35: Simple Text

![](Figure_35_Simple_Text.png)

- This figure demonstrates a basic example of text displayed in a PDF document using Essential PDF.

## API Reference

##### Classes

- **PdfDocument**: Represents a PDF document that can be created, manipulated, and saved.
- **PdfPage**: Represents a page within a PDF document, allowing the addition of content like text, images, and graphics.

##### Methods

- `Add()`: Adds a new page to the document.

## Code Examples

C# Example:
```csharp
// Create a new PDF document.
PdfDocument doc = new PdfDocument();

// Add a page to the document.
PdfPage page = doc.Pages.Add();
```

## Notes

- Ensure that the necessary namespaces are included in your code, such as `Syncfusion.Pdf` for Essential PDF operations.
- The code snippet above is foundational and can be extended to include text formatting, positioning, and other features using the PDFStringFormat class.

<!-- tags: [essential-pdf, pdf-text-pagination, text-formats, pdf-document, pdf-page, pdfstringformat, syncfusion, winforms] keywords: [text pagination, custom formats, pdf, document creation, page addition, text elements, code snippets, pdf manipulation, essentials pdf, syncfusion winforms] -->
```