```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_255.jpeg
document_name: pdf
page_number: 255
page_id: pdf#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:18Z
fidelity: lossless
-->

# PDF Document Operations

## Overview
- Lists various methods and properties for managing PDF documents.
- Focuses on adding fields, appending documents, creating bookmarks, disposing objects, and saving files.
- Includes detailed descriptions of operations like creating a form, setting compression, and handling document information.

## Content

### Method Operations

| Name                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| AddFields           | Adds the fields connected to the page.                                      |
| Append              | Appends the specified loaded document to this one.                          |
| Clone               | Creates a shallow copy of the current document.                             |
| Close               | Releases the document stream.                                               |
| CreateBookmarkRoot  | Creates the bookmark root.                                                  |
| CreateForm          | Creates a new form.                                                         |
| Dispose             | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. |
| DisposeOnClose      | Adds an object to a collection of the objects that will be disposed during document closing. *(Inherited from PdfDocumentBase.)* |
| ImportPage          | Overloaded.                                                                |
| ImportPageRange     | Imports a page range from a loaded document. *(Inherited from PdfDocumentBase.)* |
| OnDocumentSaved     | Raises DocumentSaved event. *(Inherited from PdfDocumentBase.)*              |
| Save                | Saves the document.                                                         |
| Split               | Splits a PDF file to many PDF files; each of them consists of one page from the source file. |

### Properties

| Name                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Bookmarks           | Gets the bookmarks.                                                          |
| Compression         | Gets or sets the desired level of stream compression.                      |
| Conformance         | Gets the conformance level applied in the PDF.                             |
| DocumentInformation | Gets or sets document's information and properties.                        |
| FileStructure       | Gets or sets the internal structure of the PDF file.                        |

## API Reference (if applicable)
- **Class Name**: PdfDocument
- **Methods**:
  - AddFields
  - Append
  - Clone
  - Close
  - CreateBookmarkRoot
  - CreateForm
  - Dispose
  - DisposeOnClose
  - ImportPage
  - ImportPageRange
  - OnDocumentSaved
  - Save
  - Split
- **Properties**:
  - Bookmarks
  - Compression
  - Conformance
  - DocumentInformation
  - FileStructure

## Code Examples (multi-language supported)
- Examples demonstrating the use of various methods and properties can be provided here, such as saving a PDF file:

```csharp
using Syncfusion.Pdf;

// Sample code for saving a PDF document
PdfDocument document = new PdfDocument();
// ... Add content to the document ...
document.Save("output.pdf");
document.Close();
```

### Callouts
#### Note:
- Ensure all changes to the document are saved before closing to prevent data loss.

### Warning:
- Dispose objects properly to free up system resources after use.

### Tip:
- Use the `ImportPageRange` method to efficiently import specific pages from another PDF document.

## Tagging and Keywords
<!-- tags: [PdfDocument, PDF, document manipulation, Syncfusion Winforms, api, 11.4.0.26] keywords: [AddFields, Append, Close, CreateForm, Dispose, ImportPage, Save, Bookmarks, Compression, Conformance, DocumentInformation, FileStructure] -->
```