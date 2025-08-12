```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: HTMLUI
page_number: 085
page_id: HTMLUI#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:47Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

The P tag is used to define a paragraph in the HTML document. HTMLUI supports the P tag along with its align attribute. The align attribute is used to specify the alignment of the text within the paragraph. The alignment values are as follows:

- **left**: Left-aligns the text
- **right**: Right-aligns the text
- **center**: Positions text at the center of the document
- **justify**: Left-aligns and right-aligns text

### HTML Example

```html
<html>
<body>
    <p align="left"><b>Essential Studio</b></p>
    <p align="justify">Essential Studio contains 10 .NET libraries. It has components ranging from a Grid control to a HTML display control. They are available for both Windows Forms and ASP.NET.</p>
</body>
</html>
```

### C# Example

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\paragraph\p.html");
```

### VB.NET Example

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\paragraph\p.html")
```

## 4.6.21 PRE - Preformatted Tag

The HTMLUI control renders preformatted texts written inside the `<pre>` tags. These texts are rendered with the fixed-pitch fonts and the control preserves the spaces and the line breaks used in the document.

### HTML Example

```html
<html>
<body>
    <pre>
        Evaluation Center:
        The Evaluation Center has online sample code and complete sample downloads to help you get started quickly.
    </pre>
</body>
</html>
```

<!-- tags: [syncfusion-sdk, HTMLUI, P tag, align attribute, Preformatted tag, WinForms] keywords: [essential studio, html, text alignment, fixed-pitch fonts, preformatted text, sample code, evaluation center, StartSave, MoveNext, PrintSetup] -->
```