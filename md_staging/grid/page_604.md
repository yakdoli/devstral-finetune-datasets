```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_604.jpeg
document_name: grid
page_number: 604
page_id: grid#page_604
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Sorting support in the Grid Grouping Control.
- Use of Expression Fields to include formula-based columns.
- Utilizing Unbound Fields for custom field evaluations.
- Adding preview sections for memo fields or notes in records.

## Content

### Sorting Support in the Grid Grouping Control

#### Expression Fields
Expression fields enable the inclusion of columns with formula expressions.

**Figure 249: Sorting support in the Grid Grouping Control**

- **Example of Expression Fields**:
  | Sport     | ties | wins | year | Winning % | Losing % |
  |-----------|------|------|------|-----------|----------|
  | Basketball | 0   | 15   | 2003 | 53.57     | 46.43    |
  | Football   | 0   | 6    | 2003 | 60.00     | 40.00    |
  | Baseball   | 0   | 54   | 2003 | 76.06     | 23.94    |
  | Basketball | 0   | 13   | 2002 | 43.33     | 56.67    |
  | Basketball | 0   | 11   | 2001 | 36.67     | 63.33    |
  | Basketball | 0   | 10   | 2000 | 33.33     | 66.67    |
  | Basketball | 0   | 20   | 1999 | 57.14     | 42.86    |
  | Basketball | 0   | 18   | 1998 | 56.25     | 43.75    |
  | Basketball | 0   | 23   | 1997 | 69.70     | 30.30    |

**Figure 250: Expression Fields**

### Unbound Fields

Grid Grouping control allows the use of unbound fields with custom values, similar to Expression Fields, to evaluate field values at runtime.

**Figure 251: Unbound Fields in the Grid Grouping Control**

- **Example of Unbound Fields**:
  | Contact ID | Contact Name | Unbound |
  |------------|--------------|---------|
  | 1          | ALFKI        | ✔      |
  | 2          | ARCOS        |        |
  | 3          | BERGS        | ✔      |
  | 4          | CHOPS        |        |
  | 5          | ERNSH        | ✔      |
  | 6          | FRANK        |        |
  | 7          | KETHS        | ✔      |
  | 8          | PALPS        |        |
  | 9          | RICHARD      | ✔      |
  | 10         | SAMS         |        |

### Preview Rows

It is possible to add a preview section for each group or record to display memo fields or notes.

- **Preview Rows Feature**:
  - Enable preview rows when displaying memo fields or notes.
  - This allows for additional information to be noted for a given group or record.

## API Reference (if applicable)
- None explicitly mentioned in the provided content.

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, Grid Grouping Control, Expression Fields, Unbound Fields, Preview Rows, Sorting Support, formula expressions, custom values, memo fields, notes, runtime evaluation] keywords: [expression fields, unbound fields, sorting, winning percentage, losing percentage, custom field evaluation, contact ID, contact name, grid grouping, memo fields, notes] -->
```