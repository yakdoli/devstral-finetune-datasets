```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_271.jpeg
document_name: grid
page_number: 271
page_id: grid#page_271
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:35Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains the use of conditional computation functions like `If` and `SumIf`.
- It describes the `COVAR` and `COVARIANCE.P` functions used to calculate covariance.

## Content

### Conditional Computation Functions
- Other library functions such as `If` and `SumIf` can be used to conditionally compute values.

#### COVAR
- **Description:** Returns covariance, which is the average of the products of deviations for each data point pair.
- **Syntax:**
  ```
  COVAR(array1, array2)
  ```
  Where:
  - `array1` is the first cell range of numbers.
  - `array2` is the second cell range of numbers.
- **Remarks:**
  - Arguments must be numbers or references featuring numbers.
  - `array1` and `array2` must have the same number of data points.
  - The covariance formula is:
    \[
    \text{Cov}(X, Y) = \frac{\sum{(x - \overline{x})(y - \overline{y})}}{n}
    \]
    Where:
    - \( X \) is array1.
    - \( Y \) is array2.
    - \( \overline{x} \) and \( \overline{y} \) are the sample means AVERAGE(array1) and AVERAGE(array2).
    - \( n \) is the sample size.

#### COVARIANCE.P
- **Description:** Retrieves population covariance, the average of the products of deviations for each data point pair in two data sets.
- **Syntax:**
  ```
  COVARIANCE.P(array1, array2)
  ```
  Where:
  - `array1` is the first cell range of integers.
  - `array2` is the second cell range of integers.

<!-- tags: [syncfusion, essentialgrid, windowsforms, covariance, coventfunction, functionguide] keywords: [essentialgrid, windowsforms, covar, covariance, covariance.p, covent, libraryfunctions, conditionalcompute, gridcontrol] -->
```