```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_320.jpeg
document_name: grid
page_number: 320
page_id: grid#page_320
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:42Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### #VALUE!

- Occurs if the array does not have an equal number of rows and columns.

---

### 4.1.4.6.6.153 MIRR

#### Overview

- Returns the modified internal rate of return for a series of periodic cash flows.

#### Syntax

- `MIRR(values, finance_rate, reinvest_rate)`, where:

  - **values**: is an array or a reference to cells that contain numbers. These numbers represent a series of payments (negative values) and income (positive values) occurring at regular periods.
    - Values must contain at least one positive value and one negative value to calculate the modified internal rate of return.
  - **finance_rate**: is the interest rate you pay on the money used in the cash flows.
  - **reinvest_rate**: is the interest rate you receive on the cash flows as you reinvest them.

#### Remarks

- MIRR uses the order of `values` to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want and with the correct signs (positive values for cash received, negative values for cash paid).
- If \( n \) is the number of cash flows in `values`, `frate` is the `finance_rate`, and `rrate` is the `reinvest_rate`, then the formula for MIRR is:

  \[
  \left( \frac{-NPV(rrate, values_{positive}) * (1+rrate)^{n}}{NPV(frate, values_{negative}) * (1+frate)} \right)^{\frac{1}{n-1}} - 1
  \]

---

### 4.1.4.6.6.154 MMULT

#### Overview

- The MMULT function returns the matrix product of two arrays. Both arrays should have the same number of columns and the same number of rows.

#### Syntax

- `MMULT(a1, a2)` where:
  - **a1, a2**: are the arrays that have to be multiplied.

#### Remarks

---

## Page-level Navigation/TOC
- This page covers the following:
  - MIRR Function Explanation
  - MMULT Function Explanation

## Cross References
- See also: Functions, Cash Flows, Internal Rate of Return, Matrix Operations

```html
<!-- tags: [MIRR, MMULT, Cash Flows, Internal Rate of Return, Matrix Operations, Windows Forms] keywords: [Modified Internal Rate of Return, Finance Rate, Reinvest Rate, Matrix Product, Array Operations] -->
```