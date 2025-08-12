```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_306.jpeg
document_name: DocIo
page_number: 306
page_id: DocIo#page_306
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:22Z
fidelity: lossless
-->

## Overview

To summarize the page scope, the following points are covered:

- **DOCX Conversion and Supported Elements**: 
  - The supported elements and limitations for converting DOCX to EPUB are detailed.

- **DOCX Support**:
  - Microsoft introduced .docx, and Essential DocIO provides support for creating, reading, and modifying .docx files.

- **Key Features**:
  - Embedding font files in EPUB documents and their size impact.

## Content

### ASP.NET MVC

The file path for accessing the ASP.NET MVC sample is:
Start -> All Programs -> Syncfusion -> Essential Studio x.x.x.xx -> Dashboard -> ASP.NET MVC -> DocIO.MVC -> Samples -> 3.5 -> Views -> ImportandExport -> DOCTOEPub.aspx

### Supported Elements

The following are the Supported Elements:

- Text and Paragraph Formatting
- Lists
- Tables
- Images
- Footnote
- Hyperlink
- Styles
- Table of Contents
- Document Properties

### Known Limitations

The following are the known limitations:

- Embedding font files may increase the size of the EPub document
- Embedding font files is not supported in medium trust

**Note:** Currently, Doc to EPub conversion is not supported in Silverlight application.

### 4.9 DOCX Support

Microsoft introduced the .docx file format in its new Office and Word applications to replace the commonly used doc format. Essential DocIO now provides support for .docx files. Docx files are created using the same APIs as for .doc files using Essential DocIO. Essential DocIO provides support for:

- Creating a .docx file from scratch
- Read/Modify a .docx file

#### Creating a .docx file

To create a .docx file:

1. Create a word document using Essential DocIO APIs.

## API Reference (if applicable)

### Namespace
- **Syncfusion.DocIO**
  
### Methods
- **CreateWordDocument()**
  - **Parameters**:
    - None
  - **Returns**: A new `WordDocument` object initialized for .docx.

#### Example:

```csharp
WordDocument document = new WordDocument();
document.Save("output.docx");
```

## Code Examples

#### Example: Creating a .docx File

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.Dlients;
using Syncfusion.DocIO.Formats;
using System.IO;

WordDocument document = new WordDocument();
// Add content to the document
document.Save("output.docx", WordExportFormat.OpenXML2007);
```

## Cross References

See also:
- **EPUB Conversion Documentation**: For more details on converting DOC to EPUB.

## RAG Annotations

<!-- tags: [DocIO, DOCX, EPUB, Conversion, SupportedElements, KnownLimitations, WordDocument, DocumentCreation, SyncfusionWinforms] 
keywords: [supported elements, docx, epub, conversion limitations, word document, document properties, essential docio, document creation, document modification, font embedding] -->
```
