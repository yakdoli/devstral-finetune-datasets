```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: DocIo
page_number: 086
page_id: DocIo#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:42Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Essential DocIO provides support for converting and manipulating Word documents in various formats.
- Demonstrates how to open and save Word documents in different formats.

## Content

### Document Conversion Example

#### C#

```csharp
WordDocument doc = new WordDocument();
doc.Open("SourceDocument.doc", FormatType.Doc);
doc.Save("OutDocument.docx", FormatType.Word2007);
```

#### VB.NET

```vb
Dim doc As New WordDocument()
doc.Open("SourceDocument.doc", FormatType.Doc)
doc.Save("OutDocument.docx", FormatType.Word2007)
```

**Explanation**: Essential DocIO supports reading and converting Word 2007, Word 2010, and Word 2013 files. Currently, the support for `docx` files is similar to `.doc` files, with only the format differing upon reading.

#### Reading a `.docx` File

**The following code illustrates how to read a `.docx` file.**

#### C#

```csharp
WordDocument doc = new WordDocument("C:\\sample.docx", FormatType.Docx);
```

#### VB

```vb
Dim doc As New WordDocument("c:\\sample.docx", FormatType.Docx)
```

### 4.2.3.1 Word 2010 Support

**Explanation**: Microsoft Word 2010 uses the ISO/IEC 29500 standard for document creation, whereas older versions use the ECMA-376 standard. This feature allows Essential DocIO to create and modify ISO/IEC 29500 standard documents. Using Essential DocIO, you can create a document with the ISO/IEC 29500 standard by specifying its format type as `Word 2010`.

### Use Case Scenarios

- **Scenario 1**: Creating a new document in Word 2010 format using Essential DocIO.
- **Scenario 2**: Modifying an existing document to confirm compliance with ISO/IEC 29500 standards.
- **Scenario 3**: Reading and converting legacy `.doc` files to modern `.docx` format.

## Page-level Navigation/TOC

- 4.2.3.1 Word 2010 Support
- Use Case Scenarios

## Cross References

See also:
- [Overview of Essential DocIO]
- [Supported File Formats]
- [Advanced Document Manipulation]

## API Reference

### WordDocument

- **Method**: `Open(string path, FormatType format)`
  - **Parameters**:
    - `path`: The file path of the Word document.
    - `format`: The format type of the document to open.

- **Method**: `Save(string path, FormatType format)`
  - **Parameters**:
    - `path`: The file path to save the Word document.
    - `format`: The format type of the document to save.

## Code Examples

### Opening and Saving a Document

#### C#

```csharp
using(Syncfusion.DocIO.WordDocument doc = new Syncfusion.DocIO.WordDocument())
{
    doc.Open("SourceDocument.doc", Syncfusion.DocIO.FormatType.Doc);
    doc.Save("OutDocument.docx", Syncfusion.DocIO.FormatType.Word2007);
}
```

#### VB.NET

```vb
Dim doc As New Syncfusion.DocIO.WordDocument()
doc.Open("SourceDocument.doc", Syncfusion.DocIO.FormatType.Doc)
doc.Save("OutDocument.docx", Syncfusion.DocIO.FormatType.Word2007)
```

### Reading a `.docx` File

#### C#

```csharp
using(Syncfusion.DocIO.WordDocument doc = new Syncfusion.DocIO.WordDocument("C:\\sample.docx", Syncfusion.DocIO.FormatType.Docx))
{
    // Perform operations on the document
}
```

### Creating a Word 2010 Document

#### C#

```csharp
using(Syncfusion.DocIO.WordDocument doc = new Syncfusion.DocIO.WordDocument())
{
    // Create content
    doc.Save("Output.docx", Syncfusion.DocIO.FormatType.Word2010);
}
```

#### VB.NET

```vb
Dim doc As New Syncfusion.DocIO.WordDocument()
' Create content
doc.Save("Output.docx", Syncfusion.DocIO.FormatType.Word2010)
```

<!-- tags: [DocIO, Word document, document conversion, Word 2010, ISO/IEC 29500, Syncfusion Winforms, essential docio, .docx, .doc] keywords: [conversion, format, document, essential, word, 2010, standard, create, modify, save, open, read] -->
```