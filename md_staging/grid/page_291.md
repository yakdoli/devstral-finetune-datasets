```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_291.jpeg
document_name: grid
page_number: 291
page_id: grid#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

number is the numeric value that you want to round off.

significance is the multiple to which you want to round the number off.

## Remarks

- Number and significance must have the same sign.
- Regardless of the sign of the number, a value is rounded down when adjusted away from zero. If a number is an exact multiple of significance, no rounding occurs.

## 4.1.4.6.6.95 FORECAST

Calculates a future value by using existing values using a linear regression. The predicted value is a y-value for a given x-value.

### Syntax

FORECAST(x, known_ys, known_xs), where:

- **x** is the data point for which you want to predict a value.
- **known_ys** is the dependent array or range of data.
- **known_xs** is the independent array or range of data.

### Remarks

- The equation for FORECAST is \(a + bx\), where:

  \[
  a = \bar{y} - b\bar{x}
  \]

  and

  \[
  b = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2}
  \]

<!-- tags: [product, module, control, api, version?, linear regression, forecasting] keywords: [FORECAST, known_ys, known_xs, linear regression, prediction] -->
```