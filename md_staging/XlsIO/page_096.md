```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: XlsIO
page_number: 096
page_id: XlsIO#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:02Z
fidelity: lossless
-->

# Essential XlsIO

Dim workbook As IWorkbook =excelEngine.Excel.Workbooks.Open("spreadsheetml", ExcelXmlOpenType.MExcel)

'The first worksheet object in the worksheets collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)

'Write data
sheet.Range("C3:O28").Text = "Hello world"

'Save as SpreadsheetML.
workbook.SaveAsXml("Sample.xml",ExcelXmlSaveType.MExcel)

### Note: Currently XlsIO cannot parse the Document Properties apart from elements that are not supported by MS Excel. Colors created by XlsIO will choose the closest color to it when exported to the SpreadsheetML format. For more information refer Excel 97 to 2003, Excel 2007 [Xlsx-Biff12 format], and CSV format.

## 3.7.4 CSV Format

The Comma Separated Value (CSV) file format is a file type that stores tabular data. The CSV file format is often used to exchange data between disparate applications. The file format, as it is used in Microsoft Excel, has become a pseudo standard throughout the industry, even among non-Microsoft platforms.

XlsIO provides support for reading and writing CSV files. The following code example illustrates how to open a .csv file.

[C#]

// Opening a File.
IWorkbook workbook = application.Workbooks.Open("CSVfile.csv", ",");

[VB.NET]

' Opening a File.
Dim workbook As IWorkbook = application.Workbooks.Open("CSVfile.csv", ",")

While saving files, you have options to save as Unicode, ASCII, and other Non-Unicode encoding. The following code example illustrates how to save a file to the CSV format.

```text
© 2013 Syncfusion. All rights reserved.
```
    
<!-- tags: [product, module, control, api, version?] keywords: [Essential XlsIO, IWorkbook, IWorksheet, Document Properties, SpreadsheetML, Colors, CSV Format, CSV, tabular data, Microsoft Excel, XlsIO, Xlsx-Biff12, IWorkbook.Open, IWorkbook.SaveAsXml, application.Workbooks.Open] -->
```