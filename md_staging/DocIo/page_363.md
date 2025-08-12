```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_363.jpeg
document_name: DocIo
page_number: 363
page_id: DocIo#page_363
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:26Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Highlights the use of `DocIO` for document manipulation in VB.NET.
- Demonstrates creating, formatting, and saving a Word document.
- Introduces the functionality of inserting tables into a document.

## Content

### Character Formatting Example

[VB]

```vb
' Create a new word document
Dim doc As WordDocument = New WordDocument()

Dim section As IWSection = doc.AddSection()
Dim para As IParagraph = section.AddParagraph()

' Apply formatting
Dim range As ITextRange = para.AppendText("New Text")
range.CharacterFormat.FontName = "Arial"
range.CharacterFormat.FontSize = 14

' Save the document
doc.Save("CharacterFormattingDocIO.doc", FormatType.Doc)
```

### 5.12.8 Tables

**Tables** are used to organize information and to display the information with rows and columns. You can also add images or even other tables to the table.

#### Using MS Office Interop

The following code example illustrates how to insert a table to a word document, where the table contains three rows and two columns:

#### Code Examples

While the code example for inserting a table is not provided in this section, you can refer to the previous sections or related documentation for examples of inserting tables into Word documents using `DocIO`.

#### Notes
- Ensure proper handling of resources when working with docx files to prevent memory leaks.
- Customize the table style and properties as needed within the code example.

## Page-level Navigation/TOC (if applicable)
- Essential DocIO
  - Character Formatting Example
  - 5.12.8 Tables
    - Using MS Office Interop

## Cross References
See also: Related sections in the documentation on working with tables and custom formatting options in `DocIO`.

<!-- tags: [DocIO, WordDocument, Table, formatting, VB.NET] keywords: [DocIO, Word, document manipulation, tables, character formatting, VB.NET, MS Office Interop, document structure, rows, columns, table properties, image embedding] -->
```