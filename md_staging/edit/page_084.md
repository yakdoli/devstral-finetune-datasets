```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: edit
page_number: 084
page_id: edit#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:02Z
fidelity: lossless
-->

### Essential Edit for Windows Forms

| Edit Control Property           | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| HighlightCurrentLine            | Gets / sets value indicating whether current line should be highlighted. |
| CurrentLineHighlightColor       | Gets / sets color of current line highlight.                          |

#### Code Examples

**[C#]**

```csharp
this.editControl1.HighlightCurrentLine = true;
this.editControl1.CurrentLineHighlightColor = Color.Orange;
```

**[VB.NET]**

```vb
Me.editControl1.HighlightCurrentLine = True
Me.editControl1.CurrentLineHighlightColor = Color.Orange
```

![CurrentLineHighlightColor = "Orange"](image.png)

**Figure 23: CurrentLineHighlightColor = "Orange"**

You can also highlight the selected text by using the Text Highlighting feature discussed in Background Settings.

---

### 4.4.8 Bookmarks and Custom Indicators

Essential Edit enables users to locate a section or a line of a document by using the Bookmarks and Custom Indicators feature like in Visual Studio. This provides quick access to any part of the contents of the Edit Control.

The Edit Control allows any number of custom images or bookmarks to be added to a document.

---

<!-- tags: [Syncfusion Winforms, bookmarks, custom indicators, highlight current line, edit control, text highlighting] keywords: [Essential Edit, Windows Forms, current line highlighting, bookmarks, custom indicators, document, features, text highlighting, navigation, line access, user guide] -->
```