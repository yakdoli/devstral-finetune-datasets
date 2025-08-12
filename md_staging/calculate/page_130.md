```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: calculate
page_number: 130
page_id: calculate#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:52Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Demonstrates the usage of functions like `Clean`, `ISREF`, and `AVERAGEIF`.
- Provides examples and detailed syntax for these functions.

## Content

### Example
| FORMULA                | RESULT      |
|------------------------|-------------|
| `=Clean(Syncfusion)`   | Syncfusion  |
| `=Clean("Text*")`      | Text        |

#### 4.5.6.21 ISREF
The ISREF function returns the logical value TRUE if the given value is a reference value; otherwise, the function returns FALSE.

**Syntax**  
`=ISREF(given_value)`

- **given_value**: Required. The value that is to be tested. The value argument can be a blank (empty cell), error, logical value, text, number, or reference value, or a name referring to any of these.

**Example**
| FORMULA                              | RESULT   |
|--------------------------------------|----------|
| `=ISREF("Region1")`                 | FALSE    |
| `=ISREF(ISLOGICAL(TRUE))`           | TRUE     |

#### 4.5.6.22 AVERAGEIF
The AVERAGEIF function finds the average of values in a given array that satisfy a given criteria, and returns the average value of the corresponding values in a second given array.

**Syntax**  
`=AVERAGEIF(range, criteria, average_range)`

- **range**: Array of values to be tested against the given criteria.
- **criteria**: The condition to be tested in each of the values of the given range.
- **average_range**: Numeric values to be evaluated against the criteria and averaged.

**Notes**
- If range is blank or a text value, AVERAGEIF returns the `#DIV/0!` error value.
- If a cell in criteria is empty, AVERAGEIF treats it as a `0` value.
```