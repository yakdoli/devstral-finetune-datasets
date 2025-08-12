```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: pdf
page_number: 121
page_id: pdf#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:29Z
fidelity: lossless
-->

# Essential PDF

The layouting is accomplished by using the following methods.

## Layout Methods

### C#

```csharp
public PdfLayoutResult Draw(PdfPage page, PointF location, PdfLayoutFormat format);
public PdfLayoutResult Draw(PdfPage page, RectangleF layoutRectangle, PdfLayoutFormat format);
```

### VB.NET

```vb
Public PdfLayoutResult Draw(PdfPage page, PointF location, PdfLayoutFormat format)
Public PdfLayoutResult Draw(PdfPage page, RectangleF layoutRectangle, PdfLayoutFormat format)
```

### Parameters

The parameters define the page where the layouting should start, a location or bounds on the page, and layouting settings.

### Note

> If, only the location is set, or the width or height is less than or equal to zero, the bounds are calculated, as the remaining space on the page where the location specified is a Left or Top of the bounds.

## PdfLayoutFormat Class

The `PdfLayoutFormat` class specifies basic layout settings, such as the type of page break or bounds on another page. The following properties belong to the `PdfLayoutFormat` class.

### Properties of PdfLayoutFormat

| Name              | Description                                     |
|-------------------|-------------------------------------------------|
| Break             | Gets or sets break type of the element.        |
| Layout            | Gets or sets layout type of the element.       |
| PaginateBounds    | Gets or sets the bounds on the next page.      |
| UsePaginateBounds | Gets a value that indicates whether PaginateBounds should be used or not. |

## API Reference

### Methods

- `Draw(PdfPage page, PointF location, PdfLayoutFormat format)`
  - **Parameters:**
    - `page`: A `PdfPage` instance representing the page where the layouting should start.
    - `location`: A `PointF` instance representing the location on the page where the layouting should start.
    - `format`: A `PdfLayoutFormat` instance representing the layouting settings.
  - **Returns:** `PdfLayoutResult`

- `Draw(PdfPage page, RectangleF layoutRectangle, PdfLayoutFormat format)`
  - **Parameters:**
    - `page`: A `PdfPage` instance representing the page where the layouting should start.
    - `layoutRectangle`: A `RectangleF` instance representing the bounds on the page where the layouting should start.
    - `format`: A `PdfLayoutFormat` instance representing the layouting settings.
  - **Returns:** `PdfLayoutResult`

### Properties of PdfLayoutFormat

- **Break**
  - **Type:** `PdfBreak`
  - **Description:** Gets or sets the break type of the element.

- **Layout**
  - **Type:** `PdfLayout`
  - **Description:** Gets or sets the layout type of the element.

- **PaginateBounds**
  - **Type:** `RectangleF`
  - **Description:** Gets or sets the bounds on the next page.

- **UsePaginateBounds**
  - **Type:** `bool`
  - **Description:** Gets a value that indicates whether `PaginateBounds` should be used or not.

### Example Usage

#### C#

```csharp
// Create a new PDF document
PdfDocument document = new PdfDocument();

// Add a new page
PdfPage page = document.Pages.Add();

// Create layout settings
PdfLayoutFormat format = new PdfLayoutFormat();
format.Break = PdfBreak.Callout;
format.Layout = PdfLayout.Tight;

// Draw content on the page
PdfLayoutResult result = new PDFLayoutResult();
result = Draw(page, new PointF(10, 10), format);

// Save the document
document.Save("output.pdf");
```

#### VB.NET

```vb
' Create a new PDF document
Dim document As New PdfDocument()

' Add a new page
Dim page As PdfPage = document.Pages.Add()

' Create layout settings
Dim format As New PdfLayoutFormat()
format.Break = PdfBreak.Callout
format.Layout = PdfLayout.Tight

' Draw content on the page
Dim result As PdfLayoutResult
result = Draw(page, New PointF(10, 10), format)

' Save the document
document.Save("output.pdf")
```

## Related Links

- [PdfLayoutResult Documentation](#)
- [PdfLayoutFormat Class Documentation](#)

<!-- tags: [syncfusion-sdk, pdf, layouting, pdflayoutformat, pdflayoutresult, winforms, csharp, vb.net] keywords: [layouting, pdf, PdfLayoutFormat, PdfLayoutResult, C#, VB.NET, PdfPage, PointF, RectangleF, PdfBreak, PdfLayout, PaginateBounds, UsePaginateBounds] -->
```