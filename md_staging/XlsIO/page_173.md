```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_173.jpeg
document_name: XlsIO
page_number: 173
page_id: XlsIO#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:08Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
ExcelFindType.Text);
```

### Searches for the Number with Text format
```csharp
//StartsWith the Number with Text format
IRange result = sheet.FindStringStartsWith("$8", ExcelFindType.Text);
```

### Searches for the Text with MatchCase
```csharp
//Startswith the Text with MatchCase
IRange result = sheet.FindStringStartsWith("Si", ExcelFindType.Text, false);
```

**[VB]**

```vb
'Starts with Simple Text
Dim result As IRange = result = sheet.FindStringStartsWith("Sim", ExcelFindType.Text)

'StartsWith the Number with Text format
Dim result As IRange = sheet.FindStringStartsWith("$8", ExcelFindType.Text)

'Startswith the Text with MatchCase
Dim result As IRange = sheet.FindStringStartsWith("Si", ExcelFindType.Text, False)
```

## FindStringEndsWith

### Overview
- Identifies cells that end with the specified typed value.
- The `ExcelFindType` enumerator allows setting the data type and formula value/string for the search operation.

### Methods and Descriptions

| Methods                                  | Description                                                                                                                                                                    |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FindStringEndsWith (String, ExcelFindType) | Searches for the cell that ends with the specified string value, for the given find type.                                                                          |
| FindStringStartsWith (String, ExcelFindType, bool) | Searches for the cell that ends with the specified string value, for the given find type and boolean value.                                        |

### Summary
The `FindStringEndsWith` and `FindStringStartsWith` methods offer flexibility in searching for cells based on string endings, with options to specify the search type and case sensitivity.
```

<!-- tags: [xlsio, string search, find type, syncfusion, excel, text format, boolean match, endswith, startswith] keywords: [findstringendswith, findstringstartswith, excelfindtype, string search methods, data type, case sensitivity, boolean value, typed value search, end search, start search, cell search, excel tools] -->
```