```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: HTMLUI
page_number: 073
page_id: HTMLUI#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:01Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview

- Implementation of the HTMLUI control in Windows Forms applications.
- Support for HTML tags such as `abbr` and `comment`.
- Integration of tooltip functionality via the `title` attribute.

## Content

### 4.6.3 Acronym Tag

The Acronym tag is used to define the start of an acronym. The HTMLUI control supports the acronym tag, which helps in providing useful tips to the users when marked up. The `title` attribute is used to provide a tooltip text when the mouse pointer moves over the acronym.

```html
[HTML]

File Location and Name:  C:\MyProjects\Acronym\acronym.html

<html>
 <body>
     <abbr title="World Wide Web">WWW</abbr>
 </body>
</html>
```

```csharp
[C#]

this.htmluiControl.LoadHTML(@"C:\MyProjects\Acronym\acronym.html");
```

```vb.net
[VB.NET]

Me.htmluiControl.LoadHTML(@"C:\MyProjects\Acronym\acronym.html")
```

### 4.6.4 Comment Tag

HTMLUI control supports the use of HTML Comment tags while developing applications. The `Comment` tag is used to include a brief description by the developer, which helps the user to understand the code and also helps to edit the code at a later date. Normally the content inside the comment is ignored by the HTMLUI control.

```html
[HTML]

File Location and Name:  C:\MyProjects\Comment\comment.html

<html>
 <body>
 <!-- This is a HTML comment -->
 <p>HTMLUI supports HTML commenting</p>
 </body>
</html>
```

## API Reference

- **LoadHTML**: Method to load HTML content into the HTMLUI control.
  - **Parameters**:
    - `filePath`: String specifying the path to the HTML file.
  - **Usage**: `Me.htmluiControl.LoadHTML(@"C:\MyProjects\Comment\comment.html")`

## Code Examples

- **Loading HTML with Acronym Tag**:
  ```csharp
  this.htmluiControl.LoadHTML(@"C:\MyProjects\Acronym\acronym.html");
  ```
- **Using Comment Tag**:
  ```csharp
  this.htmluiControl.LoadHTML(@"C:\MyProjects\Comment\comment.html");
  ```

## Cross References

- Refer to the HTMLUI documentation for details on supported HTML tags and attributes.
- For more information on tooltips and accessibility, see the Tooltip documentation.

## RAG Annotations

<!-- tags: [product, HTMLUI, Windows Forms, Acronym Tag, Comment Tag] keywords: [HTMLUI, Windows Forms, acronym, comment, tooltip, title, HTML tags, accessibility] -->
```