```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_337.jpeg
document_name: XlsIO
page_number: 337
page_id: XlsIO#page_337
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:30Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explanation of Excel's Data Tables feature and its functionalities.
- Overview of "Automatic except Tables" calculation mode.
- Brief introduction to XlsIO's support for calculation modes.
- Information on how to set the calculation mode using code examples.

## Content

### Automatic Except Tables
Excel's Data Tables feature is designed to perform multiple calculations of the workbook, each driven by different values in the table. So using "Automatic except Tables" will stop Excel from automatically triggering multiple calculations at each calculation, but will still calculate all dependent formulae, except tables.

XlsIO provides support for all the above modes of calculation. Following code example illustrates how to set the calculation mode.

```csharp
[IWorkbook workbook = application.Workbooks.Create();
workbook.CalculationOptions.CalculationMode = ExcelCalculationMode.Manual;
```
```vbnet
Dim workbook as IWorkbook
workbook = application.Workbooks.Create()
workbook.CalculationOptions.CalculationMode = ExcelCalculationMode.Manual
```

There are other options that Excel provides to customize the calculation further.

#### Recalculate Before Save
In Manual mode, this option controls whether Excel will recalculate the workbook as part of the Save process. The default value is set to `True`. You can control this through XlsIO by using the `RecalcOnSave` property of the `ICalculationOptions` interface.

#### Iteration
If you have intentional circular references in your workbook, these settings allow you to control the maximum number of times the workbook will be recalculated (iterations), and the convergence criteria (maximum change: when to stop). The default value should be set to `False`, so that Excel does not try to solve accidental circular references. XlsIO allows to control these iterations as follows.

```csharp
IWorkbook workbook = application.Workbooks.Create();
```

## Page-level Navigation/TOC (if applicable)
- Automatic Except Tables
  - Overview of "Automatic except Tables" calculation mode.
  - Code examples for setting CalculationMode.
- Customizing Calculation Further
  - Recalculate Before Save
  - Iteration

<!-- tags: [XlsIO, Excel, Data Tables, calculation mode, automatic except tables, manual mode, iteration, circular references, calculation options, recalculate before save] -->
```