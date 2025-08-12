```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_257.jpeg
document_name: pdf
page_number: 257
page_id: pdf#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:36Z
fidelity: lossless
-->

# Essential PDF

```csharp
const string filename = "...";
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);

PdfBookmarkBase rootCollection = ldDoc.Bookmarks;

PdfLoadedBookmark bookmark = rootCollection[0] as PdfLoadedBookmark;

ldDoc.Save(newFileName);
ldDoc.Close();
```

```vb
const string filename = "...";
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);

PdfBookmarkBase rootCollection = ldDoc.Bookmarks;

PdfLoadedBookmark bookmark = rootCollection[0] as PdfLoadedBookmark;

ldDoc.Save(newFileName);
ldDoc.Close();
```

## Bookmark Manipulation

The following manipulations can be made to the bookmarks:

- Modifying bookmarks
- Adding Actions to the bookmark

### 1. Modifying bookmarks

Bookmarks can be modified in the following ways:

- Change the bookmark style, color, title, and destination
- Add or insert new bookmarks into the root collection
- Add or insert new bookmarks as a child of another bookmark
- Assign the destination of the added bookmarks to a loaded page or a new page of the document

The following code example illustrates how to modify the bookmark style and destination.

---

© 2013 Syncfusion. All rights reserved. 257 | Page
```