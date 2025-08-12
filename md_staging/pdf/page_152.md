```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_152.jpeg
document_name: pdf
page_number: 152
page_id: pdf#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:53Z
fidelity: lossless
-->

# Essential PDF

## Overview
- The `PdfLayoutType` class is used to specify the type of pagination.
- ThePagination LayoutType allows the PdfGrid to span across multiple pages if the content exceeds the page limits.
- The OnePage layout ensures that the entire element is rendered on a single page.
- Demonstrates the use of `PdfGridLayoutFormat`, `PdfLayoutType`, and `PdfLayoutBreakType` in both C# and VB.NET.

## Content

### Specifying Pagination Type
The `PdfLayoutType` class allows for defining how the `PdfGrid` will be paginated. The provided examples illustrate how to apply pagination settings using both C# and VB.NET.

#### C# Example
```csharp
PdfGridTableLayoutFormat format = new PdfGridLayoutFormat();
format.Layout = PdfLayoutType.Paginate;
format.Break = PdfLayoutBreakType.FitElement;

// Draws the PdfGrid with the layout format
pdfGrid.Draw(pdfPage, PointF.Empty, format);
```

#### VB.NET Example
```vb.net
Dim format As PdfGridLayoutFormat = New PdfGridLayoutFormat()
format.Layout = PdfLayoutType.Paginate
format.Break = PdfLayoutBreakType.FitElement

' Draws the PdfGrid with the layout format
pdfGrid.Draw(pdfPage, PointF.Empty, format)
```

### PdfGridLayoutResult
After rendering the `PdfGrid`, you can retrieve detailed layout information using the `PdfGridLayoutResult` class. This class provides properties such as `Bounds` and `Page`, allowing you to know the precise location of the last page and the boundaries of the rendered grid.

#### Retrieving Layout Information
- Use `Bounds` to get the rectangular area of the grid on the last page.
- Use `Page` to access the exact `PdfPage` where the `PdfGrid` was rendered.

#### Properties
| Name    | Description                                                                 | Data Type       |
|---------|-----------------------------------------------------------------------------|-----------------|
| Bounds  | Gets the bounds in the last page where the grid was drawn                 | **RectangleF**  |
| Page    | Gets the last page where PdfLightTable was drawn                         | **PdfPage**     |

#### Example Usage
```csharp
// Draws the PdfGrid
```

## Page-level Navigation/TOC (if applicable)
- [unclear]

## Cross References
- See also:相关文档或参考链接。

<!-- tags: [pdf, layout, pagination, grid, syncfusion, winforms] keywords: [PdfLayoutType, PdfGridLayoutFormat, PdfLayoutBreakType, PdfGridLayoutResult, Bounds, Page, PdfPage, RectangleF] -->
```