```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: DocIo
page_number: 024
page_id: DocIo#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:29:31Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- This page describes the class diagram for the DLS Object Model (abstract) for Essential DocIO, which provides a structured representation of document objects and their relationships.
- It outlines various document elements such as Bookmarks, Styles, Sections, WSections, and several components related to text, paragraphs, and tables.
- The diagram includes legend elements categorizing objects into Abstract, Class, and Collection.

## Content

### DLS Object Model (abstract)

The DLS Object Model abstract diagram illustrates the structure and relationships between various elements in a Word Document:

#### Left Branch
- **WordDocument**
  - **Bookmarks**
    - **Bookmark**
  - **Styles**
    - **Style**
  - **ListStyles**
    - **ListStyle**
  - **Sections**
    - **WSection**
      - **PageSetup**
      - **Columns**
        - **Column**
      - **HeadersFooters**
        - **HeaderFooter**
      - **WTextBody**
        - **Paragraphs**
          - **WParagraph**
        - **Tables**
          - **WTable**
        - **Items**
            - **TextBodyItem**

#### Right Branch - TextBodyItem
- **Style**
  - **CharacterStyle**
  - **WParagraphStyle**
- **TextBodyItem**
  - **WParagraph**
    - **Items**
      - **ParagraphItem**
- **WTable**
  - **Rows**
    - **WTableRow**
      - **Cells**
        - **WTableCell**
- **ParagraphItem**
  - **WTextRange**
  - **WPicture**
  - **WField**
  - **BookmarkStart**
    - **...**

#### Legend:
- **Abstract**
- **Class**
- **Collection**

## Figures
- **Figure 10: Class Diagram for Essential DocIO**

## API Reference
The following are the primary classes and their hierarchical relationships identified in the diagram:

### WordDocument
- **Bookmarks**
  - **Bookmark**
- **Styles**
  - **Style**
- **ListStyles**
  - **ListStyle**
- **Sections**
  - **WSection**
    - **Sub-components:**
      - **PageSetup**
      - **Columns**
        - **Column**
      - **HeadersFooters**
        - **HeaderFooter**
      - **WTextBody**
        - **Paragraphs**
          - **WParagraph**
        - **Tables**
          - **WTable**
        - **Items**
          - **TextBodyItem**
- **Style**
  - **CharacterStyle**
  - **WParagraphStyle**
- **TextBodyItem**
  - **WParagraph**
    - **Items**
      - **ParagraphItem**
- **WTable**
  - **Rows**
    - **WTableRow**
      - **Cells**
        - **WTableCell**
- **ParagraphItem**
  - **WTextRange**
  - **WPicture**
  - **WField**
  - **BookmarkStart**
    - **...**

## Code Examples
- This page does not include any actual code examples. It primarily focuses on the class diagram and the structure of the DLS Object Model.

## Cross References
See also:
- Other parts of the documentation detailing implementation and usage of the DLS Object Model.

## RAG Annotations
<!-- tags: [Essential DocIO, DLS Object Model, Word Document, Document Elements, Styles, Bookmarks, Sections, Tables, Paragraphs, WTextBody, WSection, TextBodyItem] keywords: [WordDocument, WParagraph, WTable, TextBodyItem, Style, Bookmark, Section, HeaderFooter, Column] -->
```