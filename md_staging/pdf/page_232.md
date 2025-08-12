```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: pdf
page_number: 232
page_id: pdf#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:04Z
fidelity: lossless
-->

# Essential PDF

```vb
' Set header row style.
table.Style.HeaderStyle = headerStyle

' Show the header row.
table.Style.ShowHeader = True

' Repeat header in all the pages.
table.Style.RepeatHeader = True

' Set header data from column caption.
table.Style.HeaderSource = PdfHeaderSource.ColumnCaptions

' Set layout properties.
Dim format As PdfLayoutFormat = New PdfLayoutFormat()
format.Break = PdfLayoutBreakType.FitElement
format.Layout = PdfLayoutType.Paginate

' Draw table.
table.Draw(page, PointF.Empty, format)
```
## API Reference

### Members

```vb
table.Style.HeaderStyle
table.Style.ShowHeader
table.Style.RepeatHeader
table.Style.HeaderSource
PdfLayoutFormat
PdfLayoutBreakType.FitElement
PdfLayoutType.Paginate
table.Draw(page, PointF.Empty, format)
```

### Parameters

- **headerStyle**: The style to be applied to the header row.
- **showHeader**: A boolean indicating whether to display the header.
- **repeatHeader**: A boolean indicating whether to repeat the header on all pages.
- **headerSource**: The source for header data, in this case, `PdfHeaderSource.ColumnCaptions`.

### Returns

No return value. The method modifies the table's appearance and layout.

### Exceptions

- None explicitly shown; common exceptions may include invalid parameters or invalid PDF content.

<!-- tags: [syncfusion, pdf, table, header, layout, winforms, essentialpdf] keywords: [header row, repeat header, column captions, pdf layout, table draw, syncfusion winforms] -->
```