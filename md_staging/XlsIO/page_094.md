```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: XlsIO
page_number: 094
page_id: XlsIO#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:53Z
fidelity: lossless
-->

## Essential XlsIO

### Overview
- Demonstrates the process of saving Excel workbooks as XML using the Essential XlsIO library.
- Emphasizes the creation of SpreadsheetML files and the differences in saving compared to Excel 97-2003 format.
- Includes a code sample to illustrate the creation of a SpreadsheetML file.

### Content

#### Saving Excel Workbooks as XML By Using Essential XlsIO
Essential XlsIO provides support for reading and writing objects to SpreadsheetML format. Creating a SpreadsheetML file from scratch has no difference when compared to the API used for Excel 97-2003 format, except for the way it is saved.

Here is the code sample for creating a SpreadsheetML file.

```csharp
[C#]

// Create a new workbook
IWorkbook workbook = excelEngine.Excel.Workbooks.Create(3);
```

### Figure: Saving as Xml Spreadsheet
![Save As Window](https://example.com/image_path)
*Figure 31: Saving as Xml Spreadsheet*

### References
- **Saving Excel as XML file**
- **Creating a SpreadsheetML file from scratch**
- **Comparison with Excel 97-2003 format API**

### API Reference
- Namespace: `Syncfusion.XlsIO`
- Class: `ExcelEngine`
- Method: `Create(int sheetsCount)`

### RAG Annotations
<!-- tags: [Essential XlsIO, Excel Workbooks, SpreadsheetML, Winforms, Syncfusion] keywords: [XlsIO, XML, Workbook, Save, Create, SpreadsheetML, API, Excel 97, Excel 2003] -->

