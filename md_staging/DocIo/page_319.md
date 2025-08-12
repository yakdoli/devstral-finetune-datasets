```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_319.jpeg
document_name: DocIo
page_number: 319
page_id: DocIo#page_319
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:32Z
fidelity: lossless
-->

## Overview

- Introduces the essentials of formatting tables in Syncfusion's DocIO library.
- Explains two methods for table formatting.
- Includes examples in C# and VB.NET.

## Content

### Essential DocIO

#### Formatting Overview
**Note:** Following is the order in the paragraph.
1. **WField object**
2. **Field separator**
3. **Text to display**
4. **Field end**

### 5.5 How to format a Table?

#### Introduction
You can format a table in two ways.

#### Method 1

**Description**
You can use the `TableFormat` property of the table object.

**Code Example in C#**
```csharp
WTable table = doc.LastSection.AddTable() as WTable;
table.ResetCells(4, 4);
table.TableFormat.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.Double;
table.TableFormat.LeftIndent = 20;
```

**Code Example in VB.NET**
```vb
Dim table As ITable = sec.body.AddTable()
table.ResetCells(4, 4)
table.TableFormat.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.Double
table.TableFormat.LeftIndent = 20
```

#### Method 2

**Description**
You can use the `ResetCell` method of the table object to format the cell. The following code illustrates this.

<!-- tags: [syncfusion, table formatting, DocIO, tableformat, resetcell, C#, VB.NET, Winforms] keywords: [table formatting, DocIO, Syncfusion, C#, VB.NET, resetcells,_BORDERSTYLE] -->
```