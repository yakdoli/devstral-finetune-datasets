```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: HTMLUI
page_number: 115
page_id: HTMLUI#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:19Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
<body>
<p>This is a paragraph.</p>
<div>This is a division.</div>
<p>This is a new paragraph.</p>
</body>
```

### C#
```csharp
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\internal.html");
```

### VB.NET
```vbnet
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\internal.html")
```

## 4.13.1.3 External StyleSheet

The External style sheets contain style definitions in a separate .css file, for various HTML tags that are in the document. These styles are applied by linking the css file to the HTML document inside the Link tag. The Link tag should be placed in the head section of the HTML document as it contains the information about the cascading style sheet that is to be referred by this document.

### CSS
```css
/* FileName and location: C:\MyProjects\StyleSheets\styleSheet.css */

body {
    background-color: #da5f5;
    cursor: default;
}

p {
    color: Green;
}

div {
    color: Blue;
    font-family: Tahoma;
}
```

### HTML
```html
<!-- File name and location: C:\MyProjects\StyleSheets\external.html -->
```

## API Reference
- None specific to this section.

## Code Examples
### C#
```csharp
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\internal.html");
```

### VB.NET
```vbnet
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\internal.html")
```

```css
/* FileName and location: C:\MyProjects\StyleSheets\styleSheet.css */

body {
    background-color: #da5f5;
    cursor: default;
}

p {
    color: Green;
}

div {
    color: Blue;
    font-family: Tahoma;
}
```

## Conclusion
- Internal styles are defined within the HTML document itself.
- External styles are defined in a separate .css file and linked to the HTML document using the Link tag.

<!-- tags: [htmlui, windows forms, external stylesheet, internal stylesheet, winforms] keywords: [html, css, styles, cascading style sheet, link tag, style declaration, external stylesheet, internal stylesheet, htmlui] -->
```