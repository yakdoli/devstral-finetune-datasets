```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_238.jpeg
document_name: calculate
page_number: 238
page_id: calculate#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:10Z
fidelity: lossless
-->

## Calculation Methods and Functions

### Overview
- Explanation of life as the number of periods over which an asset is depreciated.
- Clarification of terms like `start_period` and `end_period` for calculating depreciation.
- Description of the `factor` and the `no_switch` parameter in calculating balance decline.

### Detailed Explanation of Depreciation Parameters

**life**: The number of periods over which the asset is depreciated (sometimes called the useful life of the asset).

- **start_period**: The starting period for which you want to calculate the depreciation. `start_period` must use the same units as life.
- **end_period**: The ending period for which you want to calculate the depreciation. `end_period` must use the same units as life.
- **factor**: The rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).
- **no_switch**: A logical value specifying whether to switch to straight-line depreciation when depreciation is greater than the declining balance calculation.
  - If `no_switch` is `True`, straight-line depreciation is not used even when the depreciation is greater than the declining balance calculation.
  - If `no_switch` is `False` or omitted, straight-line depreciation is used when depreciation is greater than the declining balance calculation.
  
All arguments except `no_switch` must be positive numbers.

---

## 4.7.183 VLOOKUP

### Overview
- The `VLOOKUP` function searches for a value in the leftmost column of a table and returns a value in the same row from a specified column.
- Recommendation to use `VLOOKUP` instead of `HLOOKUP` when comparison values are located in a column to the left of the data you want to find.

#### Syntax

```plaintext
VLOOKUP(lookup_value, table_array, col_index_num, range_lookup)
```

#### Parameters

- **lookup_value**: The value to be found in the first column of the array. Lookup_value can be a value, a reference, or a text string.
- **table_array**: The table of information in which data is looked up. Use a reference to a range or a range name.
  - If `range_lookup` is `True`, the values in the first column of the `table_array` must be placed in ascending order: ..., -2, -1, 0, 1, 2, ..., A-Z, `False`, `True`; otherwise `VLOOKUP` may not give the correct value.
  - If `range_lookup` is `False`, `table_array` does not need to be sorted.
  - The values in the first column of the `table_array` can be text, numbers, or logical values.
  - Uppercase and lowercase text are equivalent.

## RAG Annotations
<!-- tags: [depreciation, calculation, VLOOKUP, straight-line-depreciation, declining-balance-method] keywords: [start_period, end_period, factor, life, linear-depreciation, balance-decline, no_switch, range_lookup, table_array, lookup_value, col_index_num, VLOOKUP, HLOOKUP] -->
```