```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_153.jpeg
document_name: pdf
page_number: 153
page_id: pdf#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:30Z
fidelity: lossless
-->

# Essential PDF

```csharp
PdfGridLayoutResult result = pdfGrid.Draw(pdfPage, PointF.Empty, 
format);

// Returns the rectangle value for the last page.
Console.WriteLine(result.Bounds.ToString());
```

```vb
' Draws the PdfGrid.
Dim result As PdfGridLayoutResult = pdfGrid.Draw(pdfPage, PointF.Empty, 
format)

' Returns the rectangle value for the last page.
Console.WriteLine(result.Bounds.ToString())
```

## Events

The following events are associated with PdfGrid. The functionalities of these events are common for both PdfGrid and PdfLightTable.

- BeginPageLayout
- EndPageLayout

### 4.1.2.3.2.3 PdfGrid Formatting

This section explains the most direct options available to format PdfGrid. The PdfGridStyle class, accessible through Style property of PdfGrid provides options to format entire PdfGrid or parts of it. Formatting applicable for entire PdfGrid using PdfGridStyle class is discussed in this section. Header, Row, Column and Cell are discussed in the following links:

- Header
- Row
- Column
- Cell

**Note:** If the style properties are applied to both PdfGridCell and PdfGridRow, PdfGridCell takes over the precedence. Following is an example for the exact order of precedence.

```csharp
PdfBrush backgroundBrush = Cell.BackgroundBrush ?? Row.Style.BackgroundBrush ?? 
Row.Grid.Style.BackgroundBrush
```

### Properties

| Name        | Description           | Data Type  |
|-------------|-----------------------|------------|
|             |                       |            |
|             |                       |            |

© 2013 Syncfusion. All rights reserved. Page 153
```