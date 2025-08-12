```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_112.jpeg
document_name: HTMLUI
page_number: 112
page_id: HTMLUI#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:26Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates a sample showing the usage of the HTMLUIEditor control.
- Explains the integration and functionality of the HTMLUIEditor sample in Windows Forms.
- Highlights the support for style sheets in HTMLUI, enabling the definition and application of CSS styles.

## Content

### HTMLUI Editor Sample
**Figure 39: HTMLUIEditor Sample**

By default, this sample can be found under the following location:
```
C:\Documents and Settings\username\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\Samples\2.0\HTML Renderer\HTMLUIEditor
```

### 4.13 Style Sheets CSS

The support for style sheets is enabled in HTMLUI. This lets the user define styles for HTML elements and decide the appearance of the HTML elements in the application. HTMLUI supports three types of style sheets.

- **External Style sheets**
- **Internal Style sheets**
- **Inline Style sheets**

## API Reference (if applicable)
- Detailed methods, properties, and events related to HTMLUI and style sheet integration.

## Code Examples (multi-language supported)
- The provided HTML code snippet demonstrates the application of style sheets within the HTMLUIEditor sample:
```html
<html>
<head>
    <title>Products Document</title>
    <style>
        body {
            font-family: Arial;
            font-size: 12;
        }
        products {
            font-family: Tahoma;
            font-weight: bold;
        }
    </style>
</head>
<body bgcolor="#ffffff">
    <product>Essential Tools</product><br />
    <description>Collection of great user interface
    controls including XP style controls and docking windows.
    </description><p />
</body>
</html>
```

## Page-level Navigation/TOC (if applicable)
- Organized content hierarchy within the document.

## Cross References
- See also: Chapters and sections in the user guide related to HTMLUI and CSS integration.

## RAG Annotations
<!-- tags: [HTMLUI, Windows Forms, HTMLUIEditor, style sheets, CSS, External Style sheets, Internal Style sheets, Inline Style sheets, sample location] keywords: [Essential Tools, XP style controls, docking windows, HTMLUIEditor, style sheets, CSS support, design-time, runtime] -->
```