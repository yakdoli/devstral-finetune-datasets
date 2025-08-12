```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_452.jpeg
document_name: grid
page_number: 452
page_id: grid#page_452
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:43Z
fidelity: lossless
-->

## Overview
This page discusses the features and properties associated with enabling scrolling for grids in Syncfusion Winforms. It specifically focuses on the `HSscrollPixel` and `VscrollPixel` properties, which control horizontal and vertical pixel scrolling, respectively.

## Content

### Scroll Bars in Grid
The figure below illustrates a grid with horizontal and vertical scroll bars.

![Grid with Horizontal and Vertical Scroll Bars](#)

**Figure 172: Grid with Horizontal and Vertical Scroll Bars**

The following properties are associated with scrolling in the grid.

### Horizontal Scroll Pixel Property (`HSscrollPixel`)
- **Description:** Specifies whether to enable/disable horizontal pixel scrolling for the grid.
- **Default Value:** `false`.
- **Code Examples:**

#### 1. Using C#
```csharp
// Enable horizontal pixel scrolling for the grid.
this.gridControl1.HScrollPixel = true;
```

#### 2. Using VB.NET
```vb.net
' Enable horizontal pixel scrolling for the grid.
Me.gridControl1.HScrollPixel = True
```

### Vertical Scroll Pixel Property (`VscrollPixel`)
- **Description:** Specifies whether to enable/disable vertical pixel scrolling for the grid.
- **Default Value:** `false`.

## Summary
This section explains how to manage scrolling in a grid control using the `HSscrollPixel` and `VscrollPixel` properties in both C# and VB.NET, providing the necessary code examples for implementation.

## API Reference
- **Namespace:** `Syncfusion.Windows.Forms`
- **Property:** `HSscrollPixel`
  - **Type:** `bool`
  - **Description:** Enables or disables horizontal pixel scrolling for the grid.
  - **Default:** `false`
- **Property:** `VscrollPixel`
  - **Type:** `bool`
  - **Description:** Enables or disables vertical pixel scrolling for the grid.
  - **Default:** `false`

## Code Examples
- **C#**
  ```csharp
  // Enable horizontal pixel scrolling for the grid.
  this.gridControl1.HScrollPixel = true;
  ```
- **VB.NET**
  ```vb.net
  ' Enable horizontal pixel scrolling for the grid.
  Me.gridControl1.HScrollPixel = True
  ```

<!-- tags: [syncfusion, winforms, grid, scrollbars, HScrollPixel, VScrollPixel, properties] keywords: [scrolling, grid, horizontal, vertical, pixel, C#, VB.NET, synchronization, enable, disable] -->
```