```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_309.jpeg
document_name: grid
page_number: 309
page_id: grid#page_309
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:08Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- This section explains the syntax and usage of the LCM function in the context of the Essential Grid for Windows Forms.
- It provides examples and syntax for the LEFT and LN functions, emphasizing their functionality and application within Windows Forms.

### Content

#### LCM Function
The syntax of the LCM function is:
```plaintext
= LCM (number1, number2, ...)
```
- `number1 - Required.`
- If any value is not an integer, then it will be rounded down.

**Remarks:**
- `#NUM!`: If the number is less than zero (0).
- `#VALUE!`: Occurs if any of the given arguments are non-numeric.

**Example:**

| FORMULA      | RESULT   |
|--------------|----------|
| = LCM (5,2) | 10       |
| = LCM (-2)  | #NUM!    |

#### LEFT Function
##### Syntax
```plaintext
LEFT(text, num_chars)
```
Where:
- `text`: The text string containing the characters to extract.
- `num_chars`: Specifies the number of characters to extract.

**Remarks:**
- `Num_chars` must be greater than or equal to zero.
- If `num_chars` is greater than the length of `text`, `LEFT` returns all the text.
- If `num_chars` is omitted, it is assumed to be 1.

##### Example
For the `LEFT` function, consider the following:
- `text`: "Hello World"
- `num_chars`: 5

```plaintext
LEFT("Hello World", 5)
```
This returns: "Hello"

#### LN Function
The syntax for the LN function is:
```plaintext
= LN(number)
```
- `number`: The number for which the natural logarithm is to be calculated.

The LN function returns the natural logarithm (base e) of a number. It's commonly used in mathematical and scientific calculations.

**Example:**
```plaintext
= LN(2.71828)
```
This returns approximately: 1.0

### API Reference
None explicitly listed in the current content.

### Code Examples
No explicit code examples are provided in the current content.

### Cross References
- See also: Functions related to mathematical operations, string manipulation, and logarithmic calculations in the `Essential Grid for Windows Forms`.

### RAG Annotations
<!-- tags: [lcmt, left-function, ln-function, windows-forms, syntax, mathematical-functions, string-functions, natural-logarithm] keywords: [lcm, number1, number2, value!, left, num_chars, text, natural logarithm, ln] -->
```