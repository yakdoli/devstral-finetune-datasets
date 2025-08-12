```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_427.jpeg
document_name: XlsIO
page_number: 427
page_id: XlsIO#page_427
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:27Z
fidelity: lossless
-->

# Essential XlsIO

## 5.1.7 How to open an existing Xlsx workbook and save it as Xlsx?

You can open and save an existing Excel 2007 file to the `.xlsx` format by using XlsIO. The following code example illustrates how to do this.

```csharp
[C#]

// Open an existing Excel 2007 file.
IWorkbook workbook =
excelEngine.Excel.Workbooks.Open(@"..\\..\\Data\\Excel2007.xlsx",
ExcelOpenType.Automatic);

// Select the version to be saved.
workbook.Version = ExcelVersion.Excel2007;

// Save it as "Excel 2007" format.
workbook.SaveAs("Sample.xlsx");
```

```vbnet
[VB.NET]

' Open an existing Excel 2007 file.
Dim workbook As IWorkbook =
excelEngine.Excel.Workbooks.Open("..\\..\\Data\\Excel2007.xlsx",
ExcelOpenType.Automatic)

' Select the version to be saved.
workbook.Version = ExcelVersion.Excel2007

' Save it as "Excel 2007" format.
workbook.SaveAs("Sample.xlsx")
```

> **Note:** You need to change the Excel Version, if you want to save to another version.

## 5.1.8 How to protect certain cells in a spreadsheet?

All the cells in an Excel spreadsheet have a `Locked` property, which determines if the cell will be editable when the worksheet is protected. All the cells are set to "Locked", by default. Hence when a worksheet is protected, all the cells in the worksheet get protected, by default.
```


<!-- tags: [product, syncfusion-sdk, syncfusion-winforms, XlsIO, worksheet protection, cell locking, document_name, XlsIO] keywords: [open workbook, save as, Excel version, cell protection, locked property, worksheet protection, XlsIO, Syncfusion Winforms] -->
```