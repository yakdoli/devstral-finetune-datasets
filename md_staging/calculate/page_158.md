```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: calculate
page_number: 158
page_id: calculate#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:22Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides functions for counting blank cells and cells meeting specific criteria.
- Includes remarks regarding how certain types of cells (e.g., formulas returning empty text) are handled.

### COUNTBLANK(range)
**Syntax**:  
COUNTBLANK(range)  
**Where**:  
- `range` is the range from which you want to count the blank cells.

**Remarks**:  
- Cells with formulas that return "" (empty text) are also counted. Cells with zero values are not counted.

### 4.7.31 COUNTIF  
**Counts the number of cells within a range that meet the given criteria.**

**Syntax**:  
COUNTIF(range, criteria)  
**Where**:  
- `range` is the range of cells from which you want to count cells.  
- `criteria` is the criteria in the form of a number, expression, or text that defines which cells will be counted. For example, the criteria can be expressed as `">32"`.

**Remarks**:  
- If and Sumif are other library functions that can be used to conditionally compute values.

### 4.7.32 COVAR  
**Returns covariance, the average of the products of deviations for each data point pair.**

## API Reference (if applicable)
- **COUNTBLANK**  
  - **Namespace**: Essential Calculate  
  - **Parameters**: `range` (range to count blank cells from)  
  - **Remarks**: Handles cells with formulas returning empty text but not cells with zero values.  

- **COUNTIF**  
  - **Namespace**: Essential Calculate  
  - **Parameters**:  
    - `range` (range of cells to evaluate)  
    - `criteria` (criteria to filter cells)  
  - **Remarks**: Useful for conditional counting operations.  

- **COVAR**  
  - **Namespace**: Essential Calculate  
  - **Parameters**:  
    - `Array1` (first set of data points)  
    - `Array2` (second set of data points)  
  - **Remarks**: Computes covariance between two data sets.

## Code Examples
```csharp
// Example for COUNTBLANK
double blankCount = COUNTBLANK(rangeA1:A10);

// Example for COUNTIF
double countAbove32 = COUNTIF(rangeA1:A10, ">32");

// Example for COVAR
double covariance = COVAR(array1, array2);
```

## Cross References
- See also: Other conditional functions like IF and SUMIF for related operations.
- Refer to the documentation for Array manipulation for enhanced examples.

<!-- tags: [essential-calculate, countblank, countif, covar, winforms, 11.4.0.26] keywords: [count blank cells, conditional counting, covariance, data point pairs, conditional library functions] -->
```