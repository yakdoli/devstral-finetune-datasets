```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_231.jpeg
document_name: DocIo
page_number: 231
page_id: DocIo#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:27Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- The `WListFormat` class provides properties and methods to manage list formatting in a paragraph.
- It allows setting and retrieving list styles, levels, numbering behavior, and indent levels.
- Example code snippet demonstrates using `WListFormat` in `DocIO` to work with default numbered lists.

## Content

### WListFormat.WListFormat (IWParagraph)

Initializes a new instance of the `WListFormat` class.

### Public Properties

| Name                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| CurrentListLevel    | Gets or sets the paragraph's `ListLevel`.                                  |
| CurrentListStyle    | Gets or sets the paragraph's list style.                                   |
| CustomStyleName     | Gets or sets the name of the custom style.                                |
| ListLevelNumber     | Gets or sets the list nesting level.                                       |
| ListType            | Gets or sets the type of the list.                                         |
| RestartNumbering    | Gets or sets whether numbering of the list must restart from the previous list. |

### Public Methods

| Name                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| ApplyDefBulletStyle| Applies the default bullet style for the current paragraph.               |
| ApplyDefNumberedStyle| Applies the default numbered style for the current paragraph.          |
| ApplyStyle         | Gets or sets the name of the custom style.                                |
| ContinueListNumbering| Continues the last list.                                                |
| DecreaseIndentLevel| Decreases the level indentation.                                         |
| IncreaseIndentLevel| Increases the level indentation.                                         |
| RemoveList          | Removes the list from the current paragraph.                              |

### Example Usage

The following example illustrates how to use the `WListFormat` and list styles in `DocIO`.

```csharp
// Write default numbered list
```

## API Reference

### Namespace: `Syncfusion.DocIO.WListFormat`
**Class:** `WListFormat`

#### Constructor
`WListFormat.WListFormat(IWParagraph)`
- **Description:** Initializes a new instance of the `WListFormat` class.

#### Public Properties
- **Name:** CurrentListLevel
  - **Description:** Gets or sets the paragraph's `ListLevel`.
- **Name:** CurrentListStyle
  - **Description:** Gets or sets the paragraph's list style.
- **Name:** CustomStyleName
  - **Description:** Gets or sets the name of the custom style.
- **Name:** ListLevelNumber
  - **Description:** Gets or sets the list nesting level.
- **Name:** ListType
  - **Description:** Gets or sets the type of the list.
- **Name:** RestartNumbering
  - **Description:** Gets or sets whether numbering of the list must restart from the previous list.

#### Public Methods
- **Name:** ApplyDefBulletStyle
  - **Description:** Applies the default bullet style for the current paragraph.
- **Name:** ApplyDefNumberedStyle
  - **Description:** Applies the default numbered style for the current paragraph.
- **Name:** ApplyStyle
  - **Description:** Gets or sets the name of the custom style.
- **Name:** ContinueListNumbering
  - **Description:** Continues the last list.
- **Name:** DecreaseIndentLevel
  - **Description:** Decreases the level indentation.
- **Name:** IncreaseIndentLevel
  - **Description:** Increases the level indentation.
- **Name:** RemoveList
  - **Description:** Removes the list from the current paragraph.

## Code Examples

```csharp
// Write default numbered list
```

## Page-level Navigation/TOC (if applicable)

- [ ] This page is part of a larger document structure.
- [ ] Refer to the main table of contents or documentation index for more details.

## Cross References

- This documentation is related to `DocIO` functionalities in `Syncfusion Winforms`.
- Refer to other sections or modules for additional information on `DocIO` and related APIs.

## RAG Annotations

<!-- tags: [DocIO, Syncfusion, Winforms, listformatting, numberedlist, bulletedlist] keywords: [WListFormat, ListLevel, ListStyle, CustomStyleName, ListLevelNumber, ListType, RestartNumbering, ApplyDefBulletStyle, ApplyDefNumberedStyle, ApplyStyle, ContinueListNumbering, DecreaseIndentLevel, IncreaseIndentLevel, RemoveList, DocIO] -->
```