```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: XlsIO
page_number: 169
page_id: XlsIO#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:52Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Describes features related to finding and matching specific values within Excel cells.
- Provides details about enumeration types (`ExcelFindType`, `ExcelFindOptions`) and their uses in search operations.

## Content

### Member Specifications

| Member Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Match Case        | Matches case while finding the value.                                     |
| MatchEntireCell   | Matches the whole word being searched while finding the value.           |

### Find First

This method has overloads for searching the first cell with the specified typed value. The `ExcelFindType` enumerator provides options to set the data type of the string (i.e., value and formula value) to be searched, and the `ExcelFindOptions` enumerator provides the options to match the strings associated with the find value.

#### Methods

| Methods                                  | Description                                                         |
|------------------------------------------|---------------------------------------------------------------------|
| `FindFirst(Boolean)`                     | This method searches for the cell with specified bool value.      |
| `FindFirst(DateTime)`                    | This method searches for the cell with specified DateTime value.  |
| `FindFirst(TimeSpan)`                    | This method searches for the cell with specified TimeSpan value.  |
| `FindFirst(Double, ExcelFindType)`       | This method searches for the cell with specified double value.     |
| `FindFirst(String, ExcelFindType, ExcelFindOptions)` | This method searches for the cell with specified string value, again based on the Find options. |

### Code Example

```csharp
// FindFirst with Number
IRange result = sheet.FindFirst(1000000.00075, ExcelFindType.Number);

// Gets the cell display text
```

## API Reference (if applicable)
- Namespace: Refer to the Syncfusion documentation for the exact namespace details.
- Methods:
  - `FindFirst(Boolean)`: Search for cells with specified bool value.
  - `FindFirst(DateTime)`: Search for cells with specified DateTime value.
  - `FindFirst(TimeSpan)`: Search for cells with specified TimeSpan value.
  - `FindFirst(Double, ExcelFindType)`: Search for cells with specified double value.
  - `FindFirst(String, ExcelFindType, ExcelFindOptions)`: Search for cells with specified string value.

## Cross References
- Refer to the documentation on `ExcelFindType` and `ExcelFindOptions` for more information on their usage.

<!-- tags: [syncfusion-sdk, xlsx, find operations, enumeration types, data types, search methods, winforms] keywords: [match case, match entire cell, find first, boolean search, datetime search, timespan search, double search, string search, syncfusion, xlsio] -->
```