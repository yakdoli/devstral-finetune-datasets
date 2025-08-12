```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: edit
page_number: 087
page_id: edit#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:53Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to get, set, and remove bookmarks in a Windows Forms application using Syncfusion's Edit control.
- Focuses on bookmark management using methods like `SetCustomBookmark`, `RemoveCustomBookmark`, and `BookmarkClear`.

## Content

### Getting Bookmarks

To retrieve the bookmark object of the current line, you can use the following code snippet:

```vb
' Get the Bookmark object of the current line.
Dim bookmark As IBookmark = Me.EditControl1.BookmarkGet(Me.EditControl1.CurrentLine)
```

### Setting Bookmarks

Bookmarks can be set and removed using the following methods:

| Edit Control Method           | Description                                                                  |
|------------------------------|------------------------------------------------------------------------------|
| `SetCustomBookmark`          | Sets custom bookmark for the desired line.                                |
| `RemoveCustomBookmark`       | Removes the custom bookmark from the desired line.                        |

**Note:** To clear the bookmarks set by using the `SetCustomBookmark` method, you must use the `BookmarkClear` method with its `bool` argument set as `True`.

The bookmarks set by using the `SetCustomBookmark` method do not respond to the `BookmarkNext` and `BookmarkPrevious` methods automatically. To enable this functionality, you need to set the `UseInBookmarkSearch` property of the custom bookmark to `True`.

#### [C#]

```csharp
// Sets custom bookmarks and enables it to respond to BookmarkNext and BookmarkPrevious methods.
ICustomBookmark customBookmark =
    this.editControl1.SetCustomBookmark(this.editControl1.CurrentLine, new BookmarkPaintEventHandler(CustomBookmarkPainter));
customBookmark.UseInBookmarkSearch = true;

// Removes the bookmark of the current line.
ICustomBookmark customBookmark =
    this.editControl1.RemoveCustomBookmark(this.editControl1.CurrentLine, BookmarkPaintEventHandler(CustomBookmarkPainter));
```

#### [VB.NET]

```vb
' Sets custom bookmarks and enables it to respond to BookmarkNext and BookmarkPrevious methods.
Dim customBookmark As ICustomBookmark =
    Me.editControl1.SetCustomBookmark(Me.editControl1.CurrentLine, New BookmarkPaintEventHandler(CustomBookmarkPainter))
```

## Page-level Navigation/TOC (if applicable)
- **Getting Bookmarks**
- **Setting Bookmarks**

<!-- tags: [product, winforms, edit, bookmarks, version:] keywords: [bookmarks, get, set, remove, custombookmark, useinbookmarksearch] -->
```