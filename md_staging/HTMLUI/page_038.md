```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: HTMLUI
page_number: 038
page_id: HTMLUI#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:20Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Loading specified HTML documents containing links to other documents.
- Demonstrating file links in an HTML document.
- Illustrating file links that link to another HTML document.

## Content

### Loading HTML Documents

#### C#
```csharp
// Load the specified HTML Document that contains link for another document.
string filePath = @"C:\MyProjects\LoadHTML/Main.htm";
this.htmluiControl.LoadHTML(filePath);
```

#### VB.NET
```vb.net
' Load the specified HTML Document that contains link for another document.
Private filePath As String = "C:\MyProjects\LoadHTML/Main.htm"
Me.HtmluiControl1.LoadHTML(filePath)
```

### HTML Code

#### HTML Document with File Links

An HTML document containing file links is illustrated by the code given below:

```html
[HTML]

<HTML>
<HEAD>
<title>FILE LINK</title>
</HEAD>
<body bgColor="#ffffff">
<P>THIS FORM IS A SAMPLE TO SHOW FILE LINKS</P>
<FONT color="#66ffff" size="6">
<A href="MODEL1.htm">To link1</a>
</FONT>
<p>
<FONT color="#66ffff" size="6">
<A href="MODEL2.htm">To link2</a>
</FONT>
</p>
</body>
</HTML>
```

#### Output

The following image shows file links that link to another HTML Document.

*Image description: An HTML document displaying file links to separate HTML documents.*

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [HTMLUI, Windows Forms, HTML, file links, document link, C#, VB.NET, Syncfusion] -->
```