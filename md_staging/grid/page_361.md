```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_361.jpeg
document_name: grid
page_number: 361
page_id: grid#page_361
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:14Z
fidelity: lossless
-->

## Overview
- Demonstrates the use of Excel-like functions such as SUMIFS, SUMPRODUCT, and SUMSQ in the context of Syncfusion Winforms for Windows Forms.
- Explains the syntax and usage of SUMPRODUCT and SUMSQ functions, highlighting their relevance in performing calculations on multiple arrays.

## Content

### Table of Data
|   | A       | B        | C    |
|---|---------|----------|------|
| 1 | Earning | Tax      | other |
| 2 | 100000 | 3000     | 100  |
| 3 | 200000 | 6000     | 200  |
| 4 | 300000 | 7500     | 300  |
| 5 | 400000 | 9000     | 500  |

### Example: SUMIFS
| FORMULA                                          | RESULT |
|--------------------------------------------------|--------|
| SUMIFS(C2:C5, B2:B5, ">7000", B2:B5, "<10000") | 800    |

### 4.1.4.6.6.234 SUMPRODUCT
**Multiples corresponding components in the given arrays and returns the sum of those products.**

#### Syntax
SUMPRODUCT(array1, array2, array3, ...), where:

- **array1, array2, array3, ...** are 2 to 30 arrays whose components you will want to multiply and then add.

#### Remarks
- The array arguments must have the same dimensions.
- SUMPRODUCT treats array entries that are not numeric as if they were zeros.

### 4.1.4.6.6.235 SUMSQ
**Returns the sum of the squares of the arguments.**

#### Syntax
SUMSQ(number1, number2, ...), where:

<!-- tags: [Winforms, SUMIFS, SUMPRODUCT, SUMSQ, Excel functions, Syncfusion] -->
```