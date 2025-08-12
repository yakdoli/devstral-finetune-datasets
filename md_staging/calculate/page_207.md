```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_207.jpeg
document_name: calculate
page_number: 207
page_id: calculate#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:12Z
fidelity: lossless
-->

### 4.7.124 PMT

Calculates the payment for a loan based on constant payments and a constant interest rate.

#### Syntax

``` 
PMT(rate, nper, pv, fv, type)
```

#### Parameters

- **rate**: The interest rate for the loan.
- **nper**: The total number of payments for the loan.
- **pv**: The present value or the total amount that a series of future payments is worth now; also known as the principal.
- **fv**: The future value or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (zero), that is, the future value of a loan is 0.
- **type**: The number 0 (zero) or 1 and indicates when payments are due. If type equals:
  - **0**: Payments are due at the end of the period.
  - **1**: Payments are due at the beginning of the period.

#### Remarks

- The payment returned by PMT includes principal and interest but no taxes, reserve payments or fees sometimes associated with loans.
- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use `12%/12` for `rate` and `4*12` for `nper`. If you make annual payments on the same loan, use `12 percent` for `rate` and `4` for `nper`.

### 4.7.125 POISSON

Returns the Poisson distribution.

#### Syntax

``` 
POISSON(x, mean, cumulative)
```

<!-- tags: [PMT, constant payments, interest rate, POISSON, Poisson distribution, loan] keywords: [rate, nper, pv, fv, type, x, mean, cumulative, payment, principal, future value, consistent units] -->
```