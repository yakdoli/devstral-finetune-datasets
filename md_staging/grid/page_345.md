```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_345.jpeg
document_name: grid
page_number: 345
page_id: grid#page_345
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- RIGHT function extracts the last character or characters in a text string based on the number of characters specified.
- The ROMAN function converts an Arabic number to a Roman numeral, providing different styles of representation.

## Content

### 4.1.4.6.6.202 RIGHT

**Description**  
`RIGHT` returns the last character or characters in a text string, based on the number of characters you specify.

**Syntax**  
`RIGHT(text, num_chars)`, where:
- `text` is the text string containing the characters you want to extract.
- `num_chars` specifies the number of characters you want RIGHT to extract.

**Remarks**  
- `Num_chars` must be greater than or equal to zero.
- If `num_chars` is greater than the length of `text`, RIGHT returns all the text.
- If `num_chars` is omitted, it is assumed to be 1.

### 4.1.4.6.6.203 ROMAN

**Description**  
The ROMAN function converts an Arabic number to a Roman numeral. This function returns a text string depicting the Roman numeral form of the given number.

**Syntax**  
The syntax of the ROMAN function is  
`=ROMAN( number, (form) )`  
- `number` – Required.
- `Form` – Optional, this value will specify the style of the Roman numeral.

**Remarks**  
If the number is not an integer, then it will be rounded down.

**Form Types**  
| Form           | Type                             |
|----------------|-----------------------------------|
| 0 or omitted   | Classic.                         |
| 1              | More concise. See example below.  |
| 2              | More concise. See example below.  |
| 3              | More concise. See example below.  |
| 4              | Simplified.                      |

**Remarks:**  

## Page-level Navigation/TOC (if applicable)
- [unclear] (if needed)

## Cross References
- None (if not present)

<!-- tags: [product, ROMAN, RIGHT, function, Essential Grid, Windows Forms] keywords: [Roman numeral, number conversion, text extraction, data manipulation, numeric conversion, last characters, parameters, classic, concise, simplified] -->
```