```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_325.jpeg
document_name: XlsIO
page_number: 325
page_id: XlsIO#page_325
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:01Z
fidelity: lossless
-->

## Excel Formula Manipulation in XlsIO

### Overview
This section demonstrates the usage of XlsIO to manipulate and set various Excel formulas in a worksheet. Examples include using built-in Excel functions such as `INDIRECT`, `INFO`, `INTERCEPT`, `IPMT`, `IRR`, `KURT`, `LARGE`, `LOGEST`, `LOGNORMDIST`, and `MAX`/`MAXA`.

### Code Examples
The code snippet below sets different Excel formulas into specific cells of a worksheet, showcasing how to use XlsIO to dynamically create and handle formulas in a spreadsheet.

```csharp
sheet.Range["A61"].Text = "INDIRECT(B5)";
sheet.Range["B61"].Formula = "INDIRECT(B5)";

sheet.Range["A62"].Text = "INFO(B6)";
sheet.Range["B62"].Formula = "INFO(B6)";

sheet.Range["A63"].Text = "INTERCEPT(A3:A8,A13:A18)";
sheet.Range["B63"].Formula = "INTERCEPT(A3:A8,A13:A18)";

sheet.Range["A64"].Text = 
"INTERCEPT({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})";
sheet.Range["B64"].Formula = 
"INTERCEPT({150,100,200,300,500,0.3},{95,155,195,305,495,0.7})";

sheet.Range["A65"].Text = "IPMT(A18,3,A5,A6)";
sheet.Range["B65"].Formula = "IPMT(A18,3,A5,A6)";

sheet.Range["A66"].Text = "IRR(A9:A12)";
sheet.Range["B66"].Formula = "IRR(A9:A12)";

sheet.Range["A67"].Text = "IRR({-100,100,200,150})";
sheet.Range["B67"].Formula = "IRR({-100,100,200,150})";

sheet.Range["A68"].Text = "KURT(A3:A8)";
sheet.Range["B68"].Formula = "KURT(A3:A8)";

sheet.Range["A69"].Text = "KURT({150,100,200,300,500,0.3})";
sheet.Range["B69"].Formula = "KURT({150,100,200,300,500,0.3})";

sheet.Range["A70"].Text = "LARGE(A13:A18,3)";
sheet.Range["B70"].Formula = "LARGE(A13:A18,3)";

sheet.Range["A71"].Text = "LARGE({95,155,195,305,495,0.7},3)";
sheet.Range["B71"].Formula = "LARGE({95,155,195,305,495,0.7},3)";

sheet.Range["A72"].Text = "LOGEST({10,20,30},{10,20,30})";
sheet.Range["B72"].Formula = "LOGEST({10,20,30},{10,20,30})";

sheet.Range["A73"].Text = "LOGNORMDIST({10,20,30},A4,A5)";
sheet.Range["B73"].Formula = "LOGNORMDIST({10,20,30},A4,A5)";

sheet.Range["A74"].Text = "MAX({10,20,30;5,15,35;6,16,36})";
sheet.Range["B74"].Formula = "MAX({10,20,30;5,15,35;6,16,36})";

sheet.Range["A75"].Text = "MAXA({10,20,30;5,15,35;6,16,36})";
sheet.Range["B75"].Formula = "MAXA({10,20,30;5,15,35;6,16,36})";
```

## API Reference

### Methods and Functions
- **Range.Text**: Sets the text content of the specified range.
- **Range.Formula**: Sets the formula for the specified range.

Each of these functions is used to populate cells with literal text or actual Excel formulas. The examples show various combinations of direct and array formulas.

### Fields
- **B5**: A reference cell for `INDIRECT` and similar functions.
- **A3:A8, A13:A18**: Arrays used for statistical and regression calculations like `INTERCEPT`.
- **A5, A6**: Initial interest rate and number of periods for `IPMT`.
- **A9:A12**: A range for calculating internal rate of return with `IRR`.

### Notes
Ensure that all references and cell ranges are valid before setting formulas, as invalid ranges can lead to errors or unexpected results.

## Cross References
- See also: [XlsIO Formula Calculation in Spreadsheet Documents](#XlsIO-Formula-Calculation-in-Spreadsheet-Documents)
- [Using Excel Functions in XlsIO](#Using-Excel-Functions-in-XlsIO)

<!-- tags: [XlsIO, Excel, Formula Manipulation, ranges, cells, functions]
keywords: [INDIRECT, INFO, INTERCEPT, IPMT, IRR, KURT, LARGE, LOGEST, LOGNORMDIST, MAX, MAXA] -->
```
