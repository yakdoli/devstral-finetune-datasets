```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: calculate
page_number: 202
page_id: calculate#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:07Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes the `NPV` and `NPER` functions used for calculating financial values.
- Covers parameters and usage of these functions in financial calculations.

## Content

### NPER(rate, pmt, pv, fv, type)

where:
- **rate** is the interest rate per period.
- **pmt** is the payment made each period; it cannot change over the life of the annuity.
- **pv** is the present value or the lump-sum amount that a series of future payments is worth right now.
- **fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).
- **type** is the number 0 or 1 and indicates when payments are due. If type equals:
  - 0 - payments are due at the end of the period
  - 1 - payments are due at the beginning of the period

### 4.7.115 NPV

#### Overview
Calculates the net present value of an investment by using a discount rate and a series of future payments (negative values) and income (positive values).

#### Syntax
NPV(rate, value1, value2, …)

#### Parameters
where:
- **rate** is the rate of discount over the length of one period.
- **value1, value2, …** are arguments representing the payments and income. Value1, value2, … must be equally spaced in time and occur at the end of each period. NPV uses the order of value1, value2, ... to interpret the order of cash flows. Be sure to enter your payment and income values in the correct sequence.

#### Remarks
- The NPV investment begins one period before the date of the value1 cash flow and ends with the last cash flow in the list. The NPV calculation is based on future cash flows.

```markdown
<!-- tags: [financial-calculation, npv, nper, investment, payments, cash-flows] keywords: [rate, present-value, future-value, discount-rate, payments] -->
```