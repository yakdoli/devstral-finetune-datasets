```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: DocIo
page_number: 120
page_id: DocIo#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:37Z
fidelity: lossless
-->

### Example of Applying Different Formatting to Table Cells

```csharp
table.TableFormat.Borders.Color = Color.Green;

// Select the first row and append text in each cell
WTableRow row0 = table.Rows[0];
row0.Cells[0].AddParagraph().AppendText("1");
row0.Cells[0].CellFormat.Borders.LineWidth = 2f;
row0.Cells[0].CellFormat.Borders.Color = Color.Magenta;

WTableRow row = table.Rows[0];
row0.Cells[1].AddParagraph().AppendText("2");
row0.Cells[2].AddParagraph().AppendText("3");

WTableRow row1 = table.Rows[1];
row = table.Rows[1];
row1.Cells[0].AddParagraph().AppendText("4");
row1.Cells[1].AddParagraph().AppendText("5");
row1.Cells[1].CellFormat.Borders.LineWidth = 2f;
row1.Cells[1].CellFormat.Borders.Color = Color.Brown;

row1.Cells[2].AddParagraph().AppendText("6");
WTableRow row2 = table.Rows[2];
row2.Cells[0].AddParagraph().AppendText("7");
row2.Cells[1].AddParagraph().AppendText("8");
row2.Cells[2].AddParagraph().AppendText("9");
row2.Cells[2].CellFormat.Borders.LineWidth = 2f;
row2.Cells[2].CellFormat.Borders.Color = Color.Cyan;
row2.Cells[2].CellFormat.Borders.Shadow = true;
```

```vb
' Add a paragraph
paragraph = section.AddParagraph()
paragraph.AppendText("Table with different formatting")
paragraph = section.AddParagraph()

' Add a table
table = section.AddTable()

' Set number of rows and columns
table.ResetCells(3, 3)
table.TableFormat.Borders.LineWidth = 2f
table.TableFormat.Borders.Color = Color.Green

' Select the first row and append text in each cell
Dim row0 As WTableRow = table.Rows(0)
row0.Cells(0).AddParagraph().AppendText("1")
```

<!-- 
tags: [syncfusion, winforms, tables, formatting, borders, colors] 
keywords: [table, formatting, borders, line width, color, cell format, shadow, WTableRow, WTableCell, table borders, different formatting]
-->
```