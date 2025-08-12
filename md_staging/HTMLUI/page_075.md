```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: HTMLUI
page_number: 075
page_id: HTMLUI#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:54Z
fidelity: lossless
-->


# Essential HTMLUI for Windows Forms

## Overview
- Explains the use of the `BODY` tag in HTML documents.
- Demonstrates how to render HTML content using `HTMLUI` control.
- Illustrates the `BR` tag for inserting line breaks in displayed documents.

## Content

### 4.6.6 BODY - Body Tag

The **Body** element defines the body of the HTML document. This is the parent element of all the HTML elements visible in the browser. The contents to be displayed in the HTMLUI control are placed inside the body tag. In HTMLUI, the body element is considered as the basis for all the elements present in the document. The following code snippet shows the use of a body element in rendering HTML documents in HTMLUI control.

```html
[HTML]

File Location and Name:  C:\MyProjects\body\bodyTag.html

<html>
    <body bgcolor="#ffffff">
        <p>Body tag holds the contents to be displayed in the browser.</p>
    </body>
</html>
```

```csharp
[C#]

this.htmluiControl.LoadHTML(@"C:\MyProjects\body\bodyTag.html");
```

```vbnet
[VB.NET]

Me.htmluiControl.LoadHTML(@"C:\MyProjects\body\bodyTag.html")
```

### 4.6.7 BR - Break Tag

The **Break** tag is used to insert a line break in the document displayed.

```html
[HTML]

File Location and Name:  C:\MyProjects\break\br.html

<html>
    <body>
        <p>This is the first line.</p><br/><p>This is the next line</p>
    </body>
</html>
```

```csharp
[C#]

this.htmluiControl.LoadHTML(@"C:\MyProjects\break\br.html");
```

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [BODY tag, HTMLUI, BR tag, line break, HTML rendering, Windows Forms, Syncfusion Winforms] -->
```