```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_235.jpeg
document_name: calculate
page_number: 235
page_id: calculate#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:47Z
fidelity: lossless
-->

## TRUNC(number, num_digits)

### Function Description
- **TRUNC(number, num_digits)** truncates a number to a specified number of decimal places.

### Parameters
- **number**: The number you want to truncate.
- **num_digits**: A number specifying the precision of the truncation. The default value for **num_digits** is 0 (zero).

### Remarks
- **TRUNC and INT Comparison**:
  - Both functions return integers.
  - **TRUNC** removes the fractional part of the number.
  - **INT** rounds numbers down to the nearest integer based on the value of the fractional part of the number.
  - **INT and TRUNC** differ only when using negative numbers:
    - **TRUNC(-4.3)** returns `-4`.
    - **INT(-4.3)** returns `-5` because `-5` is the lower number.

---

## 4.7.176 Upper

### Function Description
The **Upper** function converts all characters in a text string to uppercase.

### Syntax
- **Upper(text)**

### Parameters
- **text**: The string you want to convert to uppercase.

---

## 4.7.177 Value

### Function Description
The **Value** function computes the date or a string that contains the number, and converts it into number format.

### Syntax
- **Value(range)**

### Parameters
- **range**: The string that contains the date or a number.

---

<!-- tags: [syncfusion-sdk, calculate, TRUNC, Upper, Value] keywords: [truncation, integer conversion, uppercase, number format, string conversion] -->
```