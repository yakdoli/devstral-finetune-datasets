```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: HTMLUI
page_number: 120
page_id: HTMLUI#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:55Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Explains the supported CSS attributes in HTMLUI.
- Describes how to use background properties including image and color for HTML elements.

## Content

### 4.13.2 Supported CSS Attributes

The following attributes are supported in HTMLUI for the cascading style sheet definition.

#### 4.13.2.1 Background - CSS

The background attribute of CSS helps the user to set the background properties for the specified element. The following are the background properties that are supported in HTMLUI for a HTML element using CSS.

##### 4.13.2.1.1 Background Image

The background-image property is used to set an image as the background of the HTML element.

```html
[HTML]

<html>
 <head>
  <style type="text/css">
   /* The url attribute gets the image from the specified location */
   body {
    background-image: url(stars.gif);
   }
  </style>
 </head>
 <body>
  <p>Image in the background.</p>
 </body>
</html>
```

##### 4.13.2.1.2 Background Color

The background-color property is used to set a background color for a HTML element.

```html
[HTML]

<html>
 <head>
  <style type="text/css">
   /* A background color is specified for the document */
   body {
    background-color: #dae5f5;
   }
  </style>
 </head>
 <body>
 </body>
</html>
```

---

```html
<!-- tags: [Syncfusion Winforms, HTMLUI, CSS, background image, background color, Windows Forms] keywords: [CSS attributes, HTML background properties, HTMLUI, cascading style sheet, background-image, background-color, HTML elements] -->
```