```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_336.jpeg
document_name: grid
page_number: 336
page_id: grid#page_336
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:41Z
fidelity: lossless
-->

## Overview
- Describes the syntax and usage of the PMT function for calculating loan payments.
- Explains the POISSON function for returning the Poisson distribution.

## Content

### PMT Function
#### Syntax
`PMT(rate, nper, pv, fv, type)`, where:

- **rate** is the interest rate for the loan.
- **nper** is the total number of payments for the loan.
- **pv** is the present value or the total amount that a series of future payments is worth now; also known as the principal.
- **fv** is the future value or a cash balance you want to attain after the last payment is made. If `fv` is omitted, it is assumed to be 0 (zero), that is, the future value of a loan is 0.
- **type** is the number 0 (zero) or 1 and indicates when payments are due. If `type` equals:
  - 0 - Payments are due at the end of the period.
  - 1 - Payments are due at the beginning of the period.

#### Remarks
- The payment returned by `PMT` includes principal and interest but no taxes, reserve payments, or fees sometimes associated with loans.
- Make sure that you are consistent about the units you use for specifying `rate` and `nper`. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use `12% / 12` for `rate` and `4 * 12` for `nper`. If you make annual payments on the same loan, use 12 percent for `rate` and 4 for `nper`.

---

### POISSON Function
#### Syntax
`POISSON(x, mean, cumulative)`, where:

- **x** is the number of events.
- **mean** is the expected numeric value.
- **cumulative** is a logical value that determines the form of the probability distribution returned. If `cumulative` is `True`, `POISSON` returns the cumulative Poisson probability that the number of random events occurring will be between zero and `x` inclusive; if `False`, it returns the Poisson probability mass function that the number of events occurring will be exactly `x`.

---

## API Reference (if applicable)

### POISSON Function Parameters
| Name     | Type       | Description                                                                 | Default | Required |
|----------|------------|-----------------------------------------------------------------------------|---------|----------|
| `x`      | Numeric    | The number of events.                                                       |         | Yes      |
| `mean`   | Numeric    | The expected numeric value.                                                 |         | Yes      |
| `cumulative` | Logical | Determines the form of the probability distribution returned.             |         | Yes      |

### Returns
- A numeric value representing the Poisson distribution.

---

## Code Examples (multi-language supported)
```csharp
// Example using POISSON in C#
double x = 5;
double mean = 3;
bool cumulative = true;
double result = POISSON(x, mean, cumulative);
```

```csharp
// Example using PMT in C#
double rate = 12 / 100 / 12; // 12% annual interest rate, monthly payments
int nper = 4 * 12; // Four years of monthly payments
double pv = 100000; // Principal amount
double fv = 0; // Future value
int type = 0; // Payments are due at the end of the period
double payment = PMT(rate, nper, pv, fv, type);
```

---

## Page-level Navigation/TOC (if applicable)
- [4.1.4.6.6.187 POISSON](#poisson-function)

---

## Cross References
- See also: [Loan Payment Calculation](#pmt-function)

<!-- tags: [syncfusion, winforms, functions, loan, distribution, mathematical] keywords: [PMT, POISSON, interest rate, expected value, probability, loan payment, Poisson distribution, cumulative, probability mass function] -->
```