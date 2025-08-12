```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: DocIo
page_number: 168
page_id: DocIo#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:24Z
fidelity: lossless
-->

## Overview
- This page explains the concept of using **BookmarkNavigator** in the Word document to navigate and manipulate content between bookmarks. It covers methods for moving to bookmarks, inserting content, deleting, and replacing content between bookmark boundaries.

## Content

### 4.4.1.3.1 Bookmark Navigator

**BookmarkNavigator** is used for navigation between bookmarks in the Word document.

#### Navigation to Bookmarks
- You can navigate to a bookmark by using the **MoveToBookmark** method. There are two overloads for this method:
  - **MoveToBookmark(string bookmarkName, bool isStart, bool isAfter)**: Moves to the bookmark with the specified name. The `isStart` parameter defines whether to move to the bookmark start or end, and the `isAfter` parameter defines whether to set the virtual "cursor" after or before the bookmark start or end.
  - **MoveToBookmark(string bookmarkName)**: Moves to the bookmark start with the specified name, and sets the "cursor" before the bookmark start.

#### Inserting Content between Bookmarks
- You can insert text between bookmark start and bookmark end using the **InsertText** method.
- You can insert a table between the bookmark start and bookmark end using the **InsertTable** method.
- You can insert a paragraph between the bookmark start and bookmark end using the **InsertParagraph** method.
- You can insert the text body part between the bookmark start and bookmark end using the **InsertTextBodyPart** method.
- You can insert paragraph items between the bookmark start and bookmark end using the **InsertParagraphItem** method.

#### Deleting and Replacing Content
- You can delete content between the bookmark start and bookmark end by using the **DeleteBookmarkContent** method.
- You can replace content between the bookmark start and bookmark end by using the **ReplaceBookmarkContent** method.

### Advanced Usage Example
```csharp
paragraph = section.AddParagraph();
paragraph.AppendBookmarkStart("multi_paragraph");
paragraph.AppendText("Bookmark starts here and ends in the next paragraph");

paragraph = section.AddParagraph();
paragraph.AppendText("This ");
paragraph.AppendBookmarkStart("overlapped bookmark");
paragraph.AppendText("bookmark over");
paragraph.AppendBookmarkEnd("multi_paragraph");
paragraph.AppendText("laps ");
paragraph.AppendBookmarkEnd("overlapped bookmark");
paragraph.AppendText("with previous one");

doc.Save("Bookmarks.doc");
```

## API Reference (if applicable)

### Methods
- **MoveToBookmark(string bookmarkName, bool isStart, bool isAfter)**: Moves the position to the specified bookmark.
- **MoveToBookmark(string bookmarkName)**: Moves to the bookmark start.
- **InsertText()**: Inserts text at the current position.
- **InsertTable()**: Inserts a table at the current position.
- **InsertParagraph()**: Inserts a paragraph at the current position.
- **InsertTextBodyPart()**: Inserts text body part at the current position.
- **InsertParagraphItem()**: Inserts paragraph items at the current position.
- **DeleteBookmarkContent()**: Deletes content between the bookmark start and end.
- **ReplaceBookmarkContent()**: Replaces content between the bookmark start and end.

## Code Examples (multi-language supported)

### C# Example
```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new Word document
WordDocument doc = new WordDocument();

// Create a section
Section section = doc.AddSection();

// Create paragraph and add bookmark
paragraph = section.AddParagraph();
paragraph.AppendBookmarkStart("multi_paragraph");
paragraph.AppendText("Bookmark starts here and ends in the next paragraph");

paragraph = section.AddParagraph();
paragraph.AppendText("This ");
paragraph.AppendBookmarkStart("overlapped bookmark");
paragraph.AppendText("bookmark over");
paragraph.AppendBookmarkEnd("multi_paragraph");
paragraph.AppendText("laps ");
paragraph.AppendBookmarkEnd("overlapped bookmark");
paragraph.AppendText("with previous one");

// Save the document
doc.Save("Bookmarks.doc");
```

## RAG Annotations
<!-- tags: Syncfusion Winforms, DocIo, BookmarkNavigator, Bookmark Manipulation, API Reference, Example Code keywords: bookmark, navigation, insertion, deletion, replacement, Word document, DocumentIO, C# example -->
```