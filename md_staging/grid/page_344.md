```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_344.jpeg
document_name: grid
page_number: 344
page_id: grid#page_344
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:28Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

- **nper**: is the total number of payment periods in an annuity.
- **pmt**: is the payment made for each period and cannot change over the life of the annuity. Typically, pmt includes the principal and interest but does not include other fees or taxes. If pmt is omitted, you must include the fv argument.
- **pv**: is the present value—the total amount that a series of future payments is worth now.
- **fv**: is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (e.g., the future value of a loan is 0).
- **type**: is the number 0 or 1 and indicates when payments are due. If type equals:
  - **0**: Payments are due at the end of the period.
  - **1**: Payments are due at the beginning of the period.
  - **guess**: is your guess for what the rate will be. If you omit guess, it is assumed to be 10 percent. If RATE does not converge, try different values for guess. RATE usually converges if guess is between 0 and 1.

### 4.1.4.6.6.201 RECEIVED

The Received function returns the amount received at maturity for a fully invested security.

#### Syntax

**RECEIVED(settlement, maturity, investment, discount, basis)** where:
- **Maturity**: security’s maturity date.
- **Settlement**: security’s settlement date.
- **Discount**: security’s discount rate.
- **Basis**: type of day count basis.

#### Remarks:
- **\#NUM!**: occurs if settlement ≥ maturity
- **\#VALUE!**: occurs if valid date is not entered for maturity and settlement.
- **\#NUM!**: occurs if investment and discount is ≤ 0

The **RECEIVED** is calculated as follows:

\[
RECEIVED = \frac{\text{investment}}{1 - \left( \text{discount} \times \frac{\text{DSM}}{\text{B}} \right)}
\]

where:
- **B**: is the number of days in the year, depending on the year basis.
- **DSM**: is the number of days from issue to maturity.
```