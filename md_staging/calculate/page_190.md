```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: calculate
page_number: 190
page_id: calculate#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:36Z
fidelity: lossless
-->

## Essential Calculate

### Syntax

LOGINV(probability, mean, standard_dev)

**where:**

- probability is the probability associated with the lognormal distribution.
- mean is the mean of ln(x).
- standard_dev is the standard deviation of ln(x).

### Remarks

- Probability must be >= 0 and < 1.
- Standard_dev must be positive.
- The inverse of the lognormal distribution function is:
  
\[
LOGINV(p, \mu, \sigma) = e^{\{ \mu + \sigma \times [NORMSINV(p)]\}}
\]

## 4.7.93 LOGNORMDIST

Returns the cumulative lognormal distribution of x, where \ln(x) is normally distributed with parameters mean and standard_dev.

### Syntax

LOGNORMDIST(x, mean, standard_dev)

**where:**

- x is the value at which the function can be evaluated.
- mean is the mean of \ln(x).
- standard_dev is the standard deviation of \ln(x).

### Remarks

- Both x and standard_dev must be positive.

```