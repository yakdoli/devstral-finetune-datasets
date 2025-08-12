```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_432.jpeg
document_name: XlsIO
page_number: 432
page_id: XlsIO#page_432
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:04Z
fidelity: lossless
-->


## Content

### Named Ranges in a Spreadsheet

```csharp
mySheet.Names.Add("TestRangeSheet", mySheet.Range["A5"]);

// Referencing from the sheet.
mySheet.Range["TestRangeSheet"].Number = 100;
```

#### [VB.NET]

```vb
' Looping through the Named Ranges in a spreadsheet.
Dim name As Syncfusion.XlsIO.IName
For Each name In mySheet.Names
    MessageBox.Show(name.Name.ToString())
Next name

' There is already a named range called "One", I am changing the address that it points to.
mySheet.Names("One").RefersToRange = mySheet.Range("B6")

' Named ranges are added to the workbook collection in both the methods mentioned below.
' Adding the named Range to the workbook.
myWorkbook.Names.Add("TestRangeBook", mySheet.Range("A5"))

' Adding the named Range to the workbook. Internally named range is added to the workbook names coll.
mySheet.Names.Add("TestRangeSheet", mySheet.Range("A5"))

' Referencing from the sheet.
mySheet.Range("TestRangeSheet").Number = 100
```

### 5.1.16 How to create and open Excel Template files by using XlsIO?

#### Creating Excel Template Files

You can create either XLT or XLTX Excel Template files by saving a file with the `ExcelSaveType` property of the `SaveAs` method. The `ExcelSaveType` property must be set to `SaveAsTemplate` to create a template file of the existing file. The following code example illustrates this.

#### Code Example

```csharp
// Save as XLT.
workbook.Version = ExcelVersion.Excel97to2003;
```

## Page-level Navigation/TOC (if applicable)
<!-- tags: [XlsIO, named ranges, Excel templates, workbook, sheet, ranges, VB.NET, C#, ExcelSaveType, SaveAsTemplate] keywords: [Syncfusion, XlsIO, named ranges, Excel templates, workbook, Excel versions, worksheet, ranges, VB.NET, C#, SaveAsTemplate, Excel97to2003] -->
```