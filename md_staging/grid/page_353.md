```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_353.jpeg
document_name: grid
page_number: 353
page_id: grid#page_353
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

This section explains how to use the `SQRT` and `SQRTPI` functions effectively in numerical data analysis. It covers the syntax, parameters, and remarks necessary to calculate square roots and square roots multiplied by π.

## Content

### Overview of Functions

- **array**: An array or range of numerical data for which you want to determine the k-th smallest value.
  - **k**: The position (from the smallest) in the array or range of data to return.

### 4.1.4.6.6.220 SQRT

#### Description
Returns a positive square root.

#### Syntax
SQRT(number), where:

- **number**: The number for which you want the square root.

#### Remarks
- **Number must be >= 0.**

### 4.1.4.6.6.221 SQRTPI

#### Description
The `SQRTPI` function returns the square root of a given number multiplied by π. Here π is the constant math value.

#### Syntax
The syntax of the `SQRTPI` function is:
``` 
=SQRTPI (number)
```
- **number - Required**.

#### Remarks:
- **#NUM!**: If the number is less than zero (0).
- **#VALUE!**: Occurs if any of the given arguments are non-numeric.

### Example:
The following example illustrates the use of the `SQRTPI` function:

| FORMULA      | RESULT      |
|--------------|-------------|
| =SQRTPI (2) | 2.506628    |

## API Reference

### SQRTPI
- **Syntax**: `=SQRTPI (number)`
- **Parameters**:
  - **number**: The number for which you want the square root multiplied by π.
- **Returns**: The square root of the given number multiplied by π.
- **Exceptions**:
  - **#NUM!**: If the number is less than zero (0).
  - **#VALUE!**: If any of the given arguments are non-numeric.

### Code Examples
```csharp
// Example of using SQRTPI in C#
double result = Math.Sqrt(Math.PI * 2); // This would return 2.506628
```

### Cross References
See also:
- [Mathematical Functions](#mathematical-functions)
- [Numerical Data Analysis](#numerical-data-analysis)

---

<!-- tags: [syncfusion, grid, mathematical functions, windows forms, version: 11.4.0.26] keywords: [SQRT, SQRTPI, numerical data, windows forms, grid control, √, π, math,数值分析] -->
```