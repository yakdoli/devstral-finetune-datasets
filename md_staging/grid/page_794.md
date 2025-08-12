```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_794.jpeg
document_name: grid
page_number: 794
page_id: grid#page_794
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:56Z
fidelity: lossless
-->

## Overview
- Describes the filtering options available for grids in Syncfusion WinForms.
- Provides a detailed explanation of various comparison operators and logical operators for filtering grid data.
- Covers the syntax for applying these filters to specific columns in a grid.

## Content

### Filtering Grid Data

The following table outlines the various operators that can be used to filter grid data based on specific conditions. These filters allow users to display records in the grid that meet the specified criteria.

| **Operator** | **Syntax** | **Description** |
|--------------|------------|-----------------|
| `/`          | `[columnname] / 'anynumber'` | Filters grid based on the divided value computed. |
| `+`          | `[columnname] + 'anynumber'` | Filters grid based on the result computed. |
| `-`          | `[columnname] - 'anynumber'` | Filters grid based on computed value. |
| `<`          | `[columnname] < 'anynumber'` | Filters grid displaying records whose specified column holds a value lesser than the mentioned value. |
| `>`          | `[columnname] > 'anynumber'` | Filters grid displaying records whose specified column holds a value greater than the mentioned value. |
| `=`          | `[columnname] = 'value'` | Filters grid displaying records whose specified column holds a value equal to the mentioned value. |
| `<=`         | `[columnname] <='anynumber'` | Filters grid displaying records whose specified column holds a value lesser than or equal to the mentioned value. |
| `>=`         | `[columnname] >='anynumber'` | Filters grid displaying records whose specified column holds a value greater than or equal to the mentioned value. |
| `<>`         | `[columnname] <> 'value'` | Filters grid displaying records whose specified column holds a value not equal to the mentioned value. |
| `AND`        | `[expression1] AND [expression2] AND [expression]` | Filters grid displaying records that meet the criteria of all the expressions. |
| `OR`         | `[expression1] OR [expression2] OR [expression]` | Filters grid displaying records that meet the criteria of either or all the expressions. |
| `XOR`        | `[expression1] XOR [expression2] XOR [expression]` | Filters grid displaying records that don't meet the criteria of either or all the expressions. |
| `LIKE`       | `[columnname] LIKE 'value'` | Filters grid displaying records whose specified column holds a value equal to the mentioned value (irrespective of case). |

## Notes
- Ensure that the column names and values used in the expressions match the grid's data source schema.
- The `LIKE` operator is case-insensitive, allowing for flexible matching of records in the grid.

## Cross References
- Related documentation on grid data binding and column customization can be found in the general WinForms user guide.

<!-- tags: [syncfusion, winforms, grid, filtering, operators, user guide] keywords: [columnname, filter, grid, operators, AND, OR, XOR, LIKE] -->
```