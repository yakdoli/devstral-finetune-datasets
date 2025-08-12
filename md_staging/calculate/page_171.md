```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: calculate
page_number: 171
page_id: calculate#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:11Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Number and significance must have the same sign.
- Regardless of the sign of the number, a value is rounded down when adjusted away from zero. If a number is an exact multiple of significance, no rounding occurs.

## Content

### 4.7.56 FORECAST

Calculates a future value by using existing values using a linear regression. The predicted value is a y-value for a given x-value.

#### Syntax

FORECAST(x, known_ys, known_xs)

where:
- x is the data point for which you want to predict a value.
- known_ys is the dependent array or range of data.
- known_xs is the independent array or range of data.

#### Remarks
- The equation for FORECAST is:
  
  $$
  \text{a + bx}
  $$

  where:
  $$
  \text{a = } \bar{y} \text{ - b}\bar{x}
  $$
  $$
  \text{b = } \frac{\sum(x - \bar{x})(y - \bar{y})}{\sum(x - \bar{x})^2}
  $$

  x-bar and y-bar are the sample means AVERAGE(know(xs)) and AVERAGE(known_ys).
```