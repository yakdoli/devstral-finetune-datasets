```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: calculate
page_number: 148
page_id: calculate#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:54Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Implements a simple calculation engine.
- Covers functions for calculating averages.
- Explains syntax and usage of AVERAGEA, AVG, and BINOMDIST functions.

## Content

### AVERAGEA

#### Syntax
```plaintext
AVERAGEA(value1, value2,...)
```

#### Where:
- `value1, value2, ...` are cells, ranges of cells, or values for which you want the average.

#### Remarks
- The arguments must be numbers, names, arrays, or references.
- Array or reference arguments that contain text evaluate as 0 (zero).
- If the calculation should not include text values in the average, then use the AVERAGE function.
- Arguments that contain True evaluate as 1; arguments that contain False evaluate as 0 (zero).

### 4.7.13 AVG

#### Returns
The average (arithmetic mean) of the arguments.

#### Syntax
```plaintext
AVG(number1, number2,...)
```

#### Where:
- `number1, number2, ...` are numeric arguments for which you want the average.

#### Remarks
- This method is the same as AVERAGE and is included for compatibility purposes.

### 4.7.14 BINOMDIST

#### Returns
The individual term binomial distribution probability.

#### Syntax

<!-- Calculate#page_148 -->
``` 
© 2013 Syncfusion. All rights reserved. 148 | Page
```

## Tag and Keywords
<!-- tags: [essential, calculate, averagea, avg, binomdist, function, syntax, average, arithmetic mean, binomial distribution, user guide, syncfusion winforms] keywords: [average, binomial probability, calculation engine, reference, numeric parameters, text evaluation, compatibility, arithmetic mean, winforms, 11.4.0.26] -->
``` 
