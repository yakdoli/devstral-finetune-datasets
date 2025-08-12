```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_152.jpeg
document_name: calculate
page_number: 152
page_id: calculate#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:06Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.19 CHITTEST

#### Overview

- Returns the test for independence. CHITEST returns the value from the chi-squared (χ²) distribution for the statistic and the appropriate degrees of freedom.
- Provides insight into whether observed values are independent of expected values.

#### Content

##### Syntax

```plaintext
CHITEST(actual_range, expected_range)
```

##### Parameters

- **actual_range**: The range of data that contains observations to test against expected values.
- **expected_range**: The range of data that contains the ratio of the product of row totals and column totals to the grand total.

##### Remarks

- The χ² test first calculates a χ² statistic using the formula:
  \[
  \chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(A_{ij} - E_{ij})^2}{E_{ij}}
  \]
  where:
  - \( A_{ij} \): actual frequency in the i-th row, j-th column
  - \( E_{ij} \): expected frequency in the i-th row, j-th column
  - \( r \): number of rows
  - \( c \): number of columns

- A low value of χ² is an indicator of independence.
- The use of CHITEST is most appropriate when Eij's are not too small. Some statisticians suggest that each Eij should be greater than or equal to 5.

### 4.7.20 Choose

#### Overview

- The Choose function returns the value from a range of values on a specific index.

#### Content

- The Choose function is useful for selecting specific values based on a given index.
- It is commonly used for creating branch logic or selecting options dynamically.

---

<!-- tags: [calculate, chitest, choose, chi-squared-test, statistical-testing, user-guide, syncfusion-winforms, version-11.4.0.26] keywords: [chitest, chi-squared, independence-test, choose function, range selection, statistical analysis, syncfusion, winforms] -->
``` 
