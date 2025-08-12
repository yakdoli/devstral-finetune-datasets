<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: XlsIO
page_number: 174
page_id: XlsIO#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:52Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

This page discusses the functionality related to finding and replacing strings using XlsIO in C# and VB.NET, specifically focusing on the `FindStringEndsWith` method and its overloads, as well as the `Replace` method.

---

## Content

### C#

```csharp
// Ends with Text
IRange result = result = sheet.FindStringEndsWith("Text", ExcelFindType.Text);

// Ends with the Number with Text format
IRange result = sheet.FindStringEndsWith("00", ExcelFindType.Text);

// Ends with the Text with MatchCase
IRange result = sheet.FindStringEndsWith("Case", ExcelFindType.Text, false);
```

### VB

```vb
' Starts with Simple Text
Dim result As IRange = result = sheet.FindStringEndsWith("Text ", ExcelFindType.Text)

' Starts with the Number with Text format
Dim result As IRange = sheet.FindStringEndsWith("00", ExcelFindType.Text)

' Starts with the Text with MatchCase
Dim result As IRange = sheet.FindStringEndsWith("Case", ExcelFindType.Text, False)
```

### Replace

The `Replace` method enables replacing a string with data from various data types and data sources, such as a data table, data column, or array. The overloads for the `Replace` method are:

| Methods               | Description                                |
|-----------------------|--------------------------------------------|
| Replace(String, DateTime) | Replaces specified string by specified value. |
| Replace(String, Double) | Replaces specified string by specified value. |

---

## API Reference

### Methods

- **Replace(String, DateTime)**  
  Replaces specified string by specified value.

- **Replace(String, Double)**  
  Replaces specified string by specified value.

---

## Code Examples

- **C#**
  ```csharp
  string originalText = "Replace this text";
  DateTime replaceValue = DateTime.Now;
  string replacedText = Replace(originalText, replaceValue);
  ```

- **VB**
  ```vb
  Dim originalText As String = "Replace this text"
  Dim replaceValue As DateTime = DateTime.Now
  Dim replacedText As String = Replace(originalText, replaceValue)
  ```

## Cross References

See also:
- Documentation on ExcelFindType
- Examples of Data Manipulation in XlsIO

## RAG Annotations

<!-- tags: [XlsIO, FindStringEndsWith, Replace, ExcelFindType, Syncfusion Winforms, C#, VB.NET] -->
<!-- keywords: [Excel, string manipulation, data replacement, ExcelFindType, text formatting, case sensitivity] -->