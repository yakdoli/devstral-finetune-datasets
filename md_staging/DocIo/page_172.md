```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: DocIo
page_number: 172
page_id: DocIo#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:46Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Demonstrates how to use the `BookmarksNavigator` class to manage bookmarks in a Word document.
- Illustrates inserting and replacing bookmark content while preserving formatting.

## Content

### Managing Bookmark Content

You can also preserve the formatting in the template (target) document while inserting or replacing the bookmark with a string, by deleting the content of the bookmark without deleting its format. The following code illustrates this.

#### C#

```csharp
IWordDocument doc = new WordDocument( Path + "BookmarkNavigator.doc" );

BookmarksNavigator bn = new BookmarksNavigator( doc );
bn.MoveToBookmark( "bm_bodypart" );
TextBodyPart part = bn.GetBookmarkContent();
bn.MoveToBookmark( "bm_empty" );
bn.ReplaceBookmarkContent( part );
TextSelection sel =(doc as WordDocument).Find( "11" , false, false );
```

### Preserving Formatting in Bookmarks

By using the `DeleteBookmarkContent(false)` method, you can remove the content of a bookmark without destroying its formatting. Once the content is replaced, the formatting is retained.

#### C#

```csharp
// Move to the Essential_DocIO bookmark.
bk.MoveToBookmark("Essential_DocIO");

// Delete bookmark content without deleting the format in the target document.
bk.DeleteBookmarkContent(false);

// Insert Text
bk.InsertText("Essential XlsIO is a Non UI component that can be used in both ASP.NET and windows forms applications. The usage is common for both environments except for the part where the created spreadsheet is saved to disk or stream in the case of a windows forms application and streamed to the client browser in the case of asp.net applications.");
```

### Maintaining Bookmarks in Documents

This approach ensures that the formatting of bookmarks is preserved when content is dynamically inserted during runtime. This is particularly useful in scenarios where the document's layout needs to remain consistent despite changes in the content.

## API Reference

### BookmarksNavigator

- **MoveToBookmark(String bookmarkName)**: Navigates to the specified bookmark.
- **GetBookmarkContent()**: Retrieves the content of the current bookmark.
- **ReplaceBookmarkContent(TextBodyPart content)**: Replaces the content of the current bookmark with the specified content.
- **DeleteBookmarkContent(Boolean deleteFormatting)**: Deletes the content of the bookmark without removing its formatting if `false` is passed.

### WordDocument

- **Find(String findText, Boolean matchCase, Boolean matchWholeWord)**: Searches for a specific text within the document.

## Code Examples

The examples provided above illustrate:

1. How to navigate to a bookmark using `MoveToBookmark`.
2. How to replace bookmark content while maintaining document formatting.
3. How to insert dynamic text into a document using bookmarks effectively.

## See also

- [BookmarksNavigator Documentation](https://www.syncfusion.com/documentation/)
- [WordDocument API Reference](https://www.syncfusion.com/documentation/)

<!-- tags: [WordDocument, BookmarksNavigator, formatting, bookmarks, document management, Word Processing] keywords: [Essential DocIO, bookmarks, content replacement, formatting preservation, Dynamic content insertion, WordDocument, BookmarksNavigator] -->
```