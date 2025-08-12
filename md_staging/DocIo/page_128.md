```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_128.jpeg
document_name: DocIo
page_number: 128
page_id: DocIo#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:03Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes the public properties and methods of the `DocIO` component.
- Provides information about paragraph-related attributes and functionalities in documents.

## Content

### Public Properties

| Name                 | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| BreakCharacterFormat | Gets character format for the break symbol.                              |
| ChildEntities        | Gets the child entities.                                                  |
| EntityType           | Gets the type of the entity.                                              |
| IsEndOfDocument      | Gets a value indicating whether this paragraph is the end of document. |
| IsEndOfSection       | Gets a value indicating whether this paragraph is the end of the section. |
| IsInCell             | Gets a value indicating whether this paragraph is in cell.               |
| Items                | Gets paragraph items.                                                     |
| ListFormat           | Gets format of the list for the paragraph.                               |
| ParagraphFormat      | Gets paragraph format.                                                    |
| StyleName            | Gets paragraph style name.                                                |
| Text                 | Gets or sets paragraph text.                                              |

### Public Methods

| Name                        | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| AppendBookmarkEnd           | Appends end of the bookmark with specified name into paragraph.           |
| AppendBookmarkStart         | Appends start of the bookmark with specified name into paragraph.         |
| AppendBreak                 | Appends break to end of the paragraph.                                    |
| AppendCheckBox              | Appends checkbox to end of paragraph.                                     |
| AppendComment               | Appends comment to end of paragraph.                                      |
| AppendDropDownFormField     | Appends DropDown form field to end of paragraph.                          |
| AppendField                 | Appends field to end of paragraph.                                        |
| AppendFootnote              | Appends footnote to end of paragraph.                                     |
| AppendPicture               | Appends picture to end of paragraph.                                      |
| AppendSymbol                | Appends special symbol to end of paragraph.                               |
| AppendTable                 | Append Table.                                                             |
| AppendText                  | Appends text to end of document.                                          |
| AppendTextBox               | Append Text box to the end of the paragraph.                              |
| AppendTextFormField         | Appends text form field to end of paragraph.                              |

## API Reference (if applicable)
- Below are the methods and properties specific to the `DocIO` component related to paragraph manipulation and formatting.

---

<!-- tags: [DocIO, public properties, public methods, paragraph formatting, document manipulation] keywords: [DocIO, BreakCharacterFormat, ChildEntities, EntityType, IsEndOfDocument, IsEndOfSection, IsInCell, Items, ListFormat, ParagraphFormat, StyleName, Text, AppendBookmarkEnd, AppendBookmarkStart, AppendBreak, AppendCheckBox, AppendComment, AppendDropDownFormField, AppendField, AppendFootnote, AppendPicture, AppendSymbol, AppendTable, AppendText, AppendTextBox, AppendTextFormField] -->
```