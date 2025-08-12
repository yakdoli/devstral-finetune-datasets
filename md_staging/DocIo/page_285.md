```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_285.jpeg
document_name: DocIo
page_number: 285
page_id: DocIo#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:10Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Enabling RTF conversion by using DoclO.
- How to save a Word document to RTF format.
- Supported document elements in DocIO.

## Content

### References for More Information
For More Information Refer:
- [Doc To RTF](Doc To RTF)
- [Doc To HTML](Doc To HTML)
- [Doc to PDF](Doc to PDF)

### 4.8.1 Doc to RTF
You can now open or create Word documents and save to the .RTF format, enabling RTF conversion by using DocIO.

The following example illustrates how to save a Word document to RTF format.

#### Code Examples

- **C#**
  ```csharp
  WordDocument doc = new WordDocument("sample.doc");
  doc.Save("samplerl.tf.rtf", FormatType.Rtf);
  ```

- **VB.NET**
  ```vb
  Dim doc As New WordDocument("sample.doc")
  doc.Save("samplerl.tf.rtf", FormatType.Rtf)
  ```

### Document Elements
DocIO supports the following document elements:

- Main Document and Document Properties
- Paragraph
- Table
- Picture
- Header / Footer
- Field (Simple)
- TOC Field
- Bookmark
- Break (Line, Page)
- Section Property
- Paragraph Format
- Table Format
- Character Format
- Text Box
- Form Fields

## Page-level Navigation/TOC (if applicable)
- 4.8.1 Doc to RTF
- Document Elements

## Cross References
See also:
- Doc To RTF
- Doc To HTML
- Doc to PDF

<!-- tags: [DocIO, RTF conversion, Word document, features, supported document elements] keywords: [DocIO, RTF, Word, document conversion, document elements] -->
```