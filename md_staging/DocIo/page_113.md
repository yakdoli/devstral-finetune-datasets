```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: DocIo
page_number: 113
page_id: DocIo#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:33Z
fidelity: lossless
-->

# Essential DocIO

## Content

### Public Methods

| Name         | Description                                   |
|--------------|-----------------------------------------------|
| AddRow       | Adds new row to the table.                   |
| Clone        | Clones this instance.                        |
| Find         | Finds text by specified pattern.             |
| Replace      | Replaces the text by specified pattern.      |
| ResetCells   | Resets rows / columns number.                |
| ApplyStyle   | Applies built-in table style to the table.   |

The following example illustrates how to create an empty table with two rows. Each row has two cells (two columns).

#### Code Examples

**[C#]**

```csharp
IWordDocument doc = new WordDocument();
IWSection section = doc.AddSection();
IWParagraph paragraph = section.AddParagraph();

paragraph.AppendText("Tiny table");
paragraph = section.AddParagraph();
IWTable table = section.AddTable();
table.ResetCells(2, 2);

doc.Save("Table.doc");
```

**[VB.NET]**

```vb
Dim doc As IWordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()
Dim paragraph As IWPparagraph = section.AddParagraph()

paragraph.AppendText("Tiny table")
paragraph = section.AddParagraph()
Dim table As IWTable = section.AddTable()
table.ResetCells(2, 2)

doc.Save("Table.doc")
```

## Page-level Navigation/TOC (if applicable)
<!-- tags: [DocIo, public methods, table manipulation, Winforms, Syncfusion] keywords: [table, rows, columns, cells, reset, applystyle, find, replace] -->
```