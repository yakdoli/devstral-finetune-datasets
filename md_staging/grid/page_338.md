```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_338.jpeg
document_name: grid
page_number: 338
page_id: grid#page_338
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:08Z
fidelity: lossless
--> 

# Essential Grid for Windows Forms

## Overview
- Provides a detailed explanation of the PPMT and PROB functions relevant to financial analysis in Windows Forms applications.
- Describes how to calculate the payment on the principal for a given period, as well as the probability of values falling within specific ranges.

## Content

### PPMT

#### Overview
Returns the payment on the principal for a given period, for an investment based on periodic, constant payments and a constant interest rate.

#### Syntax
```plaintext
PPMT(rate, per, nper, pv, fv, type)
```

#### Parameters
- `rate`: The interest rate per period.
- `per`: Specifies the period and must be in the range of 1 to `nper`.
- `nper`: The total number of payment periods in an annuity.
- `pv`: The present value—the total amount that a series of future payments is worth now.
- `fv`: The future value or a cash balance that you may want to attain after the last payment is made. If `fv` is omitted, it is assumed to be 0 (zero).
- `type`: The number 0 or 1, indicating when payments are due:
  - **0**: Payments are due at the end of the period.
  - **1**: Payments are due at the beginning of the period.

#### Remarks
- Ensure consistency in the units used for specifying `rate` and `nper`. For example:
  - If monthly payments are made on a four-year loan at 12 percent annual interest, use `12%/12` for `rate` and `4*12` for `nper`.
  - For annual payments on the same loan, use `12%` for `rate` and `4` for `nper`.

### PROB

#### Overview
Returns the probability whose values are in a range that is between two limits. If `upper_limit` is not supplied, returns the probability that values in `x_range` are equal to `lower_limit`.

#### Syntax
```plaintext
PROB(x_range, prob_range, lower_limit, upper_limit)
```

#### Parameters
- `x_range`: The range of numeric values of `x` with which there are associated probabilities.

---

<!-- tags: [syncfusion, windowsforms, ppmt, prob, financialanalysis, grid] keywords: [financial functions, ppmt function, probability function, windows forms, syncfusion documentation] -->
```