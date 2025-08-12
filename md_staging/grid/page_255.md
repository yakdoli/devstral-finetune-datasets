```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_255.jpeg
document_name: grid
page_number: 255
page_id: grid#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Functions and methods for calculating trigonometric and statistical values.
- Math-based functions such as ATAN2, ATANH, and statistical variance measures like AVEDEV are detailed.
- Specific syntax and usage guidelines for each function are provided.

## Content

### 4.1.4.6.6.15 ATAN2

Returns the inverse tangent of the specified x- and y-coordinates. The arctangent is the angle from the x-axis to a line containing the origin (0, 0) and the point (x_num, y_num). The angle is given in radians between -pi and pi, excluding -pi.

#### Syntax

```markdown
ATAN2(x_num, y_num),
```
where:
- **x_num** is the X coordinate of the point.
- **y_num** is the Y coordinate of the point.

#### Remarks
- A positive result represents a counterclockwise angle from the x-axis; a negative result represents a clockwise angle.
- ATAN2(a, b) equals ATAN(b/a), except that `a` can equal 0 in ATAN2.

---

### 4.1.4.6.6.16 ATANH

Returns the inverse hyperbolic tangent of a number. Number must be strictly between -1 and 1. The inverse hyperbolic tangent is the value whose hyperbolic tangent is number, so ATANH(TANH(number)) equals the given number.

#### Syntax

```markdown
ATANH(number),
```
where:
- **number** is any real number that is between 1 and -1.

---

### 4.1.4.6.6.17 AVEDEV

Returns the average of the absolute mean deviations of data points. AVEDEV is a measure of the variability in a data set.

#### Syntax

Not specified in the current section.

---

<!-- tags: [Essential Grid, WinForms, ATAN2, ATANH, AVEDEV, trigonometric functions, statistical measures, mathematical functions] keywords: [ATAN2, ATANH, AVEDEV, trigonometric, statistical variance, user guide, syncfusion] -->
```