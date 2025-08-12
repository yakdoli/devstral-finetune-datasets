```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: XlsIO
page_number: 104
page_id: XlsIO#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:32Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Comparison of Excel file types (xls and xlsx) for various elements.
- Preservation and conversion capabilities from xls to xlsx.

## Content

### Comparison of Xls and Xlsx Features

The following table outlines the capabilities of reading, writing, preserving, and converting between xls and xlsx file types for various Excel elements:

| Element               | xls           | xlsx          | xls to xlsx |
|-----------------------|---------------|---------------|-------------|
|                     | Read | Write | Preserve | Read | Write | Preserve |           | Convert |
| Pivot Chart          | No           | No           | Yes         | No        | No      | Yes     | No      |
| Auto Shapes          | No           | No           | Yes         | No        | No      | Yes     | No      |
| Text Box             | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Check Box            | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Combo Box            | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Page setup           | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| [Margin, origin, page size]          |               |               |               |               |               |               |             |
| Page breaks          | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Background image     | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Print settings       | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| [Print area, Print titles, page order]            |               |               |               |               |               |               |             |
| Formulas             | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Calculation options  | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Names                | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| Formula auditing     | Yes          | Yes          | Yes         | Yes       | Yes     | Yes     | Yes     |
| [Ignore              |               |               |               |               |               |               |             |

## API Reference (if applicable)

This section is not applicable to the content provided in the image.

## Code Examples (multi-language supported)

```csharp
// Example of converting between xls and xlsx file types using Syncfusion XlsIO
using Syncfusion.XlsIO;

// Load the Excel file
ExcelEngine excelEngine = new ExcelEngine();
IApplication application = excelEngine.Excel;
IWorkbook workbook = application.Workbooks.Open("input.xls");

// Save the file as xlsx
workbook.SaveAs("output.xlsx", ExcelVersion.Excel2016);

// Dispose the workbook
workbook.Dispose();
excelEngine.Dispose();
```

## Page-level Navigation/TOC (if applicable)

This section is not applicable as there is no local Table of Contents present on this page.

## Cross References

- See also: [Syncfusion XlsIO Documentation](https://syncfusion.com/documentation/xlsio/)

## RAG Annotations

<!-- tags: [xls, xlsx, excel, file format, comparison, xls to xlsx] keywords: [pivot chart, auto shapes, text box, check box, combo box, page setup, background image, print settings, formulas, calculation options, names, formula auditing, conversion, preservation, syncfusion xlsio] -->
```