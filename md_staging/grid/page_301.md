```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_301.jpeg
document_name: grid
page_number: 301
page_id: grid#page_301
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:41Z
fidelity: lossless
-->

## IFERROR Function

### Parameters

- **value** – Required. This is a value to check the error.
- **value_error** – Required. This value will be returned if the value has an error.

### Remarks

- If the value_error is an empty cell, then the function takes the error value as an empty string.

### Example

| FORMULA                                      | RESULT           |
|----------------------------------------------|------------------|
| = IFERROR (200/55, "ERROR in DIVISION")      | 3                |
| = IFERROR (200/0, "ERROR in DIVISION")       | ERROR in DIVISION |

## IFNA Function

**4.1.4.6.6.111 IFNA**

The IFNA function returns the value specified if the formula returns the #N/A error value; otherwise, it returns the result of the given formula.

### Syntax

```plaintext
=IFNA (Formula_value, value_if_na)
```

### Parameters

- **Formula_value**: Required. The argument that is checked for the #N/A error value.
- **value_if_na**: Required. The value returned if the formula evaluates to the #N/A error value.

### Example

| FORMULA                                | RESULT      |
|----------------------------------------|-------------|
| =IFNA("#N/A", "Incorrect")            | Incorrect    |
| =IFNA(1602, "incorrect")              | 1602        |

## Index Function

**4.1.4.6.6.112 Index**

The Index function returns the exact cell value from the provided row index and column index from a specific range of cells.

### Syntax

```plaintext
Index(range, row, col)
```

### Parameters

- **range**: The specified range of cells from which to retrieve the value.
- **row**: The row index of the cell.
- **col**: The column index of the cell.

---

<!-- tags: [Syncfusion Winforms, grid, IFERROR Function, IFNA Function, Index Function, error handling, cell value retrieval] keywords: [IFERROR, IFNA, Index, error value, cell index, range, grid, function, syntax, example] -->
```