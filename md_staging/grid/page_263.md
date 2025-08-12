```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_263.jpeg
document_name: grid
page_number: 263
page_id: grid#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Returns the inverse of the one-tailed probability of the chi-squared (χ²) distribution. If probability = CHIDIST(x,...), then CHIINV(probability,...) = x. Use this function to compare observed results with expected ones in order to decide whether your original hypothesis is valid.

## CHIINV

### Syntax

CHIINV(probability, degrees_freedom), where:

- **probability** is a probability associated with the chi-squared distribution.
- **degrees_freedom** is the number of degrees of freedom.

### Remarks

- Probability must be >= 0 and <= 1.
- degrees_freedom >= 1 and = 10^10.

Given a value for probability, CHIINV seeks the value x such that CHIDIST(x, degrees_freedom) = probability. Thus, precision of CHIINV depends on precision of CHIDIST. CHIINV uses an iterative search technique.

---

## 4.1.4.6.6.31 CHI- TEST

### Syntax

CHITEST(actual_range, expected_range), where:

- **actual_range** is the range of data that contains observations to test against expected values.
- **expected_range** is the range of data that contains the ratio of the product of row totals and column totals to the grand total.

### Remarks

- The χ² test first calculates a χ² statistic using the formula,

\[
\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{\left(A_{ij} - E_{ij}\right)^2}{E_{ij}}
\]

## Code Examples

```csharp
// Example of using CHITEST
double chiTestResult = CHITEST(actualRange, expectedRange);
```

---

## Page-level Navigation/TOC (if applicable)

- CHIINV
- CHITEST

### Cross References

- See also: CHIDIST

### RAG Annotations

<!-- tags: chi-squared, distribution, statistical-test, probability, degrees-of-freedom, chitest, CHIINV, grid, windows-forms, interdependent-statistics, statistical-analysis -->
```