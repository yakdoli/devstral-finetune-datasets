```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_315.jpeg
document_name: grid
page_number: 315
page_id: grid#page_315
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

\[ \text{LOGNORMDIST}(x, \mu, \sigma) = \text{NORMSDIST}\left(\frac{\ln(x) - \mu}{\sigma}\right) \]

## LOOKUP

### Overview
- The LOOKUP function returns a value either from a one-row or one-column range, or from an array.
- The LOOKUP function has two syntax forms: vector and array.

### Vector Form
- The vector form of LOOKUP looks in a one-row or one-column range for a value, and then returns a value from the same position in a second one-row or one-column range.
- **Syntax**
  \[
  = \text{LOOKUP}(lookup\_value, lookup\_vector, result\_vector)
  \]

### Array Form
- The array form of LOOKUP looks in the first row or column of an array for the specified value, and then returns a value from the same position in the last row or column of the array.
- **Syntax**
  \[
  = \text{LOOKUP}(lookup\_value, array)
  \]

### Notes
- If the LOOKUP function can't find the lookup\_value, the function matches the largest value in lookup\_vector that is less than or equal to lookup\_value.
- If lookup\_value is smaller than the smallest value in lookup\_vector, LOOKUP returns the #N/A error value.

### Example

#### Input Table

|     | A       | B      | C      |
|-----|---------|--------|--------|
| 1   | Earning | Tax    | other  |
| 2   | 100000  | 3000   | 100    |
| 3   | 200000  | 6000   | 200    |
| 4   | 300000  | 7500   | 300    |
| 5   | 400000  | 9000   | 500    |

#### Formula and Result

| FORMULA                         | RESULT |
|---------------------------------|--------|
| `=LOOKUP(6000, B2:B5, C2:C5)`   | 200    |

<!-- tags: [syncfusion-sdk, essential-grid, windows-forms, look-up-function, vector-form, array-form, lookup-value, lookup-vector, result-vector, error-handling, example] keywords: [look-up, one-row, one-column range, array, syntax, vector, array, largest value, smallest value, #N/A error, matching value, row, column, uniform-grid, tax-calculation] -->
```