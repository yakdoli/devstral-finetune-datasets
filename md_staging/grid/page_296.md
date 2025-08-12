```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_296.jpeg
document_name: grid
page_number: 296
page_id: grid#page_296
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Provides information on mathematical functions such as GCD, GEOMEAN, and Growth.
- Explains the calculation of the geometric mean and exponential growth.
- Includes formula results and a method table for reference.

## Content

### GCD

The following table shows formula examples and their results:

| FORMULA       | RESULT  |
|---------------|---------|
| `= GCD(5, 3, 2)` | `1`    |
| `= GCD(-2)`   | `#NUM!` |

### 4.1.4.6.6.102 GEOMEAN

**Returns the geometric mean of an array or range of positive data.**

#### Syntax

`GEOMEAN(number1, number2, ...)`

where:

- `number1, number2, ...` are arguments for which you want to calculate the mean.

#### Remarks

- The arguments must be either numbers or names, arrays, or references that contain numbers.
- All values must be positive.
- The equation for the geometric mean is:

\[
GM = \left( \prod_{1}^{n} y_{i} \right)^{\frac{1}{n}}
\]

### 4.1.4.6.6.103 Growth

**This feature enables you to calculate predicted exponential growth using existing data. This calculates and returns an array of values used for the regression analysis. Growth enables you to perform a regression analysis.**

#### Table 4: Method Table

| Method  | Description                                                     | Parameters                           | Type    | Return Type | Reference links |
|---------|-----------------------------------------------------------------|---------------------------------------|---------|--------------|-----------------|
| Growth() | Calculates the Growth for an array of cells.                  | Known y's, Known x's, new_x's       | Method  | String       | N/A             |

## Page-level Navigation/TOC (if applicable)

- [GCD]
- [4.1.4.6.6.102 GEOMEAN]
- [4.1.4.6.6.103 Growth]

## Cross References

- Related topics can be found in the method table and formula sections above.

<!-- tags: [GCD, GEOMEAN, Growth, Windows Forms, Grid, Essential Grid, Syncfusion, mathematical functions, geometric mean, exponential growth] keywords: [GCD, GEOMEAN, Growth, array, positive data, geometric mean, exponential growth, regression analysis, Windows Forms, Grid, algebraic calculations, synchronization, reference links] -->
```