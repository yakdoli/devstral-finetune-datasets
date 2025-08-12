```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_124.jpeg
document_name: DocIo
page_number: 124
page_id: DocIo#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:51Z
fidelity: lossless
-->

# Essential DocIO

## Content

| **LeftIndent** | Gets or sets table indent (in points). |
|-----------------|----------------------------------------|
| **Paddings**   | Gets paddings.                         |

### Adding a Table to the Textbody

#### C#

```csharp
// Adding a new Table to the textbody.
IWTable table = sec.body.AddTable();

RowFormat format = new RowFormat();
format.Paddings.All = 5;
format.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.Dot;
format.Borders.LineWidth = 2;

// Inserting rows to the table. This will apply the format to whole table
table.ResetCells(6, 6, format, 80);
```

#### VB.NET

```vb
' Adding a new Table to the textbody.
Dim table As IWTable = sec.body.AddTable()

Dim format As New RowFormat()
format.Paddings.All = 5
format.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.Dot
format.Borders.LineWidth = 2

' Inserting rows to the table. This will apply the format to whole table
table.ResetCells(6, 6, format, 80)
```

### 4.3.3.4 Table Styles

**WTableStyle** class represents table style in the Word document. Table style defines a set of formatting characteristics that can be applied to the table.

## Copyright Notice

© 2013 Syncfusion. All rights reserved.

<!-- tags: [DocIO, Table Styles, WTableStyle, Syncfusion Winforms, DocIO, 11.4.0.26] keywords: [RowFormat, ResetCells, Table Styles, WTableStyle, Essential DocIO] -->
```