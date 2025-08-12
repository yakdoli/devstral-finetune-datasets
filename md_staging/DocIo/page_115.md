<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: DocIo
page_number: 115
page_id: DocIo#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:11Z
fidelity: lossless
-->

## Essential DocIO

```vb
Dim table As IWTable = section.Body.AddTable()
table.ResetCells(1, 1)

Dim row As WTableRow = table.Rows(0)
paragraph = DirectCast(row.Cells(0).AddParagraph(), IParagraph)
paragraph.AppendPicture(New Bitmap("image.png"))
```

### 4.3.3.1 Table Row

**WTableRow** class represents a table row in the Word document. WTableRow class has a collection of table cells (WTableCell objects). Formatting for a table row is defined by the **RowFormat** property. This property returns the object of the RowFormat type.

#### Table Row Height

Table row height is of two types.

- AtLeast
- Exactly

The height type for the table row is defined by the **HeightType** property. When the height type is set to AtLeast, the height of the table row is just enough to fit the text. When the height type is set to Exactly, the row height is specified by the **Height** property, in terms of points.

The following screen shot illustrates how to set the above properties by using the Table Properties dialog box in MS Word.

## RAG Annotations

```html
<!-- tags: table, row, WTableRow, height, formatting, Word document, MS Word, heightType, Height property -->
```