```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_322.jpeg
document_name: XlsIO
page_number: 322
page_id: XlsIO#page_322
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:18Z
fidelity: lossless
-->

# XlsIO

## Overview
- XlsIO provides support for reading and writing around 520+ predefined Excel functions.
- Describes how to enter formulas in a spreadsheet using the Formula property.
- Demonstrates the usage of built-in Excel functions with XlsIO APIs.

## Content

### Formula Writing

You can enter formulas in a spreadsheet by using the `Formula` property. Following code example illustrates the built-in function of Excel by using XlsIO APIs.

```csharp
// Excel Functions
sheet.Range["A22"].Text = "ABS(ABS(-A3))";
sheet.Range["B22"].Formula = "ABS(ABS(-A3))";

sheet.Range["A23"].Text = "ABS(ABS(-100))";
sheet.Range["B23"].Formula = "ABS(ABS(-100))";

sheet.Range["A24"].Text = "-A3";
sheet.Range["B24"].Formula = "-A3";

sheet.Range["A25"].Text = "ACOS(A8)";
sheet.Range["B25"].Formula = "ACOS(A8)";

sheet.Range["A26"].Text = "ADDRESS(1,1)";
sheet.Range["B26"].Formula = "ADDRESS(1,1)";

sheet.Range["A27"].Text = "ADDRESS(1,1,2)";
sheet.Range["B27"].Formula = "ADDRESS(1,1,2)";

sheet.Range["A28"].Text = "ADDRESS(1,1,3)";
sheet.Range["B28"].Formula = "ADDRESS(1,1,3)";

sheet.Range["A29"].Text = "ADDRESS(1,1,4)";
sheet.Range["B29"].Formula = "ADDRESS(1,1,4)";

sheet.Range["A30"].Text = "ASIN(A8)";
sheet.Range["B30"].Formula = "ASIN(A8)";

sheet.Range["A31"].Text = "ATAN(A8)";
sheet.Range["B31"].Formula = "ATAN(A8)";

sheet.Range["A32"].Text = "ATANH(A8)";
```

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [XlsIO, formula writing, Excel functions, built-in functions, XlsIO APIs] keywords: [formula property, text property, sheet range, built-in Excel functions, Excel support, XlsIO, C#] -->
```