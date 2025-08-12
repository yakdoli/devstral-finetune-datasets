```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_186.jpeg
document_name: calculate
page_number: 186
page_id: calculate#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:23Z
fidelity: lossless
-->

## Essential Calculate

- If there are fewer than four data points or if the standard deviation of the sample equals zero, KURT returns the `#DIV/0!` error value.
- Kurtosis is defined as:

  \[
  \left\{ \frac{n(n+1)}{(n+1)(n+2)(n+3)} \sum \left( \frac{x_i - \overline{x}}{s} \right)^4 \right\} - \frac{3(n+1)^2}{(n+2)(n+3)}
  \]

  where:
  - \( s \) is the sample standard deviation.

## 4.7.85 LARGE

### Overview
- Returns the k-th largest value in a data set.

### Syntax
```
LARGE(array, k)
```

#### Parameters
- `array`: The array or range of data for which you want to determine the k-th largest value.
- `k`: The position (from the largest) in the array or cell range of data to return.

### Remarks
- If \( n \) is the number of data points in a range, then `LARGE(array, 1)` returns the largest value, and `LARGE(array, n)` returns the smallest value.

## 4.7.86 LEFT

### Overview
- `LEFT` returns the first character or characters in a text string, based on the number of characters you specify.

### Syntax
```
LEFT(text, [num_chars])
```

<!-- tags: [syncfusion, winforms, calculate, kurtosis, large, left, statistic, largest value, text operations, API reference] keywords: [kurtosis formula, standard deviation, array, k position, text string, num_chars, greatest, smallest] -->
```