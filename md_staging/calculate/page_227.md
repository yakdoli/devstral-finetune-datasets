```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_227.jpeg
document_name: calculate
page_number: 227
page_id: calculate#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:23Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains functions and formulas used in calculations.
- Focuses on the SUBSTITUTE function and its applications.
- Includes description of the Sum and SumIf functions.

## Content

|   | A                                  | Description (Result)                                            |
|---|------------------------------------|-----------------------------------------------------------------|
| 1 | Data                              |                                                                 |
| 2 | Sales Data                        |                                                                 |
| 3 | Quarter 1, 2008                   |                                                                 |
| 4 | Quarter 1, 2011                   |                                                                 |
|   | Formula                            | Description (Result)                                            |
|   | =SUBSTITUTE(A2, "Sales", "Cost") | Substitutes Cost for Sales (Cost Data)                          |
|   | =SUBSTITUTE(A3, "1", "2", 1)     | Substitutes first instance of "1" with "2" (Quarter 2, 2008)   |
|   | =SUBSTITUTE(A4, "1", "2", 3)     | Substitutes third instance of "1" with "2" (Quarter 1, 2012)   |

### 4.7.158 Sum

The Sum function adds all numbers in a range of cells and returns the result.

#### Syntax:
Sum( number1, number2, … number_n )

**Where:**
- number1 is the first number
- number2 is the second number
- number_n is the nth number to be added together

### 4.7.159 SumIf

SumIf function adds the specified range of cells by a given criteria.

#### Syntax:
SumIf( range, criteria, sum_range )

**Where:**
- range is the range of cells you want to apply the criteria against.

## API Reference (if applicable)
- None explicitly mentioned in this section.

## Code Examples (multi-language supported)
- No specific code examples are provided in this section.

## Page-level Navigation/TOC (if applicable)
- None explicitly present.

## Cross References
- See also: SUBSTITUTE function, Sum function, SumIf function.

<!-- tags: [product, module, control, api, version?] keywords: [SUBSTITUTE, Sum, SumIf, Excel functions, formula, calculate, data analysis] -->
```