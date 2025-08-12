```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: XlsIO
page_number: 084
page_id: XlsIO#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:08Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Demonstrates how to save Excel files using programming languages.
- Covers saving to Excel 97 to 2003 format and Excel 2007 (.xlsx) format.
- Explains setting the version for saving files in older Excel formats.

## Content

```csharp
[Worksheet].SaveAs("[Desired File Name.xls]");
// Example
myWorkBook.SaveAs("Sample.xls");
```

```vb.net
[Workbook].SaveAs("[Desired File Name.xls]")
' Example
myWorkBook.SaveAs("Sample.xls")
```

- You can also save to Excel 97 to 2003 format, while opening an Excel 2007 file, by setting the version as given below.

```csharp
workbook.Version = ExcelVersion.Excel97to2003;
```

```vb.net
Workbook.Version = ExcelVersion.Excel97to2003
```

### For more Information refer:

- [Excel 2007 [.Xlsx-Biff12 format]]
- [SpreadsheetML]
- [CSV format]

#### 3.7.2 XLSX

- Description:  
  Excel 2007 version of MS Excel has various advanced features, and overcomes the drawbacks of previous versions. Essential XlsIO introduces basic support for Excel 2007 and Excel 2010 `.xlsx` format that includes support to read and write basic elements (listed below) into the document.

- Sample Code Sample:  
  Here is a sample code sample that opens an `.xlsx` file, makes some changes, and saves it as an `.xlsx` file.

```csharp
[C#]
```

## Page-level Navigation/TOC (if applicable)

### 3.7.2 XLSX

- Description of Excel 2007 features and the need for advanced features.
- Explanation of the basic support provided by Essential XlsIO for `.xlsx` format.

## Code Examples (multi-language supported)

### C# Example

```csharp
workbook.Version = ExcelVersion.Excel97to2003;
```

### VB.NET Example

```vb.net
Workbook.Version = ExcelVersion.Excel97to2003
``` 

## Cross References

- Refer to:
  - Excel 2007 [.Xlsx-Biff12 format]
  - SpreadsheetML
  - CSV format

<!-- tags: [essential_xlsio, excel, file_format, version_control, csharp, vb.net, api_reference, programming] keywords: [excel, saveas, workbook, worksheet, version, basic_support, xlsx, biff12, 97to2003, ms_excel, essential_xlsio] -->
```