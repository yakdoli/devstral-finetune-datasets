```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: HTMLUI
page_number: 079
page_id: HTMLUI#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:07Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- **size:** Specifies the thickness or height of the line
- **noshade:** Renders the specified line in a solid color

### HTML
File Location and Name: `C:\MyProjects\HorizRule\rule.html`

```html
<html>
    <body>
        <p>Syncfusion</p>
        <hr width="100" size="10" noshade />
        <p>Essential Studio</p>
    </body>
</html>
```

### C#
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\HorizRule\rule.html");
```

### VB.NET
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\HorizRule\rule.html")
```

## 4.6.13 HTML - HTML Tag

The `HTML` tag specifies that the document to be loaded in the HTMLUI control is an HTML document. This tag contains the `head` and the `body` elements as its child elements.

### HTML
File Location and Name: `C:\MyProjects\HTML\htmlElement.html`

```html
<html>
    <head>
        <title>New html document</title>
    </head>
    <body>
        <p>The HTML tag contains the head and the body elements as its child element.</p>
    </body>
</html>
```

### C#
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\HTML\htmlElement.html");
```

### VB.NET
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\HTML\htmlElement.html")
```

## API Reference

### Notes
1. The `LoadHTML` method is used to load HTML content into the HTMLUI control.
2. The `head` and `body` elements are essential parts of the HTML structure.

## Code Examples

### C#
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\HTML\htmlElement.html");
```

### VB.NET
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\HTML\htmlElement.html")
```

<!-- tags: [HTMLUI, Windows Forms, Essential Studio, HTML Tag, LoadHTML, Syncfusion, version 11.4.0.26] keywords: [HTML document, head, body, child elements, HTMLUI control, size, noshade, document structure, Syncfusion WinForms] -->
```