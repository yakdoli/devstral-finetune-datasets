<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_343.jpeg
document_name: grid
page_number: 343
page_id: grid#page_343
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:14Z
fidelity: lossless
-->

## Overview

- This page explains the `RANDBETWEEN`, `RANK`, and `RATE` functions, providing details on their syntax, parameters, and behavior in the context of `Essential Grid for Windows Forms`.
- These functions are vital for data manipulation and financial calculations in grid-based applications.
- It highlights use cases for generating random numbers, determining ranks of values, and computing interest rates per period.

## Content

### Example: RANDBETWEEN

| FORMULA                        | RESULT                                                                                     |
|--------------------------------|---------------------------------------------------------------------------------------------|
| `= RANDBETWEEN(10,20)`         | 12. The value is generated randomly between the given values.                          |

### 4.1.4.6.6.199 RANK

#### Description
Returns the rank of a number in a list of numbers. The rank of a number is its size relative to other values in a list. If you were to sort the list, the rank of the number would be its position.

#### Syntax
```markdown
RANK(number, ref, order)
```

- `number`: The number whose rank you want to find.
- `ref`: An array of or a reference to a list of numbers.
- `order`: A number specifying how to rank numbers.

  - If the order is `0` (zero) or omitted, the number is ranked as if `ref` were a list sorted in descending order.
  - If the order is any nonzero value, the number is ranked as if `ref` were a list sorted in ascending order.

#### Remark
- `RANK` gives duplicate numbers the same rank. However, the presence of duplicate numbers will affect the ranks of subsequent numbers.

### 4.1.4.6.6.200 RATE

#### Description
Returns the interest rate per period of an annuity. `RATE` is calculated by iteration and may not converge to a unique solution.

#### Syntax
```markdown
RATE(nper, pmt, pv, fv, type, guess)
```

- `nper`: The total number of payment periods.
- `pmt`: The payment made each period.
- `pv`: The present value of the annuity.
- `fv`: The future value of the annuity.
- `type`: 0 or 1, indicating when payments are due.
- `guess`: An estimate for the rate.

## API Reference

### `RANK` Function
#### Parameters
- `number`: The number to rank.
- `ref`: Reference to the list or array of numbers.
- `order`: Order of ranking (`0` for descending, any nonzero value for ascending).

#### Returns
An integer indicating the rank of the specified number.

### `RATE` Function
#### Parameters
- `nper`: Number of payment periods.
- `pmt`: Payment made each period.
- `pv`: Present value of the annuity.
- `fv`: Future value of the annuity.
- `type`: Payment timing (0 = end of period, 1 = beginning of period).
- `guess`: An estimate of the rate.

#### Returns
A double indicating the interest rate per period.

## Code Examples

### Example: Using `RANDBETWEEN`

```csharp
int randomNumber = RANDBETWEEN(10, 20);
Console.WriteLine(randomNumber); // Example output: 15
```

### Example: Using `RANK`

```csharp
double[] numbers = { 5, 3, 8, 6, 2 };
int rank = RANK(6, numbers, 1); // Rank in ascending order
Console.WriteLine(rank); // Output: 3
```

### Example: Using `RATE`

```csharp
double interestRate = RATE(60, -100, 0, 1000, 0);
Console.WriteLine(interestRate); // Example output: 0.009933
```

### Conclusion

These functions are essential for performing complex calculations and data analysis directly within grid applications, ensuring flexibility and efficiency in handling numerical data and financial scenarios.

<!-- tags: [grid, essential-grid, windows-forms, finance, functions,Expression, RANDBETWEEN, RANK, RATE] keywords: [random numbers, rank calculation, interest rate, list of numbers, duplicate values, annuity, iteration, order,Present value,future value,payment,period] -->