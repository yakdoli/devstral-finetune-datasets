```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_443.jpeg
document_name: grid
page_number: 443
page_id: grid#page_443
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
The page discusses the "BackgroundImage" property of the Essential Grid for Windows Forms. It explains how to insert a background image for the grid and provides code examples in both C# and VB.NET for setting this property.

## Content

### BackgroundImage - Enables to insert a background image for the grid.

The following code examples can be used to set this property:

1. **Using C#**

   ```csharp
   // Specify the background image.
   this.gridControl1.BackgroundImage =
       Image.FromFile(FindImageFile(@"...\..\..\pic.jpg"));
   ```

2. **Using VB.NET**

   ```vb.net
   ' Specify the background image.
   Me.gridControl1.BackgroundImage =
       Image.FromFile(FindImageFile("...\..\..\pic.jpg"))
   ```

The following illustration shows how the Grid in "Figure 1" is transformed when the `BackgroundImage` property is set.

![Grid with Line Color set to Red](#)

- This figure demonstrates the grid with its line color set to red, serving as an illustrative example.

## API Reference

- `BackgroundImage` property: This property allows you to insert a background image for the grid. The examples in C# and VB.NET demonstrate how to set this property.

## Code Examples

- **C# Example**
  ```csharp
  // Specify the background image.
  this.gridControl1.BackgroundImage =
      Image.FromFile(FindImageFile(@"...\..\..\pic.jpg"));
  ```

- **VB.NET Example**
  ```vb.net
  ' Specify the background image.
  Me.gridControl1.BackgroundImage =
      Image.FromFile(FindImageFile("...\..\..\pic.jpg"))
  ```

## Page-level Navigation/TOC (if applicable)
This page focuses on the `BackgroundImage` property of the Essential Grid for Windows Forms, providing code examples in C# and VB.NET for setting it. It also includes an illustration to demonstrate the effect of setting this property.

<!-- tags: [Essential Grid, Windows Forms, BackgroundImage, C#, VB.NET] keywords: [Syncfusion, grid, background image, C#, VB.NET, code examples, Windows Forms] -->
```