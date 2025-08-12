<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_122.jpeg
document_name: HTMLUI
page_number: 122
page_id: HTMLUI#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:30Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
p { color: blue }
</style>
</head>
<body>
<h1>Text - HTMLUI - CSS</h1>
<p>This is a paragraph</p>
</body>
</html>
```

## Text Align

The `text-align` attribute is used to align the text inside an element to the specified horizontal direction.

```html
[HTML]

<html>
<head>
<style type="text/css">p { text-align: center }</style>
</head>
<body>
<p>Center aligned paragraph</p>
</body>
</html>
```

## Text Decoration

The `text-decoration` attribute is used to decorate a text. The HTMLUI control supports the `Underline` and the `None` style values for the text decoration attribute.

```html
[HTML]

<html><head>
<style type="text/css">.five:hover { text-decoration: underline } </style>
</head>
<body>
<p>Mouse over the links to see them change layout.</p>
</body></html>
```

### Font – CSS

The `font` attribute is used to define the font specification for a HTML element in the HTMLUI. With the CSS font specification, the user can create good presentation applications in HTMLUI.

## API Reference

Namespace: Syncfusion.Windows.Forms.HtmlUI

Class: HTMLUIControl

### Members

#### Properties

- **Font**: Specifies the font used to render the text.

## Code Examples

```csharp
using Syncfusion.Windows.Forms.HtmlUI;
using Syncfusion.Drawing;

HTMLUIControl htmluiControl = new HTMLUIControl();
htmluiControl.HtmlText = "<p style='font-family: Arial; font-size: 16px;'>Styled text</p>";
```

<!-- tags: [HTMLUI, Windows Forms, CSS, Text Alignment, Text Decoration, Font Specification, Syncfusion, Windows Forms, HTMLUIControl, Font, Text formatting] keywords: [text-align, text-decoration, font-family, font-size, HTMLUI, CSS, alignment, decoration, styling, rendering, Windows Forms, C# sample] -->