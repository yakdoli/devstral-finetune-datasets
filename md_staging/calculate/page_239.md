```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: calculate
page_number: 239
page_id: calculate#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:59Z
fidelity: lossless
-->

## Overview
- Explanation of `col_index_num` and `range_lookup` parameters in `VLOOKUP`.
- Description of the `WEEKDAY` function and its parameters.

## Content

### VLOOKUP Parameters

- **col_index_num**: The column number in the `table_array` from which the matching value must be returned.
  - A `col_index_num` of `1` returns the value in the first column of the `table_array`.
  - A `col_index_num` of `2` returns the value in the second column of the `table_array`, and so on.

- **range_lookup**: A logical value that specifies whether you want `VLOOKUP` to find an exact match or an approximate match.
  - If `True` or omitted, an approximate match is returned.
  - If an exact match is not found, the next largest value that is less than the `lookup_value` is returned.

#### Remarks
- If `VLOOKUP` can't find a `lookup_value` and the `range_lookup` is `True`, it uses the largest value that is less than or equal to the `lookup_value`.

### 4.7.184 WEEKDAY

**Returns the day of the week corresponding to a date.** The day is given as an integer, ranging from `1` (Sunday) to `7` (Saturday) by default.

#### Syntax
``` 
WEEKDAY(serial_number, return_type)
```

#### Parameters
- **serial_number**: A sequential number that represents the date of the day you are trying to find.
  - Dates should be entered using the `DATE` function or as results of other formulas or functions.
  - Example: Use `DATE(2008,5,23)` for the 23rd day of May 2008.

- **return_type**: A number that determines the type of return value.
  - **If Return_type is:**
    - `1` or omitted: Numbers `1` (Sunday) through `7` (Saturday).
    - `2`: Numbers `1` (Monday) through `7` (Sunday).
    - `3`: Numbers `0` (Monday) through `6` (Sunday).

#### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations.
  - By default, January 1, 1900 is serial number `1`, and January 1, 2008 is serial number `39448` because it is 39,448 days after January 1, 1900.

## API Reference (if applicable)
- None specified in the current content.

## Code Examples (multi-language supported)
- None specified in the current content.

<!-- tags: [vlookup, weekday, function, parameter, return_type] keywords: [col_index_num, range_lookup, serial_number, exact match, approximate match, day of the week, date, integer, monday] -->
```