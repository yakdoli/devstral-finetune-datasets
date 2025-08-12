```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_063.jpeg
document_name: DocIo
page_number: 063
page_id: DocIo#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:49Z
fidelity: lossless
-->

## WordDocument Class Overview

### Constructor Summary

| Constructor                                  | Description                                                                 |
|----------------------------------------------|-----------------------------------------------------------------------------|
| `WordDocument.WordDocument (Stream)`        | Initializes a new instance of the WordDocument class from the stream.         |
| `WordDocument.WordDocument (Stream, FormatType, string)` | Initializes a new instance of the WordDocument class from the stream of specified type, protected with password. |
| `WordDocument.WordDocument (Stream, string)` | Initializes a new instance of the WordDocument class from the Word document's stream, which is protected with password. |
| `WordDocument.WordDocument (string)`        | Initializes a new instance of the WordDocument class from Word document.        |
| `WordDocument.WordDocument (string, FormatType, string)` | Initializes a new instance of the WordDocument class from existing file of specified type protected with password. |
| `WordDocument.WordDocument (string, string)` | Initializes a new instance of the WordDocument class from existing Word document, which is protected with password. |

### Public Methods

| Name                       | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `AddListStyle`             | Adds new list style to document.                                            |
| `AddParagraphStyle`        | Adds new paragraph style to the document.                                   |
| `AddSection`               | Adds new section to document.                                                |
| `Clone`                    | Clones itself.                                                             |
| `CreateParagraph`          | Creates the paragraph.                                                      |
| `CreateParagraphItem`      | Creates new paragraph item instance.                                        |
| `EnsureMinimal`            | Adds one empty section to the document and one empty paragraph to created section. |
| `Find`                     | Finds the first entry of specified string.                                  |
| `FindAll`                  | Finds all entries of specified string.                                      |

## Code Examples

### Example: Creating a New WordDocument Instance
```csharp
using Syncfusion.DocIO;

// Using a stream
using (FileStream fileStream = new FileStream("document.docx", FileMode.Open, FileAccess.Read))
{
    WordDocument document = new WordDocument(fileStream);
}

// Using a file with password protection
string filePath = "protected_document.docx";
string password = "12345";
WordDocument document = new WordDocument(filePath, FormatType.Docx, password);
```

## Cross References

See also:
- [DocIO Documentation](https://www.syncfusion.com/documentation/docio)
- [WordDocument Class API Reference](https://help.syncfusion.com/cr/xamarin/Syncfusion.DocIO.WordDocument.html)

## RAG Annotations

<!-- tags: [Syncfusion, DocIO, WordDocument, API, Winforms, 11.4.0.26] keywords: [WordDocument, constructor, public methods, list style, paragraph style, section, clone, paragraph item, find string] -->
```