```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_241.jpeg
document_name: DocIo
page_number: 241
page_id: DocIo#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:12Z
fidelity: lossless
--> 

## Overview

- Code example demonstrating footer textbox style customizations.
- Overview of inserting XHTML formatted strings into Word documents.
- Description of scenarios for inserting HTML documents and strings.

## Content

### 4.4.2.7 Importing XHTML

Essential DocIO supports inserting XHTML formatted strings in the Word document. There are two different usage scenarios namely:

- **Insert HTML Document**
- **Insert HTML Formatted String**

---

#### Insert HTML Document

This option enables to insert a whole HTML document with the following limitations:

- XHTML 1.0 Strict is preferred; XHTML 1.0 Transitional is also acceptable.
- There is an option to validate against either XHTML Strict or Transitional schema. By default the given html string is validated against XHTML 1.0 Transitional schema and an exception is thrown, if the html is found to be non-complaint. However, you can set this property on the document object to either, validate against XHTML Transitional schema or, Strict schema.
- If a block element is not supported, then its style would still be parsed and applied to the supported child elements inside.
- All the limitations are documented in Appendix 1 and 2.

---

The following code illustrates inserting a HTML string into a section of the Word document.

```csharp
textbox1.TextBoxFormat.LineWidth = 6.0f
textbox1.TextBoxFormat.NoLine = True

section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

paragraph = New WParagraph(doc)
paragraph.AppendText("Hello footer textbox")
Dim textbox2 As ITextBox = paragraph.AppendTextBox(120, 100)
Private textbox2.TextBoxFormat.VerticalPosition = 5
textbox2.TextBoxBody.AddParagraph().AppendText("Footer textbox")
textbox2.TextBoxFormat.FillColor = System.Drawing.Color.Yellow
textbox2.TextBoxFormat.LineDashing = LineDashing.DashGEL
textbox2.TextBoxFormat.LineWidth = 3.75f
textbox2.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Square
textbox2.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Left
textbox2.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)
doc.Save("Textboxes.doc")
```

---

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content.
  <!-- tags: [DocIO, Winforms, HTML, XHTML, FooterTextbox, TextWrappingStyle, ShapeHorizontalAlignment] keywords: [Essential DocIO, Insert HTML Document, Insert XHTML Formatted String, HTML Document Limitations, VerticalPosition, FillColor, LineDashing, LineWidth, TextWrappingStyle, ShapeAlignment] -->
``` 
