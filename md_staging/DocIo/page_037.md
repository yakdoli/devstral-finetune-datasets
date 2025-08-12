```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: DocIo
page_number: 037
page_id: DocIo#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:49Z
fidelity: lossless
-->

## Essential DocIO

### Overview
- Application with Essential DocIO requires specific dependent assemblies for deployment.
- Includes Syncfusion.Core.dll, Syncfusion.Compression.Base.dll, and Syncfusion.DocIO.Base.dll.

### Content

#### Essential DocIO Deployment

Essential DocIO is now deployed in your ASP.NET application.

#### Creating a Word Document

The following code snippet will guide you to create and add a Word document to this application:

```csharp
[C#]

// Include the following namespaces.
using Syncfusion.DocIO.DLS;
using Syncfusion.DocIO;

// Create a new Word document.
// This document has no section and no paragraph by default.
WordDocument document = new WordDocument();

// Add a new section to the document.
IWSection section = document.AddSection();

// Add a new paragraph to the section.
IWParagraph paragraph = section.AddParagraph();

// Insert Text into the paragraph
paragraph.AppendText("Hello World!");

// Saving the document to disk.
document.Save("Sample.doc", FormatType.Doc);
```

---

## API Reference (if applicable)
- **Namespace**: `Syncfusion.DocIO`
- **Class**: `WordDocument`
  - **Method**: `AddSection()`
    - **Returns**: `IWSection`
  - **Method**: `AddParagraph()`
    - **Returns**: `IWParagraph`
  - **Method**: `AppendText(string text)`
    - **Parameters**: 
      - `text` | `string` | The text to append to the paragraph.
  - **Method**: `Save(string fileName, FormatType format)`
    - **Parameters**: 
      - `fileName` | `string` | The name of the file to save.
      - `format` | `FormatType` | The format type (e.g., `Doc`, `Docx`, etc.).

---

### Code Examples

```csharp
// Example of creating and saving a Word document
using Syncfusion.DocIO.DLS;
using Syncfusion.DocIO;

// Initialize a new Word document
WordDocument document = new WordDocument();

// Create a new section
IWSection section = document.AddSection();

// Create a new paragraph and add text
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("Hello World!");

// Save the document to disk
document.Save("Sample.doc", FormatType.Doc);
```

---

## Cross References
- See also: [Essential DocIO Documentation](https://www.syncfusion.com/downloads/docio)

<!-- tags: [Syncfusion, DocIO, Word Document, C#, WinForms] keywords: [Essential DocIO, Word Document, C#, WinForms, API Reference, Code Examples, Deployment, Section, Paragraph, AppendText, Save] -->
```