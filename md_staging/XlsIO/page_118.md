```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: XlsIO
page_number: 118
page_id: XlsIO#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:19Z
fidelity: lossless
-->

# Essential XlslO

```csharp
sheet.Range("B4").CellStyle.Rotation = 90
```

## Text Direction

You can specify the text orientation by using the **ReadingOrder** property. The following code example illustrates this.

### C#

```csharp
// Text Direction Setting.
sheet.Range("B8").CellStyle.ReadingOrder =
    Syncfusion.XlsIO.ExcelReadingOrderType.LeftToRight;
sheet.Range("B10").CellStyle.ReadingOrder =
    Syncfusion.XlsIO.ExcelReadingOrderType.RightToLeft;
sheet.Range("B12").CellStyle.ReadingOrder =
    Syncfusion.XlsIO.ExcelReadingOrderType.Context;
```

### VB.NET

```vb
' Text Direction Setting.
sheet.Range("B8").CellStyle.ReadingOrder =
    Syncfusion.XlsIO.ExcelReadingOrderType.LeftToRight
sheet.Range("B10").CellStyle.ReadingOrder =
    Syncfusion.XlsIO.ExcelReadingOrderType.RightToLeft
sheet.Range("B12").CellStyle.ReadingOrder =
    Syncfusion.XlsIO.ExcelReadingOrderType.Context
```

<!-- tags: [product, XlsIO, text direction, Rotation, ReadingOrder, C#, VB.NET] keywords: [text orientation, ReadingOrder property, LeftToRight, RightToLeft, Context, Excel, cell style] -->
```