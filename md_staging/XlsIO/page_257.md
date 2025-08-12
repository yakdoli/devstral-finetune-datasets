```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_257.jpeg
document_name: XlsIO
page_number: 257
page_id: XlsIO#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:47Z
fidelity: lossless
-->

### XlsIO

```vb
' Total Row
table1.Columns(0).TotalsRowLabel = "Total"
table1.Columns(1).TotalsCalculation = ExcelTotalsCalculation.Sum
table1.Columns(2).TotalsCalculation = ExcelTotalsCalculation.Sum
```

## Formatting Table

You can apply built-in styles for the tables by using the `TableBuiltInStyles` enumerator of XlsIO.

```csharp
// Apply built-in style.
table1.BuiltInTableStyle = TableBuiltInStyles.TableStyleMedium9;
```

```vb
' Apply built-in style.
table1.BuiltInTableStyle = TableBuiltInStyles.TableStyleMedium9
```

## Reading Existing Table

XlsIO provides support to read an existing table from the spreadsheet. It can be accessed from the sheet by using the "Table Index".

```csharp
IListObject table = sheet.ListObjects[0];
table.BuiltInTableStyle = TableBuiltInStyles.TableStyleMedium1;
```

```vb
Dim table As IListObject = sheet.ListObjects(0)
table.BuiltInTableStyle = TableBuiltInStyles.TableStyleMedium1
```

<!-- tags: [XlsIO, Table, built-in styles, TableBuiltInStyles, reading existing table, support, spreadsheet, Sheet, Table Index] -->
```