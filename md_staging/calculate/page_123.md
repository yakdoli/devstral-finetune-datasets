```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: calculate
page_number: 123
page_id: calculate#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:25Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Describes the functionality of subtotal functions and their handling in nested structures.
- Explains the MROUND function, which rounds numbers to the nearest multiple of a specified value.
- Details the syntax and behavior of the RANDBETWEEN function, which generates random numbers within a specified range.

## Content

### 4.5.6.8 MROUND

The MROUND function rounds a given number up or down to the nearest multiple of a given number.

#### Syntax

The syntax of the MROUND function is:

```
=MROUND(number, multiple)
```

- **Number** – The value to be rounded. This value is required.
- **Multiple** – This value is required.

**Note:** The number must be greater than or equal to half the value of multiple.

#### Errors

- **#NUM!** - Occurs if the number and multiple have different signs.
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example

| FORMULA         | RESULT |
|------------------|--------|
| =MROUND(10, 2.6) | 8      |
| =MROUND(-10, -2.6) | -8     |
| =MROUND(10, -2)  | #NUM!  |

### 4.5.6.9 RANDBETWEEN

The RANDBETWEEN function returns a random number that is between the given ranges. This function returns a new random number each time in recalculation.

#### Syntax

The syntax of the RANDBETWEEN Function is:

```
=RANDBETWEEN(start_num, end_num)
```

- **start_num** – Required. This is the smallest integer.
- **end_num** – Required. This is the largest integer.

#### Errors

- **#NUM!** - Occurs if the end_num value is larger than start_num value.

## API Reference (if applicable)

Not applicable in this context, as the content is focused on function usage and behavior rather than API details.

## Code Examples (multi-language supported)

Not applicable in this context, as the content does not include specific code examples.

## Page-level Navigation/TOC (if applicable)

Not applicable in this context, as the page is focused on explaining two specific functions without a separate TOC.

## Cross References

See also:

- Subtotal functions handling nested subtotals.
- Function behavior in recalculation and error scenarios.

<!-- tags: [calculation, subtotal, mround, randbetween, random number, rounding, error handling, syncfusion, winforms] keywords: [nested subtotal, double counting, rounding rules, random number generation, mround, randbetween, error conditions] -->
```