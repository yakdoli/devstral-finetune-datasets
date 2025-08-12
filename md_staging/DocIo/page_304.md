```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_304.jpeg
document_name: DocIo
page_number: 304
page_id: DocIo#page_304
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:13Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Instructions on exporting headers and footers in an EPub document.
- Code examples in C# and VB for enabling header and footer export.
- Description of the output EPub document with header and footer disabled.

## Content

### Setting Up Header and Footer Export

#### C#

The following code snippet demonstrates how to enable the export of headers and footers when saving a Word document as an EPub file.

```csharp
// Turn on exporting headers and footers
document.SaveOptions.HtmlExportHeadersFooters = true;

// Save the EPub file
document.Save("Sample.epub", FormatType.EPub);
```

#### VB

The following code snippet achieves the same functionality, but in Visual Basic.

```vb
' Load any .doc or .docx file
Dim document As WordDocument = New WordDocument(filename)

' Turn on exporting headers and footers
document.SaveOptions.HtmlExportHeadersFooters = True

' Save the EPub file
document.Save("Sample.epub", FormatType.EPub)
```

### Output EPub Document with Headers and Footers Disabled

The following is the sample image of the output EPub document with header and footer disabled.

## Code Examples

### C# Example

```csharp
// Import necessary namespaces
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Load the document
WordDocument document = new WordDocument(filename);

// Enable header and footer export
document.SaveOptions.HtmlExportHeadersFooters = true;

// Save the document as EPub
document.Save("Sample.epub", FormatType.EPub);
```

### VB Example

```vb
' Import necessary namespaces
Imports Syncfusion.DocIO
Imports Syncfusion.DocIO.DLS

' Load the document
Dim document As WordDocument = New WordDocument(filename)

' Enable header and footer export
document.SaveOptions.HtmlExportHeadersFooters = True

' Save the document as EPub
document.Save("Sample.epub", FormatType.EPub)
```

## API Reference

### `HtmlExportHeadersFooters`

- **Namespace:** Syncfusion.DocIO.SaveOptions
- **Description:** A property to enable or disable the export of headers and footers during EPub document saving.
- **Parameters:** None
- **Return Type:** Boolean
- **Default Value:** false

### `FormatType.EPub`

- **Namespace:** Syncfusion.DocIO
- **Description:** An enumeration value indicating the EPub format for saving documents.

## Page-level Navigation/TOC

- [Main Content](#content)
  - [Setting Up Header and Footer Export](#setting-up-header-and-footer-export)
  - [Output EPub Document with Headers and Footers Disabled](#output-epub-document-with-headers-and-footers-disabled)

### See also

- [DocIO EPub Export Documentation](https://docs.syncfusion.com/windowsforms/docio/working-with-epub-format/)
- [Syncfusion DocIO Features](https://www.syncfusion.com/products/windowsforms/docio)

<!-- tags: [syncfusion, windowsforms, docio, epub, headers, footers, export, kitจร์] keywords: [syncfusion, DocIO, EPub, headers, footers, export, code example, VB, C#] -->
```