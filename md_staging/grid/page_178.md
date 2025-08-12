```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_178.jpeg
document_name: grid
page_number: 178
page_id: grid#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes how to use the GridStyleInfo class to specify cell properties, including images, background colors, and special gradient backgrounds.
- Focuses on configuring BackColor and Interior properties for custom cell backgrounds.

## Content

### GridStyleInfo Properties

| Property                     | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| ImageList GridStyleInfo.ImageList | Holds a list of images for use by the cell.                             |
| Int GridStyleInfo.ImageIndex | Picks a particular image from the ImageList property.                     |

**Note:** Refer the GridStyleInfo topic in the Essential Grid Class Reference for a complete description of all the GridStyleInfo class members.

### 4.1.4.2.1.1.1 BackColor

The BackColor property specifies the background color for the cell. If you want to use a special brush to get a gradient background, you can use the Interior property of GridStyleInfo to specify a brush that can be used to draw the cell background.

#### Interior Property Example

![Interior Property](url_to_image)
*Figure 96: Interior Property*

The figure shows a grid with different cell backgrounds (Interior) and text colors (TextColor). The cells display various gradient and solid patterns, demonstrating the use of the Interior property.

## API Reference

### GridStyleInfo Class
- **Properties:**
  - BackColor: Specifies the background color of the cell.
  - Interior: Specifies a brush that can be used for more complex backgrounds, such as gradients.

### Methods/Events (if any)
- Explicit methods or events related to GridStyleInfo are not listed in the provided content.

## Code Examples

```csharp
// Example: Using Interior property for a gradient background
Syncfusion.Windows.Forms.Grid.GridStyleInfo style = new Syncfusion.Windows.Forms.Grid.GridStyleInfo();
style.Interior = new System.Drawing.Drawing2D.LinearGradientBrush(
    new System.Drawing.Point(0, 0),
    new System.Drawing.Point(100, 100),
    System.Drawing.Color.Red,
    System.Drawing.Color.Blue
);
// Apply the style to a specific cell or range of cells
```

## Cross References
- See also: GridStyleInfo, BackColor, Interior, Gradient Brush, Cell Background Colors

<!-- tags: [syncfusion-sdk, winforms, grid, gridstyleinfo, backcolor, interior, gradient] keywords: [custom cell backgrounds, backcolor property, interior property, gridstyleinfo, essential grid] -->
```