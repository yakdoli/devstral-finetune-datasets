```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_360.jpeg
document_name: grid
page_number: 360
page_id: grid#page_360
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Adds the cells specified by a given criteria using the SUMIF function.
- Sums the values in a given array that satisfy a set of given criteria using the SUMIFS function.

### 4.1.4.6.6.232 SUMIF

**Description:**  
Adds the cells specified by a given criteria.

**Syntax:**  
SUMIF(range, criteria, sum_range), where:
- **range:** the range of cells you want evaluated.
- **criteria:** the criteria in the form of a number, expression, or text that defines which cells will be added. For example, criteria can be expressed as ">32" or some other logical expression.
- **sum_range:** the actual cells to sum.

**Remarks:**
- The cells in `sum_range` are summed only if their corresponding cells in `range` match the `criteria`.
- If `sum_range` is omitted, the cells in `range` are summed.

### 4.1.4.6.6.233 SUMIFS

**Description:**  
The SUMIFS function sums the values in a given array that satisfy a set of given criteria.

**Syntax:**  
=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)

**Parameters:**
- **criteria_range1:** Array of values to be tested against the given criteria.
- **criteria1:** The condition to be tested on each of the values of given range.
- **sum_range:** The range of values to be summed if the associated criteria range meets the specified criteria.

**Notes:**
- Cells in the `sum_range` argument that contain TRUE evaluate to 1; cells in `sum_range` that contain FALSE evaluate to 0 (zero).

### Example

- **Input Table:**

---

### Page-level Navigation/TOC (if applicable)
- This section provides references to the functions SUMIF and SUMIFS, detailing their usage and parameters.

### Cross References
- See also: SUMIF, SUMIFS

<!-- tags: [syncfusion.winforms, grid, sumif, sumifs] keywords: [sumif, sumifs, range, criteria, sum_range, array, condition, function, windows forms, essential grid] -->
```