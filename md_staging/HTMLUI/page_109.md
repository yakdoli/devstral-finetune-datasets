```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: HTMLUI
page_number: 109
page_id: HTMLUI#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:03Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Overview
- The HTMLUI control facilitates the rendering of web pages, offering the functionality of a lightweight web browser.
- It is suitable for compact applications with links to references.
- The ability to load from strings enables the creation of HTML editors for tutorial applications.

### Content

#### Loading HTML from a URI
The HTMLUI control can load HTML documents from a `System.Uri` and render them, providing a lightweight web browsing experience.

**C#**
```csharp
// Load the specified HTML document from System.Uri in to HTMLUI Control and renders it.
string path = "http://www.Google.com";
Uri uri = new Uri(path);
htmluiControl1.LoadHTML(uri);
```

**VB.NET**
```vb
' Load the specified HTML document from System.Uri in to HTMLUI Control and renders it.
Private path As String = "http://www.Google.com"
Private uri As Uri = New Uri(path)
HtmluiControl1.LoadHTML(uri)
```

#### Loading HTML from a String
The HTMLUI control's capability to load HTML from strings is useful for creating HTML editors for educational or instructional purposes.

**C#**
```csharp
// Load HTML Document from String.
string htmlString = "<HTML>
<BODY> Document loaded through the LoadFromString method </BODY>
</HTML>";
this.htmluiControl1.LoadFromString(htmlString);
```

**VB.NET**
```vb
Private htmlString As String = "<HTML>
<BODY>Document loaded through the LoadFromString method</BODY>
</HTML>"
Me.HtmluiControl1.LoadFromString(htmlString)
```

#### HTML Editor Demonstration
The following figure depicts an HTML Editor rendered using HTMLUI.

```markdown
The following figure shows an HTML Editor rendered using HTMLUI.
```

## Conclusion
The HTMLUI control provides versatile functionality, supporting both web page rendering and HTML editing capabilities, making it a valuable tool for building interactive and educational applications within Windows Forms.

## Page-level Navigation/TOC
- Essential HTMLUI for Windows Forms
  - Loading HTML from a URI
  - Loading HTML from a String
  - HTML Editor Demonstration

## Cross References
- See also: Web page rendering, HTML editors, tutorial applications.

### RAG Annotations
<!-- tags: HTMLUI, Windows Forms, Web page rendering, HTML editors, tutorial applications. keywords: Essential HTMLUI, System.Uri, LoadHTML, LoadString, HTML Editor, Windows Forms, Syncfusion -->
```