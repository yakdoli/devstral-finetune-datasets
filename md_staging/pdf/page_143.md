```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_143.jpeg
document_name: pdf
page_number: 143
page_id: pdf#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:25Z
fidelity: lossless
-->

# Essential PDF

```csharp
PdfPens.Green)
altStyle.BackgroundBrush = PdfBrushes.DarkGray

Dim headerStyle As Syncfusion.Pdf.Tables.PdfCellStyle
= New Syncfusion.Pdf.Tables.PdfCellStyle(Font, PdfBrushes.White, 
PdfPens.Brown)
headerStyle.BackgroundBrush = PdfBrushes.Red

pdfLightTable.Style.AlternateStyle = altStyle
pdfLightTable.Style.HeaderStyle = headerStyle
```

## PdfLightTable Customization

PdfLightTable offers a set of events that help to change the look and feel in the PDF. The following are the list of events and links that discuss them:

### 4.1.2.3.1.4.1 BeginPageLayout

This event is raised before layout starts on a page. The arguments of this event are as follows:

- **Page** (read-only): Page on which layout should be performed
- **Bounds**: Size of the PdfLightTable part, which should be laid out on the page
- **Cancel**: Enables to cancel layout

### 4.1.2.3.1.4.2 EndPageLayout

This event is raised when layout on a page finishes. The arguments of this event are as follows:

- **Result** (read-only): Layout result for the current page
- **NextPage**: Page on which layout should continue

### 4.1.2.3.1.4.3 BeginRowLayout

This event is raised when row layout starts. The arguments of this event are as follows:

- **RowIndex** (read-only): Index of the row (zero based)
- **CellStyle**: Style of the cells within the row
- **ColumnSpanMap**: Array of integers specifying column span
- **Cancel**: Enables to cancel layout
- **IgnoreColumnFormat**: Gets or sets a value indicating whether column string format should be ignored.

## Page-Level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist. 
<!-- tags: [pdf, table, customization, events, syncfusion] keywords: [pdfLightTable, BeginPageLayout, EndPageLayout, BeginRowLayout, layout events, customization, style, header, alternate style] -->
```