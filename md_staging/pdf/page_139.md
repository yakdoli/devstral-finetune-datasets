```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: pdf
page_number: 139
page_id: pdf#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:08Z
fidelity: lossless
-->

# Essential PDF

```csharp
pdfLightTable.Style.CellPadding = 4
pdfLightTable.Style.CellSpacing = 10
```

## Header

### Overview
- Header is a set of rows that repeat on each page and has its own style.
- Rows for the header might be taken either from column captions or from ordinary rows.
- When rows are treated as headers, they do not appear in the body of the PdfLightTable.

### Implementation

#### Header from column captions (C#)
```csharp
// Header from column captions
pdfLightTable.Style.ShowHeader = true;
pdfLightTable.Style.HeaderSource = PdfHeaderSource.ColumnCaptions;
pdfLightTable.Style.RepeatHeader = true;
pdfLightTable.Style.HeaderStyle = headerStyle;
```

#### Header from rows (C#)
```csharp
// Header from rows
pdfLightTable.Style.ShowHeader = true;
pdfLightTable.Style.HeaderSource = PdfHeaderSource.Rows;
pdfLightTable.Style.RepeatHeader = true;
pdfLightTable.Style.HeaderRowCount = 3;
pdfLightTable.Style.HeaderStyle = headerStyle;
```

#### Header from column captions (VB.NET)
```vb
' Header from column captions
pdfLightTable.Style.ShowHeader = True
pdfLightTable.Style.HeaderSource = PdfHeaderSource.ColumnCaptions
pdfLightTable.Style.RepeatHeader = True
pdfLightTable.Style.HeaderStyle = headerStyle
```

#### Header from rows (VB.NET)
```vb
' Header from rows
pdfLightTable.Style.ShowHeader = True
pdfLightTable.Style.HeaderSource = PdfHeaderSource.Rows
pdfLightTable.Style.RepeatHeader = True
pdfLightTable.Style.HeaderRowCount = 3
pdfLightTable.Style.HeaderStyle = headerStyle
```

The `headerStyle` is an instance of `PdfCellStyle` that can be set to the header row.

### Row

### Overview
- Focus on configuring headers in PdfLightTable using Syncfusion Winforms.

### References
- Syncfusion Winforms version: 11.4.0.26
- Related components: PdfLightTable, PdfCellStyle
- Page content: `Example and configuration for headers in PdfLightTable`

## API Reference

### PdfLightTable.Style
- **ShowHeader**: Boolean to enable or disable headers.
- **HeaderSource**: Enum to specify source of headers (e.g., `ColumnCaptions`, `Rows`).
- **RepeatHeader**: Boolean to specify if headers should repeat on each page.
- **HeaderRowCount**: Integer to specify the number of rows treated as headers.
- **HeaderStyle**: Instance of `PdfCellStyle` for styling headers.

### PdfCellStyle
- Used to define styles for header rows in PdfLightTable.
- Properties include font, alignment, padding, background color, etc.

### Example Usage
```csharp
PdfCellStyle headerStyle = new PdfCellStyle();
headerStyle.BackgroundBrush = new PdfSolidBrush(Color.LightGray);
headerStyle.Font = new PdfFont(PdfFontFamily.TimesRoman, 12f, PdfFontStyle.Bold);
``` 

<!-- tags: Essential PDF, PdfLightTable, Header, Row, Style, Syncfusion Winforms, PdfCellStyle -->
```