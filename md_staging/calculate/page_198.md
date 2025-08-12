```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: calculate
page_number: 198
page_id: calculate#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:57Z
fidelity: lossless
-->

### 4.7.107 NEGBINOMDIST

Returns the negative binomial distribution. NEGBINOMDIST returns the probability that there will be number_f failures before the number_s-th success, when the constant probability of a success is probability_s.

#### Syntax

NEGBINOMDIST(number_f, number_s, probability_s)

where:
- number_f is the number of failures.
- number_s is the threshold number of successes.
- probability_s is the probability of a success.

#### Remarks
- number_s must be >= 1.
- probability_s must be >= 0 and <= 1.
- number_f must be >= 0.
- The equation for the negative binomial distribution is:

\[ nb(x;r;p) = \binom{x+r-1}{r-1} p^r (1-p)^x \]

where:
- \( x \) is number_f
- \( r \) is number_s
- \( p \) is probability_s

### 4.7.108 NORMDIST

---

© 2013 Syncfusion. All rights reserved.
```