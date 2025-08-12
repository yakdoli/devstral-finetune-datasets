```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_264.jpeg
document_name: grid
page_number: 264
page_id: grid#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the chi-square test (`CHITEST`) and its appropriate use.
- Explains the `CLEAN` function and its syntax.
- Provides details about the `COMBIN` function and its syntax.

## Content

### CHITEST
The chi-square test is used to determine the independence between two categorical variables. It involves the following components:
- $ A_{ij} = $ actual frequency in the $ i $-th row, $ j $-th column
- $ E_{ij} = $ expected frequency in the $ i $-th row, $ j $-th column
- $ r = $ number of rows
- $ c = $ number of columns
- A low value of $ \chi^2 $ is an indicator of independence.

The use of `CHITEST` is most appropriate when $ E_{ij} $'s are not too small. Some statisticians suggest that each $ E_{ij} $ should be greater than or equal to 5.

### 4.1.4.6.6.32 CLEAN
The `CLEAN` function is used to remove non-printable characters (represented by numbers 0 to 31 of the 7-bit ASCII code) from the given text.

#### Syntax
```csharp
=Clean(Text)
```

#### Parameters
- **Text**: Required. The string or text from which to remove non-printable characters.

#### Example
| FORMULA           | RESULT     |
|-------------------|------------|
| =Clean(Syncfusion) | Syncfusion |
| =Clean("Text*")   | Text       |

### 4.1.4.6.6.33 COMBIN
The `COMBIN` function returns the number of combinations for a given number of items. Use it to determine the total possible number of groups for a given number of items.

#### Syntax
```csharp
COMBIN(number, number_chosen)
```

#### Parameters
- **number**: The number of items.
- **number_chosen**: The number of items in each combination.

## RAG Annotations
<!-- tags: [SYNCFUNION, GRID, CHITEST, CLEAN, COMBIN, STATISTICS, COMBINATIONS] keywords: [chi-square, non-printable characters, combination, independence, ASCII, expected frequency, actual frequency] -->
```