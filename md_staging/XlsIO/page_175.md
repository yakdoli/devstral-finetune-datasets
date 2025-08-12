```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_175.jpeg
document_name: XlsIO
page_number: 175
page_id: XlsIO#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:35Z
fidelity: lossless
-->

# Overview

- Covers various methods to replace strings with different data types.
- Demonstrates string replacement using text, datetime, arrays, DataColumns, DataTables, and more.
- Illustrates the use of boolean parameters in replacement functions.

## Content

### Overview of Replacement Methods

The following table outlines the various `Replace` methods available:

| Method Signature                                     | Description                                                                             |
|------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `Replace(String, String)`                           | Replaces specified string by specified value.                                           |
| `Replace(String, DataColumn, Boolean)`              | Replaces specified string by data column values.                                        |
| `Replace(String, DataTable, Boolean)`               | Replaces specified string by data table values.                                         |
| `Replace(String, Double[], Boolean)`                | Replaces specified string by data from array.                                           |
| `Replace(String, Int32[], Boolean)`                 | Replaces specified string by data from array.                                           |
| `Replace(String, String[], Boolean)`                | Replaces specified string by data from array.                                           |

### Code Example: Replacing Strings with Various Data

The following code example provides examples in both C# and VB.NET for replacing strings using different types of data.

#### C#

```csharp
[C#]

// Replacing the Text.
sheet.Replace("Find and Replace", "New Find and Replace");

// Replacing a date value by using datetime.
sheet.Replace("Datevalue", DateTime.Now);

// Replace using array value.
sheet.Replace("Arrayvalue", new string[] { "ArrayValue1", "ArrayValue2", "ArrayValue3" }, true);

// Replacing a data table by calling a function SampleDataTable().
DataTable table = SampleDataTable();
sheet.Replace("DataTable", table, true);
```

#### VB.NET

```vbnet
[VB.NET]

' Replacing the Text.
sheet.Replace("Find and Replace", "New Find and Replace")

' Replacing a date value by using datetime.
sheet.Replace("Datevalue", DateTime.Now)

' Replace using array value.
sheet.Replace("Arrayvalue", New String() {"ArrayValue1", "ArrayValue2", "ArrayValue3"}, True)

' Replacing a data table by calling a function SampleDataTable().
Dim table As DataTable = SampleDataTable()
```

### Explanation of Code Example

- **Text Replacement**: Simple string replacement with another string.
- **DateTime Replacement**: Replacing a placeholder with the current date and time using `DateTime.Now`.
- **Array Replacement**: Replacing a placeholder with multiple values from an array, specifying whether to replace all occurrences.
- **DataTable Replacement**: Replacing a placeholder with values from a DataTable retrieved by a function call.

## Cross References

See also:
- Documentation for `Syncfusion.XlsIO` API.
- Examples and tutorials for string manipulation and data handling in Excel documents.

<!-- tags: [XlsIO, string replacement, Syncfusion Winforms] keywords: [Replace, string, DateTime, array, DataTable] -->
```