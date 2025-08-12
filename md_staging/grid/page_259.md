```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_259.jpeg
document_name: grid
page_number: 259
page_id: grid#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:54Z
fidelity: lossless
-->

## Overview

- Describes the formula and its result.
- Details the syntax and usage of the `AVG` function for calculating the average of numeric arguments.
- Explains the `BASE` function for converting numbers into text representations with a specified radix.
- Outlines the `BigMul` function for multiplying two 32-bit numbers.

## Content

### Formula and Result

| FORMULA                                                                 | RESULT |
|--------------------------------------------------------------------------|--------|
| AVERAGEIFS(C2:C5, B2:B5, ">7000", B2:B5, "<10000")                     | 400    |

### 4.1.4.6.6.22 AVG

#### Description

Returns the average (arithmetic mean) of the arguments.

#### Syntax

```
AVG(number1, number2, ...)
```

Where:
- `number1, number2, ...` are numeric arguments for which you want the average.

#### Remarks

- This method is the same as `AVERAGE` and is included for compatibility purposes.

---

### 4.1.4.6.6.23 BASE

#### Description

A number has been converted into a text representation with the given radix (base).

#### Syntax

```
BASE(Number, Radix [Min_length])
```

Where:
- `Number` is the value that you want to convert.
- `Radix` is the base radix that you want to convert the number into.
- `Min_length` is the minimum length of the returned string. `Min_length` is optional.

#### Remarks:

- `#NUM!` - occurs if `Number`, `Radix`, or `Min_length` are outside the minimum or maximum constraints.
- `#VALUE!` - occurs if `Number` is a non-numeric value.

---

### 4.1.4.6.6.24 BigMul

#### Description

The `BigMul` function gives the full value of multiplying two 32-bit numbers.

#### Syntax

[Unclear: syntax details are not provided in the image.]

## Page-level Navigation/TOC (if applicable)

- Formula and Result
- 4.1.4.6.6.22 AVG
- 4.1.4.6.6.23 BASE
- 4.1.4.6.6.24 BigMul

---

<!-- tags: [syncfusion-winforms, formula, average, base-conversion, multiplication] keywords: [formula, averageifs, avg, base, bigmul, 32-bit multiplication] -->
```