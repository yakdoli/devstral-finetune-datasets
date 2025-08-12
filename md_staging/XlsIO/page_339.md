```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_339.jpeg
document_name: XlsIO
page_number: 339
page_id: XlsIO#page_339
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:58Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Disables the calculations of Essential Calculate supported formulas that are added at runtime to the worksheet.
- Illustrates how to disable and enable sheet formula calculations.
- Sample code demonstrating formula evaluation and computation using Essential XlsIO, ensuring compatibility with MS Excel.

## Content

### Disabling Sheet Formula Calculations

Essential XlsIO allows you to disable the calculations of Essential Calculate supported formulas that are added at runtime to the worksheet. The following code sample illustrates how to disable the sheet formula calculations.

```csharp
IWorksheet sheet = workbook.Worksheets[0];
// Formula calculation is enabled for the sheet.
sheet.DisableSheetCalculations();
```

### Enabling and Evaluating Sheet Formula Calculations

Here are some code samples to evaluate some formulas entered by using Essential XlsIO during runtime. The XlsIO computed value is identical to the values computed by using MS Excel.

```csharp
[C#]

// Inserting sample text into the first cell of the first worksheet.
sheet.Range["A1"].Number = 10.99;
sheet.Range["B1"].Number = 10;
sheet.Range["C1"].Formula = "A1+B1";
sheet.Range["D1"].Formula = "AVERAGE(A1:B1)";

// Formula calculation is enabled for the sheet.
sheet.EnableSheetCalculations();

Console.WriteLine(sheet.Range["C1"].CalculatedValue.ToString(), sheet.Range["C1"].Formula);
Console.WriteLine(sheet.Range["D1"].CalculatedValue.ToString(), sheet.Range["D1"].Formula);

// Add more data
sheet.Range["A2"].Number = 11.99;
sheet.Range["B2"].Number = 11;
sheet.Range["C2"].Formula = "A2+B2";
sheet.Range["D2"].Formula = "AVERAGE(A2:B2)";

Console.WriteLine(sheet.Range["C2"].CalculatedValue.ToString(), sheet.Range["C2"].Formula);
```

### Explanation of the Code
- **Disabling and Enabling Calculations**: The `DisableSheetCalculations()` and `EnableSheetCalculations()` methods manage the activation of formula calculations on the worksheet.
- **Formula Input**: Formulas like `=A1+B1` and `=AVERAGE(A1:B1)` are assigned to specific cells.
- **Computed Value Output**: The `CalculatedValue` property retrieves the evaluated result of the formulas, ensuring consistency with MS Excel computations.

## API Reference

### Essential XlsIO Methods
- `DisableSheetCalculations()`: Disables all calculations on the worksheet.
- `EnableSheetCalculations()`: Enables all calculations on the worksheet.
- `Range[string cellAddress].Number`: Sets the numerical value for the specified cell.
- `Range[string cellAddress].Formula`: Assigns a formula to the specified cell.
- `Range[string cellAddress].CalculatedValue`: Retrieves the evaluated result of the formula in the specified cell.

### Parameters
- `cellAddress`: Specifies the cell address in the format `A1`, `B2`, etc.
- `Number`: Numeric value to be assigned to the cell.
- `Formula`: String representation of the formula to be assigned.

### Returns
- `CalculatedValue`: The evaluated result of the formula as a numerical value.

## Code Examples

The provided code examples demonstrate the use of Essential XlsIO to handle formula calculations, ensuring that the results are consistent with those computed by MS Excel. This flexibility makes it suitable for scenarios requiring runtime formula evaluations while maintaining compatibility with Excel.

## Cross References
- Refer to the documentation for `Formula` and `CalculatedValue` properties for more information.
- See related sections on handling Excel formulas and computations for additional examples and best practices.

<!-- tags: [Essential XlsIO, formula calculations, runtime formulas, calculation management] keywords: [disable, enable, calculated values, compatibility, Excel, formula, computations, runtime, disabled, enabled] -->
```
