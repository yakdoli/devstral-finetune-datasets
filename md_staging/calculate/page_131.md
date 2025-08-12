```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: calculate
page_number: 131
page_id: calculate#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:01Z
fidelity: lossless
-->

## Overview
- The page explains the syntax and usage of the AVERAGEIF and AVERAGEIFS functions in relevant software.
- It details how to calculate averages based on specified criteria, including examples and notes on error handling.

## Content

### AVERAGEIF Function
#### Overview
- If no cells in the range meet the criteria, AVERAGEIF returns the `#DIV/0!` error value.

#### Example
**Input Table**

|    | A          | B          |
|----|------------|------------|
| 1  | Earning    | Tax        |
| 2  | 100000     | 3000       |
| 3  | 200000     | 6000       |
| 4  | 300000     | 7500       |
| 5  | 400000     | 9000       |

**FORMULA** | **RESULT**
|------------|------------|
| `=AVERAGEIF(B2:B5, "<7000")` | 4500 |
| `=AVERAGEIF(A2:A5, ">250000")` | 350000 |

### 4.5.6.23 AVERAGEIFS

#### Description
- The AVERAGEIFS function finds the average of values in a given array that satisfy a set of given criteria.

#### Syntax
```markdown
=AVERAGEIFS(average_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

- **average_range**: Specific set of values to be averaged if the criteria range meets the provided criteria.
- **criteria_range1**: Array of values to be tested against the given criteria.
- **criteria1**: The condition to be tested on each of the values of the given range.

#### Notes
- If `average_range` is blank or a text value, AVERAGEIFS returns the `#DIV/0!` error value.
- If a cell in a criteria range is empty, AVERAGEIFS treats it as a `0` value.
- If cells in `average_range` cannot be translated into numbers, AVERAGEIFS returns the `#DIV/0!` error value.

#### Example

## API Reference (if applicable)
- None explicitly mentioned in the provided content.

## Code Examples (multi-language supported)
- None explicitly mentioned in the provided content.

<!-- tags: [averageif, averageifs, error handling, criteria, averaging] keywords: [average, criteria, averaging, error, div0] -->
```