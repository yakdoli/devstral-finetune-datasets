```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_196.jpeg
document_name: DocIo
page_number: 196
page_id: DocIo#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:38Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This section explains how to use the TableOfContent class to add a Table of Contents (TOC) to a Word document.
- Lists the steps to add a TOC in a Word document manually and programmatically.
- Introduces additional features such as styling and updating the TOC.

## Content

### Table Of Contents

The `TableOfContent` class represents the Table Of Contents (TOC) in the Word document. To add the Table of Contents to the contents in the Word document, follow the steps listed below:

1. Open the Insert menu and click Field.
2. Then select the TOC field type.

You can use the `AppendTOC` method of the `WParagraph` class to add a TOC to the DocIO document.

#### UpperHeadingLevel and LowerHeadingLevel
`UpperHeadingLevel` and `LowerHeadingLevel` define the number of heading levels to be displayed for the TOC. For example, if `UpperHeadingLevel` is set to 4 and `LowerHeadingLevel` is set to 3, then the TOC will display heading levels from third to fourth.

#### SetTOCLevelStyle
The `SetTOCLevelStyle` method sets the style for each TOC level. For example, `SetTOCLevelStyle(1, "Normal")` will set the Normal style for the first level of the TOC.

#### UpdatingTableOfContents
The `UpdatingTableOfContents` method of the `WordDocument` class updates the table of contents field in the word document. Internally, Essential DocIO updates page numbers in the table of contents using the Doc to PDF layout engine. Hence, the limitations are similar to the limitations in Doc to PDF layout.

**Note:** Updating the Table of Contents is not supported in the Silverlight platform.

#### Known Limitations
The following are the known limitations:
- Currently, Auto shapes, footnote, and endnote, drawing canvas are not preserved in Doc to PDF layout, which may lead to updating of incorrect page number.
- Text wrapping support is partially handled in Doc to PDF layout, which may lead to updating of incorrect page number.

### Class Hierarchy
- `ParagraphItem`
  - `TableOfContent`

## Code Examples

Example usage of the `AppendTOC` method:

```csharp
WordDocument document = new WordDocument();
WSection section = document.AddSection();
WParagraph paragraph = section.AddParagraph();
paragraph.AppendTOC();
```

Example usage of the `SetTOCLevelStyle` method:

```csharp
document.Styles.SetTOCLevelStyle(1, "Normal");
```

## RAG Annotations
<!-- tags: [TableOfContent, WordDocument, WParagraph, Essential DocIO, Syncfusion Winforms, version: 11.4.0.26] keywords: [Table of Contents, TOC, UpperHeadingLevel, LowerHeadingLevel, SetTOCLevelStyle, UpdatingTableOfContents] -->
```