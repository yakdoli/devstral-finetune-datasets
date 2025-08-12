```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_327.jpeg
document_name: XlsIO
page_number: 327
page_id: XlsIO#page_327
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:09Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to set various predefined formulas in a worksheet.
- Shows the usage of common Excel functions like MODE, NEGBINOMDIST, NORMINV, etc.
- Examples include setting formulas for cells with references to other cells.

## Content

### Setting Formulas in Worksheet Cells

The following code snippet demonstrates how to set predefined formulas in different cells of a worksheet. Each cell contains a specific Excel function or formula.

```csharp
sheet.Range["A91"].Text = "MODE(A3:A4)";
sheet.Range["B91"].Formula = "MODE(A3:A4)";

sheet.Range["A92"].Text = "NEGBINOMDIST(A3,A4,A8)";
sheet.Range["B92"].Formula = "NEGBINOMDIST(A3,A4,A8)";

sheet.Range["A93"].Text = "NORMINV(A8,A4,A5)";
sheet.Range["B93"].Formula = "NORMINV(A8,A4,A5)";

sheet.Range["A94"].Text = "NORMSINV(A8)";
sheet.Range["B94"].Formula = "NORMSINV(A8)";

sheet.Range["A95"].Text = "NPER(A3,A4,A5)";
sheet.Range["B95"].Formula = "NPER(A3,A4,A5)";

sheet.Range["A96"].Text = "NPV(A3,A4)";
sheet.Range["B96"].Formula = "NPV(A3,A4)";

sheet.Range["A97"].Text = "PEARSON(A3:A8,A13:A18)";
sheet.Range["B97"].Formula = "PEARSON(A3:A8,A13:A18)";

sheet.Range["A98"].Text = "PERCENTILE(A3:A8,A18)";
sheet.Range["B98"].Formula = "PERCENTILE(A3:A8,A18)";

sheet.Range["A99"].Text = "PERCENTRANK(A3:A8,A3)";
sheet.Range["B99"].Formula = "PERCENTRANK(A3:A8,A3)";

sheet.Range["A100"].Text = "PERMUT(A3,2)";
sheet.Range["B100"].Formula = "PERMUT(A3,2)";

sheet.Range["A101"].Text = "PMT(A3,A4,A5)";
sheet.Range["B101"].Formula = "PMT(A3,A4,A5)";

sheet.Range["A102"].Text = "PPMT(A8,A4,A5,A6)";
sheet.Range["B102"].Formula = "PPMT(A8,A4,A5,A6)";

sheet.Range["A103"].Text = "PROB(A3:A4,A8:A18,A3)";
sheet.Range["B103"].Formula = "PROB(A3:A4,A8:A18,A3)";

sheet.Range["A104"].Text = "PRODUCT({150,2,3,4,5,20})";
sheet.Range["B104"].Formula = "PRODUCT({150,2,3,4,5,20})";

sheet.Range["A105"].Text = "PV(A3,A4,A5)";
sheet.Range["B105"].Formula = "PV(A3,A4,A5)";

sheet.Range["A106"].Text = "QUARTILE(A3:A7,A8)";
```

Each formula is assigned to both a cell's text (for display) and formula (for computation).

## Notes
- Ensure that the referenced cells (e.g., A3, A4) contain valid data for accurate calculations.
- The `Formula` property expects valid Excel functions with correct syntax.

## Cross References
- Refer to the Excel documentation for detailed descriptions of each function used in the code.
- For more information on setting formulas in XlsIO, consult the Syncfusion XlsIO documentation.

<!-- tags: XlsIO, Excel, Worksheet, Formulas, Functions, WinForms keywords: mode, negbinomdist, norminv, normsinv, nper, npv, pearson, percentile, percentrank, permut, pmt, ppmt, prob, product, pv, quartile -->
```