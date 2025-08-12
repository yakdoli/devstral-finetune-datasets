```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_262.jpeg
document_name: grid
page_number: 262
page_id: grid#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:59Z
fidelity: lossless
-->

## Remarks

- Both values must be numeric.
- Regardless of the sign of a number, a value is rounded up when adjusted away from zero. If the number is an exact multiple of significance, no rounding occurs.

### 4.1.4.6.6.28 CEILING.MATH

The CEILING.MATH function rounds a number up to the nearest multiple of significance.

**Syntax:**

CEILING(number, [significance], [mode]) where:
- number must be less than 9.99E+307 and greater than -2.229E-308.
- significance must be the multiple to which the number is to be rounded.
- mode is for negative numbers, it controls whether the number is rounded toward or away from zero.

### 4.1.4.6.6.29 CHIDIST

Returns the one-tailed probability of the chi-squared (\(\chi^2\)) distribution. The \(\chi^2\) distribution is associated with a \(\chi^2\) test.

**Syntax**

CHIDIST(x, degrees_freedom), where:
- x is the value at which you want to evaluate the distribution.
- degrees_freedom is the number of degrees of freedom.

**Remarks**
- Both arguments should be numeric.
- degrees_freedom \(\geq\) 1 and < \(10^{10}\).
- CHIDIST is calculated as CHIDIST = P(X > x), where X is a \(\chi^2\) random variable.

### 4.1.4.6.6.30 CHIINV



<!-- tags: [Syncfusion, Winforms, CEILING.MATH, CHIDIST, CHIINV, API Reference, grid, version 11.4.0.26] keywords: [CEILING, MATH, CHI squared distribution, one-tailed probability, degrees of freedom, random variable] -->
```