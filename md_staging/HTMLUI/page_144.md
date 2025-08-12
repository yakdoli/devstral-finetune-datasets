```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: HTMLUI
page_number: 144
page_id: HTMLUI#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:28Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- The HTMLUI control enables users to search for text within documents displayed in the control.
- Features include "Updown" and "Matchcase" search options.
- Utilizes the `DisplayFindForm` method for search functionality.
- The `CTRL+F` shortcut can also be used to enable the search feature.

## Content

The HTMLUI control, similar to popular browsers, allows users to search for a given text within the document displayed. This functionality is achieved using the `DisplayFindForm` method, which supports "Updown" and "Matchcase" search options. These features make it easy for users to locate the required text within the displayed document.

The `CTRL+F` shortcut can also be used to enable this search feature.

### Code Examples

#### C#

```csharp
// Display the Find form for searching the text content of the HTMLUI control's current document
this.htmluiControl1.DisplayFindForm();
```

#### VB.NET

```vb
' Display the Find form for searching the text content of the HTMLUI control's current document
Me.htmluiControl1.DisplayFindForm()
```

### 4.20.1 HTMLUI Searching Sample

This sample demonstrates how a text can be searched in a document loaded into the HTMLUI control.

## Page-level Navigation/TOC (if applicable)
- Essential HTMLUI for Windows Forms
  - Overview
  - Content
    - Code Examples
    - 4.20.1 HTMLUI Searching Sample

## Cross References
See also: HTMLUI control, text search, `DisplayFindForm`, `CTRL+F` shortcut, Updown search, Matchcase search.

<!-- tags: [product: Syncfusion Winforms, module: HTMLUI, control: HTMLUI, api: DisplayFindForm, version: 11.4.0.26] keywords: [HTMLUI, text search, DisplayFindForm, Matchcase, Updown, CTRL+F, sample] -->
```