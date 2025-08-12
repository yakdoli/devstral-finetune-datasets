```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: XlsIO
page_number: 097
page_id: XlsIO#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:52Z
fidelity: lossless
-->

## Essential XlsIO

```csharp
// Saving the workbook to disk.
sheet.SaveAs("Sample.csv",",", Encoding.ASCII);
```

```vb.net
' Saving the workbook to disk.
sheet.SaveAs("Sample.csv",",", Encoding.ASCII)
```

### For More Information Refer:
- [Excel 97 to 2003, Excel 2007 [.Xlsx-Biff12 format], SpreadsheetML](Excel_97_to_2003,_Excel_2007_[.Xlsx-Biff12_format],_SpreadsheetML)

## 3.8 Using Templates

This is the most widely used functionality of XlsIO as it is the easiest and the most convenient to use. An existing spreadsheet is used as a template for generating new spreadsheets. There are several advantages of using the Template-based approach.

- The spreadsheet can be formatted by using the MS Excel GUI, and the data alone can be inserted dynamically by using XlsIO. This saves the problem of writing code for formatting by using the XlsIO API.
- There are some features like VBA Macros which cannot be created by using the XlsIO's API. Even these features can be preserved by XlsIO, when a spreadsheet is opened and saved programmatically.
- Editing an existing data in the spreadsheet is also possible by opening the template with XlsIO.

```csharp
// New instance of XlsIO is created. [Equivalent to launching MS Excel with no workbooks open].
// The instantiation process consists of two steps.

// Step 1: Instantiate the spreadsheet creation engine.
ExcelEngine excelEngine = new ExcelEngine();

// Step 2: Instantiate the excel application object.
IApplication application = excelEngine.Excel;
```

<!-- tags: [XlsIO, Winforms, Syncfusion, XlsIO Template-based approach, spreadsheet creation, VBA Macros preservation, editing existing data] keywords: [template-based spreadsheets, XlsIO, Excel GUI, dynamic data insertion, VBA Macros, programmatically opening and saving, editing existing spreadsheet data] -->
```