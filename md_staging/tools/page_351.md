```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_351.jpeg
document_name: tools
page_number: 351
page_id: tools#page_351
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- This page explains how to configure image settings for the `ButtonAdv` control in Windows Forms.
- It provides guidance on setting properties such as `Image`, `ImageAlign`, `ImageIndex`, and `ImageList`.
- Demonstrates code snippets in both C# and VB.NET for configuring the button's image alignment and settings.

## Content

### Image Settings Configuration

The following screenshot illustrates the image settings for a `ButtonAdv` control.

![Figure 162: Image Settings For ButtonAdv](Untitled.png)

#### Properties Overview
- **FlatStyle**: Standard
- **Font**: Verdana, 8.25pt
- **ForeColor**: PowderBlue
- **Image**: `System.Drawing.Bitmap`
- **ImageAlign**: TopLeft
- **ImageIndex**: 0
- **ImageList**: imageList1
- **RightToLeft**: No
- **Text**: None
- **TextAlign**: TopCenter
- **TextImageRelation**: ImageBeforeText

#### Note
The image settings will be effective only when `ButtonType` is set to Normal.

### Code Examples

#### C#

```csharp
this.btnAlignment.Image = 
    (System.Drawing.Bitmap)(resources.GetObject("btnAlignment.Image"));
this.btnAlignment.ImageAlign = 
    System.Drawing.ContentAlignment.MiddleLeft;
this.btnAlignment.ImageIndex = 3;
this.btnAlignment.ImageList = this.imageList1;
```

#### VB.NET

```vb
Me.btnAlignment.Image = 
    CType(resources.GetObject("btnAlignment.Image"), System.Drawing.Bitmap)
Me.btnAlignment.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
Me.btnAlignment.ImageIndex = 3
Me.btnAlignment.ImageList = Me.imageList1
```

## API Reference

### Properties

| Property           | Type                          | Description |
|--------------------|-------------------------------|-------------|
| `Image`           | `System.Drawing.Bitmap`       | Specifies the image to be displayed on the button. |
| `ImageAlign`      | `System.Drawing.ContentAlignment`  | Specifies the alignment of the image relative to the text in the button. |
| `ImageIndex`      | `int`                         | Specifies the index of the image to be displayed from the `ImageList`. |
| `ImageList`       | `System.Windows.Forms.ImageList` | The `ImageList` that contains the images to be displayed. |

### Methods

The `ButtonAdv` control includes methods for dynamically setting and retrieving settings, such as `SetImage` and `GetImage`.

### Events

- **Paint**: Triggered when the control is redrawn.
- **Click**: Triggered when the button is clicked.

## Code Examples (Revisited)

The snippets provided demonstrate how to programmatically set the image properties of a `ButtonAdv` control, including alignment, index, and list. These examples are applicable in both a designer setting and dynamically at runtime.

### Tips

- Always ensure that the `ButtonAdv` control has a valid `ImageList` assigned if you are using the `ImageIndex` property.
- Adjust `ImageAlign` to achieve the desired visual presentation of images and text on the button.

## Page-level Navigation/TOC

- [Image Settings Configuration]
  - [Properties Overview]
  - [Note]
- [Code Examples]
  - [C#]
  - [VB.NET]
- [API Reference]
  - [Properties]
  - [Methods]
  - [Events]
- [Code Examples (Revisited)]
- [Tips]

## Cross References

- See also: [Custom Button Appearance](other-link-in-document)
- See also: [ImageList Management](other-link-in-document)

<!-- tags: [syncfusion, winforms, buttonadv, image setting, c#, vb.net] keywords: [image alignment, image index, image list, buttonadv properties, code snippets, windows forms] -->
```