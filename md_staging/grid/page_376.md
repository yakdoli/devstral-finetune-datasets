```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_376.jpeg
document_name: grid
page_number: 376
page_id: grid#page_376
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:16Z
fidelity: lossless
-->

## Overview

- This page explains the syntax and usage of financial and logical functions like `XIRR`, `XOR`, and `YEAR` in the context of Windows Forms development. These functions are used for financial calculations and logical operations in software applications.

## Content

### 4.1.4.6.6.263 XOR

The `XOR` function returns the exclusive OR for the given arguments.

#### Syntax

```markdown
XOR(logical_value1, logical_value2,...)
```

- **Logical_value1**: Required. This can be either TRUE or FALSE, and can be logical values, arrays, or references.

#### Notes

If the given arguments do not have logical values, XOR returns the `#VALUE!` error value.

#### Example

| FORMULA          | RESULT |
|------------------|--------|
| = XOR(5>0, 7<9 ) | FALSE  |
| =XOR(3>12, 4>6) | TRUE   |

### 4.1.4.6.6.264 YEAR

The `YEAR` function returns the year corresponding to a date. The year is returned as an integer in the range 1900-9999.

#### Syntax

```markdown
YEAR(serial_number)
```

- **serial_number**: The serial number representing a date.

## API Reference

### Functions

#### XIRR(cashflow, datelist, value)
- **Parameters**:
  - `cashflow`: The range of cash flow.
  - `datelist`: The list of serial number of the corresponding date values.
  - `value`: An initial guess integer value which reflects in the result of the function.
- **Returns**: A calculated internal rate of return.

#### XOR(logical_value1, logical_value2,...)
- **Parameters**:
  - `logical_value1`: Required logical values.
- **Returns**: A boolean result representing the exclusive OR of the given arguments.

#### YEAR(serial_number)
- **Parameters**:
  - `serial_number`: The serial number representation of a date.
- **Returns**: An integer representing the year in the range 1900-9999.

## Code Examples

Here are examples of using the `XOR` and `YEAR` functions in practice:

```csharp
// Example usage of XOR function
bool result1 = false;
bool result2 = true;

bool xorResult1 = xor(result1, result2); // Output: TRUE

// Example usage of YEAR function
double dateSerial = 44197; // Serial number representing a date
int year = year(dateSerial); // Output: 2024 (example year)
```

## Cross References

See also:
- `XIRR` function for financial calculations.
- Documentation on Windows Forms for more functions and methods.

<!-- tags: [Windows Forms, financial functions, logical functions, XIRR, XOR, YEAR, Syncfusion Windows Forms] keywords: [internal rate of return, cash flow, exclusive OR, date serial, year, logical values, boolean operations] -->
```