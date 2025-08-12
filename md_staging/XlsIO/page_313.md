```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_313.jpeg
document_name: XlsIO
page_number: 313
page_id: XlsIO#page_313
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:19Z
fidelity: lossless
-->

## Horizontal and Vertical Page Breaks in VB.NET

### Overview
- This section demonstrates how to enter text into cells and set both horizontal and vertical page breaks using VB.NET code.

### Content

#### Code Example
```vb
[VB.NET]

' Entering text into the cells.
sheet.Range("A1:M20").Text = "PageBreak"

' Giving Horizontal Page Breaks.
sheet.HPageBreaks.Add(sheet.Range("A5"))
sheet.HPageBreaks.Add(sheet.Range("A10"))
sheet.HPageBreaks.Add(sheet.Range("A15"))

' Giving Vertical Page Breaks.
sheet.VPageBreaks.Add(sheet.Range("B5"))
sheet.VPageBreaks.Add(sheet.Range("E10"))
sheet.VPageBreaks.Add(sheet.Range("K15"))
```

### Explanation
- **Text Entry**: The code enters the text "PageBreak" into the cells ranging from `A1` to `M20`.
- **Horizontal Page Breaks**:
  - Added at rows `A5`, `A10`, and `A15`.
  - These breaks divide the print view of the sheet horizontally.
- **Vertical Page Breaks**:
  - Added at columns `B5`, `E10`, and `K15`.
  - These breaks divide the print view of the sheet vertically.

### API Reference
- **Horizontal Page Breaks**:
  - `HPageBreaks.Add(sheet.Range("A5"))`
  - Adds a horizontal page break at row `A5`.
  - Similar for `A10` and `A15`.

- **Vertical Page Breaks**:
  - `VPageBreaks.Add(sheet.Range("B5"))`
  - Adds a vertical page break at column `B5`.
  - Similar for `E10` and `K15`.

### Code Examples
The provided VB.NET code illustrates the step-by-step process of setting these page breaks in a spreadsheet.

### Related Topics
- For more details on page breaks and print settings, refer to the XlsIO documentation on print settings and layout options.

<!-- tags: [XlsIO, page breaks, VB.NET, horizontal, vertical, print layout, Syncfusion Winforms] keywords: [page breaks, horizontal page breaks, vertical page breaks, VB.NET code, xlsio, print settings, sheet page breaks] -->
```