```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: HTMLUI
page_number: 078
page_id: HTMLUI#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:40Z
fidelity: lossless
-->

## Overview
- This section discusses how to load and use HTML within Windows Forms using `htmluiControl` for header tags (`H1` to `H6`) and the horizontal rule tag (`HR`).
- Demonstrates loading external HTML files to display content with various header tags and horizontal rule styles.

## Content

### Header Tags: H1 to H6
#### Loading External HTML for Headers

[C#]
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\heading\head.html");
```

[VB.NET]
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\heading\head.html")
```

#### Explanation of Header Tags

The Header tags are defined as the h tags. These header tags are classified into six types based on the font size. HTMLUI control supports all the header tags ranging from h1 - the largest header to h6 - the smallest header.

#### HTML Code for Header Tags

[HTML]
```
File Location and Name: C:\MyProjects\header\h.html

<html>
    <body>
        <h1 align="center">Header 1</h1><br/>
        <h2 align="left">Header 2</h2><br/>
        <h3 align="justify">Header 3</h3><br/>
        <h4 align="right">Header 4</h4><br/>
        <h5>Header 5</h5><br/>
        <h6>Header 6</h6><br/>
    </body>
</html>
```

[C#]
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\header\h.html");
```

[VB.NET]
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\header\h.html")
```

### Horizontal Rule Tag (HR)

#### Horizontal Rule Tag Usage

The Horizontal Rule tag is used to draw an horizontal line in the document. The `<hr>` tag in HTMLUI supports the following attributes.

- **width**: Specifies the width of the line

---

## API Reference

### Namespaces and Classes
- **htmluiControl**: This class is used for rendering and displaying HTML content in Windows Forms.

### Methods
- **LoadHTML(string path)**: Loads and displays external HTML files within the control.

### Attributes Supported for `<hr>`
- **width**: Used to specify the width of the horizontal line.

## Code Examples

### Loading HTML Files

[C#]
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\header\h.html");
```

[VB.NET]
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\header\h.html")
```

### HTML Tags Example

[HTML]
```
<html>
    <body>
        <h1 align="center">Header 1</h1><br/>
        <h2 align="left">Header 2</h2><br/>
        <hr width="50%">
    </body>
</html>
```

### Horizontal Line HTML Example

[HTML]
```
<html>
    <body>
        <hr width="80%">
    </body>
</html>
```

---

## Cross References
- Refer to sections discussing `htmluiControl` for more details on integrating HTML controls in WinForms applications.

<!-- tags: [Syncfusion Winforms, HTMLUI, Header Tags, Horizontal Rule, htmluiControl] keywords: [header tags, H1, H6, horizontal rule, HR, width, external HTML, Windows Forms, htmluiControl] -->
```