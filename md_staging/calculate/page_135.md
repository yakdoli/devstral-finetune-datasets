```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: calculate
page_number: 135
page_id: calculate#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:17Z
fidelity: lossless
-->

## Essential Calculate

### Input Table

|   | A       | B    | C      |
|---|---------|------|--------|
| 1 | Earning | Tax  | other  |
| 2 | 100000  | 3000 | 100    |
| 3 | 200000  | 6000 | 200    |
| 4 | 300000  | 7500 | 300    |
| 5 | 400000  | 9000 | 500    |

### Formula and Results

| FORMULA                                    | RESULT |
|--------------------------------------------|--------|
| =LOOKUP(6000,B2:B5,C2:C5)                 | 200    |
| =LOOKUP("C",{ "a", "b", "c", "d" };1,2,3,4) | 3      |

### 4.5.6.28 SEARCH

The SEARCH function returns the location of a substring in a string. This function is NOT case-sensitive.

#### Syntax

SEARCH(substring, string, [start_position])

- **substring**: Required. The text to be found.
- **string**: Required. The text in which to search for the value of the substring.
- **start_num**: Optional. The starting position for searching in the string.

#### Notes

- If the value of `find_text` is not found, the `#VALUE!` error value is returned.
- If the `start_num` argument is omitted, it is assumed to be 1.
- If `start_num` is not greater than 0, or is greater than the length of the `string` argument, the `#VALUE!` error value is returned.

#### Example

| FORMULA                     | RESULT |
|-----------------------------|--------|
| =SEARCH("base","database")  | 5      |

<!-- tags: [syncfusion, winforms, essential calculate, search function, lookup function, api reference, code examples] keywords: [lookup, search, substring, string, start_position, error handling, case sensitivity, find_text, start_num, value, lookup function, search function, substring search, string, base, database, result, 200, 3, 5] -->
``` 
