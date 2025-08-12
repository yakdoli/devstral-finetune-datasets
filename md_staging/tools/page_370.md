```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_370.jpeg
document_name: tools
page_number: 370
page_id: tools#page_370
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Adjust text alignment and image placement on buttons.
- Control the relative location of images and text in buttons.
- Demonstrate code examples in both C# and VB.NET for configuring button properties.

## Content

### Button Child Property Adjustments

#### Properties and Descriptions

| Property          | Description                                      |
|-------------------|--------------------------------------------------|
| TextAlign         | Sets the alignment of the text in the child button control. |
| TextImageRelation | Sets the relative location of the image to the text in the button. |

---

#### Code Examples

##### C#

```csharp
this.buttonEditChildButton2.Image =
    ((System.Drawing.Image)(resources.GetObject("buttonEditChildButton2.Image")));
this.buttonEditChildButton2.ImageAlign =
    System.Drawing.ContentAlignment.MiddleLeft;
this.buttonEditChildButton2.Text = "Browse";
this.buttonEditChildButton2.TextAlign =
    System.Drawing.ContentAlignment.MiddleLeft;
this.buttonEditChildButton2.TextImageRelation =
    System.Windows.Forms.TextImageRelation.ImageBeforeText;
this.buttonEditChildButton2.PREFERREDWIDTH = 64;
```

##### VB.NET

```vb
Me.buttonEditChildButton2.Image =
    DirectCast((resources.GetObject("buttonEditChildButton2.Image")), System.Drawing.Image)
Me.buttonEditChildButton2.ImageAlign =
    System.Drawing.ContentAlignment.MiddleLeft
Me.buttonEditChildButton2.Text = "Browse"
Me.buttonEditChildButton2.TextAlign =
    System.Drawing.ContentAlignment.MiddleLeft
Me.buttonEditChildButton2.TextImageRelation =
    System.Windows.Forms.TextImageRelation.ImageBeforeText
Me.buttonEditChildButton2.PREFERREDWIDTH = 64
```

---

### Visual Representation

![](https://via.placeholder.com/300x200?text=Figure%20179:%20TextAlign%20=%20%22MiddleLeft%22;

#### Caption

Figure 179: TextAlign = "MiddleLeft"; ImageAlign = "MiddleLeft"; TextImageRelation = "ImageBeforeText"

---

### Flat Style for the Buttons

#### Properties and Descriptions

| Properties       | Description |
|------------------|-------------|
| Properties       | Description |

---

```html
<!-- tags: [WinForms, Button, TextAlignment, ImagePosition, Essentials, Tools] keywords: [TextAlign, TextImageRelation, ContentAlignment, ImageBeforeText, FlatStyle, ButtonChildProperty, CSharpExample, VBNetExample] -->
```