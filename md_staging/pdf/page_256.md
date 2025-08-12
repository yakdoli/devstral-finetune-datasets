```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_256.jpeg
document_name: pdf
page_number: 256
page_id: pdf#page_256
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:25Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Provides methods to access essential components of a PDF document, including forms, pages, security parameters, and viewer preferences.
- Describes how to clone a PDF document using the `PdfLoadedDocument.Clone` method.
- Explains handling bookmarks while working with `PdfLoadedDocument`.

## Content

### Document Components

The following table lists the essential components of a PDF document that can be accessed:

| Term | Description |
|------|-------------|
| Form | Gets the loaded form. |
| Pages | Gets the pages. |
| Security | Gets the security parameters of the document. |
| ViewerPreferences | Gets or sets a viewer preferences object, controlling the way the document is to be presented on the screen, or in print. |

### Cloning a document

You can clone a PDF document in order to copy the document without saving it. This can be done by using the `PdfLoadedDocument.Clone` method.

#### Example code for cloning a document

**C#**

```csharp
PdfLoadedDocument ldoc = new PdfLoadedDocument("sample.pdf");
PdfLoadedDocument doc = lDoc.Clone() as PdfLoadedDocument;
```

**VB.NET**

```vbnet
Dim ldoc As New PdfLoadedDocument(sample.pdf)
Dim doc As PdfLoadedDocument = TryCast(lDoc.Clone(), PdfLoadedDocument)
```

> **Note:** To open and save the document asynchronously for Windows Store apps, refer to the **Asynchronous Support** section.

#### Bookmarks in PDF Documents

##### 4.2.1.1 Bookmark

While loading an existing document, the library loads all bookmarks of the document. Each loaded bookmark is represented by the `PdfLoadedBookmark` class, inherited from the `PdfBookmark` class. You can access the root collection of document bookmarks by using the `Bookmark` property of the `PdfLoadedDocument` class. This collection is represented by the `PdfBookmarkBase` class.

The following code example illustrates how to access a loaded bookmark.

## API Reference

- **Classes:**
  - `PdfLoadedDocument`
  - `PdfLoadedBookmark`
  - `PdfBookmark`
  - `PdfBookmarkBase`

- **Methods:**
  - `PdfLoadedDocument.Clone()`

## Code Examples

Refer to the examples provided in the Cloning a document section and the Bookmark section for usage details.

<!-- tags: [pdf, document components, cloning, bookmarks, pdfloadeddocument, pdfloadedbookmark, viewerpreferences] keywords: [form, pages, security parameters, viewer preferences, asynchronous support, bookmark, loaded document, clone, bookmarks] -->
```