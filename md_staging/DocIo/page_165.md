```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: DocIo
page_number: 165
page_id: DocIo#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:46Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- This page discusses the mechanism for adding and managing bookmarks in a document using DocIO.
- It covers the bookmark naming rules and methods for finding and removing bookmarks.
- Describes the structure of bookmarks, including BookmarkStart and BookmarkEnd classes.

## Content

3. Type the name of the bookmark.  
4. Click the Add button.

**Note:** Bookmark names must begin with a letter and can contain numbers. You cannot include spaces in a bookmark name. However, you can use the underscore character to separate words.

DocIO provides a simple mechanism for adding bookmarks to a document and managing them. Every Word document contains a collection of bookmarks accessible through the Bookmarks property of the Word document. This collection contains objects of the Bookmark type, enabling you to find and delete bookmarks.

You can find a bookmark in the Bookmarks Collection by specifying its name using the FindByName procedure. To remove a bookmark, you can specify its index using the RemoveAt procedure or remove a specified bookmark using the Remove procedure.

Every DocIO bookmark consists of the BookmarkStart and BookmarkEnd. The BookmarkStart class represents the start of a specific bookmark, while the BookmarkEnd class represents the end. Both classes have a common property, `Name`, which defines the name of the DocIO bookmark.

### Class Hierarchy

- **ParagraphItem**
  - WBookmarkStart
- **ParagraphItem**
  - WBookmarkEnd

### BookmarkStart Public Constructor

| Name                               | Description                             |
|------------------------------------|-----------------------------------------|
| BookmarkStart.BookmarkStart(IWordDocument, string) | Initializes a new instance of the BookmarkStart class. |

## API Reference

- **Namespace:** Unspecified in the given context.
- **Class:** BookmarkStart
- **Members:**
  - **Constructor:** 
    - **Name:** BookmarkStart(IWordDocument, string)
    - **Description:** Initializes a new instance of the BookmarkStart class.

## Code Examples

No code examples are provided in the given text.

## Page-level Navigation/TOC (if applicable)

No TOC or navigation content is present in the given text.

## Cross References

No cross-references are explicitly mentioned in the given text.

<!-- tags: [DocIO, bookmarks, Word documents, WordDocument, Bookmarks property, BookmarkStart, BookmarkEnd, FindByName, RemoveAt, Remove] keywords: [bookmark naming, removing bookmarks, managing bookmarks, Word document bookmarks] -->
```