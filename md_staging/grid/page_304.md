```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_304.jpeg
document_name: grid
page_number: 304
page_id: grid#page_304
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:37Z
fidelity: lossless
--> 

# Essential Grid for Windows Forms

## IPMT Function

### Syntax

```plaintext
IPMT(rate, per, nper, pv, fv, type), where:
```

- `rate` is the interest rate per period.
- `per` is the period for which you want to find the interest and must be in the range 1 to `nper`.
- `nper` is the total number of payment periods in an annuity.
- `pv` is the present value or the lump-sum amount that a series of future payments is worth right now.
- `fv` is the future value or a cash balance that you want to attain after the last payment is made. If `fv` is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).
- `type` is the number 0 or 1 and indicates when payments are due. If `type` is omitted, it is assumed to be 0. If `type = 0`, payments are made at the end of the period. If `type = 1`, payments are made at the beginning of the period.

### Remarks

- Make sure that you are consistent about the units you use for specifying `rate` and `nper`. If you make monthly payments on a four-year loan at 12 percent annual interest, use `12%/12` for `rate` and `4*12` for `nper`. If you make annual payments on the same loan, use `12%` for `rate` and `4` for `nper`.

## 4.1.4.6.6.118 IRR

### Overview

Calculates the internal rate of return for a series of cash flows represented by the numbers in `values`. The cash flows must occur at regular intervals such as monthly or annually.

### Syntax

```plaintext
IRR(values, guess), where:
```

- `values` is an array or a reference to cells that contain numbers for which you want to calculate the internal rate of return.

### Notes

- Values must contain at least one positive value and one negative value to calculate the internal rate of return.
- IRR uses the order of values to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want.

## Footer

© 2013 Syncfusion. All rights reserved. | Page 304
``` 

<!-- tags: [syncfusion-sdk, ipmt, irr, financial functions, windows forms, grid] keywords: [ipmt, per, fv, values, guess, internal rate of return, cash flows, payments, annual interest] -->
``` 
