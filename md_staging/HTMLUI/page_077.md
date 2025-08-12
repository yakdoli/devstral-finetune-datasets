```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: HTMLUI
page_number: 077
page_id: HTMLUI#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:20Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

File Location and Name: `C:\MyProjects\UserInput\form.html`

```html
<html>
    <body>
        <form>
            <input type="text" /><br />
            <input type="submit" /><br />
            <input type="radio" /><br />
            <input type="checkbox" /><br />
        </form>
    </body>
</html>
```

## C#

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\UserInput\form.html");
```

## VB.NET

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\UserInput\form.html")
```

### 4.6.10 HEAD - Head Tag

The **Head** element contains the information required for processing the document. The contents of the head tag will not be displayed in the HTMLUI control. The HTMLUI control receives information only through the head element. The following are the information obtained:

- **Link reference to the style sheets by using the Link tag of the head section**
- **Styles to the html elements by using the Style tag of the head section**
- **Title for the document in the Title tag of the head section**

#### [HTML]

File Location and Name: `C:\MyProjects\heading\head.html`

```html
<html>
    <head>
        <link href="style.css" rel="stylesheet" type="text/css" />
        <style>p{“background-color: #dae5f5;”}</style>
        <title>Head section</title>
    </head>
    <body>
        <p>The head contains the title for the document</p>
    </body>
</html>
```

---

<!-- tags: [Syncfusion Winforms, HTMLUI, Head Tag, Essential HTMLUI] keywords: [Windows Forms, HTML, C#, VB.NET, Head element, Link reference, Styles, Title, Document processing, UI control, version 11.4.0.26] -->
```