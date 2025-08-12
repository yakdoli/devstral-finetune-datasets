```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: XlsIO
page_number: 108
page_id: XlsIO#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:52Z
fidelity: lossless
-->

## Overview
- Overview of Excel file formats supported by XlsIO: xls and xlsx.
- Comparison of features supported for reading and writing in the two formats.

## Content

### Feature Comparison Table

The following table shows the support status for various elements in xls and xlsx formats for reading and writing operations:

| Element                  | xls    |       | xlsx      |       |
| :----------------------- | :----- | :---- | :-------- | :---- |
|                        | Read   | Write | Read      | Write |
|--------------------------|--------|-------|-----------|-------|
| Charts                   | Yes    | Yes   | Yes       | Yes   |
| Hyperlinks               | Yes    | Yes   | Yes       | Yes   |
| Header/Footer           | Yes    | Yes   | Yes       | Yes   |
| Pivot tables             | No     | No    | No        | Yes   |
| Auto Shapes              | No     | No    | No        | No    |
| Text box                 | Yes    | Yes   | Yes       | Yes   |
| Combo box                | Yes    | Yes   | Yes       | Yes   |
| Check box                | Yes    | Yes   | Yes       | Yes   |
| Page setup [Margin, origin, page size] | Yes    | Yes   | Yes   | Yes   |
| Page breaks              | Yes    | Yes   | Yes       | Yes   |
| Background image         | Yes    | Yes   | No        | No    |
| Print settings [Print area, Print titles, page order] | Yes    | Yes   | Yes   | Yes   |
| Formulas                 | Yes    | Yes   | Yes       | Yes   |
| Calculation options     | Yes    | Yes   | Yes       | Yes   |
| Names                    | Yes    | Yes   | Yes       | Yes   |
| Formula auditing [Ignore error] | Yes    | Yes   | Yes   | Yes   |
| AutoFilter               | Yes    | Yes   | Yes       | Yes   |
| Data validation          | Yes    | Yes   | Yes       | Yes   |

### Summary of Differences
- **Pivot tables**: Supported only for writing in xlsx format.
- **Background image**: Supported for both reading and writing in xls, but not available in xlsx.

## Cross References
- See also: XlsIO documentation for handling specific features, such as pivot tables and background images.

<!-- tags: [xlsio, excel, file formats, pivot tables, background images] keywords: [xls, xlsx, read, write, features] -->
```