```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_176.jpeg
document_name: calculate
page_number: 176
page_id: calculate#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:20Z
fidelity: lossless
-->

## Essential Calculate

Returns the harmonic mean of a data set. The harmonic mean is the reciprocal of the arithmetic mean of reciprocals.

### Syntax

**HARMEAN(number1, number2,...)**  
`number1, number2, ...` are arguments for which you want to calculate the mean.

### Remarks

- The arguments must be either numbers or names, arrays, or references that contain numbers.
- All data values must be positive.
- The equation for the harmonic mean is:

\[ H = \frac{n}{\sum \frac{1}{y_i}} \]

## 4.7.64 HLOOKUP

Searches for a value in the top row of the array of values and then returns a value in the same column from a row you specify in the array. Use HLOOKUP when your comparison values are located in a row across the top of a table of data and you want to look down a specified number of rows. Use VLOOKUP when your comparison values are located in a column to the left of the data you want to find.

### Syntax

**HLOOKUP(lookup_value, table_array, row_index_num, range_lookup)**

#### where:
- `lookup_value` is the value to be found in the first row of the table. Lookup_value can be a value, a reference, or a text string.
- `table_array` is a table of information in which data is looked up. Use a reference to a range or a range name.

<!-- tags: [syncfusion, winforms, harmonic mean, arithmetric mean, reciprocals, lookup, hlookup, vlookup, array, data set] keywords: [harmonic mean, arithmetric mean, reciprocals, lookup value, table, row, number, reference, equation, search, comparison, data, page, harmonic mean equation] -->
```