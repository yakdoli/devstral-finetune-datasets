```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_329.jpeg
document_name: XlsIO
page_number: 329
page_id: XlsIO#page_329
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:34Z
fidelity: lossless
-->

## Overview
- Demonstrates the use of various Excel formula functions such as `SUM`, `SUMIF`, `SUMPRODUCT`, and more within a worksheet.
- Closely matches the Excel formula fields and their corresponding names, ensuring accurate formula implementation.
- Illustrates how to set both the text and formula for cells programmatically.

## Content

The following code snippets illustrate how to set specific formulas and text descriptions for cells in an Excel worksheet using the XlsIO library.

### Formula Implementation

#### Basic Functions
```csharp
sheet.Range["A122"].Text = "SUM(A3:A8,A13:A18)";
sheet.Range["B122"].Formula = "SUM(A3:A8,A13:A18)";
```
- `SUM`: Sums up the values from the specified ranges (A3:A8 and A13:A18).

```csharp
sheet.Range["A123"].Text = "SUMIF(A3:A8,\">300\",A13:A18)";
sheet.Range["B123"].Formula = "SUMIF(A3:A8,\">300\",A13:A18)";
```
- `SUMIF`: Sums up the values in A13:A18 where the corresponding values in A3:A8 are greater than 300.

```csharp
sheet.Range["A124"].Text = "SUMPRODUCT(A3:A8,A13:A18)";
sheet.Range["B124"].Formula = "SUMPRODUCT(A3:A8,A13:A18)";
```
- `SUMPRODUCT`: Calculates the sum of the products of the corresponding entries in the specified arrays.

```csharp
sheet.Range["A125"].Text = "SUMSQ(A3:A8)";
sheet.Range["B125"].Formula = "SUMSQ(A3:A8)";
```
- `SUMSQ`: Returns the sum of the squares of the provided arguments.

#### Advanced Statistical Functions
```csharp
sheet.Range["A126"].Text = "SUMX2MY2(A3:A8,A13:A18)";
sheet.Range["B126"].Formula = "SUMX2MY2(A3:A8,A13:A18)";
```
- `SUMX2MY2`: Returns the sum of the difference of squares of corresponding values in two arrays.

```csharp
sheet.Range["A127"].Text = "SUMX2PY2(A3:A8,A13:A18)";
sheet.Range["B127"].Formula = "SUMX2PY2(A3:A8,A13:A18)";
```
- `SUMX2PY2`: Returns the sum of the sum of squares of corresponding values in two arrays.

```csharp
sheet.Range["A128"].Text = "SUMXMY2(A3:A8,A13:A18)";
sheet.Range["B128"].Formula = "SUMXMY2(A3:A8,A13:A18)";
```
- `SUMXMY2`: Returns the sum of the product of differences of corresponding values in two arrays.

#### Financial and Date-Time Functions
```csharp
sheet.Range["A129"].Text = "SYD(A3,A4,A5,A19)";
sheet.Range["B129"].Formula = "SYD(A3,A4,A5,A19)";
```
- `SYD`: Returns the sum-of-years’ digits depreciation of an asset for a specified period.

```csharp
sheet.Range["A130"].Text = "TDIST(A3,1,A19)";
sheet.Range["B130"].Formula = "TDIST(A3,1,A19)";
```
- `TDIST`: Returns the percentage points (probability) for the Student t-distribution.

```csharp
sheet.Range["A131"].Text = "TIMEVALUE(B10)";
sheet.Range["B131"].Formula = "TIMEVALUE(B10)";
```
- `TIMEVALUE`: Converts a time in text format to a decimal number that can be used in mathematical calculations.

```csharp
sheet.Range["A132"].Text = "TINV(A8,A4)";
sheet.Range["B132"].Formula = "TINV(A8,A4)";
```
- `TINV`: Returns the t-value of the Student’s t-distribution as a function of the probability and the degrees of freedom.

```csharp
sheet.Range["A133"].Text = "TRANSPOSE({150,2,3,4,5,20})";
sheet.Range["B133"].Formula = "TRANSPOSE({150,2,3,4,5,20})";
```
- `TRANSPOSE`: Returns a vertical range of cells as a horizontal range, or vice versa.

```csharp
sheet.Range["A134"].Text = "TREND({150,2,3,4,5,20},{110,21,6,1,3,50})";
sheet.Range["B134"].Formula = "TREND({150,2,3,4,5,20},{110,21,6,1,3,50})";
```
- `TREND`: Returns values along a linear trend.

```csharp
sheet.Range["A135"].Text = "TRIMMEAN(A3:A8,A18)";
sheet.Range["B135"].Formula = "TRIMMEAN(A3:A8,A18)";
```
- `TRIMMEAN`: Returns the mean of the interior of a data set, excluding a percentage of the data points from the top and bottom tails.

```csharp
sheet.Range["A136"].Text = "TTEST(A3:A8,A13:A18,1,1)";
sheet.Range["B136"].Formula = "TTEST(A3:A8,A13:A18,1,1)";
```
- `TTEST`: Returns the probability associated with a Student’s t-test.

## Code Examples

The following examples demonstrate how to programmatically assign formulas to specific cells:

```csharp
// Assigning a formula to a range
sheet.Range["B122"].Formula = "SUM(A3:A8,A13:A18)";
// Assigning a text description to a range
sheet.Range["A122"].Text = "SUM(A3:A8,A13:A18)";

// Transposing a data set
sheet.Range["B133"].Formula = "TRANSPOSE({150,2,3,4,5,20})";
sheet.Range["A133"].Text = "TRANSPOSE({150,2,3,4,5,20})";

// Performing a trend analysis
sheet.Range["B134"].Formula = "TREND({150,2,3,4,5,20},{110,21,6,1,3,50})";
sheet.Range["A134"].Text = "TREND({150,2,3,4,5,20},{110,21,6,1,3,50})";
```

## Cross References
- Refer to the "Working with Formulas" section for more detailed information on formula implementation.
- For additional examples, see the "Formula Examples" section.

<!-- tags: [xlsio, formulas, programming, worksheet, functions] keywords: [sum, sumif, sumproduct, sumsq, sumxmy2, sumx2my2, sumx2py2, syd, tdist, timevalue, tinv, transpose, trend, trimmean, ttest, workbook, ranges, office, spreadsheet] -->
```
