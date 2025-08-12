```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_369.jpeg
document_name: grid
page_number: 369
page_id: grid#page_369
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Implements text formatting functions such as converting strings to uppercase and converting text to numbers.
- Discusses variance estimation for a sample population using the `VAR` function.

## Content

### Upper(text)

#### Definition
The `Upper(text)` function converts a string to uppercase.

#### Parameters
- `text`: The string you want to convert to uppercase.

---

### 4.1.4.6.6.252 VALUE

#### Description
Converts a text string that represents a number to a number.

#### Syntax
- `VALUE(text)`, where:
  - `text`: The text enclosed in quotation marks or a reference to a cell containing the text you want to convert.

#### Remarks
- Text can be in any of the constant number, date, or time formats recognized by **Essential Calculate**.
- You do not generally need to use the `VALUE` function in a formula, as the text is automatically converted to numbers as necessary.

---

### 4.1.4.6.6.253 VAR

#### Description
Estimates variance based on a sample.

#### Syntax
- `VAR(number1, number2, ...)`, where:
  - `number1, number2, ...`: Arguments corresponding to a sample of a population.

#### Remarks
- `VAR` assumes that its arguments are a sample of the population. If your data represents the entire population, then compute the variance using `VARP`.

---

## API Reference (if applicable)

### Functions
- `Upper(text)`
  - **Parameters**: `text`
  - **Returns**: The string converted to uppercase.

- `VALUE(text)`
  - **Parameters**: `text`
  - **Returns**: A numeric value equivalent to the provided text.

- `VAR(number1, number2, ...)`
  - **Parameters**: `number1, number2, ...`
  - **Returns**: The estimated variance based on a sample.

---

## RAG Annotations
<!-- tags: [grid, text formatting, value conversion, variance estimation] keywords: [uppercase, text to number conversion, VAR function, sample variance] -->
```