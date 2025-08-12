```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_171.jpeg
document_name: XlsIO
page_number: 171
page_id: XlsIO#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:20Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates search functionality within Excel documents using different data types.
- Provides methods to find all occurrences of specified data in a sheet.

---

```csharp
ExcelFindType.Text, ExcelFindOptions.MatchEntireCellContent
```

'Gets the cell display text.  
```csharp
txtDisplay.Text = result.DisplayText.ToString()
```

## FindAll

This method searches all the cells and returns all the entries in the sheet that matches the specified data.

### Methods and Descriptions

| **Methods**                     | **Description**                                                                 |
|----------------------------------|---------------------------------------------------------------------------------|
| `FindAll(Boolean)`              | This method searches for all the cells with specified bool value.               |
| `FindAll(DateTime)`             | This method searches for all the cells with specified DateTime value.           |
| `FindAll(TimeSpan)`             | This method searches for all the cells with specified TimeSpan value.           |
| `FindAll(Double, ExcelFindType)`| This method searches for all the cells with specified double value.             |
| `FindAll(String, ExcelFindType, ExcelFindOptions)`| This method searches for all the cells with specified string value, again based on the Find options.|

## Code Examples

[C#]
```csharp
// Find All with Text
IRange[] result = sheet.FindAll("Simple Text", ExcelFindType.Text);

// Find All with Simple text and Match Case
IRange[] result = sheet.FindAll("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchCase);
```

## API Reference

This section details the methods available for searching data within an Excel sheet.

### Methods

- **FindAll(Boolean)**: Searches for all cells matching the specified boolean value.
- **FindAll(DateTime)**: Searches for all cells matching the specified DateTime value.
- **FindAll(TimeSpan)**: Searches for all cells matching the specified TimeSpan value.
- **FindAll(Double, ExcelFindType)**: Searches for all cells matching the specified double value.
- **FindAll(String, ExcelFindType, ExcelFindOptions)**: Searches for all cells matching the specified string value based on the Find options.

## Page-level Navigation/TOC (if applicable)

- [FindAll]
  - Methods and their descriptions
  - Code examples

<!-- tags: XlsIO, Syncfusion, ExcelFindType, ExcelFindOptions, Search, FindAll, C# 
keywords: FindAll, ExcelFindType, ExcelFindOptions, Search, methods, examples, C# -->
```