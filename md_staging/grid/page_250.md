```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_250.jpeg
document_name: grid
page_number: 250
page_id: grid#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:14Z
fidelity: lossless
-->

## ABS Function

### Overview
- ABS returns the absolute value of a number.
- The absolute value of a non-negative number is the number itself.
- The absolute value of a negative number is `-1` times the number.

### Syntax
- **ABS(number)**
  - `number`: The real number for which you want the absolute value.

---

## ACCRINT Function

### Overview
- The ACCRINT function returns the accrued interest for a security that pays periodic interest.

### Syntax
- **ACCRINT(issue, first_interest, settlement, rate, par, frequency, [basis], [calc_method])**
  - `issue`: Security's issue date.
  - `first_interest`: Security's first interest date.
  - `settlement`: Security's settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer.
  - `rate`: Security's annual coupon rate.
  - `par`: Security's par value.
  - `frequency`: Number of coupon payments per year.
  - `[basis]`: [Optional] Day count basis.
  - `[calc_method]`: [Optional] Calculation method.

### Remarks
- **#VALUE!**
  - Occurs if `issue`, `first_interest`, or `settlement` is not a valid date.
- **#NUM!**
  - Occurs if `rate ≤ 0` or if `par ≤ 0`.
  - Occurs if `frequency` is any number other than `1`, `2`, or `4`.
  - Occurs if `basis < 0` or if `basis > 4`.
  - Occurs if `issue ≥ settlement`.

### Calculation
- ACCRINT is calculated as follows:
  \[
  ACCRINT = par \times \frac{rate}{frequency} \times \sum_{i=1}^{N} \frac{A_i}{NL_i}
  \]

<!-- tags: [winforms, accrint, abs, financial functions, syncfusion] keywords: [accrual interest, periodic interest, security, issue date, settlement date, coupon rate, par value, frequency] -->
```