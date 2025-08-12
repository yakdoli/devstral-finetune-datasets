```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_318.jpeg
document_name: grid
page_number: 318
page_id: grid#page_318
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:45Z
fidelity: lossless  
-->

# Essential Grid for Windows Forms

## Overview
- This section covers the use of the `MID`, `MIN`, and `MINA` functions in Syncfusion WinForms.
- These functions assist in extracting strings and calculating minimum values, which are crucial for implementing data operations.

## Content

### MID

**MID** returns a text segment of a character string. The parameters specify the starting position and the number of characters.

#### Syntax

`MID(text, start_position, num_chars)`, where:
- `text` is the text containing the characters to extract.
- `start` is the position of the first character in the text to extract.
- `num_chars` specifies the number of characters in the part of the text.

---

### MIN

**MIN** returns the smallest number in a set of values.

#### Syntax

`MIN(number1, number2, ...)`, where:
- `number1, number2, ...` are numbers for which you want to find the minimum value.

#### Remarks
- If an argument is an array or reference, only numbers in that array or reference are used.
- Empty cells, logical values, or text in the array or reference are ignored. If logical values and text should not be ignored, use `MINA`.

---

### MINA

**MINA** returns the smallest value in the list of arguments. Text and logical values such as `True` and `False` are compared as well as numbers.

#### Syntax

<!-- tags: [syncfusion, winforms, mid, min, mina, functions, data extraction, minimum values, text operations, logical values, array processing] -->
```html
```  
```