```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: calculate
page_number: 124
page_id: calculate#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:37Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains conditions under which errors like #VALUE! and #NUM! occur in calculations.
- Demonstrates the usage of functions such as RAND BETWEEN, SQRTPI, and QUOTIENT.

## Content

### #VALUE! Error
Occurs if any of the given arguments are non-numeric.

#### Example
| FORMULA                          | RESULT                                                                  |
|----------------------------------|-------------------------------------------------------------------------|
| = RAND BETWEEN (`10`, `20`)     | `12`<br>The value is generated randomly between the given values. |

### 4.5.6.10 SQRTPI

The SQRTPI function returns the square root of a given number multiplied by π. Here π is the constant math value.

#### Syntax
The syntax of the SQRTPI function is:
```
=SQRTPI (number)
```
- **number** – Required.

#### Error Conditions
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example
| FORMULA                          | RESULT                     |
|----------------------------------|----------------------------|
| = SQRTPI (`2`)                  | `2.506628`                |
| = SQRTPI (`-2`)                 | `#NUM!`                   |

### 4.5.6.11 QUOTIENT

The QUOTIENT function returns the integer portion of a division between two given numbers. The returned value will be an integer value.

#### Syntax
The syntax of the QUOTIENT function is:
```
=QUOTIENT (numerator, denominator)
```
- **Numerator** – Required.
- **Denominator** – Required.

## RAG Annotations
<!-- tags: [error handling, numeric functions, math, sqrt, integer division, winforms] keywords: [#VALUE!, #NUM!, RAND BETWEEN, SQRTPI, QUOTIENT, math functions, division, integer portion, numeric arguments] -->
```