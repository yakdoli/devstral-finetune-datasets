```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_205.jpeg
document_name: calculate
page_number: 205
page_id: calculate#page_205
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:16Z
fidelity: lossless
-->

# Essential Calculate

- The arguments must be either numbers or names, array constants or references that contain numbers.
- The formula for the Pearson product moment correlation coefficient, \( r \), is:

\[
r = \frac{\sum(x - \bar{x})(y - \bar{y})}{\sqrt{\sum(x - \bar{x})^2 \sum(y - \bar{y})^2}}
\]

where:
\(\bar{x}\)-bar and \(\bar{y}\)-bar are the sample means AVERAGE(array1) and AVERAGE(array2).

## 4.7.120 PERCENTILE

Returns the k-th percentile of values in a range.

### Syntax

PERCENTILE(array, k)

#### where:

- array is the array or range of data that defines relative standing.
- k is the percentile value in the range 0..1, inclusive.

### Remarks

- k must be >=0 and <= 1.
- If k is not a multiple of \( \frac{1}{(n - 1)} \), PERCENTILE interpolates to determine the value at the k-th percentile.

## 4.7.121 PERCENTRANK

Returns the rank of a value in a data set as a percentage of the data set.

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```