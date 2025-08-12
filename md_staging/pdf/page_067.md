```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: pdf
page_number: 067
page_id: pdf#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:17Z
fidelity: lossless
-->

# Essential PDF

## Content
### Document Members
The following table lists the properties of the Document class.

| Property | Description |
| --- | --- |
| Document | Gets the document. |
| Item | Gets the PdfPage at the specified index. |
| PageLabel | Gets or sets the page label. |
| Pages | Gets the pages. |
| PageSettings | Gets or sets the page settings of the section. |
| Template | Gets or sets a template for the pages in the section. |

### Events
The following table lists the events associated with the Document class.

| Name | Description |
| --- | --- |
| PageAdded | This event is raised when a new page is added. |

### Page
#### Overview
- Represents a rectangular area where the user can draw something, attach annotations, and so on.
- Each page has layers. When a page is created, it has one default layer.
- You can create more layers and refer them by an index.
- Each layer is associated with a graphics stream and has its own graphics (PdfGraphics class).

#### PdfPage Class
- The PdfPage class is used to create a page.
- The following are the members exposed by this class.

### Methods
#### Overview
The following table lists the methods of the PdfPage class.

| Name | Description |
| --- | --- |
| CreateTemplate | Creates a template from the page content and all annotation appearances. |
| ExtractImages | Extracts images from the given PDF page. |
| ExtractText | Extracts text from the given PDF Page. |
| GetAnnots | Gets the annotations array. |
| GetClientSize | Returns a page size reduced by page margins and page template dimensions. |

### WinForms-specific conventions
- In the context of the page, all the described functionalities are typically implemented in a Windows Forms environment using the Syncfusion Winforms library.
- The methods listed (e.g., CreateTemplate, ExtractImages) are part of the PdfPage class, which is a component of the Syncfusion PDF library for Windows Forms applications.
- These methods enable developers to manipulate PDF pages by creating templates, extracting media content, and retrieving annotations.

### API Reference
#### Namespace: Syncfusion.Pdf
#### Class: PdfPage
- **Methods**
  - **CreateTemplate()**
    - **Description**: Creates a template from the page content and all annotation appearances.
  - **ExtractImages()**
    - **Description**: Extracts images from the given PDF page.
  - **ExtractText()**
    - **Description**: Extracts text from the given PDF Page.
  - **GetAnnots()**
    - **Description**: Gets the annotations array.
  - **GetClientSize()**
    - **Description**: Returns a page size reduced by page margins and page template dimensions.

### Code Examples
- The following example demonstrates how to extract text from a PDF page using the `ExtractText` method:
```csharp
using Syncfusion.Pdf;
using System;

class Program
{
    static void Main()
    {
        // Create a PdfViewer to load the PDF document.
        PdfDocument document = new PdfDocument("Sample.pdf");

        // Access the first page.
        PdfPage page = document.Pages[0];

        // Extract text from the page.
        string extractedText = page.ExtractText();

        // Output the extracted text.
        Console.WriteLine("Extracted text: " + extractedText);
    }
}
```

## RAG Annotations
<!-- tags: [pdf, document, page, annotations, Syncfusion Winforms, version: 11.4.0.26] keywords: [PdfPage, CreateTemplate, ExtractImages, ExtractText, GetAnnots, GetClientSize, layers, graphics stream, WinForms] -->
```