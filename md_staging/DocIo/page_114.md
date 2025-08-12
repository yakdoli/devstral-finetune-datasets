```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_114.jpeg
document_name: DocIo
page_number: 114
page_id: DocIo#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:50Z
fidelity: lossless
-->

# Essential DocIO

![Figure: Table with Two Rows and Two Columns](Tiny_Table.png)
*Figure 37: Table with Two Rows and Two Columns*

## Nested Table

You can create nested tables by creating a table in the cell of the parent table by using DocIO. The following code illustrates this.

### C#

```csharp
// Adding a nested Table to the cell (2,2) of the parent table.
IWTable nestTable = table[2, 2].AddTable();
nestTable.ResetCells(3, 3);
```

### VB.NET

```vb
' Adding a new Table to the cell (2,2) of the parent table.
Dim nestTable as IWTable = table[2, 2].AddTable()
nestTable.ResetCells(3, 3)
```

## Cell Image

You can also insert images in the table cells by appending a picture to the cell paragraph. The following code illustrates how to insert a picture in the first cell.

### C#

```csharp
IWTable table = section.Body.AddTable();
table.ResetCells(1, 1);

WTableRow row = table.Rows[0];
paragraph = (IWParagraph)row.Cells[0].AddParagraph();
paragraph.AppendPicture(new Bitmap("image.png"));
```

<!-- tags: [DocIO, nested tables, cell images, programming, C#, VB.NET] keywords: [nested tables, cell images, append picture, table, DocIO, Winforms, programming] -->
```