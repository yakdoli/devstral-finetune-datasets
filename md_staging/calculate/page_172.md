```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: calculate
page_number: 172
page_id: calculate#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:07Z
fidelity: lossless
-->

## Content

### 4.7.57 FV

The **FV** function returns the future value of an investment, based on an interest rate and a constant payment schedule.

#### Syntax:

```
FV( interest_rate, number_payments, payment, PV, Type )
```

#### where:
- **interest_rate** is the interest rate for the investment.
- **number_payments** is the number of payments for the annuity.
- **payment** is the payment made on each period.
- **PV** is the present value of the payments. This is optional. The FV function assumes PV value as 0, when this parameter is omitted.
- **Type** indicates the payments due. Type accepts the following values:
  - **0 - Payments at the end of the period (default)**.
  - **1 - Payments at the beginning of the period**.

This is optional. The FV function assumes Type value as 0, when this parameter is omitted.

### 4.7.58 GAMMADIST

#### Returns the gamma distribution.

#### Syntax

```
GAMMADIST(x, alpha,beta, cumulative)
```

#### where:
- **x** is the value at which you want to evaluate the distribution.
- **alpha** is a parameter to the distribution.
- **beta** is a parameter to the distribution. If beta = 1, GAMMADIST returns the standard gamma distribution.
- **cumulative** is a logical value that determines the form of the function. If cumulative is True, GAMMADIST returns the cumulative distribution function; if False, it returns the probability density function.

---

#### Remarks

---

##### Page-level Navigation/TOC (if applicable)

- **FV**
- **GAMMADIST**

---

<!-- tags: [syncfusion, winforms, calculate, fv, gammadist, api, 11.4.0.26] keywords: [futures value, annuity, interest rate, present value, gamma distribution, cumulative distribution function, probability density function] -->
```