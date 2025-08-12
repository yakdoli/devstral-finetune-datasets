```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: DocIo
page_number: 043
page_id: DocIo#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:44Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Instantiate the `WordDocument` class to create a Word document in memory.
- Add sections and paragraphs to the document.
- Save the document to a file stream.

## Content

### Document Creation and Content Insertion
#### C#
```csharp
// Create a new Word document.
// This document has no section and no paragraph by default.
WordDocument document = new WordDocument();

// Add a new section to the document.
IWSection section = document.AddSection();

// Adding a new paragraph to the section.
IWParagraph paragraph = section.AddParagraph();

// Insert Text into the paragraph
paragraph.AppendText("Hello World!");

// Save the file to stream.
SaveFileDialog sfd = new SaveFileDialog();
sfd.DefaultExt = ".xls";
sfd.Filter = "Files(*.xls)|*.xls";
if (sfd.ShowDialog() == true)
{
    using (Stream stream = sfd.OpenFile())
    {
        document.Save(stream, FormatType.Doc);
    }
}
```

#### VB.NET
```vb.net
' Create a new Word document.
' This document has no section and no paragraph by default.
Dim document As WordDocument = New WordDocument()

' Add a new section to the document.
Dim section As IWSection = document.AddSection()

' Adding a new paragraph to the section.
Dim paragraph As IWParagraph = section.AddParagraph()

' Insert Text into the paragraph
paragraph.AppendText("Hello World!")
```

## API Reference (if applicable)
- `WordDocument`: Represents the Word document that will be created in memory.
- `AddSection()`: Adds a new section to the document.
- `AddParagraph()`: Adds a new paragraph to the section.
- `AppendText(string text)`: Inserts text into the paragraph.
- `Save(Stream stream, FormatType formatType)`: Saves the document to the specified stream in the given format.

## Code Examples
- The provided C# and VB.NET examples demonstrate how to create a Word document, add a section and a paragraph, insert text, and save the document to a file stream.

<!-- tags: [Syncfusion Winforms, DocIO, WordDocument, section, paragraph, text insertion, file saving] keywords: [WordDocument, AddSection, AddParagraph, AppendText, SaveFileDialog, Stream, FormatType, DocIO] -->
```