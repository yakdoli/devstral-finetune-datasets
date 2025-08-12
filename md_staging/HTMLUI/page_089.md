```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: HTMLUI
page_number: 089
page_id: HTMLUI#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:59Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Method 1: By specifying the Tag Names

Specifies styles by writing CSS styles with the tag name inside the Style tag.

```html
[HTML]

<style>
p { color: red; }
</style>
<p>Sample</p>
```

### Method 2: By specifying the Class Names to the Styles

Specifies styles with the help of the class names inside the Style tag.

```html
[HTML]

<style>
span { color: green; }
</style>
<span class="span">Sample</span>
```

### Method 3: By specifying ID Class Selectors

Specifies styles by writing styles with the unique id inside the Style tag, and assigning them to the HTML elements by using the `id` attribute.

```html
[HTML]

<style>
#divide { color: blue; }
</style>
<div id="divide">Sample</div>
```

### Style Tag Type Attribute

The `style` tag in HTMLUI also supports the `type` attribute. The type attribute is optional and it specifies the type of the content in the HTML document.

```html
[HTML]

File Location and Name: C:\MyProjects\style\style.html

<html>
<head>
    <style type="text/css">
        p { color: red; }
        .span { color: blue; }
        #bluebg { background-color: #dae5f5; background-repeat: repeat-x; }
    </style>
</head>
<body id="bluebg">
    <p>100% .NET HTML display engine that can be used to create extremely flexible user interfaces. Part of <span class="span">Essential Studio</span> Enterprise.</p>
</body>
</html>
```

### Summary Footer
© 2013 Syncfusion. All rights reserved. | Page 89
``` 

<!-- tags: [syncfusion-sdk, windows-forms, html, style-tag, essential-studio, version:11.4.0.26] keywords: [HTMLUI, Windows Forms, CSS styles, tag names, class names, ID selectors, type attribute, style tag, .NET HTML display engine, Essential Studio Enterprise] -->
```