```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_648.jpeg
document_name: tools
page_number: 648
page_id: tools#page_648
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:03Z
fidelity: lossless
-->

## Overview
- This page explains how to set a background image for the GradientPanel control in Windows Forms using C# and VB.NET.
- It provides an example using the `BackgroundImage` and `BackgroundImageLayout` properties.
- The layout of the background image is demonstrated using the `Stretch` option, ensuring it fits the panel.

## Content

### Image Settings
Background image for the GradientPanel control is set using the following properties:

| GradientPanel Properties      | Description                                                                          |
|-------------------------------|--------------------------------------------------------------------------------------|
| `BackgroundImage`             | Sets the background image for the control.                                          |
| `BackgroundImageLayout`       | Specifies the layout of the image.                                                  |

#### Code Examples

##### [C#]
```csharp
this.gradientPanel1.BackgroundImage =
    ((System.Drawing.Image)(resources.GetObject("gradientPanel1.BackgroundImage")));
this.gradientPanel1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
```

##### [VB.NET]
```vbnet
Me.gradientPanel1.BackgroundImage = CType((resources.GetObject("gradientPanel1.BackgroundImage")), System.Drawing.Image)
Me.gradientPanel1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
```

### Visual Example
![Figure 398: Background Image for GradientPanel](https://i.imgur.com/SampleImage.png)
*Figure 398: Background Image for GradientPanel*

### See Also
- [Border Settings](Border Settings)
- [3.5.6.2.4.2 Border Settings](3.5.6.2.4.2 Border Settings)

## Page-level Navigation/TOC (if applicable)
- [Image Settings](#image-settings)
- [C# Example](#c-example)
- [VB.NET Example](#vbnet-example)
- [Visual Example](#visual-example)
- [See Also](#see-also)

### RAG Annotations
<!-- tags: [Windows Forms, GradientPanel, BackgroundImage, ImageLayout, Stretch, C#, VB.NET] keywords: [GradientPanel, BackgroundImage, ImageLayout, Stretch, C#, VB.NET, Windows Forms] -->
```