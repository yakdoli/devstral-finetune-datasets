```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_129.jpeg
document_name: calculate
page_number: 129
page_id: calculate#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:40Z
fidelity: lossless
-->

## Logical Value and Logical Functions

### Logical_value1: Required

This can be either TRUE or FALSE, and can be logical values, arrays, or references.

#### Example

The XOR function is used to determine if an odd number of logical arguments are TRUE. If the arguments do not have logical values, XOR returns the #VALUE! error.

| FORMULA                   | RESULT   |
|---------------------------|----------|
| = XOR( 5>0, 7<9 )        | FALSE    |
| =XOR(3>12, 4>6)          | TRUE     |

### 4.5.6.19 IFNA

#### Overview

The IFNA function returns the value specified if the formula returns the #N/A error value; otherwise, it returns the result of the given formula.

#### Syntax

```markdown
=IFNA (Formula_value, value_if_na)
```

##### Parameters
- **Formula_value**: Required. The argument that is checked for the #N/A error value.
- **value_if_na**: Required. The value returned if the formula evaluates to the #N/A error value.

##### Example

| FORMULA                     | RESULT    |
|-----------------------------|-----------|
| =IFNA("#N/A","Incorrect")   | Incorrect |
| =IFNA(1602,"incorrect")     | 1602     |

### 4.5.6.20 CLEAN

#### Overview

The CLEAN function is used to remove non-printable characters from the given text, represented by numbers 0 to 31 of the 7-bit ASCII code.

#### Syntax

```markdown
=Clean(Text)
```

##### Parameters
- **Text**: Required. String or text from which to remove nonprintable characters.

---
<!-- tags: [logical functions, xor, ifna, clean, syncfusion winforms, 11.4.0.26] keywords: [logical_value1, formula_value, value_if_na, non-printable characters, ascii code, error handling] -->
```