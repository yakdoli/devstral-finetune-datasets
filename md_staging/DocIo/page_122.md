```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: DocIo
page_number: 122
page_id: DocIo#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:22Z
fidelity: lossless
-->

# Essential DocIO

```csharp
// Format first cell second paragraph.
range = cell.AddParagraph().AppendText("bbbbbbbbbbbbbbbbbbbb") as WTextRange;
range.CharacterFormat.Italic = true;
range.CharacterFormat.FontSize = 12;
```

## [C#]

```vb
' Adding a new Table to the text body.
Dim table As ITable = sec.body.AddTable()

' Inserting rows to the table. This will apply the format to whole table.
table.ResetCells(6, 6, Format, 80)
Dim cell As WTableCell = TryCast(table.Rows(0).Cells(0), WTableCell)
Dim range As WTextRange = TryCast(cell.AddParagraph().AppendText("aaaaaaaaaaaaaaaaaa"), WTextRange)

' Format first cell first paragraph.
range.CharacterFormat.FontName = "Arial"
range.CharacterFormat.FontSize = 10

' Format first cell second paragraph.
range = TryCast(cell.AddParagraph().AppendText("bbbbbbbbbbbbbbbbbbbb"), WTextRange)
range.CharacterFormat.Italic = True
range.CharacterFormat.FontSize = 12
```

### 4.3.3.3 Row Format

The **RowFormat** class represents table or table row formatting in the Word document.

#### Properties

- **Borders**: defines format of row borders (width of line, line color and so on)
- **Paddings**: defines margins for the cells in the row or table
- **CellSpacing**: defines spacing between cells
- **LeftIndent**: defines left indent of table or table row
- **IsAutoResized**: defines if table or row auto resizes to fit the text

The following screenshot illustrates how to set the Row Format in MS Word.

<!-- tags: [Syncfusion, Winforms, DocIO, Table, RowFormat] keywords: [RowFormat, Borders, Paddings, CellSpacing, LeftIndent, IsAutoResized] -->
```