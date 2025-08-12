```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_339.jpeg
document_name: grid
page_number: 339
page_id: grid#page_339
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- `prob_range` is a set of probabilities associated with values in `x_range`.
- `lower_limit` is the lower bound on the value for which you want a probability.
- `upper_limit` is the optional upper bound on the value for which you want a probability.

## Content

### Remarks
- Any value in `prob_range` must be > 0 and < 1.
- If `upper_limit` is omitted, `PROB` returns the probability of being equal to `lower_limit`.

#### 4.1.4.6.6.192 PRODUCT
- Multiplies all the numbers given as arguments and returns the product.

##### Syntax
PRODUCT(number1, number2, ...), where:
- `number1, number2, ...` are numbers that you want to multiply.

#### 4.1.4.6.6.193 PV
- Returns the present value of an investment. The present value is the total amount that a series of future payments is worth now.

##### Syntax
PV(rate, nper, pmt, fv, type), where:
- `rate` is the interest rate per period. For example, if you obtain an automobile loan at a 10% annual interest rate and make monthly payments, your interest rate per month is 10%/12 or 0.83%. You would enter 10%/12 or 0.83% or 0.0083, into the formula as the rate.
- `nper` is the total number of payment periods in an annuity. For example, if you get a four-year car loan and make monthly payments, your loan has 4*12 (or 48) periods. You would enter 48 into the formula for `nper`.

<!-- tags: [syncfusion, grid, windows forms, probability, product, present value, probabilities, interest rate, payment periods, financial functions] keywords: [prob_range, x_range, lower_limit, upper_limit, PROB, PRODUCT, PV, present value, interest rate, nper] -->
```