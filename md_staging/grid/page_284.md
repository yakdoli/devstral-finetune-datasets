```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_284.jpeg
document_name: grid
page_number: 284
page_id: grid#page_284
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the functionality and usage of various Excel-like functions in the Essential Grid for Windows Forms.
- Provides syntax and examples for the DVARP and EVEN functions.
- Describes the ERROR.TYPE function and its return values.

## Content

### 4.1.4.6.6.80 DVARP

The DVARP function calculates the variance of a population based on the entire population by using the numbers in a column of a list or database which matches the conditions that have been specified.

#### Syntax:
DVARP(database, field, criteria) where:
- `database` is the range of cells that makes up the list or database.
- `field` indicates which column is used in the function.
- `criteria` is the range of cells that contains the conditions that you specify.

### 4.1.4.6.6.81 EVEN

Returns the number rounded up to the nearest even integer.

#### Syntax:
EVEN(number), where:
- `number` is the value that is to be rounded.

#### Remarks
- Regardless of the sign of the number, a value is rounded up when adjusted away from zero. If the number is an even integer, no rounding occurs.

### 4.1.4.6.6.82 ERROR.TYPE

The Error.Type function returns an integer for the given error value that denotes the type of the given error.

#### Syntax:
The syntax of the ERROR.TYPE function is
```
= ERROR.TYPE(value)
```
- The given value is required.

#### Return Value:
This section concludes with the return value of the function.

## API Reference (if applicable)
- Provides additional information on the functions and their usage within the Essential Grid for Windows Forms context.

## Code Examples (multi-language supported)
- Includes examples demonstrating the use of these functions.

<!-- tags: windows-forms, dvarp, even, error.type, function, essential-grid, api-reference, version:11.4.0.26 -->
```