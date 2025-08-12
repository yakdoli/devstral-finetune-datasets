```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_375.jpeg
document_name: grid
page_number: 375
page_id: grid#page_375
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

- The equation for the Weibull cumulative distribution function is,
  
  \[
  F(x; \alpha, \beta) = 1 - e^{-\left(\frac{x}{\beta}\right)^\alpha}
  \]

- The equation for the Weibull probability density function is,
  
  \[
  f(x; \alpha, \beta) = \frac{\alpha}{\beta^\alpha} x^{\alpha - 1} e^{-\left(\frac{x}{\beta}\right)^\alpha}
  \]

- When \(\alpha = 1\), WEIBULL returns the exponential distribution with,
  
  \[
  \lambda = \frac{1}{\beta}
  \]

### 4.1.4.6.6.261 WEIBULL.DIST

The WEIBULL.DIST function returns the Weibull distribution.

**Syntax:**

WEIBULL.DIST(x, alpha, beta, cumulative) where:

- \(x\) is the value at which to evaluate the function.
- \(\alpha\) is a parameter of the distribution.
- \(\beta\) is a parameter of the distribution.
- `cumulative` determines the form of the function.

**Remarks:**

- **\#NUM!** - occurs if \(x\) is less than zero.
- **\#VALUE!** - occurs if \(x\) is non-numeric.
- **\#VALUE!** - occurs if \(\alpha\) is non-numeric.
- **\#NUM!** - occurs if \(\alpha\) is equal to or less than zero.
- **\#VALUE!** - occurs if \(\beta\) is non-numeric.
- **\#NUM!** - occurs if \(\beta\) is equal to or less than zero.

### 4.1.4.6.6.262 Xirr

The Xirr function computes the internal rate-of-return for a schedule of possibly non-periodic cash flows.
```