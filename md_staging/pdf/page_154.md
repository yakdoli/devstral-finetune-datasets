```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_154.jpeg
document_name: pdf
page_number: 154
page_id: pdf#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:01Z
fidelity: lossless
-->

# **Essential PDF**

## Content

The following table lists the properties of the `PdfGrid` control:

| Property                | Description                                          | Type                 |
|-------------------------|------------------------------------------------------|----------------------|
| `AllowHorizontalOverflow` | Gets or sets a value indicating whether to allow horizontal overflow. | Boolean              |
| `BackgroundBrush`       | Gets or sets background brush.                      | PdfBrush            |
| `BorderOverlapStyle`    | Gets or sets border overlap style.                  | PdfBorderOverlapStyle|
| `CellPadding`           | Gets or sets cell padding.                          | PdfPaddings         |
| `CellSpacing`           | Gets or sets cell spacing.                          | Float               |
| `Font`                  | Gets or sets the font.                              | PdfFont             |
| `HorizontalOverflowType` | Gets or sets the type of horizontal overflow.      | PdfHorizontalOverflowType |
| `TextBrush`             | Gets or sets the text brush.                       | PdfBrush            |
| `TextPen`               | Gets or sets the text pen.                          | PdfPen              |

### **AllowHorizontalOverflow**

If set to `True`, the columns exceeding the current page width would be wrapped and drawn in the next or last page. The default value is `false`. It should be used along with `HorizontalOverflowType` property. The default value of `HorizontalOverflowType` is `PdfHorizontalOverflowType.LastPage`.

#### **Code Examples**

- **C#**
  ```csharp
  pdfGrid.Style.AllowHorizontalOverflow = true;
  pdfGrid.Style.HorizontalOverflowType =
      PdfHorizontalOverflowType.NextPage;
  ```

- **VB.NET**
  ```vb
  pdfGrid.Style.AllowHorizontalOverflow = True
  pdfGrid.Style.HorizontalOverflowType =
      PdfHorizontalOverflowType.NextPage
  ```

### **BorderOverlapStyle**

<!-- tags: [Syncfusion, Winforms, PdfGrid, Properties, AllowHorizontalOverflow, BorderOverlapStyle, CellPadding, CellSpacing, Font, HorizontalOverflowType, TextBrush, TextPen] keywords: [Essential PDF, C#, VB.NET, PdfHorizontalOverflowType, grid properties, grid drawing, overflow handling, font settings, border styles, cell spacing, cell padding, text formatting, pdf document, style customization] -->
```