```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: XlsIO
page_number: 166
page_id: XlsIO#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:29Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### Copying a Range

```vb.net
' Copying a Range.
Dim source As IRange = sheet.Range("A1")
Dim des As IRange = sheet.Range("A5")
source.CopyTo(des)
```

**MoveTo** method is used for moving a range of cells to the destination. The only difference between copy and move operation is that Move will not create a copy in the source. This is similar to the **Cut** and **Paste** option in Excel.

**Note:** Move does not update formulas.

```csharp
// Moving a Range.
Dim source As IRange = sheet.Range("A1")
Dim des As IRange = sheet.Range("A5")
source.MoveTo(des)
```

```vb.net
' Moving a Range.
Dim source As IRange = sheet.Range("A1")
Dim des As IRange = sheet.Range("A5")
source.MoveTo(des)
```

### Clearing a Range

While editing Excel workbooks, one of the most common action that users perform is clearing or deleting cells. Clearing cells mean erasing everything within them, whereas deleting actually deletes the entire cell. You can clear the cell content by using the **Clear** method. XlsIO also provides options to clear styles or data alone.

Following code example illustrates how to clear a range along with its formatting.

```csharp
// Clearing a Range and its formatting.
sheet.Range["A4"].Clear(true);
```

## Footer

© 2013 Syncfusion. All rights reserved. 
**166 | Page**

<!-- tags: XlsIO, Workbooks, Range, Clear, Delete, CopyTo, MoveTo, Excel Cells -->
```