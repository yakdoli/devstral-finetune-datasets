```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: pdf
page_number: 137
page_id: pdf#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:35Z
fidelity: lossless
-->

# Essential PDF

## Properties

| Name  | Description                                                                                          | Data Type   |
|-------|----------------------------------------------------------------------------------------------------------|-------------|
| Bounds | Gets the bounds in the last page where it was drawn                                               | RectangleF   |
| LastRowIndex | Gets the index of the last row                                                             | Integer      |
| Page   | Gets the last page where PdfLightTable was drawn                                                  | PdfPage      |

### C#

```csharp
// Drawing the PdfLightTable.
PdfLightTableLayoutResult result = pdfLightTable.Draw(page, PointF.Empty, format);

// Returning the rectangle value for the last page.
Console.WriteLine(result.Bounds.ToString());
```

### VB.NET

```vb
' Drawing the PdfLightTable.
Dim result As PdfLightTableLayoutResult = pdfLightTable.Draw(page, PointF.Empty, format)

' Returning the rectangle value for the last page.
Console.WriteLine(result.Bounds.ToString())
```

### 4.1.2.3.1.3 PdfLightTable Formatting

This section talks about the most direct and indirect formatting options (through events) that are possible with PdfLightTable. The PdfLightTableStyle class, accessed through the Style property of PdfLightTable, has a number of properties that allow formatting the entire PdfLightTable or parts of it. Border and few other properties are discussed below. Header, Cell, Row, and Column are discussed in the following links:

- Header
- Row
- Column
- Cell

### Border

<!-- tags: [pdflighttable, formatting, pdflighttablestyle, pdflighttablelayoutresult, bounds, lastrowindex, page, header, row, column, cell] keywords: [table formatting, pdf, last page, bounds, row index, page reference, header, row, column, cell, border] -->
```