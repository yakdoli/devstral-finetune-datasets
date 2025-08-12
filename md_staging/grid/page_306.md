```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_306.jpeg
document_name: grid
page_number: 306
page_id: grid#page_306
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Provides functions for testing numeric values and calculating investment parameters.

## Content

### ISNUMBER
Returns True if the value parses as a numeric value.

#### Syntax
```plaintext
ISNUMBER(value), where:
```
- `value`: The value that is to be tested.

---

### ISPMT (Interest Payment)
Calculates the interest paid during a specific period of an investment.

#### Syntax
```plaintext
ISPMT(rate, per, nper, pv), where:
```
- `rate`: The interest rate for the investment.
- `per`: The period for which you want to find the interest and must be between 1 and `nper`.
- `nper`: The total number of payment periods for the investment.
- `pv`: The present value of the investment. For a loan, `pv` is the loan amount.

#### Remarks
- Ensure consistency in the units used for specifying `rate` and `nper`. For example:
  - For monthly payments on a four-year loan at an annual interest rate of 12%, use `12%/12` for `rate` and `4*12` for `nper`.
  - For annual payments on the same loan, use `12%` for `rate` and `4` for `nper`.

---

### ISREF
The `ISREF` function returns the logical value TRUE if the given value is a reference value; otherwise, the function returns FALSE.

#### Syntax
```plaintext
=ISREF(given_value)
```
- `given_value`: Required. The value that is to be tested. The value argument can be a blank (empty cell), error, logical value, text, number, or reference value, or a name referring to any of these.

---

## Page-level Navigation/TOC (if applicable)
- ISNUMBER
- ISPMT
- ISREF

## Cross References
- Refer to the documentation for more details on other functions and their usage.

## RAG Annotations
<!-- tags: [windowsforms, essentialgrid, numericvalue, interestpayment, invest] keywords: [ISNUMBER, ISPMT, ISREF, numerical test, interest rate calculation, investment period, reference test] -->
```