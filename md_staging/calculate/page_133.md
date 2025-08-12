```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: calculate
page_number: 133
page_id: calculate#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:53Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- SUMIFS function is explained with syntax, arguments, and an example.
- Address function is briefly introduced.

## Content

### 4.5.6.25 SUMIFS

The SUMIFS function sums the values in a given array that satisfy a set of given criteria.

#### Syntax
```plaintext
=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

- **criteria_range1**: Array of values to be tested against the given criteria.
- **criteria1**: The condition to be tested on each of the values of the given range.
- **sum_range**: The range of values to be summed if the associated criteria range meets the specified criteria.

#### Notes
- Cells in the `sum_range` argument that contain `TRUE` evaluate to 1; cells in `sum_range` that contain `FALSE` evaluate to 0 (zero).

#### Example
**Input Table**

|       | A         | B      | C     |
|-------|-----------|--------|-------|
| **1** | Earning   | Tax    | other |
| **2** | 100000    | 3000   | 100   |
| **3** | 200000    | 6000   | 200   |
| **4** | 300000    | 7500   | 300   |
| **5** | 400000    | 9000   | 500   |

**Formula and Result**

| FORMULA                                             | RESULT   |
|-----------------------------------------------------|----------|
| `SUMIFS(C2:C5, B2:B5, ">7000", B2:B5, "<10000")`   | **800**  |

### 4.5.6.26 ADDRESS

The ADDRESS function returns the address of a cell in a worksheet given specified row and column numbers.

## Page-level Navigation/TOC (if applicable)
- None present

## Cross References
- None present

## API Reference (if applicable)
- None present

## Code Examples (multi-language supported)
- None present

<!-- tags: [SUMIFS, ADDRESS, function, array, criteria, sum, Excel, Syncfusion Winforms] keywords: [sumifs, address, function, row, column, worksheet, criteria, range, sum_range, tax, other] -->
```