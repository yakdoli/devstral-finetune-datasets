```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_209.jpeg
document_name: calculate
page_number: 209
page_id: calculate#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:27Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.127 POWER

Returns the result of a number raised to a power.

#### Syntax

`POWER(number, power)`

where:
- `number` is the base number. It can be any real number.
- `power` is the exponent to which the base number is raised.

### 4.7.128 PPMT

Returns the payment on the principal for a given period, for an investment based on periodic, constant payments and a constant interest rate.

#### Syntax

`PPMT(rate, per, nper, pv, fv, type)`

where:
- `rate` is the interest rate per period.
- `per` specifies the period and must be in the range of `1` to `nper`.
- `nper` is the total number of payment periods in an annuity.
- `pv` is the present value—the total amount that a series of future payments is worth now.
- `fv` is the future value or a cash balance that you may want to attain after the last payment is made. If `fv` is omitted, it is assumed to be `0` (zero), that is, the future value of a loan is `0`.
- `type` is the number `0` or `1` and indicates when payments are due. If `type` equals:
  - `0`: Payments are due at the end of the period.
  - `1`: Payments are due at the beginning of the period.

### Remarks

---
© 2013 Syncfusion. All rights reserved.
```