```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_321.jpeg
document_name: grid
page_number: 321
page_id: grid#page_321
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Describes error handling for when cells in an array are empty or contain strings.
- Highlights cases where #VALUE! occurs in calculations with arrays.

## Content

### 4.1.4.6.6.155 MOD

#### Description
Returns the remainder after the number is divided by a divisor. The result has the same sign as the divisor.

#### Syntax
```markdown
MOD(number, divisor)
```

#### Parameters
- **number**: The number for which you want to find the remainder.
- **divisor**: The value by which you want to divide the number.

#### Remarks
- The MOD function can be expressed in terms of the INT function:
  ```
  MOD(n, d) = n - d * INT(n/d)
  ```

### 4.1.4.6.6.156 MODE

#### Description
Returns the most frequently occurring or repetitive value in an array or range of data.

#### Syntax
```markdown
MODE(number1, number2, ...)
```

#### Parameters
- **number1, number2, ...**: Arguments for which you want to calculate the mode.

#### Remarks
- In a set of values, the mode is the most frequently occurring value.

## API Reference

### Methods
- **MOD(number, divisor)**: Returns the remainder after division.
- **MODE(number1, number2, ...)**: Returns the mode of a set of values.

## Code Examples

### C#
```csharp
using System;

int number = 10;
int divisor = 3;
int result = number % divisor; // Using C#'s modulus operator
Console.WriteLine($"MOD({number}, {divisor}) = {result}");

int[] numbers = { 1, 2, 2, 2, 3, 4, 5 };
int mode = numbers.GroupBy(n => n).OrderByDescending(g => g.Count()).First().Key;
Console.WriteLine($"Mode of {string.Join(", ", numbers)} = {mode}");
```

### VB
```vb
Imports System

Module Example
    Sub Main()
        Dim number As Integer = 10
        Dim divisor As Integer = 3
        Dim result As Integer = number Mod divisor
        Console.WriteLine($"MOD({number}, {divisor}) = {result}")

        Dim numbers() As Integer = {1, 2, 2, 2, 3, 4, 5}
        Dim mode As Integer = numbers.GroupBy(Function(n) n).OrderByDescending(Function(g) g.Count()).First().Key
        Console.WriteLine($"Mode of {string.Join(", ", numbers)} = {mode}")
    End Sub
End Module
```

## Cross References

- See also: array operations, error handling, mathematical functions, statistical functions.

<!-- tags: [essential grid, windows forms, mode, mod, array, mathematical functions, statistical analysis] keywords: [mode, mod, arrays, divisor, remainder, frequently occurring value,頻繁出現的值，數學函數，統計分析] -->
```