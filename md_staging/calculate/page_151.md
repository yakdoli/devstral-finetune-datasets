```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_151.jpeg
document_name: calculate
page_number: 151
page_id: calculate#page_151
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:08Z
fidelity: lossless
-->

# Essential Calculate

## Content

### Remarks

- Both arguments should be numeric.
- `degrees_freedom >= 1` and `< 10^{10}`.
- `CHIDIST` is calculated as follows:

  \[
  \text{CHIDIST} = \text{P}(X > x)
  \]

  where:
  - \( X \) is a \(\chi^2\) random variable.

### 4.7.18 CHIINV

Returns the inverse of the one-tailed probability of the chi-squared (\(\chi^2\)) distribution. If probability = `CHIDIST(x,...)`, then `CHIINV(probability,...) = x`. Use this function to compare observed results with expected ones in order to decide whether your original hypothesis is valid.

#### Syntax

```markdown
CHIINV(probability, degrees_freedom)
```

where:
- `probability` is a probability associated with the chi-squared distribution.
- `degrees_freedom` is the number of degrees of freedom.

#### Remarks

- Probability must be \(\geq 0\) and \(\leq 1\).
- `degrees_freedom >= 1` and \( = 10^{10}\).

Given a value for `probability`, `CHIINV` seeks the value \( x \) such that `CHIDIST(x, degrees_freedom) = probability`. Thus, precision of `CHIINV` depends on precision of `CHIDIST`. `CHIINV` uses an iterative search technique.
```


<!-- tags: [syncfusion, winforms, chidist, chiinv, chi-squared distribution] keywords: [chidist, chiinv, degrees of freedom, probability, hypothesis testing, chi-squared distribution] -->
```