```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: DocIo
page_number: 171
page_id: DocIo#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:46Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Provides details about the BookmarkNavigator class.
- Explains the Public Constructor, Public Properties, and Public Methods for managing bookmarks in a document.
- Demonstrates how to use the BookmarkNavigator class with an example.

## Content

### Public Constructor
The following table lists the public constructor of the BookmarkNavigator class:

| Name | Description |
|------|-------------|
| `BookmarkNavigator.BookmarkNavigator(IWordDocument)` | Initializes a new instance of the BookmarkNavigator class. |

### Public Properties
The following table lists the public properties of the BookmarkNavigator class:

| Name | Description |
|------|-------------|
| `CurrentBookmark` | Gets the current bookmark. |
| `Document` | Gets or sets Document that this object is attached to. |

### Public Methods
The following table lists the public methods of the BookmarkNavigator class:

| Name | Description |
|------|-------------|
| `DeleteBookmarkContent` | Deletes the bookmark content. |
| `GetBookmarkContent` | Gets the bookmark content. |
| `InsertParagraphItem` | Inserts the paragraph item to current position. |
| `InsertTable` | Inserts the table. |
| `InsertText` | Inserts the text. |
| `MoveToBookmark` | Moves to bookmark. |
| `ReplaceBookmarkContent` | Replaces bookmark content. |
| `InsertParagraph` | Inserts the paragraph. |
| `InsertTextBodyPart` | Inserts the body part of the text. |

### Note
**Note:** The `GetBookmarkContent` method works fine for tables, if they are located between the bookmark start and bookmark end.

The following example demonstrates how to use the `BookmarkNavigator` class.
```