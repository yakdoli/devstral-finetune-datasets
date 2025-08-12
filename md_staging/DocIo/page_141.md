```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: DocIo
page_number: 141
page_id: DocIo#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:13Z
fidelity: lossless
-->

# Essential DocIO

```csharp
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);
paragraph = new WParagraph(doc);
paragraph.AppendField("Field's Name", FieldType.FieldMergeField);
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);

paragraph = new WParagraph(doc);
paragraph.AppendText("[ FIRST PAGE Footer ]\r");
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph);
```

### [VB.NET]

```vb
Dim section As IWSection = doc.AddSection()
Dim paragraph As IWParagraph = section.AddParagraph()
paragraph.AppendText("Testing writing Merge Fields into Header")

section.PageSetup.DifferentFirstPage = True
section.PageSetup.DifferentOddAndEvenPages = True

paragraph = New WParagraph(doc)
paragraph.AppendText("[ FIRST PAGE Header ]")
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

paragraph = New WParagraph(doc)
paragraph.AppendField("Field's Name", FieldType.FieldMergeField)
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

paragraph = New WParagraph(doc)
paragraph.AppendText("[ FIRST PAGE Footer ]" & Constants.vbCr)
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)
```

### 4.4.1.2.2 Embed Field

The `WEmbedField` class represents an embed field type in the Word document. Word does not allow creating an embed field type manually (using Microsoft Word interface). This field is used when the document has embedded objects. This field usually points to the container in the document which encloses the embedded object.

<div class="note">Note: Modification of `WEmbedField` properties can cause document corruption or incorrect document preservation. DocIO preserves only fields of this type.</div>

### Class Hierarchy

- `WTextRange`
  - `|`

## API Reference (if applicable)
- None specified in this section.

## Code Examples (if applicable)
- None specified in this section.

## RAG Annotations

<!-- tags: [DocIO, Word processing, embed fields, different page headers and footers, footer, header, Syncfusion Winforms, version: 11.4.0.26] keywords: [embed field, WEmbedField, Word document, document corruption, different page setup, footer, header, Microsoft Word interface, embedded objects, field merge] -->
```