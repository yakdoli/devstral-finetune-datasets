```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: pdf
page_number: 093
page_id: pdf#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:20Z
fidelity: lossless
-->

## Overview

- Save and restore the current graphics state.
- Use translation, rotation, and primitives for drawing.
- Manage transparency for pen and brush operations.
- Specify transparency blend modes using `SetTransparency`.
- Various `DrawString` methods for text output.
- Use `PdfPen` and `PdfBrush` for text styling and filling.

## Content

### Graphics States and Transformations

You may save the current graphics state, translate the origin, rotate and draw some primitives, restore the graphics state and continue drawing with the restored coordinate system.

### Transparency

You may specify transparency for pen operations (for example: drawing lines), brush operations (for example: filling shapes), and for both of them simultaneously.

Also, you may specify the method of the resulting color calculation. Transparency is set by using the `SetTransparency` method of `PdfGraphics`. It includes the following blend modes:

- Normal
- Multiply
- Screen
- Overlay
- Darken
- Lighten
- ColorDodge
- ColorBurn
- HardLight
- SoftLight
- Difference
- Exclusion

### Text Output

There are plenty of `DrawString` methods in `PdfGraphics` that allow text printing. The format of the methods are similar to the `System.Drawing.Graphics.DrawString` methods.

`PdfPen` as well as `PdfBrush` are used to print the text. You can use either object, or even both pen and brush for the text output. `PdfPen` sets the text boundaries while `PdfBrush` fills the internal area of the text.

If the coordinates are used for the text output only, it will be printed despite the graphics boundaries. New lines symbols split the text by lines only. If the bound (RectangleF structure) of the text is set, the text will be laid out to fit the boundaries. If the width of the boundaries is set to 0 or less, the text will not be limited horizontally. If the height of the boundaries is set to 0 or less, the text will be limited by the boundaries of the `PdfGraphics`.

### Text Output Settings

#### Summary

- **Graphics Handling**: Supports saving, translating, rotating, and restoring the graphics state.
- **Transparency Management**: Allows setting transparency and blend modes for pen and brush operations.
- **Text Printing**: Offers `DrawString` methods with options to use `PdfPen` and `PdfBrush` for styling and filling text boundaries.

#### Detailed Insights

- **Graphic States**: The ability to save and restore graphics states allows for creating complex visual effects by manipulating translation, rotation, and other transformations without affecting the global coordinate system.
- **Transparency Blend Modes**: The inclusion of various blend modes (Normal, Multiply, Screen, etc.) provides flexibility in how transparent elements interact with underlying content, enhancing the visual depth and complexity of drawings.
- **Text Customization**: The use of `PdfPen` and `PdfBrush` enables precise control over the appearance of text, including boundary outlines and internal fills. This feature is crucial for creating styled text that fits specific design requirements.

## API Reference

### Methods

- **SetTransparency**: Configures transparency and blend modes for graphical elements.
- **DrawString**: Renders text with various options for styling and layout.

### Classes

- **PdfGraphics**: Manages drawing operations in PDF documents, including graphic states and text output.
- **PdfPen**: Defines the styling and boundaries of text and graphical elements.
- **PdfBrush**: Defines the internal fill color and pattern of text and graphical elements.

## Code Examples

```csharp
// Example: Using SetTransparency with a blend mode
PdfGraphics graphics = new PdfGraphics(page);
graphics.SetTransparency(0.5f, PdfTransparencyMode.Normal);
// Drawing operations using set transparency

// Example: Using DrawString with PdfPen and PdfBrush
PdfPen pen = new PdfPen(Color.Black);
PdfBrush brush = new PdfSolidBrush(Color.White);
graphics.DrawString("Sample Text", new Font("Arial", 12), brush, new PointF(100, 100));
graphics.DrawRectangle(pen, new RectangleF(95, 95, 150, 50));
```

### Summary and Notes

- The `PdfGraphics` class provides methods for drawing primitives and handling text output.
- Transparency settings and blend modes enhance the visual capabilities of PDF graphics.
- The use of `PdfPen` and `PdfBrush` offers fine-grained control over text and graphical elements' appearance.

## Cross References

- See also: `System.Drawing.Graphics`, `PdfPen`, `PdfBrush`, `DrawString`, `Transparency`.

<!-- tags: [pdf, graphics, text output, transparency, blend modes, winforms] keywords: [PdfGraphics, PdfPen, PdfBrush, DrawString, SetTransparency] -->
```
