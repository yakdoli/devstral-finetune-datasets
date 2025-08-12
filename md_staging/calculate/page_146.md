```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_146.jpeg
document_name: calculate
page_number: 146
page_id: calculate#page_146
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:46Z
fidelity: lossless
-->

# Essential Calculate

**y_num** is the Y coordinate of the point.

## Remarks

- A positive result represents a counterclockwise angle from the x-axis; a negative result represents a clockwise angle.
- ATAN2(a,b) equals ATAN(b/a), except that `a` can equal 0 in ATAN2.

### 4.7.9 ATANH

**Returns the inverse hyperbolic tangent of a number.** Number must be strictly between -1 and 1. The inverse hyperbolic tangent is the value whose hyperbolic tangent is number, so `ATANH(TANH(number))` equals the given number.

#### Syntax

`ATANH(number)`

where:

- **number** is any real number that is between 1 and -1.

### 4.7.10 AVEDEV

**Returns the average of the absolute mean deviations of data points.** AVEDEV is a measure of the variability in a data set.

#### Syntax

`AVEDEV(number1, number2, ...)`

where:

- **number1, number2, …** are arguments for which you want the average of the absolute deviations. You can also use a single array or a reference to an array instead of arguments separated by commas.

---

<!-- tags: [syncfusion, winforms, calculate, atan, atan2, atanh, ave-dev, api, version 11.4.0.26] keywords: [y-coordinate, angle calculation, inverse hyperbolic tangent, average deviation, variability, data analysis, atanh, avedev, atan2, atan] -->
```