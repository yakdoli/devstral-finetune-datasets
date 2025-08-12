```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: pdf
page_number: 122
page_id: pdf#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:53Z
fidelity: lossless
-->

## Essential PDF

### Overview
- PdfLayoutFormat contains the PaginateBounds property that specifies the bounds of the element on the pages that follows. If this property is set, the element will use it for laying out the next pages; otherwise, the element will be laid out according to the bounds used on the first page (layoutRectangle parameter or calculated as mentioned above), but with the Y coordinate set to zero (0).
- Each element may implement its own layout settings depending on its own structure and specifications.
- The objects supporting page layout can be drawn on simple graphics or by using the provided methods.

### Content
#### Note:
- **PdfLayoutFormat and LayoutBounds:**
  - The `PdfLayoutFormat` class contains the `PaginateBounds` property, which specifies the bounds of the element on the pages that follow. If this property is set, the element will use it for laying out the next pages. Otherwise, the element will be laid out according to the bounds used on the first page (layoutRectangle parameter or calculated as mentioned above), but with the Y coordinate set to zero (0).
- **Element-Specific Layout Settings:**
  - Each element may implement its own layout settings depending on its structure and specifications.
- **Drawing Methods:**
  - The objects supporting page layout can be drawn on simple graphics or by using the following methods:

  **C#:**
  ```csharp
  public void Draw(PdfGraphics graphics);
  public void Draw(PdfGraphics graphics, PointF location);
  ```

  **VB.NET:**
  ```vb.net
  Public Sub Draw(PdfGraphics graphics)
  Public Sub Draw(PdfGraphics graphics, PointF location)
  ```

- **Layout Result:**
  After laying out, each element returns a layout result, depending on the element and the settings. The base result is described by the `PdfLayoutResult` class.

The basic information stored in the result is the page where the element ends and the bounds of the element on that page, which might be helpful for further drawing operations on this page.

#### PdfLayoutResult Class Properties

| Name    | Description                                       |
|---------|---------------------------------------------------|
| Bounds  | Gets the bounds of the element on the last page where it was drawn. |
| Page    | Gets the last page where the element was drawn. |

#### Example Usage:
- **PdfTextLayoutResult:**
  The `PdfTextLayoutResult` provides a text that was not laid out and a width of the last laid-out line. `PdfMetafile` as well as graphics primitives also supports multipage layout.
- **PdfMetafileLayoutFormat:**
  Additionally, if it is required to eliminate the splitting of text lines between the pages, the `PdfMetafileLayoutFormat` is used as the input parameter of the `Draw` method. This class contains a property that allows enabling or disabling splitting of text lines.

## Page-level Navigation/TOC
- [Start of Document](#start)
- [Essential PDF Overview](#essentials_pdfoverview)
- [Contact Us](#contact_info)

## Code Examples
**C#:**
```csharp
// Example of using PdfTextLayoutResult
PdfTextLayoutResult textResult = textLayout.Format(Text, Rectangle, layoutFormat);
Rectangle last_bounds = textResult.Bounds;
int last_page = textResult.Page;

Console.WriteLine($"Text was last drawn on page {last_page} with bounds {last_bounds}");
```

**VB.NET:**
```vb.net
' Example of using PdfTextLayoutResult
Dim textResult As PdfTextLayoutResult = textLayout.Format(Text, Rectangle, layoutFormat)
Dim last_bounds As Rectangle = textResult.Bounds
Dim last_page As Integer = textResult.Page

Console.WriteLine($"Text was last drawn on page {last_page} with bounds {last_bounds}")
```

## Cross References
- See also:
  - [Syncfusion Winforms Documentation](https://www.syncfusion.com/documentation/windowsforms/starter-kit)
  - [Syncfusion Essential PDF Features](https://www.syncfusion.com/products/windowsforms/pdf)

## RAG Annotations
<!-- tags: [Syncfusion, WindowsForms, PDF, Layout, PdfLayoutResult, PdfTextLayoutResult] keywords: [PdfLayoutFormat, PaginateBounds, Draw, layoutRectangle, multipage layout, graphics primitives] -->
```