```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_128.jpeg
document_name: HTMLUI
page_number: 128
page_id: HTMLUI#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:22Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## 4.13.2.9 Pseudo - Classes

The Pseudo-Classes are used to add special effects to the HTML hyperlink element display. For understanding this case clearly in HTMLUI, let us define a general case, where the link should change its appearance when a mouse pointer is moved over it.

The HTMLUI control supports the link and the hover classes in order to display the links in the HTMLUI control.

- **link:** Specifies the properties for the display of a hyperlink in the normal state.
- **hover:** Specifies the CSS properties for the hyperlink when a mouse is moved over the link

The following sample shows how different properties can be set for the hyperlink element by using the pseudo-classes.

```html
<html>
<head>
<style type="text/css">
.ChangeColor:link { color: #ff0000 }
.ChangeColor:hover { color: #ffcc00 }

.ChangeFont:link { color: #ff0000 }
.ChangeFont:hover { font-size: 150%; font-family: Tahoma }

.ChangeBcolor:link { color: #ff0000 }
.ChangeBcolor:hover { background-color: #66ff66 }

.ChangeTextDec:link { color: #ff0000; text-decoration: none }
.ChangeTextDec:hover { text-decoration: underline }
</style>
</head>
<body>
<a class="ChangeColor" href="none.htm" target="_blank">This link changes color</a><br />
<a class="ChangeFont" href="none.htm" target="_blank">This link changes font</a><br />
<a class="ChangeBcolor" href="none.htm" target="_blank">This link changes background-color</a><br />
<a class="ChangeTextDec" href="none.htm" target="_blank">This link changes text-decoration</a><br />
</body>
</html>
```

## HTMLUIUseCSS Sample

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations

<!-- tags: [product, module, control, api, version] keywords: [HTMLUI, Pseudo Classes, CSS, Windows Forms, Hyperlink Effects, Link, Hover, Color, Font, Background, Text Decoration] -->
```