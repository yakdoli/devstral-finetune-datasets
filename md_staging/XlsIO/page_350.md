```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_350.jpeg
document_name: XlsIO
page_number: 350
page_id: XlsIO#page_350
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:07Z
fidelity: lossless
-->

### Essential XlsIO

| UnlockedFormulaCells | Represents UnlockedFormulaCells flag of excel ignore error indicator. |
|-----------------------|-------------------------------------------------------------------------|
| All                   | Represents All flag of excel ignore error indicator.                |

Following code example illustrates how to ignore or set an error indicator.

```csharp
[C#]

// Sets warning if number is entered as text.
sheet.Range["A2:D2"].IgnoreErrorOptions = ExcelIgnoreError.NumberAsText;

// Ignores all the error warnings.
sheet.Range["A3"].IgnoreErrorOptions = ExcelIgnoreError.None;
```

```vbnet
[VB.NET]

' Sets warning if number is entered as text.
sheet.Range["A2:D2"].IgnoreErrorOptions = ExcelIgnoreError.NumberAsText

' Ignores all the error warnings.
sheet.Range["A3"].IgnoreErrorOptions = ExcelIgnoreError.None
```

## 4.5 Data

XlsIO has advanced support to work with data in a worksheet and here are some key functionalities that makes it easier.

### 4.5.1 Filter

MS Excel **AutoFilter** feature literally makes filtering out unwanted data in a data list, as easy as clicking a button. When the cell pointer is located within any cell in your data list, open the **Data** menu, point to **Filter**, and select **AutoFilter**. Once this is done, the program adds drop-down buttons to each of the field names in the top row of the list. This feature is specifically used in large spreadsheets, when the user wants to look for particular data, based on some criteria.
```html

<!-- tags: [XlsIO, error indicator, ignore error options, AutoFilter, data filtering, filtering, user interface, advanced support, Syncfusion Winforms, 11.4.0.26] keywords: [UnlockedFormulaCells, All, ExcelIgnoreError, AutoFilter, drop-down buttons, field names, top row, large spreadsheets, particular data, criteria, user interface] -->
```