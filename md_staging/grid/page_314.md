```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_314.jpeg
document_name: grid
page_number: 314
page_id: grid#page_314
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Syntax

LOGINV(probability, mean, standard_dev), where:

- probability is the probability associated with the lognormal distribution.
- mean is the mean of ln(x).
- standard_dev is the standard deviation of ln(x).

## Remarks

- Probability must be >= 0 and < 1.
- Standard_dev must be positive.
- The inverse of the lognormal distribution function is:

  \[
  \text{LOGINV}(p, \mu, \sigma) = e^{\left\{\mu + \sigma NORMSINV(p)\right\}}
  \]

## 4.1.4.6.6.141 LOGNORMDIST

Returns the cumulative lognormal distribution of x, where ln(x) is normally distributed with parameters mean and standard_dev.

### Syntax

LOGNORMDIST(x, mean, standard_dev), where:

- x is the value at which the function can be evaluated.
- mean is the mean of ln(x).
- standard_dev is the standard deviation of ln(x).

### Remarks

- Both x and standard_dev must be positive.
- The equation for the lognormal cumulative distribution function is:

<!-- tags: [lognormal distribution, LOGINV, LOGNORMDIST, Windows Forms] keywords: [lognormal, inverse, cumulative, distribution, probability, standard deviation, mean, x, function, equation] --> 
```