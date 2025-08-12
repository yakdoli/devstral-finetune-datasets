```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_373.jpeg
document_name: grid
page_number: 373
page_id: grid#page_373
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:55Z
fidelity: lossless
--> 

# Essential Grid for Windows Forms

## VLOOKUP

### Overview
- Searches for a value in the leftmost column of a table and then returns a value in the same row from a column you specify in the table.
- Use VLOOKUP instead of HLOOKUP when your comparison values are located in a column to the left of the data you want to find.

### Description
- The V in VLOOKUP stands for "Vertical."

### Syntax
- **VLOOKUP(lookup_value, table_array, col_index_num, range_lookup)**, where:

#### Parameters
- **lookup_value**: The value to be found in the first column of the array. Lookup_value can be a value, a reference, or a text string.
- **table_array**: The table of information in which data is looked up. Use a reference to a range or a range name.
  - **range_lookup**: 
    - If `range_lookup` is True, the values in the first column of the `table_array` must be placed in ascending order: ..., -2, -1, 0, 1, 2, ..., A-Z, False, True; otherwise, VLOOKUP may not give the correct value.
    - If `range_lookup` is False, `table_array` does not need to be sorted.
  - The values in the first column of the `table_array` can be text, numbers, or logical values.
  - Uppercase and lowercase text are equivalent.
- **col_index_num**: The column number in the `table_array` from which the matching value must be returned.
  - A `col_index_num` of 1 returns the value in the first column of the `table_array`.
  - A `col_index_num` of 2 returns the value in the second column of the `table_array`, and so on.
- **range_lookup**: A logical value that specifies whether you want VLOOKUP to find an exact match or an approximate match.
  - If True or omitted, an approximate match is returned. In other words, if an exact match is not found, the next largest value that is less than or equal to the `lookup_value` is returned.

### Remarks
- If VLOOKUP can't find a `lookup_value` and the `range_lookup` is True, it uses the largest value that is less than or equal to the `lookup_value`.

## WEEKDAY

### Overview
- Returns the day of the week corresponding to a date. The day is given as an integer, ranging from 1 (Sunday) to 7 (Saturday) by default.

### Syntax

### Code Examples

### API Reference

### Cross References

<!-- tags: [VLOOKUP, WEEKDAY, grid, table, array, date, Windows Forms, Syncfusion, function, lookup, range_match] keywords: [lookup_value, table_array, col_index_num, range_lookup, approximate match, exact match, weekday, date function] -->
```