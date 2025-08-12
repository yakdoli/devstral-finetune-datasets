```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_328.jpeg
document_name: XlsIO
page_number: 328
page_id: XlsIO#page_328
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:24Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Implements various Excel formula functions such as `QUARTILE`, `RATE`, `RANK`, `RSQ`, and others for different ranges.
- Provides examples to demonstrate how to use Excel-style functions within the `XlsIO` API.

## Content

### Using Excel Formula Functions in XlsIO

The following code demonstrates how to assign different Excel formula functions to specific cells in a spreadsheet using the `XlsIO` library:

```csharp
sheet.Range["B106"].Formula = "QUARTILE(A3:A7,A8)";
sheet.Range["A107"].Text = "RATE(A19,-A3,A4)";
sheet.Range["B107"].Formula = "RATE(A19,-A3,A4)";
sheet.Range["A108"].Text = "RANK(A3,A3:A8)";
sheet.Range["B108"].Formula = "RANK(A3,A3:A8)";
sheet.Range["A109"].Text = "RSQ(A3:A8,A18:A18)";
sheet.Range["B109"].Formula = "RSQ(A3:A8,A18:A18)";
sheet.Range["A110"].Text = "SEARCH(B4,B7)";
sheet.Range["B110"].Formula = "SEARCH(B4,B7)";
sheet.Range["A111"].Text = "SEARCHB(B4,B7)";
sheet.Range["B111"].Formula = "SEARCHB(B4,B7)";
sheet.Range["A112"].Text = "SKEW(A3:A8)";
sheet.Range["B112"].Formula = "SKEW(A3:A8)";
sheet.Range["A113"].Text = "SLOPE(A3:A8,A13:A18)";
sheet.Range["B113"].Formula = "SLOPE(A3:A8,A13:A18)";
sheet.Range["A114"].Text = "SMALL(A3:A8,3)";
sheet.Range["B114"].Formula = "SMALL(A3:A8,3)";
sheet.Range["A115"].Text = "STDEV(A3:A8)";
sheet.Range["B115"].Formula = "STDEV(A3:A8)";
sheet.Range["A116"].Text = "STDEVA(A3:A8)";
sheet.Range["B116"].Formula = "STDEVA(A3:A8)";
sheet.Range["A117"].Text = "STDEVP(A3:A8)";
sheet.Range["B117"].Formula = "STDEVP(A3:A8)";
sheet.Range["A118"].Text = "STDEVPA(A3:A8)";
sheet.Range["B118"].Formula = "STDEVPA(A3:A8)";
sheet.Range["A119"].Text = "STEYX(A3:A8,A13:A18)";
sheet.Range["B119"].Formula = "STEYX(A3:A8,A13:A18)";
sheet.Range["A120"].Text = "SUBSTITUTE(B3,B4,\"Test\")";
sheet.Range["B120"].Formula = "SUBSTITUTE(B3,B4,\"Test\")";
sheet.Range["A121"].Text = "SUBTOTAL(A19,A3:A8)";
sheet.Range["B121"].Formula = "SUBTOTAL(A19,A3:A8)";
```

## API Reference

### Methods

- `Formula`: Assigns an Excel formula to a cell.
- `Text`: Sets the text value of a cell explicitly.

## Code Examples

### Example: Implementing Excel Functions in XlsIO

```csharp
// Assign QUARTILE formula
sheet.Range["B106"].Formula = "QUARTILE(A3:A7,A8)";

// Assign RATE formula with text and formula
sheet.Range["A107"].Text = "RATE(A19,-A3,A4)";
sheet.Range["B107"].Formula = "RATE(A19,-A3,A4)";

// Assign RANK formula
sheet.Range["A108"].Text = "RANK(A3,A3:A8)";
sheet.Range["B108"].Formula = "RANK(A3,A3:A8)";

// Assign RSQ formula
sheet.Range["A109"].Text = "RSQ(A3:A8,A18:A18)";
sheet.Range["B109"].Formula = "RSQ(A3:A8,A18:A18)";
```

## Page-level Navigation/TOC
- [Excel Formula Functions]
- [Implementing Functions in XlsIO]
- [Code Examples]

## Cross References
- Refer to the section on handling formulas in `XlsIO`.

<!-- tags: [XlsIO, formula, Excel, functions] keywords: [QUARTILE, RATE, RANK, RSQ, SEARCH, SKEW, SLOPE, SMALL, STDEV, STDEVA, STDEVP, STDEVPA, STEYX, SUBSTITUTE, SUBTOTAL] -->
```