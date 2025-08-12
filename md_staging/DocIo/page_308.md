```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_308.jpeg
document_name: DocIo
page_number: 308
page_id: DocIo#page_308
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:31Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to create and save a Word document using `WordDocument`.
- Explains the ability to save `.doc` files into `.docx` format.
- Lists key features supported in `.docx` format.

## Content

### Creating a Word Document

```vb
[VB.NET]

Dim document As New WordDocument()
' Add a new section to the document.
Dim section As IWSection = document.AddSection()
' Adding a new paragraph to the section.
Dim paragraph As IWParagraph = section.AddParagraph()
' Insert Text into the paragraph
paragraph.AppendText("Hello World!")
Dim sfd As New SaveFileDialog()
If sfd.ShowDialog() = True Then
    Using stream As Stream = sfd.OpenFile()
        document.Save(stream, FormatType.Docx)
    End Using
End If
```

#### Saving a .doc File as .docx

DocIO also has the ability to save `.doc` files into `.docx` format (i.e., Microsoft Word 2007/2010/2013 files format). All the elements supported by `.Doc` are supported in `.Docx`. Some of the supported elements are listed below.

1. **Creating an instance of Word document.**

The following code snippet creates an instance of the word document and opens the word document named `SourceDocument.doc`. The `FormatType.Doc` specifies that the document is of type Word 97-2003.

```csharp
[C#]

WordDocument document = new WordDocument();
document.Open("SourceDocument.doc", FormatType.Doc);
SaveFileDialog sfd = new SaveFileDialog()
{
    Filter = "Docx files (*.docx)|*.docx|All files (*.*)|*.*",
    DefaultExt = ".docx",
    FilterIndex = 1
};
```

2. **Save the document as .docx format.**

The following code snippet will display the Save dialog on the screen and save the Word document.

```csharp
[C#]
```

## API Reference

- `WordDocument`: Represents a Word document.
- `IWSection`: Represents a section in a Word document.
- `IWParagraph`: Represents a paragraph in a Word document.
- `FormatType.Doc`: Specifies the document is of type Word 97-2003.
- `FormatType.Docx`: Specifies the document format is `.docx`.

## Code Examples

- VB.NET example for creating and saving a `.docx` document.
- C# examples for opening a `.doc` file and saving it as `.docx`.

## Page-level Navigation/TOC
- [Overview]
- [Content]
  - [Creating a Word Document]
  - [Saving a .doc File as .docx]

## Cross References

See also:
- DocIO API Documentation for more details on supported features.
- WordDocument class for creating and manipulating Word documents.

<!-- tags: [DocIO, WordDocument, WordProcessing, SDK, VersionControl] keywords: [DocIO, Word, Document, VB.NET, C#, SaveFileDialog, FormatType, Open, Save, .docx, .doc] -->
```