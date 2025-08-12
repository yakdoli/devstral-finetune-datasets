```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: edit
page_number: 086
page_id: edit#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:24Z
fidelity: lossless
-->

## Overview
- Describes bookmark functionalities in syncfusion forms.
- Highlights methods for adding, removing, navigating, and clearing bookmarks.
- Provides C# and VB.NET code examples demonstrating bookmark operations.

## Content
### WinForms Bookmark Operations

#### Table of Bookmark Methods
| Method          | Description                             |
|-----------------|-----------------------------------------|
| BookmarkAdd     | Sets a bookmark at the specified line.  |
| BookmarkRemove  | Removes a bookmark at the specified line. |
| BookmarkGet     | Gets a bookmark at the specified line.   |
| BookmarkNext    | Navigates to the next bookmark.         |
| BookmarkPrevious| Navigates to the previous bookmark.     |
| BookmarkClear   | Clears all bookmarks.                   |

#### Code Examples

##### C#

```csharp
// Sets bookmark at the specified line.
this.editControl.BookmarkAdd(this.editControl.CurrentLine);

// Removes bookmark at the specified line.
this.editControl.BookmarkRemove(this.editControl.CurrentLine);
this.editControl.BookmarkRemove(this.editControl.CurrentLine);

// Draw the bookmark with custom look and feel specified in the BrushInfo object.
BrushInfo brushInfo = new BrushInfo(GradientStyle.ForwardDiagonal,
Color.IndianRed, Color.Ivory);
this.editControl.BookmarkAdd(this.editControl.CurrentLine,
brushInfo);

// Get the Bookmark object of the current line.
IBookmark bookmark =
this.editControl.BookmarkGet(this.editControl.CurrentLine);
```

##### VB.NET

```vb.net
' Sets bookmark at the specified line.
Me.editControl.BookmarkAdd(Me.editControl.CurrentLine)

' Removes bookmark at the specified line.
Me.editControl.BookmarkRemove(Me.editControl.CurrentLine)

' Draw the bookmark with custom look and feel specified in the BrushInfo object.
Dim brushInfo As BrushInfo = new 
BrushInfo(GradientStyle.ForwardDiagonal, Color.IndianRed, Color.Ivory)
Me.editControl.BookmarkAdd(Me.editControl.CurrentLine, brushInfo)
```

## API Reference

### Methods
- `BookmarkAdd`: Adds a bookmark at the specified line.
- `BookmarkRemove`: Removes a bookmark at the specified line.
- `BookmarkGet`: Retrieves a bookmark at the specified line.
- `BookmarkNext`: Navigates to the next bookmark.
- `BookmarkPrevious`: Navigates to the previous bookmark.
- `BookmarkClear`: Clears all bookmarks.

### Parameters
| Name           | Description                                       |
|----------------|---------------------------------------------------|
| CurrentLine    | The line number where the bookmark is to be set. |

### Returns
- `IBookmark`: An object representing the bookmark at the specified line.

### Exceptions
- `System.ArgumentOutOfRangeException`: Thrown if the line number is invalid.

## Code Examples (continued)

The provided examples demonstrate how to interact with bookmarks programmatically, showing both standard and customized bookmark creation, removal, and retrieval processes.

## RAG Annotations
<!-- tags: [syncfusion, windows forms, bookmarks, guidance, operations, C#, VB.NET] keywords: [bookmarkAdd, bookmarkRemove, bookmarkGet, bookmarkNext, bookmarkPrevious, bookmarkClear, editControl, currentLine, brushInfo, gradientStyle, indianRed, ivory] -->
```