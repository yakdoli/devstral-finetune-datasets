```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_359.jpeg
document_name: grid
page_number: 359
page_id: grid#page_359
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:20Z
fidelity: lossless
--> 

## Overview

- Explanation of the `SUBTOTAL` function.
- Detailed syntax and function list for calculating subtotals within a list.
- Description of the `Sum` function and its use in adding numbers.

## Content

### SUBTOTAL Function

#### Syntax:
The syntax of the `SUBTOTAL` function is:
```
=SUBTOTAL (function_Number, ref1, (ref2),...)
```

A `function_Number` is required. This specifies which function to use in calculating subtotals within a list. Here is the list of functions supported by Syncfusion:

| FUNCTION NUMBER | FUNCTION NAME |
|------------------|---------------|
| 1               | AVERAGE       |
| 2               | COUNT         |
| 3               | COUNTA        |
| 4               | MAX           |
| 5               | MIN           |
| 6               | PRODUCT       |
| 7               | STDEV         |
| 8               | STDEVP        |
| 9               | SUM           |
| 10              | VAR           |

**Ref1**: The first named range which is used for the subtotal. This value is required.  
**Ref2**: This value is optional.

#### Remarks:
- If the subtotal function has any nested subtotal functions, then the nested subtotal is ignored for double counting.

### Sum Function

The `Sum` function adds all numbers in a range of cells and returns the result.

#### Syntax:
Sum(number1, number2, ... number_n)

where:
- `number1` is the first number,
- `number2` is the second,
- `number_n` is the nth number to be added together.

## API Reference (if applicable)

### Subtotal Function Parameters

| Name            | Type | Description |
|------------------|------|-------------|
| function_Number | int  | Function number specifying the type of calculation to perform. |
| ref1            | Range| First referenced range or named range used for the subtotal. |
| ref2            | Range| Optional referenced range or named range used for the subtotal. |

### Sum Function Parameters

| Name          | Type | Description               |
|---------------|------|---------------------------|
| number1       | int  | First number to be added. |
| number2       | int  | Second number to be added.|
| number_n      | int  | nth number to be added.   |

## Code Examples (multi-language supported)

Example of using the `SUBTOTAL` function:
```csharp
// Calculating the SUM subtotal using the SUM function (function_number 9)
double subtotal = worksheet.Cells.SubTotal(9, "A1:A10");
```

Example of using the `Sum` function:
```csharp
// Summing numbers
double total = worksheet.Cells.Sum(10, 20, 30);
```

## Cross References

- See also:
  - Overview of functions supported by Syncfusion in Windows Forms.
  - Detailed usage of grid controls in Windows Forms applications.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, SUBTOTAL function, SUM function, grid, Windows Forms] keywords: [SUBTOTAL, SUM, function_Number, ref1, ref2, subtotal, sum, numbers] -->
```