```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: XlsIO
page_number: 127
page_id: XlsIO#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:41Z
fidelity: lossless
-->



Essential XlsIO  
```csharp
sheet.Range[1, 2].Value = "Test";
sheet.Range[1, 3].Value = "=SUM(F1:F10)";
```

You can use these properties in the following way.

- If you have an object, and independent of its type, use Value2.
- If you have a string that can have different data types and do not want to parse it, use Value property.
- When you know the exact data (cell) type, use typed properties.

The following code example illustrates how to get the display text and value in the cell.

```csharp
[C#]

sheet.Range["C4"].Number = 1.20;
sheet.Range["B4"].Text = "$#,##0.00";

Console.Writeline(sheet.Range["C4"].DisplayText);
Console.Writeline(sheet.Range["C4"].Value2.ToString());
```

```vbnet
[VB.NET]

sheet.Range("C4").Number = 1.20
sheet.Range("B4").Text = "$#,##0.00"

Console.Writeline(sheet.Range("C4").DisplayText)
Console.Writeline(sheet.Range("C4").Value2.ToString())
```
```