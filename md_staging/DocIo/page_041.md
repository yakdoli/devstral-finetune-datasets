```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_041.jpeg
document_name: DocIo
page_number: 041
page_id: DocIo#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:07Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Demonstrates how to create and save a Word document.
- Highlights the procedure to save a document to disk using `FormatType.Doc`.
- Includes both C# and VB.NET examples for saving a document.

## Content

### Saving a Word Document

The following code snippets demonstrate how to save a Word document to disk:

```csharp
document.Save("Sample.doc", FormatType.Doc);
```

```vb.net
' Saving the document to disk.
document.Save("Sample.doc", FormatType.Doc)
```

#### Word Document Example

The sample Word document created through the above procedure is shown below.

![Figure 19: Word Document](https://example.com/figure19.png)

A Word document is created in the WPF application.

### 3.3.4 Silverlight

## API Reference

- **Namespace**: `Syncfusion.DocIO`
- **Class**: `WordDocument`
- **Method**: `Save(string fileName, FormatType format)`
  - **Parameters**:
    - `fileName`: The path where the document will be saved.
    - `format`: The file format (e.g., `FormatType.Doc`).
  - **Returns**: `void`
  - **Description**: Saves the document to the specified file with the given format.

## Code Examples

### C# Example

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.Dls;
using Syncfusion.Windows.Forms鞬
// ... Additional usings if required

WordDocument document = new WordDocument();
// ... Add content to the document
document.Save("Sample.doc", FormatType.Doc);
```

### VB.NET Example

```vb.net
Imports Syncfusion.DocIO
Imports Syncfusion.DocIO.Dls
Imports Syncfusion.Windows.Forms鞬
' ... Additional imports if required

Dim document As New WordDocument()
' ... Add content to the document
document.Save("Sample.doc", FormatType.Doc)
```

## Page-level Navigation/TOC (if applicable)

- [ ] Overview
- [ ] Content
- [ ] API Reference
- [ ] Code Examples

## Cross References

See also:

- [ ] Document creation and modification methods.
- [ ] Additional examples for Silverlight integration.

<!-- tags: DocIO, WordDocument, WPF, Silverlight, Save, FormatType, WindowsFormsTools keyword: document-saving, Word, WPF application, Silverlight, Syncfusion -->
```