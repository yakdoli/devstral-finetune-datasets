```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_114.jpeg
document_name: HTMLUI
page_number: 114
page_id: HTMLUI#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:01Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Content

### 4.13.1.1 Inline StyleSheet

**Overview**
- The Inline style sheet is applied directly within an HTML tag as an attribute named `Style`. This allows specific styles to be defined for the content of that tag.
- An example demonstrates how an inline style is applied to an HTML element within the document.

#### Example Code

**HTML**
```html
[HTML]

File name and location: C:\MyProjects\StyleSheets\inline.html
<html>
<body>
<p style="background-color: #dae5f5;">Inline style applied to a paragraph.</p>
</body>
</html>
```

**C#**
```csharp
[C#]
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\inline.html");
```

**VB.NET**
```vbnet
[VB.NET]
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\inline.html")
```

### 4.13.1.2 Internal StyleSheet

**Overview**
- The Internal style sheet allows the definition of styles that apply to all occurrences of a specific tag within the document.
- This style sheet is defined inside a `style` tag, typically placed in the `head` section of the document.
- An example illustrates the definition of an internal style sheet for specific tags (`p` and `div`) in an HTML document.

#### Example Code

**HTML**
```html
[HTML]

File name and location: C:\MyProjects\StyleSheets\internal.html
<html>
<head>
<style type="text/css">
p { color: blue }
div { color: red }
</style>
</head>
```

## API Reference
- **htmluiControl.LoadHTML**
  - Loads the HTML content from the specified file path into the HTMLUI control.
  - Parameters:
    - `filePath`: The path to the HTML file to load.

## Code Examples
- The examples provided demonstrate how to apply inline and internal styles within an HTML document and load this document into a `.NET` application using `htmluiControl`.

## Cross References
- Refer to the documentation on how to use the `htmluiControl` for more details on loading and manipulating HTML content.

<!-- tags: HTMLUI, StyleSheet, InlineStyleSheet, InternalStyleSheet, WinForms, htmluiControl, Syncfusion, 11.4.0.26
keywords: inline style, internal style, HTML tag, style attribute, style sheet, WinForms, .NET, C#, VB.NET, CSS, HTMLUI -->
```