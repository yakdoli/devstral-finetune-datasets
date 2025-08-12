```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_258.jpeg
document_name: grid
page_number: 258
page_id: grid#page_258
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:42Z
fidelity: lossless
--> 

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of the `AVERAGEIFS` function in calculating averages based on multiple criteria in specific ranges.

## Content

### 4.1.4.6.6.21 AVERAGEIFS

The AVERAGEIFS function finds the average of values in a given array that satisfy a set of given criteria.

#### Syntax
= AVERAGEIFS(average_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)

- **average_range**: Specific set of values to be averaged if the criteria range meets the provided criteria.
- **criteria_range1**: Array of values to be tested against the given criteria.
- **criteria1**: The condition to be tested on each of the values of the given range.

#### Notes
- If `average_range` is blank or a text value, AVERAGEIFS returns the #DIV/0! error value.
- If a cell in a criteria range is empty, AVERAGEIFS treats it as a 0 value.
- If cells in `average_range` cannot be translated into numbers, AVERAGEIFS returns the #DIV/0! error value.

#### Example

##### Input Table

|   | A         | B       | C      |
|---|-----------|---------|--------|
| 1 | Earning   | Tax     | other  |
| 2 | 100000    | 3000    | 100    |
| 3 | 200000    | 6000    | 200    |
| 4 | 300000    | 7500    | 300    |
| 5 | 400000    | 9000    | 500    |

### Formula and Result Examples

| FORMULA                        | RESULT   |
|--------------------------------|----------|
| =AVERAGEIF(B2:B5,"<7000")     | 4500     |
| =AVERAGEIF(A2:A5,">250000")   | 350000   |

## API Reference (if applicable)
- Note: No specific API details are provided in the image, so this section is omitted.

## Code Examples (multi-language supported)
- Note: No specific code examples are provided in the image, so this section is omitted.

## Page-level Navigation/TOC (if applicable)
- Note: No table of contents or links are present in the image, so this section is omitted.

## Cross References
- Note: No explicit cross-references are mentioned in the image, so this section is omitted.

## RAG Annotations
<!-- tags: [Syncfusion WinForms, AVERAGEIFS, Formulas, Essential Grid, Windows Forms] keywords: [average, criteria, array, formula, error handling] -->
```