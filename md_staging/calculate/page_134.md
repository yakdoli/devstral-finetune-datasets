```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: calculate
page_number: 134
page_id: calculate#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:05Z
fidelity: lossless
-->

### Essential Calculate

#### Syntax

`ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])`

- `row_num`: A numeric value that specifies the row number.
- `column_num`: A numeric value that specifies the column number.
- `abs_num`: Optional. A numeric value that specifies the type of reference to return.
- `A1`: A logical value that specifies the A1 or R1C1 reference style.

#### Example

| FORMULA                       | RESULT                  |
|-------------------------------|-------------------------|
| `=ADDRESS(2,3,2,FALSE)`      | `R2C[3].`              |
| `=ADDRESS(2,3,1,FALSE,"[Book1]Sync1")` | `[Book1]Sync1!R2C3` |

### 4.5.6.27 LOOKUP

The LOOKUP function returns a value either from a one-row or one-column range, or from an array. The LOOKUP function has two syntax forms: vector and array.

#### Vector Form

The vector form of LOOKUP looks in a one-row or one-column range for a value, and then returns a value from the same position in a second one-row or one-column range.

**Syntax**

`=LOOKUP(lookup_value, lookup_vector, result_vector)`

#### Array Form

The array form of LOOKUP looks in the first row or column of an array for the specified value, and then returns a value from the same position in the last row or column of the array.

**Syntax**

`=LOOKUP(lookup_value, array)`

#### Notes

- If the LOOKUP function can't find the `lookup_value`, the function matches the largest value in `lookup_vector` that is less than or equal to `lookup_value`.
- If `lookup_value` is smaller than the smallest value in `lookup_vector`, LOOKUP returns the `#N/A` error value.

#### Example
```html

<!-- tags: [syncfusion, winforms, look-up-function, address-function, essential-calculate] keywords: [lookup, vector, array, reference-style, row-number, column-number, address, error-values] -->
```