```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_240.jpeg
document_name: calculate
page_number: 240
page_id: calculate#page_240
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:18Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.185 Weibull

The Weibull function returns the Weibull distribution. This distribution is used in reliability analysis, such as calculating a device's mean time to failure.

#### Syntax:
```plaintext
WEIBULL(x, alpha, beta, cumulative)
```

Where:
- **X** is the value at which the function is evaluated.
- **Alpha** is a parameter to the distribution.
- **Beta** is a parameter to the distribution.
- **Cumulative** determines the form of the function.

#### Remarks:
- If x, alpha, or beta is nonnumeric, WEIBULL returns the #VALUE! error value.
- If x < 0, WEIBULL returns the #NUM! error value.
- If alpha ≤ 0 or if beta ≤ 0, WEIBULL returns the #NUM! error value.

### 4.7.186 Xirr

The Xirr function computes the internal rate of return for a schedule of possibly non-periodic cash flows.

#### Syntax:
```plaintext
Xirr(cashflow, datelist, value)
```

Where:
- **cashflow** is the range of cash flow.
- **datelist** is the list of corresponding date serial number values.
- **value** is an initial guess at the return value.

### 4.7.187 YEAR

Returns the year corresponding to a date. The year is returned as an integer in the range 1900-9999.

#### Syntax
```plaintext
 YEAR
```

---
Source: Syncfusion Inc., 2013. All rights reserved.
---

## Cross References
See also:
- Weibull
- Xirr
- YEAR

<!-- tags: [essential-calculate, weibull-distribution, reliability-analysis, xirr-function, cash-flow-analysis, year-function, syncfusion-winform, version-11.4.0.26] keywords: [weibull-distribution, mean-time-to-failure, reliability-analysis, internal-rate-of-return, non-periodic-cash-flows, initial-guess, year-function, essential-calculate, numeric-parameters, error-values, date-serial-number] -->
```