```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_274.jpeg
document_name: grid
page_number: 274
page_id: grid#page_274
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:46Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

- **Basis** – type of day count basis.

#### Remarks:

- **#VALUE!** – occurs if settlement or maturity is not a valid date.
- **#NUM!** – occurs if coupon < 0 or yld < 0
- **#NUM!** – occurs if frequency number is other than 1,2 and 4
- **#NUM!** – occurs basis is less than 0 and greater than 4
- **#NUM!** – occurs if settlement is >= Maturity

#### 4.1.4.6.6.54 CUMPRINC

The CUMPRINC function returns the cumulative principal paid on a loan between the `start_period` and `end_period`.

##### Syntax:

```text
CUMPRINC(rate, nper, pv, start_period, end_period, type)
```

Where:
- **Rate** – the interest rate.
- **Nper** – total number of payment periods.
- **pv** – The present value.
- **start_period** – first period in calculation. Begins with one.
- **end_period** – last period in calculation.
- **type** – timing of the payment.

#### Remarks:

- **#NUM!** – occurs if `rate`, `nper`, or `pv` is less than or equal to zero.
- **#NUM!** – occurs if `start_period` or `end_period` is less than one.
- **#NUM!** – occurs if `start_period` is greater than `end_period`.
- **#NUM!** – occurs if `type` is any number other than 0 or 1.

#### 4.1.4.6.6.55 DATE

Returns the sequential serial number that represents a particular date.

##### Syntax

---

<!-- tags: [WinForms, Grid, CumulativePrincipal, Date, CUMPRINC, DATE] keywords: [EssentialGrid, WindowsForms, DayCountBasis, CUMPRINCFunction, DateFunction] -->
```