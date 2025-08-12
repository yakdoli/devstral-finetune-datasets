```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_249.jpeg
document_name: pdf
page_number: 249
page_id: pdf#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:14Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Highlights Viewer Preference settings in Adobe Reader.
- Explains hiding toolbar, menubar, and window UI elements.
- Demonstrates using code examples for enabling these features.

## Content

### Page Settings

![Figure: Page Settings](./pdf#page_249#fig-55)

**Figure 55: Page Settings**

### Viewer Preference Settings

Essential PDF supports Viewer Preference options for the pdf pages such as hiding toolbar, hiding menubar, and hiding window UI. The `HideToolbar`, `HideMenuBar`, and `HideWindowUI` properties can be used for enabling these features. The following code example illustrates this.

#### Code Examples

##### C#
```csharp
// To hide the viewer application's Tool bar
doc.ViewerPreferences.HideToolbar = true;

// To hide the viewer application's Menu bar
doc.ViewerPreferences.HideMenuBar = true;

// To hide the user interface elements such as Scroll bar, navigation controls
doc.ViewerPreferences.HideWindowUI = true
```

##### VB.NET
```vbnet
' To hide the viewer application's Tool bar
doc.ViewerPreferences.HideToolbar = True

' To hide the viewer application's Menu bar
doc.ViewerPreferences.HideMenuBar = True

' To hide the user interface elements such as Scroll bar, navigation controls
doc.ViewerPreferences.HideWindowUI = True
```

<!-- tags: [pdf, viewer-preference, settings, hide-toolbar, hide-menubar, hide-window-ui] keywords: [essential pdf, adobe reader, toolbar, menubar, window ui, properties, hidetoolbar, hidemenubar, hidewindowui] -->
```