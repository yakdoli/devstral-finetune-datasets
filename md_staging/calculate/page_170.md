```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: calculate
page_number: 170
page_id: calculate#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:11Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- y is the value for which you want to perform the inverse of the transformation.
- The equation for the inverse of the Fisher transformation is provided.
- The `Fixed` and `FLOOR` functions are explained.

## Content

### Remarks
- **Inverse of the Fisher Transformation:**
  The equation for the inverse of the Fisher transformation is:
  \[
  x = \frac{e^{2y} - 1}{e^{2y} + 1}
  \]

### 4.7.54 Fixed
The `Fixed` function rounds off to a specified number of decimal places and returns the value in text format.

#### Syntax:
```
Fixed ( number, decimal_places, no_commas )
```
- **Parameters:**
  - `number`: The number you want to round.
  - `decimal_places`: The number of decimal places you want to display in the result.
  - `no_commas`: A logical value. This displays commas when it is set to `FALSE`, and does not display commas when it is set to `TRUE`.

### 4.7.55 FLOOR
Rounds off the given number down, toward zero, to the nearest multiple of significance.

#### Syntax
```
FLOOR(number, significance)
```
- **Parameters:**
  - `number`: The numeric value that you want to round off.
  - `significance`: The multiple to which you want to round the number off.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Essential Calculate, Fixed function, FLOOR function, Fisher Transformation] keywords: [Fisher Transformation, decimal places, rounding, significance, fixed text format] -->
```