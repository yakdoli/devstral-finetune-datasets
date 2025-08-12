```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: DocIo
page_number: 084
page_id: DocIo#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:20Z
fidelity: lossless
-->

## DocIO

### Creating a Word Document

**Overview**
- Demonstrates how to create and modify a Word document using Syncfusion's DocIO library in VB.NET and C#.

### Content

#### Example 1: Creating a New Word Document in Word 2007 Format

In this example, a new Word document is created, a section is added, a paragraph is inserted, and text is appended. The document is then saved in the Word 2007 format.

```vb
'[VB.NET]

Dim doc As New WordDocument()
'Add a new section to the document.
Dim section As ISection = doc.AddSection()
'Adding a new paragraph to the section.
Dim paragraph As IParagraph = section.AddParagraph()
'Insert text into the paragraph.
paragraph.AppendText("Hello World!")
'Saves the document in Word 2007 format type.
doc.Save("OutDocument.docx", FormatType.Word2007)
```

---

#### Example 2: Opening and Modifying a Word 2010 Format Document

This section illustrates how to open an existing Word 2010 format document, add a new paragraph, and then save the document in the Word 2010 format.

##### C#

```csharp
[C#]

WordDocument doc = new WordDocument();
//Opens the Word 2010 format document.
document.Open(filename, FormatType.Automatic);
//Adding a new paragraph to the last section.
IParagraph paragraph = document.LastSection.AddParagraph()
//Insert text into the paragraph.
paragraph.AppendText( "Creating Word 2010 format document!" );
//Saves the document in Word 2010 format type.
doc.Save("Sample.docx", FormatType.Word2010);
```

##### VB.NET

```vb
[VB.NET]

Dim doc As New WordDocument()
'Opens the Word 2010 format document.
document.Open(filename, FormatType.Automatic)
'Adding a new paragraph to the last section.
Dim paragraph As IParagraph = document.LastSection.AddParagraph()
'Insert text into the paragraph.
paragraph.AppendText("Creating Word 2010 format document!")
```

---

### Summary

The examples above demonstrate the basic operations of creating and modifying Word documents using Syncfusion's DocIO library in both VB.NET and C#. Different document formats (Word 2007 and Word 2010) can be handled using the `FormatType` enum.

---

### API References

- **`WordDocument`**: Represents a Word document that can be created, modified, and saved.
- **`FormatType`**: Enumerates the formats supported for saving and loading documents (e.g., Word2007, Word2010).

### Code Examples

The code snippets provided show how to:
- Create a new `WordDocument` and add sections and paragraphs.
- Open an existing document and modify its content.
- Save the document in specified formats.

### Page-level Navigation/TOC

To explore more advanced features of DocIO, refer to the full user guide or documentation.

---

<!-- tags: [DocIO, WordDocument, Word2007, Word2010, VB.NET, C#] keywords: [Syncfusion, DocIO, Word, document creation, Word format, document manipulation] -->
```