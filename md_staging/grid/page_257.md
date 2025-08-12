```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_257.jpeg
document_name: grid
page_number: 257
page_id: grid#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:54Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the AVERAGEA and AVERAGEIF functions, their syntax, and usage in calculating averages.
- Highlights the handling of specific data types and conditions within these functions.

## Content
### AVERAGEA(value1, value2, ...)
- **Syntax**:
  ```
  AVERAGEA(value1, value2, ...)
  ```
- **Where**:
  - `value1, value2, ...` are cells, ranges of cells, or values for which you want the average.

#### Remarks
- The arguments must be numbers, names, arrays, or references.
- Array or reference arguments containing text evaluate as 0 (zero). Use AVERAGE if text values should not be included.
- Arguments containing `True` evaluate as 1; arguments containing `False` evaluate as 0 (zero).

---

### 4.1.4.6.6.20 AVERAGEIF
- **Description**: The AVERAGEIF function finds the average of values in a given array that satisfy a given criterion and returns the average value of the corresponding values in a second given array.
- **Syntax**:
  ```
  =AVERAGEIF(range, criteria, average_range)
  ```
- **Parameters**:
  - `range`: Array of values to be tested against the given criteria.
  - `criteria`: The condition to be tested in each of the values of the given range.
  - `average_range`: Numeric values to be evaluated against the criteria and averaged.

#### Notes
- If `range` is blank or a text value, AVERAGEIF returns the `#DIV/0!` error value.
- If a cell in `criteria` is empty, AVERAGEIF treats it as a 0 value.
- If no cells in the `range` meet the criteria, AVERAGEIF returns the `#DIV/0!` error value.

#### Example
- **Input Table**:
  |   |   A     |   B   |
  |---|---------|-------|
  | 1 | Earning | Tax   |
  | 2 | 100000  | 3000  |

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [AVERAGEA, AVERAGEIF, Windows Forms, Essential Grid, average, criteria, range, cells, values, array] -->
```