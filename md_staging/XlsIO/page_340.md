```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_340.jpeg
document_name: XlsIO
page_number: 340
page_id: XlsIO#page_340
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:22Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
Console.WriteLine(sheet.Range["D2"].CalculatedValue.ToString(), sheet.Range["D2"].Formula);
```

### Sample Code: VB.NET

```vb
' Inserting sample text into the first cell of the first worksheet.
sheet.Range("A1").Number = 10.99
sheet.Range("B1").Number = 10
sheet.Range("C1").Formula = "A1+B1"
sheet.Range("D1").Formula = "AVERAGE(A1:B1)"

' Formula calculation is enabled for the sheet.
sheet.EnableSheetCalculations()

Console.WriteLine(sheet.Range("C1").FormulaNumberValue.ToString(), sheet.Range("C1").Formula)
Console.WriteLine(sheet.Range("D1").FormulaNumberValue.ToString(), sheet.Range("D1").Formula)

' Add more data.
sheet.Range("A2").Number = 11.99
sheet.Range("B2").Number = 11
sheet.Range("C2").Formula = "A2+B2"
sheet.Range("D2").Formula = "AVERAGE(A2:B2)"

Console.WriteLine(sheet.Range("C2").FormulaNumberValue.ToString(), sheet.Range("C2").Formula)
Console.WriteLine(sheet.Range("D2").FormulaNumberValue.ToString(), sheet.Range("D2").Formula)
```

<!-- tags: [XlsIO, VB.NET, Excel, Formula, Calculation, EnableSheetCalculations] keywords: [CalculateValue, FormulaNumberValue, cell reference, worksheet, sheet, range, text, number, average] -->
```