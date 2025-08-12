```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_346.jpeg
document_name: grid
page_number: 346
page_id: grid#page_346
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Description of the #VALUE! error handling in numeric expressions.
- Explanation of the ROMAN formula and its example usage.
- Syntax and behavior of the ROUND and ROUNDDOWN functions.

## Content

### #VALUE! Error
- Happens if any of the given values is non-numeric, or for values less than 0 and greater than 3999.

#### Example
| FORMULA         | RESULT   |
|------------------|----------|
| = ROMAN (499,0) | CDXCIX   |
| = ROMAN (499,1) | ID       |
| =ROMAN(-100)    | #VALUE!  |

### 4.1.4.6.6.204 ROUND
- Rounds a number to a specified number of digits.

#### Syntax
`ROUND(number, num_digits)`, where:
- `number` is the number you want to round off.
- `num_digits` specifies the number of digits you want to round off.

#### Remarks
- If `num_digits > 0`, then `number` is rounded off to the specified number of decimal places.
- If `num_digits = 0`, then `number` is rounded off to the nearest integer.
- If `num_digits < 0`, then `number` is rounded off to the left of the decimal point.

### 4.1.4.6.6.205 ROUNDDOWN
- Rounds a number down towards zero.

#### Syntax
`ROUNDDOWN(number, num_digits)`, where:
- `number` is the number you want to round down.
- `num_digits` specifies the number of digits you want to round down to.

## API Reference (if applicable)
- This section may contain namespace, class, or member details from `Syncfusion.Windows.Forms.Tools` for the functions described above.

## Code Examples (multi-language supported)
- Provide examples of the `ROUND` and `ROUNDDOWN` functions in C# or VB as applicable.

## Page-level Navigation/TOC (if applicable)
- No explicit TOC listed on this page.

## Cross References
- See also references are without external URLs and strictly based on visible text on the page.

<!-- tags: [EssentialGrid, WindowsForms, ROUND, ROUNDDOWN, ROMAN, WinForms,SyncfusionSDK] keywords: [ROUND, ROUNDDOWN, ROMAN, formulas, numeric expressions, error handling, decimal places, rounding, numeric digits] -->
```