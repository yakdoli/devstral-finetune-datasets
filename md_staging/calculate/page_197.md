```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_197.jpeg
document_name: calculate
page_number: 197
page_id: calculate#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:51Z
fidelity: lossless
-->

## Overview
- Learn about using the `MODE` function to find the most frequently occurring value in a set of numbers.
- Understand the syntax and usage of the `MONTH` function to return the month from a date represented as a serial number.

## Content

### `MODE`

#### Overview
Returns the most frequently occurring or repetitive value in an array or range of data.

#### Syntax
```markdown
MODE(number1, number2, ...)
```

#### Arguments
- `number1, number2, ...`: Arguments for which you want to calculate the mode.

#### Remarks
- In a set of values, the mode is the most frequently occurring value.

---

### `MONTH`

#### Overview
Returns the month of a date represented by a serial number. The month is given as an integer, ranging from 1 (January) to 12 (December).

#### Syntax
```markdown
MONTH(serial_number)
```

#### Arguments
- `serial_number`: The date of the month you are trying to find. Dates should be entered using the `DATE` function or as results of other formulas or functions. For example, use `DATE(2002,11,12)` for the 12th day of Nov, 2002.

#### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900.

<!-- tags: [syncfusion, winforms, function, mode, month, essential calculate] keywords: [calculate, mode, month, serial number, date, most frequent, integer, data analysis, formula, remarks, january, december, serial numbers, range, arguments] -->
``` 
