```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_285.jpeg
document_name: grid
page_number: 285
page_id: grid#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Documentation for the `ERROR.TYPE` function in Syncfusion Grid.
- Lists error types and their codes.
- Demonstrates how to use the `ERROR.TYPE` function in formulas.
- Explanation of the `EXP` and `EXPONDIST` functions.

## Content

### Error Types and Error Codes

#### Table: Error Types and Return Values

| Given Value        | Return value of function |
|--------------------|--------------------------|
| `#NULL!`           | 1                        |
| `#DIV/0!`          | 2                        |
| `#VALUE!`          | 3                        |
| `#REF!`            | 4                        |
| `#NAME?`           | 5                        |
| `#NUM!`            | 6                        |
| `#N/A`             | 7                        |
| `#GETTING_DATA`    | 8                        |
| Anything else      | `#N/A`                   |

#### Example of `ERROR.TYPE` Function Usage

| FORMULA              | RESULT             |
|----------------------|--------------------|
| `= ERROR.TYPE(#NULL!)` | 1                  |
| `= ERROR.TYPE(even)`    | `#NA`              |

### `EXP` Function

#### Description
Returns e raised to the power of the given number.

#### Syntax
`EXP(number)`

Where:
- `number` is the exponent applied to the base e.

### `EXPONDIST` Function

#### Description
Returns the exponential distribution.

#### Syntax
Not explicitly detailed in the provided image.

## API Reference

### `ERROR.TYPE` Function
- **Parameters**:
  - `value`: The error value to evaluate.
- **Returns**:
  - An integer code corresponding to the type of error.

### `EXP` Function
- **Parameters**:
  - `number`: The exponent applied to the base e.
- **Returns**:
  - The result of e raised to the power of the given number.

### `EXPONDIST` Function
- **Returns**:
  - The exponential distribution value.

## Code Examples

#### Example 1: Using `ERROR.TYPE` Function
```csharp
// Example formula
= ERROR.TYPE(#NULL!)
// Result
1
```

#### Example 2: Using `ERROR.TYPE` Function with Logical Expression
```csharp
// Example formula
= ERROR.TYPE(even)
// Result
#N/A
```

#### Example 3: Using `EXP` Function
```csharp
// Example formula
XP(2)
// Result
e^2
```

## Page-level Navigation/TOC

- Error Types and Error Codes
- Example of Error Types in Formulas
- `EXP` Function
- `EXPONDIST` Function

## Cross References

- See also: Other functions and features in Syncfusion Grid.

<!-- tags: [syncfusion, grid, windows forms, error handling, exp, expondist, function reference] keywords: [error type, null error, division error, value error, reference error, name error, number error, not available error, getting data error, exponential function, exponential distribution] -->
```