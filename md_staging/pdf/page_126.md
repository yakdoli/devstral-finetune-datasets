```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: pdf
page_number: 126
page_id: pdf#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:17Z
fidelity: lossless
-->

**Essential PDF**

It is based on cell model that offers rich API for formatting and layout options. It can take input from DataTable, arrays or any other entity class. Formatting can be done to all levels of PdfGrid. More features like Nested Table, Row and Column Spanning are also supported. It offers full control over the appearance and is recommended to draw complex table structures. Check the following comparison table for more details.

### Comparison between PdfLightTable and PdfGrid

| Platforms    | PdfLightTable | PdfGrid |
|--------------|---------------|---------|
| Windows Forms | Yes           | Yes     |
| WPF           | Yes           | Yes     |
| ASP.NET       | Yes           | Yes     |
| ASP.NET MVC   | Yes           | Yes     |
| Silverlight   | Yes           | Yes     |

#### Features

| Features        | PdfLightTable                                    | PdfGrid                                       |
|------------------|-------------------------------------------------|-----------------------------------------------|
| **Formatting**   |                                                 |                                               |
| Row             | No direct API, possible through events          | Yes                                           |
| Column          | Yes (StringFormat)                              | Yes (StringFormat)                            |
| Cell            | No direct API for single cell formatting,       | Yes                                           |
|                 | possible through events                         |                                               |
| **Others**       |                                                 |                                               |
| Row span        | No                                              | Yes                                           |
| Column span     | No direct API, possible through events          | Yes                                           |
| Nested Grid     | Possible through events                         | Yes                                           |
| Layout Events   | BeginCellLayout, BeginPageLayout,              | BeginPageLayout, EndPageLayout                |
|                 | BeginRowLayout, EndCellLayout,<br>             |                                               |
|                 | EndPageLayout, EndRowLayout                     |                                               |

### 4.1.2.3.1 PdfLightTable

The PdfLightTable class represents simple tables that are used for publishing structured data from arrays, data tables or data columns. There are no real cells or rows, and all the data is taken from the data source (DataSource property).

### References

- **PdfGrid**
- **PdfLightTable**
- **DataTable**
- **Formatting API**

<!-- 
tags: [syncfusion-sdk, winforms, essential-pdf, PdfLightTable, PdfGrid, formatting, complex-table-structures] 
keywords: [cell-model, rich-api, layout-options, DataTable, arrays, entity-class, nested-table, row-span, column-span, full-control, appearance, comparison-table, Windows Forms, WPF, ASP.NET, ASP.NET MVC, Silverlight, StringFormat, nested-grid, layout-events, DataSource] 
-->
```