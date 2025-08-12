```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_330.jpeg
document_name: grid
page_number: 330
page_id: grid#page_330
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the functions `NPER` and `NPV`, used for calculating the time periods required for an investment and the net present value of future cash flows, respectively.
- Parameters include rate of interest, payment amounts, present value, future value, and payment timing (type).

## Content

### NPER(rate, pmt, pv, fv, type)

The `NPER` function calculates the number of periods required to pay off a loan or to reach a financial goal based on a constant payment amount and interest rate.

- **rate**: The interest rate per period.
- **pmt**: The payment made each period; remains constant over the life of the annuity.
- **pv**: The present value or lump-sum amount derived from a series of future payments.
- **fv**: The future value or cash balance after the last payment. If omitted, it is assumed to be 0.
- **type**: Indicates when payments are due:
  - 0: Payments due at the end of the period.
  - 1: Payments due at the beginning of the period.

### 4.1.4.6.6.174 NPV

The `NPV` function calculates the net present value of an investment by using a discount rate and a series of future cash flow values (negative for payments and positive for income).

#### Syntax

`NPV(rate, value1, value2, ...)`

Parameters:
- **rate**: The discount rate over the length of one period.
- **value1**, **value2**, ...: Arguments representing future cash flows.
  - Must be equally spaced in time and occur at the end of each period.
  - The order of the cash flows is significant and must match the sequence of cash flows.

#### Remarks
- The NPV investment begins one period before the date of the value1 cash flow and ends with the last cash flow listed.
- If the first cash flow occurs at the beginning of the first period, it should be added to the NPV result rather than included as a value argument.
- The formula for NPV, where `n` is the number of cash flows, is:

\[
NPV = \sum_{i=1}^{n} \frac{values_i}{(1 + rate)^i}
\]

## API Reference

### Parameters (NPV)
- **rate**: The discount rate over the length of one period.
- **value1, value2, ...**: Future cash flow amounts (negative for payments, positive for income).

### Formula for NPV
\[
NPV = \sum_{i=1}^{n} \frac{values_i}{(1 + rate)^i}
\]

---
```markdown

<!-- tags: [financial functions, NPER, NPV, Windows Forms, Syncfusion] keywords: [rate, pmt, pv, fv, type, net present value, cash flows, discount rate] -->
```