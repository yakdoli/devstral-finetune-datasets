```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_259.jpeg
document_name: pdf
page_number: 259
page_id: pdf#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:39Z
fidelity: lossless
-->

## Essential PDF

### Overview
- This section describes various actions and destinations that can be used in PDF documents.
- It includes types of actions such as PdfUriAction, PdfJavaScriptAction, and PdfDestination.
- Demonstrates how to create bookmarks with specific actions in C#.

### WinForms-specific Conventions
- This section follows the conventions of Syncfusion Winforms, showcasing how to implement PDF features.

### Content

#### Actions and Destinations in PDF Documents

| Action/Destination | Description |
|--------------------|-------------|
| PdfUriAction | Acts as a unique resource identifier. |
| PdfJavaScriptAction | Performs a JavaScript action in the PDF document. |
| PdfDestination | Represents an anchor in the document where bookmarks and annotations can direct when clicked. |
| PdfGoToAction | This action goes to a destination in the current document. |

#### C# Code Examples

```csharp
[C#]

// Create new Bookmark
PdfBookmark bookmarkaction = doc.Bookmarks.Add("Annotations");

PdfLaunchAction action = new PdfLaunchAction(@"..\..\Data\Book.txt");

// launch file when we click the Bookmark
bookmarkaction.Action = action;

PdfBookmark bookmarkaction1 = doc.Bookmarks.Add("Uriaction");

// Create uri action
PdfUriAction uriAction = new PdfUriAction("http://www.google.com");

// Set uri action. Clicking the bookmark will move to the corresponding uri
bookmarkaction1.Action = uriAction;

PdfBookmark bookmarkaction2 = doc.Bookmarks.Add("Scriptaction");

// Create Java action
PdfJavaScriptAction javaAction = new PdfJavaScriptAction("app.alert(\"You are looking at Java script action of PDF \")");
bookmarkaction2.Action = javaAction;

PdfBookmark bookmarkaction3 = doc.Bookmarks.Add("Pagelocation");
PdfDestination dest = new PdfDestination(doc.Pages[1], new Point(0, 100));
PdfGoToAction goToAction = new PdfGoToAction(doc.Pages[1]);
goToAction.Destination = dest;

// Will move to a particular location of this page
bookmarkaction3.Action = goToAction;
```

#### VB.NET Code Example

```vbnet
[VB.NET]
```

### Page-level Navigation/TOC
- [unclear]

### Cross References
- See also: [unclear]

## API Reference

### Namespaces, Classes, and Members
- Refer to the documentation for detailed API information.

<!-- tags: [syncfusion pdf actions, pdf javascript, pdf bookmarks, pdf destinations] keywords: [pdflaunchaction, pdfuriaction, pdfjavascriptaction, pdfdestination, pdfgototoaction, annotations, javascript action, url action, document actions, bookmarks] -->
```