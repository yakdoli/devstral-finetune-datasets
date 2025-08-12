```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: HTMLUI
page_number: 118
page_id: HTMLUI#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:16Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- This section explains the use of class selectors in HTMLUI for defining styles in Windows Forms.
- Internal and external styles can be applied using the class selectors, which define styles under a common class name.
- The section covers both Name Class Selectors and ID Class Selectors.

## Content

### 4.13.1.4 Class Selectors

Internal and external styles are not only defined by mentioning the names of the tags, but also by the Style Class Selectors. The class selectors are used to define the styles under a common class name and apply the styles to different tags by specifying the name of the class as the value of the class attribute, for the specific element.

HTMLUI supports two types of styles definitions for the HTML documents with the help of the class selectors as given below:

#### 4.13.1.4.1 Name Class Selectors

The Name Class Selectors contain a common name that is given to the style class, which is defined in the internal or external css file. The following snippet shows how the name class selectors are defined for html elements in the document.

```html
[HTML]

File name and location: C:\MyProjects\StyleSheets\NameClass.html

<html>
<head>
    <style>
        .red { color: red }
        .blue { color: blue }
    </style>
</head>
<body>
    <h1 class="red">Red Heading</h1>
    <p class="blue">Blue colored paragraph.</p>
</body>
</html>
```

```csharp
[C#]

htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\NameClass.html");
```

```vbnet
[VB.NET]

htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\NameClass.html")
```

#### 4.13.1.4.2 ID Class Selectors

``` 

<!-- tags: [htmlui, windows forms, class selectors, styles, name class selectors, id class selectors, syncfusion w Informations. финансов, typescript.unions, winforms, syncfusion sdk