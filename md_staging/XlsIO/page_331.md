```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_331.jpeg
document_name: XlsIO
page_number: 331
page_id: XlsIO#page_331
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:31Z
fidelity: lossless
-->

## Accessing and Working with Formulas Across Worksheets

Essential Xlsl0

```csharp
workbook.SetSeparators(";", ",", "")
```

- In addition to being able to access values in the same worksheet, you can also access values across worksheets. Assume that the "B" is present on the second worksheet, then use the following code for calculation.

**[C#]**
```csharp
sheet.Range["C2:C4"].Formula = "=SUM(Sheet2!B2:B4,Sheet1!A2:A4)";
```

- Sheet1 and Sheet2 are the default names of the worksheets.

**[VB.NET]**
```vb.net
sheet.Range("C2:C4").Formula = "=SUM(sheet2!B2:B4,sheet1!A2:A4)"
```

### Reading Formula Text and Computed Values

You can also read the Formula Text and the Computed Value of the formula in the cell.

Following code example illustrates how to read the formulas and computed values.

**[C#]**
```csharp
// Read computed Formula Value.
this.txtFomulaNumber.Text = sheet.Range["C1"].FormulaNumberValue.ToString();

// Read Formula.
this.txtFormula.Text = sheet.Range["C1"].Formula;
```

**[VB.NET]**
```vb.net
' Read computed Formula Value.
Me.txtFomulaNumber.Text = sheet.Range("C1").FormulaNumberValue.ToString()

' Read Formula.
Me.txtFormula.Text = sheet.Range("C1").Formula
```

### Retrieving Formula Values

You can also get the Formula values as bool, date, and number type. Note that XlsIO can only read already computed formulas, and cannot compute. Please refer to the [Calculation Engine] for more information on dynamic formula computation.

### Using IRange Interface for Formulas

Following properties of the IRange interface are used to fetch formulas, computed values, and to check if there exists a formula in the cell.

---
© 2013 Syncfusion. All rights reserved.  
331 | Page
```

<!-- tags: [xlsio, worksheets, formulas, computed values, workbook, ranges, calculations, syncfusion, winforms] keywords: [accessing formulas,跨工作表计算,read formulas,computed values,dynamic computation,IRange interface] -->
```