```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_433.jpeg
document_name: XlsIO
page_number: 433
page_id: XlsIO#page_433
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:13Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
workbook.SaveAs("Sample.xlt", ExcelSaveType.SaveAsTemplate);
// Save as XLTX.
workbook.Version = ExcelVersion.Excel2007;
workbook.SaveAs("Sample.xltx", ExcelSaveType.SaveAsTemplate);
```

### [VB.NET]

```vbnet
' Save as XLT.
workbook.Version = ExcelVersion.Excel97to2003
workbook.SaveAs("Sample.xlt", ExcelSaveType.SaveAsTemplate)

' Save as XLTX.
workbook.Version = ExcelVersion.Excel2007
workbook.SaveAs("Sample.xltx", ExcelSaveType.SaveAsTemplate)
```

## Opening Excel Template Files

An Excel Template file is opened in the same way a document is opened. The following code example illustrates how to open a template file.

```csharp
[C#]
workbook = application.Workbooks.Open(fileName, ExcelOpenType.Automatic);
```

```vbnet
[VB.NET]
workbook = application.Workbooks.Open(fileName, ExcelOpenType.Automatic)
```

### 5.1.17 How to open an Excel 2007 Macro Enabled Template?

XlsIO now provides support to open and save an Excel 2007 Macro Enabled Template to XLSM (Excel 2007 Macro Enabled Document) format. The following code example illustrates this.

```csharp
[C#]
// Open an existing XLTM file.
Workbook = application.Workbooks.Open(@"Template.xltm", ExcelOpenType.Automatic);

// Save the file as XLSM.
workbook.Version = ExcelVersion.Excel2007;
```

``` 
```