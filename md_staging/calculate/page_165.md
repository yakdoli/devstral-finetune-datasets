```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: calculate
page_number: 165
page_id: calculate#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:55Z
fidelity: lossless
-->

## Overview
- The Dollar function converts a number to text in currency format, allowing customization of decimal places.
- The EVEN function rounds a number to the nearest even integer, irrespective of its sign.
- The Exact function compares two values for equality without considering their formatting.

## Content

### Dollar
The Dollar function converts a number to text, using a currency format with the pattern `$#,##0.00_($#,##0.00)`.

#### Syntax
```plaintext
Dollar(number, decimal_places)
```
where:
- `number` is the number you want to convert to text.
- `decimal_places` is the number of digits in decimal places you want to display. The value will be rounded accordingly.

### EVEN
Returns the number rounded up to the nearest even integer.

#### Syntax
```plaintext
EVEN(number)
```
where:
- `number` is the value that is to be rounded.

#### Remarks
- Regardless of the sign of the number, a value is rounded up when adjusted away from zero. If the number is an even integer, no rounding occurs.

### Exact
The Exact function compares two values, ignoring the styles, and returns the boolean value as `true` or `false`.

#### Syntax
```plaintext
Exact(value1, value2)
```
where:
- `value1` is the first value you want to compare.
- `value2` is the second value you want to compare.

<!-- tags: [Dollar, EVEN, Exact, number, currency, rounding, boolean comparison, Winforms, version: 11.4.0.26] keywords: [Dollar function, EVEN, rounding to even integer, Exact function] -->
```