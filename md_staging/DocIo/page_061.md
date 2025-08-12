```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_061.jpeg
document_name: DocIo
page_number: 061
page_id: DocIo#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:18Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Provides an overview of the functionality to save and open documents asynchronously and in read-only mode.
- Lists public properties of the document object that can be accessed.

## Content

### Methods

- **SaveAsync(Stream stream, FormatType formatType)**: saves the document asynchronously into the stream in the specified format type.

To open the document which is already opened in Word, use the **OpenReadOnly** method to open the document in the read-only mode.

- **OpenReadOnly(string fileName, FormatType formatType)**: opens the document in the read-only mode.

### Public Properties

| Property                      | Description                                                                             |
|-------------------------------|-----------------------------------------------------------------------------------------|
| Background                    | Gets document's background.                                                             |
| Bookmarks                     | Gets document bookmarks.                                                                |
| BuiltInDocumentProperties     | Gets document built-in properties object.                                              |
| ChildEntities                 | Gets the child entities.                                                                |
| CustomDocumentProperties      | Gets document custom properties object.                                               |
| EndnoteNumberFormat           | Gets or sets endnote numbering format.                                                |
| EndnotePosition               | Gets or sets endnote position in the document.                                        |
| EntityType                    | Gets the type of the entity.                                                           |
| FootnoteNumberFormat          | Gets or sets footnote numbering format.                                               |
| FootnotePosition              | Gets or sets footnote position in the document.                                       |
| InitialEndnoteNumber          | Gets or sets the initial endnote number.                                              |
| InitialFootnoteNumber         | Gets or sets the initial footnote number.                                             |
| LastParagraph                 | Gets last section object.                                                               |
| LastSection                   | Gets last section of the document.                                                     |
| ListStyles                    | Gets document list styles.                                                             |
| MailMerge                     | Gets mail merge engine.                                                                |
| ProtectionType                | Gets or sets the type of protection of the                                            |

## API Reference (if applicable)
- This section describes the properties listed above.
- Additional methods and properties not explicitly mentioned may also exist.

## Code Examples (multi-language supported)
- Refer to the Syncfusion documentation for examples of using these methods and properties.

## Page-level Navigation/TOC (if applicable)
- This section provides navigation links to other relevant parts of the documentation.

## Cross References
- See related sections in the documentation for more details on document manipulation and properties.

## RAG Annotations
<!-- tags: [syncfusion-sdk, DocIo, methods, read-only mode, async saving] keywords: [Background, Bookmarks, BuiltInDocumentProperties, ChildEntities, CustomDocumentProperties, EndnoteNumberFormat, EndnotePosition, EntityType, FootnoteNumberFormat, FootnotePosition, InitialEndnoteNumber, InitialFootnoteNumber, LastParagraph, LastSection, ListStyles, MailMerge, ProtectionType] -->
```