```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_295.jpeg
document_name: grid
page_number: 295
page_id: grid#page_295
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the functions GAMMAINV and GCD used in the context of the Essential Grid for Windows Forms.
- Details the syntax, usage, and remarks for both functions.
- Provides examples and considerations for their implementation.

## Content

### GAMMAINV

#### Overview
Returns the inverse of the gamma cumulative distribution. If \( p = \text{GAMMADIST}(x, \dots) \), then \( \text{GAMMAINV}(p, \dots) = x \).

#### Syntax

\[ \text{GAMMAINV(probability, alpha, beta)} \], where:
- **probability** is the probability associated with the gamma distribution.
- **alpha** is a parameter to the distribution.
- **beta** is a parameter to the distribution.

#### Remarks
- Probability must be \( \geq 0 \) and \( \leq 1 \).
- Alpha and beta must be positive.

Given a value for probability, GAMMAINV seeks a value \( x \) such that \( \text{GAMMADIST}(x, \alpha, \beta, \text{True}) = \text{probability} \). Thus, the precision of GAMMAINV depends on the precision of GAMMADIST. GAMMAINV uses an iterative search technique.

### GCD

#### Overview
The GCD function returns the greatest common divisor of two or more given values. The values must be numeric.

#### Syntax
The syntax of the GCD function is:
\[ \text{= GCD (number1, number2, ...)} \]
- Number1 – Required.
- If any value is not an integer, then it will be rounded down.

#### Remarks
- **#NUM!** – If the number is less than zero (0).
- **#VALUE!** – Occurs if any of the given arguments are non-numeric.

#### Example:
No specific example provided in the text.

<!-- tags: [syncfusion, winforms, gamma distribution, greatest common divisor, GAMMAINV, GCD, mathematical functions] keywords: [inverse gamma distribution, probability parameter, alpha parameter, beta parameter, greatest common divisor, gcd, non-numeric values, iterative search technique] -->
```