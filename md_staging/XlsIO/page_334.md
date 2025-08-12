```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_334.jpeg
document_name: XlsIO
page_number: 334
page_id: XlsIO#page_334
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:15Z
fidelity: lossless
-->


Essential XlsIO

// Insert Array Formula.
sheet.Range["A1:D1"].FormulaArray = "{1,2,3,4}";
sheet.Names.Add("ArrayRange", sheet.Range["A1:D1"]);
sheet.Range["A2:D2"].FormulaArray = "ArrayRange+100";

```vbnet
' Insert Array Formula.
sheet.Range("A1:D1").FormulaArray = "{1,2,3,4}"
sheet.Names.Add("ArrayRange", sheet.Range("A1:D1"))
sheet.Range("A2:D2").FormulaArray = "ArrayRange+100"
```

![Figure 119: XlsIO with Array Formula](./image.png)

### See Also

- [External Formula](External Formula)

### 4.4.1.2 External Formula

#### Overview
- This section explains how to insert formulas that refer to values in other worksheets/workbooks using Essential XlsIO.
- It highlights the limitation that XlsIO can only write/preserve formulas, not update/refresh calculated values, which must be refreshed by MS Excel.

#### Content

Essential XlsIO allows you to insert/preserve formulas that refer values in other worksheets/workbooks. Note that XlsIO can only write/preserve formulas. You cannot update/refresh the calculated values in Excel, which should be refreshed by MS Excel.

Following code illustrates the insertion of a formula that refers to a value in another workbook.

##### C#
```csharp
// Write external Formula Value.
sheet.Range["C1"].Formula = "[One.xls]Sheet1!$A$1*5";
```

##### VB.NET
```vbnet
' Write external Formula Value.
sheet.Range("C1").Formula = "[One.xls]Sheet1!$A$1*5";
```

---

© 2013 Syncfusion. All rights reserved. 334 | Page
```