```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_249.jpeg
document_name: DocIo
page_number: 249
page_id: DocIo#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:46Z
fidelity: lossless
-->

## Overview

- Understanding the functionality and interactions of TextSelection, TextBodySelection, and TextBodyPart classes in Essential DocIO.
- Describing how these classes enable finding and replacing specific text in documents.
- Exploring the rich support in Essential DocIO for finding and replacing strings and document elements.

## Content

### Background

You need to understand how TextSelection, TextBodySelection, and TextBodyPart classes work to understand this feature in DocIO. In short, this feature enables finding specific text in a document and replacing it with new text.

This section describes the rich support of Essential DocIO for finding and replacing strings and document elements.

For More Information Refer:

- Text Selection
- TextBody Part
- TextBody Selection
- Find
- Replace

### 4.5.1 TextSelection

#### Overview

TextSelection represents selected text in the Word document with the following limitations:

- **Selected Text must be complete**: Text selection does not represent split selections.
- **Selected Text must be a single paragraph**: Text selection inside two or more paragraphs is ignored.

TextSelection uses the `Find` and `FindAll` methods to select text. For details, see Find.

#### Public Constructors

| Name | Description |
| ---- | ----------- |
| TextSelection.TextSelection(WParagraph, int, int) | Initializes a new instance of the TextSelection class. |

#### Public Properties

| Name | Description |
| ---- | ----------- |
| Count | Gets the count of text chunks. |
| SelectedText | Gets the selected text. |

#### Public Methods

| Name | Description |
| ---- | ----------- |
| *TBD* | *TBD* |

## API Reference

### TextSelection Class

#### Constructors

- **`TextSelection(WParagraph, int, int)`**: Initializes a new instance of the TextSelection class.

#### Properties

- **`Count`**: Gets the count of text chunks.
- **`SelectedText`**: Gets the selected text.

---

<!-- tags: [Essential DocIO, TextSelection, TextBodySelection, TextBodyPart, Word document, find and replace, WParagraph] keywords: [TextSelection, TextBodySelection, TextBodyPart, find, replace, Word document, API reference, WParagraph, count, selected text, limitations] -->
```