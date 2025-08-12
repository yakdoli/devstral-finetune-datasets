```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: HTMLUI
page_number: 131
page_id: HTMLUI#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:10Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates methods of changing the background color in HTMLUI control.
- Provides examples using different approaches: body attribute, internal style, and external CSS.

## Content

The following HTML coding shows the different methods of changing the background color that HTMLUI control supports, leaving it to the user to choose the best among the various options as per the requirements.

```html
[HTML]
<html>
    <head>
        <link type="text/css" rel="stylesheet" href="backgroundColor.CSS"></link>
        <style>
            .div{background-color: #ffffcc;}
        </style>
    </head>
    <body bgcolor="#dae5f5">
        <p style="background-color: #ffffff;">Background color changed through the style attribute</p>
    </body>
</html>
```

The following figure shows the backcolor of the HTML document customized by using HTMLUI.

![Figure 42: Background Color of the HTML document customized by using the HTMLUI Control](attachment:HTMLUIPage131Figure42.png)

**Figure 42: Background Color of the HTML document customized by using the HTMLUI Control**

### 4.14.1 HTMLUIAppearance Sample

This sample illustrates the customization of HTMLUI Appearance.

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.HTMLUI
- **Class**: HTMLUI

## Code Examples (if applicable)
- This page contains sample HTML code demonstrating background color changes using various methods.

## Page-level Navigation/TOC (if applicable)
- Section: Essential HTMLUI for Windows Forms
- Subsection: 4.14.1 HTMLUIAppearance Sample

## Cross References
- Refer to the HTMLUI documentation for additional examples and detailed information.

<!-- tags: [product, module, control, api, version] keywords: [HTMLUI, background color, appearance, customization, Windows Forms, Syncfusion, version 11.4.0.26] -->
```