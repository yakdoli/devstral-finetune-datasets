```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_357.jpeg
document_name: DocIo
page_number: 357
page_id: DocIo#page_357
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:57Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to add headers and footers to each section in a Word document using C#.
- Includes code for alignment and field insertion in headers and text insertion in footers.
- Examples of saving and closing the modified document.

## Content

### Adding Headers and Footers to a Word Document

#### Code Example

```csharp
[C#]

// Open the word document
WordDocument doc = new WordDocument("original.doc");

// Add header and footer for each section in the document
foreach (WSection sec in doc.Sections)
{
    // Header
    WParagraph para = new WParagraph(doc);
    para.AppendField("page", FieldType.FieldPage);
    para.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Right;
    sec.HeadersFooters.Header.Paragraphs.Add(para);

    // Footer
    WParagraph para1 = new WParagraph(doc);
    para1.AppendText("Internal");
    para1.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Left;
    sec.HeadersFooters.Footer.Paragraphs.Add(para1);
}

// Save the document
doc.Save("HeaderFooterDocIO.doc", FormatType.Doc);

// Close the document
doc.Close();
```

#### Explanation
- **Opening the Document:** The `WordDocument` object is initialized with the file path to the original document.
- **Processing Each Section:** A loop iterates over each section of the document to add headers and footers.
- **Header Creation:** 
  - A new paragraph is created.
  - A page field is appended to the paragraph.
  - The paragraph is aligned to the right.
  - The paragraph is added to the section's header.
- **Footer Creation:** 
  - A new paragraph is created.
  - Static text "Internal" is appended.
  - The paragraph is aligned to the left.
  - The paragraph is added to the section's footer.
- **Saving and Closing:** The modified document is saved with a new filename and closed to free resources.

### Conclusion
This example illustrates the process of programmatically adding headers and footers to a Word document using C# and the Syncfusion DocIO library. The alignment properties and field handling provide flexibility in customizing the document layout.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, DocIO, WordDocument, headers, footers, C#] keywords: [C#, WordDocument, header, footer, horizontal alignment, field, paragraph, save, close] -->

```