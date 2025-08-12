```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_234.jpeg
document_name: calculate
page_number: 234
page_id: calculate#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:56Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- TRIMMEAN calculates the mean of a data set after excluding a specified percentage of data points from the top and bottom tails.
- The True function returns the logical value for True.
- TRUNC truncates a number to an integer by removing the fractional part of the number.

## Content

### 4.7.173 TRIMMEAN

**Description:**
Returns the mean of the interior of a data set. TRIMMEAN calculates the mean taken by excluding a percentage of data points from the top and bottom tails of a data set.

**Syntax:**
```plaintext
TRIMMEAN(array, percent)
```

**Where:**
- `array` is the array or range of values to trim and average.
- `percent` is the fractional number of data points to exclude from the calculation. For example, if `percent = 0.2`, 4 points are trimmed from a data set of 20 points (20 x 0.2): 2 from the top and 2 from the bottom of the set.

**Remarks:**
- Percent must be >= 0 and <= 1.
- TRIMMEAN rounds off the number of excluded data points down to the nearest multiple of 2. If `percent = 0.1`, 10 percent of 30 data points equals 3 points. For symmetry, TRIMMEAN excludes a single value from the top and bottom of the data set.

### 4.7.174 True

**Description:**
The True function returns the logical value for True.

**Syntax:**
```plaintext
True(stringvalue)
```

**Where:**
- `stringvalue` is to provide an empty string.

### 4.7.175 TRUNC

**Description:**
Truncates a number to an integer by removing the fractional part of the number.

**Syntax:**
---

## API Reference

Not applicable for this section.

## Code Examples

Not applicable for this section.

## Cross References

Not applicable for this section.

<!-- tags: [calculate, TRIMMEAN, True, TRUNC, Winforms, Syncfusion] keywords: [mean, data points, logical value, truncate, number, integer, fractional part, numerical calculation, data set] -->
```