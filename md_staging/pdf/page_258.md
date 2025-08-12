```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_258.jpeg
document_name: pdf
page_number: 258
page_id: pdf#page_258
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:46Z
fidelity: lossless
-->

# Essential PDF

## Overview

- This section demonstrates how to manipulate bookmarks in a PDF document using C# and VB.NET.
- Tips on modifying bookmark properties, such as destination, color, text style, and title.

---

## Content

### Modifying Bookmarks in a PDF Document

#### Example Codes

##### C#

```csharp
const string filename = "...";
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);
bookmarPdfLoadedPage ldPage = loadedDoc.Pages[1] as PdfLoadedPage;

PdfBookmarkBase rootCollection = ldDoc.Bookmarks;

PdfLoadedBookmark bookmark = rootCollection[0] as PdfLoadedBookmark;
bookmark.Destination = new PdfDestination(ldPage);
bookmark.Color = Color.Green;
bookmark.TextStyle = PdfTextStyle.Bold;
bookmark.Title = "Changed title";

ldDoc.Save(newFileName);
ldDoc.Close();
```

##### VB.NET

```vbnet
Const filename As String = "..."
Dim ldDoc As New PdfLoadedDocument(filename)
Dim ldPage As bookmarPdfLoadedPage = TryCast(loadedDoc.Pages(1), PdfLoadedPage)

Dim rootCollection As PdfBookmarkBase = ldDoc.Bookmarks

Dim bookmark As PdfLoadedBookmark = TryCast(rootCollection(0), PdfLoadedBookmark)
bookmark.Destination = New PdfDestination(ldPage)
bookmark.Color = Color.Green
bookmark.TextStyle = PdfTextStyle.Bold
bookmark.Title = "Changed title"

Const newFileName As String = "..."
ldDoc.Save(newFileName)
ldDoc.Close()
```

---

### 2. Adding Actions to Bookmark

#### Overview

You can perform actions by clicking the bookmarks at run time. To add custom actions to the bookmarks, use the following classes.

#### Supported Actions

| Class Name        | Description               |
|-------------------|---------------------------|
| PdfLaunchAction   | Launches an application, opens or prints a document. |

---

### API Reference

- **Namespace**: EssentialPDF
- **Class**: PdfLoadedDocument
- **Class**: PdfLoadedPage
- **Class**: PdfBookmarkBase
- **Class**: PdfLoadedBookmark
- **Class**: PdfDestination
- **Class**: PdfLaunchAction

---

### Code Examples

#### Modifying a Bookmark

- **C#**
  - Demonstrates modifying the destination, color, text style, and title of a bookmark.

- **VB.NET**
  - Similar functionality to C#, with syntax adjustments for VB.NET.

#### Adding Actions to a Bookmark

```csharp
// Example of adding a launch action to a bookmark
PdfLaunchAction launchAction = new PdfLaunchAction("path_to_application.exe");
bookmark.Action = launchAction;
```

```vbnet
' Example of adding a launch action to a bookmark
Dim launchAction As PdfLaunchAction = New PdfLaunchAction("path_to_application.exe")
bookmark.Action = launchAction
```

---

## Page-level Navigation/TOC

- [2. Adding Actions to Bookmark](#2-adding-actions-to-bookmark)

---

## Cross References

- Refer to the PDF manipulation section for more details on document loading and saving.
- See the Actions section for additional types of actions that can be associated with bookmarks.

---

<!-- tags: [EssentialPDF, PDF manipulation, bookmarks, C#, VB.NET, Action] keywords: [PdfLoadedDocument, PdfDestination, PdfLaunchAction, bookmark properties] -->
```