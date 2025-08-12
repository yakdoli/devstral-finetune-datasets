```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_088.jpeg
document_name: DocIo
page_number: 088
page_id: DocIo#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:38Z
fidelity: lossless
-->

## Macro-enabled Document Support

**Overview**

- Sections related to creating and handling memory streams and file streams for word documents.
- Support for word processing with macro-enabled documents and templates in different Microsoft Word formats.

### Content

#### Code Example
```vb
' Create a Memory Stream.
Dim memStream As New MemoryStream()

'Save the document into memory stream.
document.Save(memStream)

'Move the pointer to the first position
memStream.Seek(0, SeekOrigin.Begin)

'Create a file Stream
Dim fs As New FileStream("Sample.doc", FileMode.Create)
memStream.WriteTo(fs)

'Open the Word document from stream
Dim sourceDoc As New WordDocument(memStream, FormatType.Doc)

'Close the Streams.
memStream.Close()
fs.Close()
```

#### Subsection: 4.2.5 Macro-enabled Document Support

A macro is a piece of Visual Basic (VB) programming code that is embedded in a word file to automate repetitive tasks. Essential DocIO provides support for manipulating Microsoft Word macro-enabled documents (*.docm) and Microsoft Word macro-enabled templates (*.dotm) of Word 2007 and Word 2010 formats.

Microsoft Word macro-enabled format files can be created with the following format type enumerations while saving the WordDocument object:

- Word2007Docm - Microsoft Word 2007 macro enabled document format.
- Word2007Dotm - Microsoft Word 2007 macro enabled template format.
- Word2010Docm - Microsoft Word 2010 macro enabled document format.
- Word2010Dotm - Microsoft Word 2010 macro enabled template format.
- Word2013Docm - Microsoft Word 2013 macro enabled document format.
- Word2013Dotm - Microsoft Word 2013 macro enabled template format.

#### Note

The macros present in the input macro-enabled document will be preserved as it is in the output macro-enabled document. However, **Essential DocIO does not have support to create or edit macro commands** in the macro-enabled documents.

## Page-level Navigation/TOC (if applicable)
- If applicable, this section would reference local TOC links or external cross-references.

<!-- tags: [DocIO, macro-enabled documents, Microsoft Word, memory streams, file streams] keywords: [macro, Visual Basic, memory stream, file stream, Microsoft Word, macro-enabled document format, Word 2007, Word 2010, Word 2013] -->
```