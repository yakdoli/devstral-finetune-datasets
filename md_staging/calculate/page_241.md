```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_241.jpeg
document_name: calculate
page_number: 241
page_id: calculate#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:03Z
fidelity: lossless
-->

## Essential Calculate

### YEAR(serial_number)

**where:**

- `serial_number` is the date of the year you want to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use DATE(2002,11,12) for the 12th day of November 2002.

#### Remarks

- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900, is serial number 1, and January 1, 2008, is serial number 39448 because it is 39,448 days after January 1, 1900.

### 4.7.188 ZTEST

**Returns the one-tailed probability-value of a z-test.**

#### Syntax

ZTEST(array, u0, sigma)

**where:**

- `array` is the array or range of data against which, to test u0
- `u0` is the value to test.
- `sigma` is the population (known) standard deviation. If omitted, the sample standard deviation is used.

#### Remarks

- ZTEST is calculated as follows when `sigma` is not omitted:

  \[
  ZTEST(array, \mu_0) = 1 - NORMSDIST \left( \frac{(\overline{x} - \mu_0)\sqrt{n}}{\sigma} \right)
  \]

- or when `sigma` is omitted:
