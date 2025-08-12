```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_345.jpeg
document_name: DocIo
page_number: 345
page_id: DocIo#page_345
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:10Z
fidelity: lossless
-->

# Essential DocIO

DocIO provides support for adding page numbers to a word document. The page number field can be added to the header or footer of the word document. In the following code example, the page numbers are inserted to the footer of the word document.

```csharp
[C#]

// Open the word document
WordDocument doc = new WordDocument("PageNumbers.docx", FormatType.Docx);

// Add page number in footer for every section
foreach (WSection sec in doc.Sections)
{
    IWParagraph para = sec.AddParagraph();
    para.AppendField("footer", FieldType.FieldPage);
    para.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Center;
    sec.PageSetup.PageNumberStyle = PageNumberStyle.Arabic;
    sec.HeadersFooters.Footer.Paragraphs.Add(para);
}

// Save the document
doc.Save("PageNumbersUpdated.docx", FormatType.Docx);

// Close the document
doc.Close();
```

<!-- tags: [DocIO, WordDocument, C#, formatType, page numbering, footer] keywords: [page numbers, header, footer, word document, page setup, paragraph, save, close] -->
```
