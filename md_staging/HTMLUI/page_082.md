```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: HTMLUI
page_number: 082
page_id: HTMLUI#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:02Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Describes the use of HTML Tags in Windows Forms applications.
- Focuses on the `<li>` and `<link>` tags for organizing list items and linking external resources.

## Content

### 4.6.16 LI - List Item Tag

The List Item tag defines a list item. The `<li>` tag is used inside the `<ol>` tag or `<ul>` tag to define each and every list item included inside them.

#### Code Example: HTML
```html
<html>
  <body>
    <ol>
      <li>Essential Tools</li>
      <li>Essential Chart</li>
      <li>Essential HTMLUI</li>
    </ol>
  </body>
</html>
```

#### File Location: 
```plaintext
C:\MyProjects\listItem\li.html
```

#### C# Code to Load HTML
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\listItem\li.html");
```

#### VB.NET Code to Load HTML
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\listItem\li.html")
```

### 4.6.17 LINK - Link Tag

The Link tag is used to link another document to the current HTML document. This tag is generally used to link an external CSS style sheet to the HTML document. The following attributes for the link tag are supported in the HTMLUI control:

- **rel**: Specifies the relationship between the two documents
- **type**: Specifies the type of the document to be linked, either text or image
- **href**: Specifies the location of the document to be linked to the current document

#### Code Example: HTML
```html
<html>
  <body>
    <!-- Link tag example -->
  </body>
</html>
```

#### File Location: 
```plaintext
C:\MyProjects\link\link.html
```

## API Reference

### Attributes of `<link>` Tag
- **rel**: Specifies the relationship between the two documents.
- **type**: Specifies the type of the document to be linked, either text or image.
- **href**: Specifies the location of the document to be linked to the current document.

## Code Examples

The examples above demonstrate how to use the `<li>` and `<link>` tags within a Windows Forms application.

## Cross References

See also:
- HTML Tags Fundamentals
- Working with Links in HTML

## RAG Annotations
<!-- tags: HTMLUI, Windows Forms, LI, Link, HTML Tags, Windows Forms Control, version: 11.4.0.26 -->
```