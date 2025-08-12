```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_461.jpeg
document_name: grid
page_number: 461
page_id: grid#page_461
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:00Z
fidelity: lossless
-->

### Overview

This page discusses the configuration of scroll bars in the Essential Grid control for Windows Forms. It provides examples in C# and VB.NET to enable horizontal and vertical scroll bars. Additionally, it covers custom drawing on grid cells using events like `DrawCell` and `CellDrawn`.

### Content

**Enabling Horizontal Scroll Bar**

- Enable the horizontal scroll bar using the `HScroll` property.

```vb.net
' Enable horizontal scroll bar.
Me.gridControl.HScroll = True
```

**VScroll - Specifying Vertical Scroll Bar**

- The `VScroll` property determines whether the vertical scroll bar is enabled or disabled. Below are code examples for setting this property:

1. **Using C#**

   ```csharp
   // Enable vertical scroll bar.
   this.gridControl.VScroll = true;
   ```

2. **Using VB.NET**

   ```vb.net
   ' Enable vertical scroll bar.
   Me.gridControl.VScroll = True
   ```

A sample demonstrating these properties is available at the following location:

```plaintext
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Zoom and Scrolling\Scroll Bar Demo
```

**4.1.4.13.5 Custom Drawing**

- Essential Grid allows custom drawing on its cells. Custom Drawing involves adding text and drawings such as lines, polygons, etc., to the cell. It includes events like `CellDrawn` and `DrawCell`, which let you define the precise appearance of cells in your application.

- **DrawCell Event**: This event is triggered for every cell before the grid draws it. It is commonly used to add custom drawing to a cell and can be utilized to draw shapes like lines and polygons.

- **CellDrawn Event**: This event is triggered for every cell after the grid has finished drawing it. You can handle this event and use its `Graphics` argument to perform custom drawing.

### API Reference

- **Properties**
  - `HScroll`: Enables/disables the horizontal scroll bar.
  - `VScroll`: Enables/disables the vertical scroll bar.

- **Events**
  - `DrawCell`: Triggered before the grid draws a cell.
  - `CellDrawn`: Triggered after the grid has finished drawing a cell.

### Code Examples

```csharp
// Enabling vertical scroll bar in C#
this.gridControl.VScroll = true;

// Enabling vertical scroll bar in VB.NET
Me.gridControl.VScroll = True
```

### Notes

- Ensure that the `HScroll` and `VScroll` properties are set appropriately based on the data and layout requirements of your application.
- Utilize the `DrawCell` and `CellDrawn` events to customize the appearance of grid cells as needed.

### See also

- [Scroll Bar Properties in Essential Grid](#scroll-bar-properties-in-essential-grid)
- [Custom Drawing in Grid Controls](#custom-drawing-in-grid-controls)

<!-- tags: [grid, scroll bar, custom drawing, events, windows forms, winforms, essential grid] keywords: [HScroll, VScroll, DrawCell, CellDrawn, custom drawing, scroll bar, windows forms] -->
```