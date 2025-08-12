```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: HTMLUI
page_number: 074
page_id: HTMLUI#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:27Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\Comment\comment.html");
```

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\Comment\comment.html")
```

## 4.6.5 Font Style Tags

The Font Style tags are used to format the appearance of the specified text when rendered in HTMLUI. The following are the font style tags supported in HTMLUI:

- `<b>`: Bold tag renders the text in bold face
- `<i>`: Italics tag renders italicized text
- `<u>`: Underline tag renders underlined text
- `<em>`: Emphasizing Text tag highlights important text in the document
- `<strong>`: Strong tag renders specified text in bold face
- `<code>`: Code tag renders specified text similar to computer-coded text

```html
[HTML]

File Location and Name: C:\MyProjects\FontStyle\fontStyle.html

<html>
<body>
    <b>bold text</b><br />
    <i>italic text</i><br />
    <u>Underlined text</u><br />
    <em>Emphasized Text</em><br />
    <strong>Strong Text</strong><br />
    <code>Computer coded text</code>
</body>
</html>
```

```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\FontStyle\fontStyle.html");
```

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\FontStyle\fontStyle.html")
```

<!-- tags: [Syncfusion, HTMLUI, WinForms, font style tags, bold, italics, underline, emphasis, strong, code tag] keywords: [font formatting, text rendering, HTMLUI in Windows Forms] -->
```