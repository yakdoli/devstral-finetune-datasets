```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: DocIo
page_number: 121
page_id: DocIo#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:58Z
fidelity: lossless
-->

## Essential DocIO

```csharp
row0.Cells(0).CellFormat.Borders.LineWidth = 2f
row0.Cells(0).CellFormat.Borders.Color = Color.Magenta

Dim row As WTableRow = table.Rows(0)
row0.Cells(1).AddParagraph().AppendText("2")
row0.Cells(2).AddParagraph().AppendText("3")

Dim row1 As WTableRow = table.Rows(1)
row = table.Rows(1)
row1.Cells(0).AddParagraph().AppendText("4")
row1.Cells(1).AddParagraph().AppendText("5")
row1.Cells(1).CellFormat.Borders.LineWidth = 2f
row1.Cells(1).CellFormat.Borders.Color = Color.Brown

row1.Cells(2).AddParagraph().AppendText("6")
Dim row2 As WTableRow = table.Rows(2)
row2.Cells(0).AddParagraph().AppendText("7")
row2.Cells(1).AddParagraph().AppendText("8")
row2.Cells(2).AddParagraph().AppendText("9")
row2.Cells(2).CellFormat.Borders.LineWidth = 2f
row2.Cells(2).CellFormat.Borders.Color = Color.Cyan
row2.Cells(2).CellFormat.Borders.Shadow = True
```

### Cell Content Formatting

The AddParagraph method of the WTableCell class is used to add paragraphs to the table cell. The TextRange property of this method is used to format the contents of the cell. For details, see [Text Range](#).

```csharp
[C#]

// Adding a new Table to the text body.
IWTable table = sec.body.AddTable();

// Inserting rows to the table. This will apply the format to whole table.
table.ResetCells(6, 6, format, 80);
WTableCell cell = table.Rows[0].Cells[0] as WTableCell;
WTextRange range = cell.AddParagraph().AppendText("aaaaaaaaaaaaaaaa") as WTextRange;

//Format first cell first paragraph.
range.CharacterFormat.FontName = "Arial";
range.CharacterFormat.FontSize = 10;
```

<!-- tags: [product, DocIO, WTable, WTableRow, WTableCell, AddParagraph, TextRange, WTextRange] keywords: [Table, Cell Formatting, Paragraph, CharacterFormat, FontName, FontSize, Borders, Shadow] -->
```