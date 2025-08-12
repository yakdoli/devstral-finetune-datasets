<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_371.jpeg
document_name: DocIo
page_number: 371
page_id: DocIo#page_371
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:51Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to add comments to a document using DocIO.
- Provides a C# code example to insert comments into a word document.

## Content

### Adding Comments Using DocIO

You can insert the comments to a paragraph or text in a word document using DocIO. The following code examples show how to insert the comments to the word document.

```csharp
// Create a new word document
WordDocument doc = new WordDocument();
IWSection section = doc.AddSection();

// Add a paragraph to the document
IWPParagraph para = section.AddParagraph();
para.AppendText("New Text");

// Add comment to the paragraph
para.AppendComment("Comment goes here");

// Save the document
doc.Save("CommentDocIO.doc", FormatType.Doc);
```

### API Reference

#### Members

- **AppendComment(string comment)**: Adds a comment to the paragraph.

## Code Examples

The provided C# code demonstrates how to:
1. Create a new Word document.
2. Add a section to the document.
3. Insert a paragraph with text.
4. Attach a comment to the paragraph.
5. Save the document with the added comment.

## Cross References

See also:
- [Syncfusion DocIO Documentation](https://www.syncfusion.com/products/net/file-formats/docio)

<!-- tags: [DocIO, Word Documents, Comments, C# Examples] keywords: [DocIO, Word Document, Comments, C#, Syncfusion] -->