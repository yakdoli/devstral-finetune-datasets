```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: XlsIO
page_number: 172
page_id: XlsIO#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:30Z
fidelity: lossless
-->

## Overview
- Explains how to find all instances of a specific text in a worksheet.
- Demonstrates the use of various options for text matching, including case sensitivity and entire cell content matching.
- Introduces the `FindStringStartsWith` method for searching cells that start with a specified value.

## Content

### Text Matching Examples

#### Using `FindAll` with Text

```csharp
// Find All with Simple Text and MatchEntireCellContent
IRange[] result = sheet.FindAll("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchEntireCellContent);
```

```vb
' Find All with Text
Dim result() As IRange = sheet.FindAll("Simple Text", ExcelFindType.Text)

' Find All with Simple text and Match Case
Dim result() As IRange = sheet.FindAll("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchCase)

' Find All with Simple Text and MatchEntireCellContent
Dim result() As IRange = sheet.FindAll("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchEntireCellContent)
```

### FindStringStartsWith

The `FindStringStartsWith` method has overloads to search for the first cell that starts with the specified value. The `ExcelFindType` enumerator provides options to set the data type of the string (i.e., value and formula value) to be searched.

| **Methods**                                   | **Description**                                                                 |
|-----------------------------------------------|---------------------------------------------------------------------------------|
| `FindStringStartsWith(String, ExcelFindType)` | These methods search for cells that start with the specified string value for the given find type. |
| `FindStringStartsWith(String, ExcelFindType, boolean)` | These methods search for cells which start with the specified string value, for the given find type and boolean value. |

#### Example in C#

```csharp
// Starts with Simple Text
IRange result = sheet.FindStringStartsWith("Sim",
```

## Code Examples (multi-language supported)

```csharp
// Example in C#
// Finds all instances of "Simple text" in the sheet and matches the entire cell content.
IRange[] result = sheet.FindAll("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchEntireCellContent);
```

```vb
' Example in VB
' Finds all instances of "Simple text" in the sheet with case sensitivity.
Dim result() As IRange = sheet.FindAll("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchCase)
```

## Cross References

- Refer to the documentation on `ExcelFindType` and `ExcelFindOptions` for more information on available options.
- See also: `Find`, `FindNext`, and other related search methods for working with text in Excel.

<!-- tags: [XlsIO, ExcelFindType, ExcelFindOptions, FindStringStartsWith] keywords: [text search, case sensitivity, entire cell content, string matching, C# example, VB example] -->
```