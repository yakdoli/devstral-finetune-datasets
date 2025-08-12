```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: calculate
page_number: 159
page_id: calculate#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:37Z
fidelity: lossless
-->

# Essential Calculate

## Syntax

`COVAR(array1, array2)`

where:
- `array1` is the first cell range of numbers.
- `array2` is the second cell range of numbers.

## Remarks

- The arguments must either be numbers or be names, arrays or references that contain numbers.
- `array1` and `array2` must have the same number of data points.
- The covariance is:

\[
Cov(X,Y) = \frac{\sum (x-\bar{x})(y-\bar{y})}{n}
\]

where:
- \( X \) is `array1`
- \( Y \) is `array2`
- \( \bar{x} \) and \( \bar{y} \) are the sample means AVERAGE(`array1`) and AVERAGE(`array2`).
- \( n \) is the sample size.

### 4.7.33 CRITBINOM

**Returns the smallest value for which, the cumulative binomial distribution is greater than or equal to a criterion value.**

#### Syntax

`CRITBINOM(trials, probability_s, alpha)`

#### where:
- `trials` is the number of Bernoulli trials.
```