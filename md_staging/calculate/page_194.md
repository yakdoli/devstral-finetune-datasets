```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: calculate
page_number: 194
page_id: calculate#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:45Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains the syntax and usage of functions such as `MID`, `MIN`, and `MINA`.
- Provides detailed descriptions and remarks for each function to understand their behavior.

## Content

### Syntax

#### MID Function
MID(text, start_position, num_chars)

Where:
- **text** is the text containing the characters to extract.
- **start** is the position of the first character in the text to extract.
- **number** specifies the number of characters in the part of the text.

#### 4.7.100 MIN
Returns the smallest number in a set of values.

- **Syntax**
    MIN(number1, number2, ...)

Where:
- **number1, number2, ...** are numbers for which you want to find the minimum value.

- **Remarks**
    - If an argument is an array or reference, only numbers in that array or reference are used.
    - Empty cells, logical values, or text in the array or reference are ignored. If logical values and text should not be ignored, use `MINA`.

#### 4.7.101 MINA
Returns the smallest value in the list of arguments. Text and logical values such as True and False are compared as well as numbers.

- **Syntax**
    MINA(value1, value2, ...)

### Summary of Functions
The functions `MID`, `MIN`, and `MINA` are described with their syntax, parameters, and remarks to ensure users understand how to effectively use them in their calculations.

## RAG Annotations
<!-- tags: [functions, syntax, min, mina, mid] keywords: [MID, MIN, MINA, start_position, text, num_chars, values, remarks, array, reference] -->
```