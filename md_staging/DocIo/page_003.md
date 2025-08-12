```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: DocIo
page_number: 003
page_id: DocIo#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:28:18Z
fidelity: lossless
-->

## Overview
- Discusses detailed features and functionalities related to document processing and manipulation.
- Covers sections on macro-enabled document support, tracking changes, font substitution for Word documents, and section cloning and merging.
- Includes detailed instructions on handling headers, footers, tables, content control, and various paragraph elements.

## Content

### 4.3 Section
- **4.3.1 Cloning and Merging** (Page 100)
- **4.3.2 Headers and Footers** (Page 103)
- **4.3.3 Table** (Page 111)
  - **4.3.3.1 Table Row** (Page 115)
  - **4.3.3.2 Table Cell** (Page 117)
  - **4.3.3.3 Row Format** (Page 122)
  - **4.3.3.4 Table Styles** (Page 124)
- **4.3.4 Content Control** (Page 126)

### 4.4 Paragraph
- **4.4.1 Paragraph Item** (Page 130)
  - **4.4.1.1 Text Range** (Page 132)
  - **4.4.1.2 Fields** (Page 135)
    - **4.4.1.2.1 Merge Field** (Page 139)
    - **4.4.1.2.2 Embed Field** (Page 141)
    - **4.4.1.2.3 Seq Field** (Page 142)
    - **4.4.1.2.4 Form Field** (Page 143)
    - **4.4.1.2.5 Hyperlink** (Page 155)
    - **4.4.1.2.6 Document Variable** (Page 158)
    - **4.4.1.2.7 Fields Updating Engine** (Page 161)
  - **4.4.1.3 Bookmark** (Page 163)
    - **4.4.1.3.1 Bookmark Navigator** (Page 168)
  - **4.4.1.4 Shapes** (Page 173)
    - **4.4.1.4.1 Picture** (Page 174)
    - **4.4.1.4.2 TextBox** (Page 178)
    - **4.4.1.4.3 Comment** (Page 182)
  - **4.4.1.5 Footnote and Endnote** (Page 187)
    - **4.4.1.5.1 Footnote and Endnote Separators** (Page 190)
  - **4.4.1.6 Symbol** (Page 191)
  - **4.4.1.7 Break** (Page 193)
  - **4.4.1.8 Table Of Contents** (Page 196)

### 4.2 Advanced Features
- **4.2.4 Stream Support** (Page 87)
- **4.2.5 Macro-enabled Document Support** (Page 88)
- **4.2.6 Track Changes** (Page 90)
- **4.2.7 Font Substitution for Word Documents** (Page 92)

## API Reference (if applicable)
- Namespace: `Syncfusion.DocIO`
- Members: Methods (Like `MergeField`, `EmbedField`), Properties (Like `Header`, `Footer`), Events, and others.

## Code Examples (multi-language supported)
```csharp
// Example: Creating a new document with headers and footers
using Syncfusion.DocIO;

public void CreateDocumentWithHeaders()
{
    // Create a new Word document and add sections and paragraphs.
    WordDocument document = new WordDocument();
    WordSection section = document.AddSection();
    section.HeadersFooters.Exists;
    section.HeadersFooters.HeaderText.AddParagraph(). AppendText("Header Text");
    section.HeadersFooters.FooterText.AddParagraph().AppendText("Footer Text");
    document.Save("Sample.docx", SaveFormat.Docx);
}
```

## Page-level Navigation/TOC (if applicable)
- Local TOC list as shown in the markdown structure above.

## Cross References
- See also: **Page 87** for Stream Support, **Page 88** for Macro-enabled Document Support, and **Page 111** for handling tables.

<!-- tags: [DocIo, section, paragraph, document processing, macro-enabled, headers, footers, table, content control, field, bookmark, shapes, footnote] keywords: [4.2.4, 4.2.5, 4.2.6, 4.2.7, 4.3, 4.3.1, 4.3.2, 4.3.3, 4.3.4, 4.4, 4.4.1, 4.4.1.2, 4.4.1.3, 4.4.1.4, 4.4.1.5, 4.4.1.6, 4.4.1.7, 4.4.1.8] -->
```