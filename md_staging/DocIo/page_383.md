```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_383.jpeg
document_name: DocIo
page_number: 383
page_id: DocIo#page_383
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:23Z
fidelity: lossless
-->

## Using DocIO

### Overview
- Demonstrates how to insert and update a table of contents in a Word document using DocIO.
- Includes both C# and VB.NET code examples for clarity and versatility.

### Content
#### Inserting and Updating a Table of Contents in a Word Document
The following code examples illustrate how to append and update a table of contents within a Word document using DocIO.

##### C#
```csharp
// Open the word document
WordDocument doc = new WordDocument("TOCDocument.doc", FormatType.Doc);
IWSection sec = doc.Sections[0];

// Append TOC to the first paragraph of the document
WParagraph para = new WParagraph(doc);
TableOfContent toc = para.AppendTOC(1, 3);
sec.Paragraphs.Insert(0, para);

// Update table of contents
doc.UpdateTableOfContents();

// Save the document
doc.Save("TOCUpdatedDocIO.doc", FormatType.Doc);
```

##### VB.NET
```vb
' Open the word document
Dim doc As WordDocument = New WordDocument("TOCDocument.doc", FormatType.Doc)
Dim sec As IWSection = doc.Sections(0)

' Append TOC to the first paragraph of the document
Dim para As WParagraph = New WParagraph(doc)
Dim TOC As TableOfContent = para.AppendTOC(1, 3)
sec.Paragraphs.Insert(0, para)

' Update table of contents
doc.UpdateTableOfContents()

' Save the document
doc.Save("TOCUpdatedDocIO.doc", FormatType.Doc)
```

---

<!-- tags: [DocIO, WordDocument, TableOfContent, WinForms] keywords: [insert table of contents, update table of contents, C#, VB.NET, WordDocument, DocIO, Syncfusion] -->
```