```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_260.jpeg
document_name: pdf
page_number: 260
page_id: pdf#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:40Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Create and configure bookmarks with various actions, including launching files, navigating to URLs, executing JavaScript, and moving to specific page locations.

## Content

### Adding Bookmarks with Actions

```vb
' Create new Bookmark
Dim bookmarkaction As PdfBookmark = doc.Bookmarks.Add("Annotations")
Dim action As New PdfLaunchAction("...\Data\Book.txt")

' launch file when we click the Bookmark
bookmarkaction.Action = action

' Create url action
Dim bookmarkaction1 As PdfBookmark = doc.Bookmarks.Add("Uriaction")
Dim uriAction As New PdfUriAction("http://www.google.com")

' Set uri action. Clicking the bookmark will move to the corresponding uri
bookmarkaction1.Action = uriAction

' Create Java action
Dim bookmarkaction2 As PdfBookmark = doc.Bookmarks.Add("Scriptaction")
Dim javaAction As New PdfJavaScriptAction("app.alert(""You are looking at Java script action of PDF "")")
bookmarkaction2.Action = javaAction

' Create page location action
Dim bookmarkaction3 As PdfBookmark = doc.Bookmarks.Add("Pagelocation")
Dim dest As New PdfDestination(doc.Pages(1), New Point(0, 100))
Dim goToAction As New PdfGoToAction(doc.Pages(1))
goToAction.Destination = dest

' Will move to this page particular location
bookmarkaction3.Action = goToAction
```

## API Reference
- **Namespace**: Syncfusion.Pdf (or relevant PDF library namespace)
- **Class**: 
  - `PdfBookmark`: Represents a bookmark in a PDF document.
  - `PdfAction`: Base class for various types of actions that can be attached to bookmarks.
  - `PdfLaunchAction`: Launches a file when the bookmark is clicked.
  - `PdfUriAction`: Navigates to a URL when the bookmark is clicked.
  - `PdfJavaScriptAction`: Executes JavaScript when the bookmark is clicked.
  - `PdfGoToAction`: Moves to a specific page or location in the PDF when the bookmark is clicked.
- **Properties/Methods**:
  - `Bookmarks`: Collection of bookmarks in the PDF document.
  - `Add`: Adds a new bookmark to the document.
  - `Action`: Sets the action that will be executed when the bookmark is clicked.
  - `PdfDestination`: Represents a location in the PDF document.

## Code Examples
The provided VB code demonstrates the creation of bookmarks with different actions:
- `PdfLaunchAction`: Opens a file.
- `PdfUriAction`: Navigates to a webpage.
- `PdfJavaScriptAction`: Executes a JavaScript alert.
- `PdfGoToAction`: Moves to a specific location on a page.

## Page-level Navigation/TOC (if applicable)
- This page explains how to create bookmarks with various actions in a PDF document.

## Cross References
- Refer to the documentation on `PdfLaunchAction`, `PdfUriAction`, `PdfJavaScriptAction`, and `PdfGoToAction` for more details on their functionality.

<!-- tags: [pdf, bookmarks, actions, launch, url, javascript, goto, document] keywords: [Syncfusion Winforms, bookmarks, actions, PDF manipulation, document actions, bookmark configuration] -->
```