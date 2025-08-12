```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: pdf
page_number: 075
page_id: pdf#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:49Z
fidelity: lossless
-->

# Essential PDF

## 4.1.1.3 Pen and Brush

### Overview
- Pen and Brush are two types of virtual graphics tools for creating objects like rectangles, ellipses, or text.
- Pen controls stroking operations (drawing borders and lines), while the brush controls filling operations (non-stroking).

### Brush

**Summary**
- There are four types of brushes: solid, tiling, linear gradient, and radial gradient.
- These brushes control the filling of the interior region of shapes.

### Brush Types

**Solid Brush**
- Fills a shape with a single color, which can be set while constructing the brush.
- Example:
  ```csharp
  PdfBrush brush = new PdfSolidBrush(Color.Black);
  ```
  ```vb
  Dim brush As Syncfusion.Pdf.Graphics.PdfBrush = New Syncfusion.Pdf.Graphics.PdfSolidBrush(Color.Black)
  ```

**PdfTilingBrush**
- Enables filling the shape's interior with a repetitive pattern.
- To create a custom pattern, use the `Graphics` property to obtain the `PdfGraphics` class instance.

**PdfLinearGradientBrush**
- Similar to the .NET `LinearGradientBrush`, with properties to specify blend colors and positions.
- Requires start and end positions relative to the current origin to calculate gradient parameters and colors.
- Optionally, specifies a rectangle, a `LinearGradientMode` (determines the orientation), or an angle from the x-axis.

## API Reference
- **Namespace**: Syncfusion.Pdf.Graphics

### PdfSolidBrush
- **Parameters**:
  - `Color`: The color to fill the shape.

### PdfTilingBrush
- **Properties**:
  - `Graphics`: To create and customize the pattern.

### PdfLinearGradientBrush
- **Properties**:
  - `StartPoint`: The start position for the gradient.
  - `EndPoint`: The end position for the gradient.
  - `Colors`: An array of colors for the gradient.
  - `Rect`: Optional rectangle to define the gradient area.
  - `Mode`: Optional mode (`LinearGradientMode`) to determine the orientation.
  - `Angle`: Optional angle from the x-axis.

## Code Examples
- **C#**
  ```csharp
  PdfBrush brush = new PdfSolidBrush(Color.Black);
  ```
- **VB.NET**
  ```vb
  Dim brush As Syncfusion.Pdf.Graphics.PdfBrush = New Syncfusion.Pdf.Graphics.PdfSolidBrush(Color.Black)
  ```

```