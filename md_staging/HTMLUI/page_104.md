```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: HTMLUI
page_number: 104
page_id: HTMLUI#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:00Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

The following image shows the bookmarks implemented using HTMLUI.

![HTML Bookmarks inserted into the HTMLUI Control](image.png)

**Figure 32: HTML Bookmarks inserted into the HTMLUI Control**

## HTMLUI Bookmarks Sample

This sample illustrates the implementation of Bookmarks in HTMLUI.

### Summary:
- Demonstrates bookmarks functionality in HTMLUI for Windows Forms.
- Includes visual representation of bookmarks within a UI control.
- Focuses on linking to file bookmarks and bookmarks within the same file.

### Content

### HTMLUI Bookmarks Sample

This sample illustrates the implementation of Bookmarks in HTMLUI.

#### Key	points:
- **Bookmark functionality** is showcased within the HTMLUI control.
- The sample includes links to file bookmarks (`File 1`) and bookmarks within the same file.
- This demonstrates how bookmarks can be utilized effectively in an HTMLUI-based Windows Forms application.

### Code Example (partial):
```csharp
// Example of setting up bookmarks in HTMLUI
var bookmarkList = new List<Bookmark>();
bookmarkList.Add(new Bookmark() { Name = "Link to File 1 Bookmark", URL = "file:/path/to/File1.html#bookmark1" });
bookmarkList.Add(new Bookmark() { Name = "Link to Bookmark in this file", URL = "#SameFileBookmark" });

htmlUI1.Bookmarks = bookmarkList;

// HTML for demonstration purposes:
<div>
    <a href="#bookmark1">Link to File 1 Bookmark</a>
    <a href="#SameFileBookmark">Same File</a>
</div>
```

### Notes:
- Ensure that the paths and links in the bookmarks are valid and correctly configured.
- Test the bookmarks functionality across different browsers and scenarios to confirm reliability.
- Customize the appearance and behavior of bookmarks as needed.

### References:
- Refer to the Syncfusion WinForms documentation for detailed information on HTMLUI controls and bookmarking functionality.
- Visit the Syncfusion support portal for additional examples and FAQs.

### RAG Annotations:
<!-- tags: HTMLUI, bookmarks, WinForms, Syncfusion, HTML Bookmarks, Windows Forms, feature implementation keywords: bookmarks, HTMLUI, UI control, file links, internal links, Windows Forms, Syncfusion -->

```
