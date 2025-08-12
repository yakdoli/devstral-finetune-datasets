```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_308.jpeg
document_name: grid
page_number: 308
page_id: grid#page_308
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:53Z
fidelity: lossless
-->

## Remarks

- The arguments must be either numbers or names, arrays or references that contain numbers.
- If an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with the value zero are included.
- If there are fewer than four data points or if the standard deviation of the sample equals zero, KURT returns the #DIV/0! error value.
- Kurtosis is defined as:

\[
\left\{\frac{n(n+1)}{(n+1)(n+2)(n+3)} \sum\left(\frac{x_i-\bar{x}}{s}\right)^{4}\right\}-\frac{3(n+1)^{2}}{(n+2)(n+3)}
\]

where \( s \) is the sample standard deviation.

### 4.1.4.6.6.128 LARGE

**Returns the k-th largest value in a data set.**

#### Syntax

**LARGE(array, k)**, where:

- **array** is the array or range of data for which you want to determine the k-th largest value.
- **k** is the position (from the largest) in the array or cell range of data to return.

#### Remarks

- If \( n \) is the number of data points in a range, then LARGE(array,1) returns the largest value, and LARGE(array,n) returns the smallest value.

### 4.1.4.6.6.129 LCM

**The LCM function returns the least common multiple of two or more given values. The values must be numeric values.**

#### Syntax
<!-- end of the structured content -->

<!-- tags: [syncfusion, winforms, large, kurt, lcm, function, kurtosis, largest, least common multiple] keywords: [array, k, n, data points, sample standard deviation, remarks, syntax] -->
```