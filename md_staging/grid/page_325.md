```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_325.jpeg
document_name: grid
page_number: 325
page_id: grid#page_325
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:07Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### 4.1.4.6.6.163 NEGBINOMDIST

Returns the negative binomial distribution. NEGBINOMDIST returns the probability that there will be number_f failures before the number_s-th success, when the constant probability of a success is probability_s.

#### Syntax

NEGBINOMDIST(number_f, number_s, probability_s), where:

- number_f is the number of failures.
- number_s is the threshold number of successes.
- probability_s is the probability of a success.

#### Remarks

- number_s must be >= 1.
- probability_s must be >= 0 and <= 1.
- number_f must be >= 0.
- The equation for the negative binomial distribution is,

\[ nb(x;r;p) = \binom{x + r - 1}{r - 1} p^r (1 - p)^x \]

where \( x \) is number_f, \( r \) is number_s, and \( p \) is probability_s.

### 4.1.4.6.6.164 NETWORKDAYS

The NETWORKDAYS function is used to calculate the number of whole work days between two given dates. This includes all weekdays from Monday to Friday, but excludes a supplied list of holidays.

#### Syntax

= NETWORKDAYS(start_date, end_date, [holidays])

##### Parameters

- start_date: The start of the period to find the working days
- end_date: The end of the period to find the working days.

---

<!-- tags: [negative binomial distribution, probability, success, failure, threshold, excluded holidays, working days] keywords: [NEGBINOMDIST, NETWORKDAYS, probability_s, number_f, number_s] -->
```