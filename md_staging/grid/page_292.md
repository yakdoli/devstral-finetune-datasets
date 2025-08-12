```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_292.jpeg
document_name: grid
page_number: 292
page_id: grid#page_292
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:55Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

x-bar and y-bar are the sample means AVERAGE(known_xs) and AVERAGE(known_ys).

## FV

Returns the future value of an investment based on periodic, constant payments and interest rate.

### Syntax

`FV(rate, nper, pmt, pv, type)`, where:

- `rate` is the interest rate per period.
- `nper` is the total number of payment periods in an annuity.
- `pmt` is the payment made each period; it cannot change over the life of the annuity. Typically, `pmt` contains principal and interest but, no other fees or taxes. If `pmt` is omitted, you must include the `pv` argument.
- `pv` is the present value or lump-sum amount that a series of future payments is worth right now. If `pv` is omitted, it is assumed to be 0 (zero), and you must include the `pmt` argument.
- `type` is the number 0 or 1 and indicates when payments are due. If `type` is omitted, it is assumed to be 0. If `type` equals:
  - `0` - Payments are due at the end of the period.
  - `1` - Payments are due at the beginning of the period.

### Note

For a more complete description of the arguments in `FV`, see `PV`.

### Remarks

- Make sure that you are consistent about the units you use for specifying `rate` and `nper`. If you make monthly payments for a four-year loan at 12 percent annual interest, use `12%/12` for `rate` and `4*12` for `nper`. If you make annual payments on the same loan, use `12%` for `rate` and `4` for `nper`.
- For all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend checks, is represented by positive numbers.

## Fvschedule

After applying a series of compound interest rates, the `Fvschedule` method returns the future value of an initial principle.

<!-- tags: [grid, windows forms, fv, fvschedule, finance, calculations] keywords: [x-bar, y-bar, sample means, periodic payments, interest rate, future value, lump sum, compound interest, present value, payment due, general finance functions] -->
```