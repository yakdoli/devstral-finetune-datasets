```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: pdf
page_number: 130
page_id: pdf#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:33Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Describes the use of sorting properties in data handling.
- Explains theAllowRowBreakAcrossPages property for row splitting across pages.
- Outlines the initialization of data to PdfLightTable using DataSource.

## Content

### Ignore Sorting

If there is a DataTable assigned as a data source, you may specify whether you need sorted or unsorted data. If this property is set to True, the DataTable sorting will be ignored.

**Note**: *Sorting is disabled, by default. This is because sorted data takes more time.*

### AllowRowBreakAcrossPages

This property allows changing the row split behavior across pages. By default, this Boolean property is set to True, which allows splitting the row across pages when the row cannot accommodate within the bounds of the page. If set to false, the entire row will be shifted to the next page.

**Note**: *If the row height is greater than the page height, it will be forcibly split across pages ignoring this property.*

### 4.1.2.3.1.2.1 Data

You can initialize the data to the PdfLightTable with the help of the DataSource property. This is achieved through:

- **External DataSource**: By assigning the External data source
- **Table Direct**: By adding columns and rows to the PdfLightTable
- **Event Handlers**: By adding columns and rows by using the event handlers

#### 4.1.2.3.1.2.1.1 External DataSource

Data source is an object that might be an array (two-dimensional, one-dimensional or nested), a DataTable, DataColumn, DataView or DataSet. To draw an external data source, you must set DataSourceType property to PdfLightTableDataSourceType.External.

The following code example illustrates how to assign external data source to PdfLightTable:

#### Code Examples

```csharp
[C#]
pdfLightTable.DataSourceType = PdfLightTableDataSourceType.External;
pdfLightTable.DataSource = dataTable;
```

```vbnet
[VB.NET]
pdfLightTable.DataSourceType = PdfLightTableDataSourceType.External
pdfLightTable.DataSource = dataTable
```

---

<!-- tags: [pdf, data handling, sorting, row breaking, data source, grid, datasource type] keywords: [DataTable, PdfLightTable, sorting, row split, pages, external data source, direct table, event handlers, initialization, PdfLightTableDataSourceType] -->
```