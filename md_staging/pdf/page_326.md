```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_326.jpeg
document_name: pdf
page_number: 326
page_id: pdf#page_326
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:59Z
fidelity: lossless
-->

## Content

#### HTML to Tagged PDF Conversion

```csharp
html.EnableJavaScript = True
html.EnableActiveXContents = True

' Convert to Tagged PDF.
result = html.ConvertToTaggedPDF(document, url)
End Using

' Save and close the document.
document.Save("Sample.pdf")
document.Close(True)
```

**Note:** The HTML to PDF conversion, which creates a metafile during the evolution, would interpret the content as either text or an image. The outcome of this PDF would contain only paragraph and figure tags; hyperlinks are not supported.

### 4.4.2 Text Extraction

#### Overview
- A PDF file represents an ordered sequence of fixed pages. The planned appearance of everything that each page contains is completely specified down to the smallest detail.
- All the graphics, images, and text are specified to appear at precise spots on the page, in a particular color, of a given and fixed size, and so on.
- Essential PDF provides support to extract text from an existing PDF document. By using the `ExtractText` method, you can extract the text, page by page.

#### Code Example

```csharp
[C#]

// Load an existing PDF
PdfLoadedDocument ldoc = new PdfLoadedDocument("Sample.pdf");

// Loading first page
PdfLoadedPage page = ldoc.Pages[0];

// Extract text from first page
string s = page.ExtractText();
```

## API Reference

### Methods
- **ExtractText()**
  - **Description**: Extracts the text from a loaded page.
  - **Returns**: A `string` containing the extracted text.

## Cross References

- [Unclear] for further use cases related to PDF manipulation.
- [Unclear] for details on handling metafiles during HTML to PDF conversion.

<!-- tags: [pdf, html, tagged pdf, text extraction, syncfusion pdf, syncfusion winforms, version: 11.4.0.26] keywords: [convert to tagged pdf, extract text, pdfloadeddocument, pdfloadedpage, converttopaggedpdf, extracttext, metafile, support, image, hyperlink, page extraction, text extraction] -->
```