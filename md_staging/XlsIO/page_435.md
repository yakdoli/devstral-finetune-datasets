```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_435.jpeg
document_name: XlsIO
page_number: 435
page_id: XlsIO#page_435
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:54Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Essential XlsIO provides data binding functionality from various data sources.
- Supports data binding using data sources, variables, variable arrays, and formulas.
- Various arguments can be used with markers for controlling data import formatting.

## Content

### Data Source

This includes data tables, datasets, data readers, and data views. A data source can be used to bind a large number of records to the template document. This will add the rows for each record, and the fields to be bound are identified through the field name in the template.

**Syntax:** `%DataSource.FieldName`

### Variable Name

This option allows you to bind a single data value stored in a variable to the marker in the template.

**Syntax:** `%VariableName`

### Variable Array

This option allows you to bind an array of data stored in an array to the marker in the template.

**Syntax:** `%VariableArray`

### Formulas

This option allows you to create formulas for each row when multiple records comprising formula in the cells are bound to the marker. If a cell contains a formula, by default it will be stretched to the rows/columns for any of the above sources of data binding.

#### Figure: Formulas
![Formulas](image.png)

### What are the Various Arguments for the Marker?

The following arguments can be used with the marker to control the formatting while binding the data:

- **Horizontal:** This argument specifies the horizontal direction of the data import for complex variables.
- **Vertical:** This argument specifies the vertical direction of the data import for complex variables.
- **Insert:** This argument inserts new rows or columns depending on the direction argument for each new cell. By default, the rows cannot be added.
- **insert:copystyles:** This argument copies the style from the row above or the left column.

## RAG Annotations
<!-- tags: [data binding, Excel templates, data sources, variables, formulas, formatting arguments] keywords: [Essential XlsIO, data tables, datasets, data readers, data views, formula stretching, horizontal, vertical, insert, copystyles] -->
```