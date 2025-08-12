```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_364.jpeg
document_name: grid
page_number: 364
page_id: grid#page_364
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:35Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the SYD calculation.
- Provides details about the T function in Windows Forms.
- Explains how the T function tests whether a value is text.

## Content

### SYD Calculation
- **cost**: The initial cost of the asset.
- **salvage**: The value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life**: The number of periods over which the asset is depreciated (sometimes called the useful life of the asset).
- **per**: The period and must use the same units as life.

#### Remarks
- SYD is calculated as follows:
  \[
  \frac{(cost - salvage) * (life - per + 1) * 2}{life \times (life + 1)}
  \]

### T Function: Testing for Text

#### Description
The T function tests whether the given value is text or not. If the given value is text, then it returns the given text. Otherwise, the function returns an empty text string.

#### Syntax
The syntax of the T function is:
\[
=T(value)
\]
- **value**: Required. This is a value to be checked.

#### Remarks
If the value is not a number or logical value, then the function returns an empty string.

### Example:
| FORMULA             | RESULT          |
|---------------------|-----------------|
| =T("SYNCFUSION")   | SYNCFUSION      |
| =T(TRUE)           |                 |
| =T(10)             |                 |

## API Reference

## Code Examples

## Cross References

<!-- tags: [SYD, T function, WindowsForms, Syncfusion] keywords: [SYD calculation, SYD formula, T function, text testing, Windows Forms, value testing, T function syntax] -->
```