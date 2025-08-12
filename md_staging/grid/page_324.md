```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_324.jpeg
document_name: grid
page_number: 324
page_id: grid#page_324
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:57Z
fidelity: lossless
-->

## The `N` Function

### Overview
- The `N` function converts the given value into a numeric value.
- Converts numerical values as numeric values.
- Converts date values as serial numbers.
- Converts `TRUE` values as `1` and other values as `0`.

### Syntax
- The syntax of the `N` function is:
  ```plaintext
  =N(value)
  ```
- A value is required.

### Example

| FORMULA      | RESULT   |
|--------------|----------|
| `=N(7)`      | `7`      |
| `=N("EVEN")` | `0`      |
| `=N(1/1/2008)`| `39448` |
| `=N(TRUE)`   | `1`      |

---

## The `NA` Function

### Overview
- The `NA` function returns the #N/A error.
- This error message is produced when a formula is unable to find a value that it needs.
- This error message denotes 'value not available.'

### Syntax
- The syntax of the `NA` function is:
  ```plaintext
  =NA()
  ```
- The `NA` function syntax has no arguments.

### Remarks
- The function doesn’t have any arguments.

### Example

| FORMULA | RESULT |
|---------|--------|
| `=NA()` | `#NA`  |

---

## References

<!-- tags: [syncfusion, winforms, grid, n-function, na-function, version:11.4.0.26] keywords: [numeric conversion, date conversion, logic values, error handling, reference, documentation, grid control] -->
```