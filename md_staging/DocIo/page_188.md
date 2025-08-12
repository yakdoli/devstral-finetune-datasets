```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_188.jpeg
document_name: DocIo
page_number: 188
page_id: DocIo#page_188
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:04Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- DocIO has the ability to preserve Word footnotes and endnotes.
- Creation and modification of these notes via DocIO API is limited.
- Footnotes and endnotes consist of a special marker and special data in the document.
- The `WFootnote` class represents the structure and properties of footnotes and endnotes.

## Content

### Introduction to Footnotes and Endnotes
DocIO has an ability to preserve Word footnotes and endnotes, but their creation and modification with DocIO API is limited.

#### Components of Footnotes and Endnotes
Footnotes and Endnotes are the subdocuments of Word. Presentation of these subdocuments in the document consists of two parts:
1. **Special marker**: Defines the footnote or endnote location in the document.
2. **Special data**: Defines the text and formatting of the subdocument.

### Class Representation
The `WFootnote` class represents the structure and properties of footnotes and endnotes. As footnotes and endnotes share the same structure in the document, a single class is used to represent them. This class has the `FootnoteType` property, which enables you to add a footnote or endnote. It takes two values:
- Footnote
- Endnote

#### Class Hierarchy
```plaintext
ParagraphItem
    |
    WFootnote
```

### Public Constructor
The `WFootnote` class includes a public constructor:
- **Name**: `WFootnote.WFootnote (IWordDocument)`
- **Description**: Initializes a new instance of the `WFootnote` class.

### Public Properties
The `WFootnote` class has the following public properties:

| Name            | Description                    |
|-----------------|--------------------------------|
| `EntityType`    | Gets the type of the entity    |
| `FootnoteType`  | Gets or sets footnote type: footnote or endnote |
| `IsAutoNumbered`| Gets the value indicating if the footnote is auto numbered |

## API Reference
### Class: WFootnote
#### Properties
- `EntityType`:
  - **Type**: Object
  - **Description**: Gets the type of the entity.
- `FootnoteType`:
  - **Type**: Enum (Footnote or Endnote)
  - **Description**: Gets or sets the type of the footnote.
- `IsAutoNumbered`:
  - **Type**: Boolean
  - **Description**: Indicates whether the footnote is auto-numbered.

## Code Examples
### Example: Creating a Footnote
```csharp
WFootnote footnote = new WFootnote(wordDocument);
footnote.FootnoteType = FootnoteType.Footnote;
footnote.Text = "This is a footnote example.";
wordDocument.LastSection.Body.Paragraphs.Add(footnote);
```

### Example: Creating an Endnote
```csharp
WFootnote endnote = new WFootnote(wordDocument);
endnote.FootnoteType = FootnoteType.Endnote;
endnote.Text = "This is an endnote example.";
wordDocument.LastSection.Body.Paragraphs.Add(endnote);
```

## Page-level Navigation/TOC
- Introduction to Footnotes and Endnotes
- Class Representation
  - Class Hierarchy
  - Public Constructor
  - Public Properties
- API Reference
  - Class: WFootnote
  - Properties
- Code Examples
  - Creating a Footnote
  - Creating an Endnote

## Cross References
See also:
- [Footnote and Endnote Option in MS Word](#footnote-and-endnote-option-in-ms-word)

<!-- tags: [DocIO, Winforms, footnotes, endnotes, MS Word, WFootnote class, WFootnote API] keywords: [footnotes, endnotes, footnotetype, wfootnote, winforms, syncfusion, docio, word documents, automatic numbering] -->
```