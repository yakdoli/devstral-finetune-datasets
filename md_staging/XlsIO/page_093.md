```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: XlsIO
page_number: 093
page_id: XlsIO#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:40Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
workbook.Close()
excelEngine.Dispose()
```

## Overview

- A list of compression enumerations is provided, explaining the behavior of each option.
- An introduction to SpreadsheetML and its functionality within Excel workbooks.

## Content

Following are the list of enumerations available:

| Enum          | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| NoCompression | File will not be compressed.                                                                      |
| BestSpeed     | Fast compression with more size than normal compression.                                          |
| BelowNormal   | Compression speed and size will be between Normal and BestSpeed.                                 |
| Normal        | Both size and speed will be Normal.                                                               |
| AboveNormal   | Takes more time to compress, with reduced file size.                                              |
| Best          | Slow compression, file size reduced to the best level.                                           |

### 3.7.3 SpreadsheetML

SpreadsheetML is an XML dialect developed by Microsoft to represent the information in an Excel workbook. SpreadsheetML allows you to save Excel workbooks as XML documents, and to open them in Excel. Microsoft created a format that allows you to save, in an XML-based file, almost every Excel customization (including formulas, data, and formatting).

SpreadsheetML file can be created with Office 2003 by selecting the **Save as type: as XML Spreadsheet (*.xml)**.

## Page-level Navigation/TOC (if applicable)

- Overview of compression enumerations
- Explanation of SpreadsheetML functionality

## RAG Annotations

<!-- tags: [product, module, control, api, version?] keywords: [SpreadsheetML, compression, enumerations, Excel, XML, file formats, Office 2003] -->
```