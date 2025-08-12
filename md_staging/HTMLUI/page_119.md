```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: HTMLUI
page_number: 119
page_id: HTMLUI#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:33Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

The ID Class Selectors are defined like the name class selectors. Instead of specifying names, a unique identity is specified for the styles while defining them, and these style names are passed as the values of the `id` attribute to the concerned HTML elements.

## Content

### HTML

File name and location: C:\MyProjects\StyleSheets\idClass.html

```html
<html>
<head>
    <style>
        #red { color: red; }
        #blue { color: blue; }
    </style>
</head>
<body>
    <h1 id="red">Red Heading</h1>
    <p id="blue">Blue colored paragraph.</p>
</body>
</html>
```

### C#

```csharp
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\idClass.html");
```

### VB.NET

```vb
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\idClass.html")
```

## 4.13.1.5 CSS Comments

The HTMLUI control supports comments inside the cascading style sheet. The comments help the developer to explain his ideas behind the styles and also help the user to understand the functionality of the styles. A CSS comment begins with `/*` and ends with `*/` (For eg., `/* This is a comment */`). The comments are not visible in the browser at run time.

### CSS

```
/* blue colored font for the p elements */
p { color: blue; }

/* red colored font for the div elements */
div { color: red; }
```

## Page-level Navigation/TOC

Not applicable in this context.

## Cross References

Not applicable in this context.

## RAG Annotations

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```