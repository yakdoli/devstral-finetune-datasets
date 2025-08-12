```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_431.jpeg
document_name: XlsIO
page_number: 431
page_id: XlsIO#page_431
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:40Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.RemovePanes();
```

```vb.net
sheet.Cell(8, 1).FreezePanes()
sheet.RemovePanes()
```

## 5.1.14 What is the maximum range of Rows and Columns?

XlsIO supports 16,384 columns by 1,048,576 rows in Excel 2007 xlsx format, and 256 columns by 65,536 rows in Excel 97 to 2003 format. Note that this is the worksheet size of MS Excel itself.

For more information, see [http://office.microsoft.com/en-us/excel/HA100778231033.aspx](http://office.microsoft.com/en-us/excel/HA100778231033.aspx).

## 5.1.15 How to use Named Ranges with XlsIO?

The `NamedRanges` collection belongs to the workbook and not to the worksheet. If you define two named ranges with the same name, the named range that is defined last will replace the previous named range.

```csharp
// Looping through the Named Ranges in a spreadsheet.
foreach (INamedRange name in mySheet.Names)
{
    MessageBox.Show(name.Name.ToString());
}

// There is already a named range called "One", I am changing the address that it points to.
mySheet.Names["One"].RefersTo = mySheet.Range["B6"];

// Named ranges are added to the workbook collection in both the methods mentioned below.
// Adding the named Range to the workbook.
myWorkbook.Names.Add("TestRangeBook", mySheet.Range["A5"]);

// Adding the named Range to the workbook. Internally named range is added to the workbook names collection.
```

## 431 | Page
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [syncfusion, winforms, XlsIO, named ranges, worksheet size, maximum range, Excel format, APIs] keywords: [named ranges, worksheet size, maximum range, Excel formats, APIs,冻,移 getting started] -->
```