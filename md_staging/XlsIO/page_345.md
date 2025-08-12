```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_345.jpeg
document_name: XlsIO
page_number: 345
page_id: XlsIO#page_345
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:09Z
fidelity: lossless
-->

# XlsIO with Named Ranges

## Overview
- Demonstrates how to manage named ranges at the sheet level in XlsIO.
- Includes examples in C# and VB.NET for adding and retrieving named ranges.

## Content

### Figure 125: XlsIO with Named Ranges

The screenshot illustrates the use of named ranges in XlsIO. The table shows a list of Microsoft Office products in column A, along with numerical values in columns C, D, and E.

```plaintext
Ms-Excel    |        | 100  | 200 | 300
Ms-Word     |        |      |     |
Ms-Access   |        |      |     |
Ms-Publisher |        |      |     |
Ms-Outlook  |        |      |     |
Ms-Powerpoint |      |      |     |
```

### Code Example: Managing Named Ranges

#### C#

The following code example demonstrates how to add and retrieve a named range in C#.

```csharp
IWorksheet sheet = workbook.Worksheets[0];

// Add a name.
IName lname1 = sheet.Names.Add("CellName");
lname1.RefersToRange = sheet.Range("C3");

// Get name.
Console.WriteLine(sheet.Names["CellName"].Value);
```

#### VB.NET

The following code example demonstrates how to add a named range in VB.NET.

```vbnet
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Add a name.
```

### Notes
- The example shows how to dynamically add and retrieve named ranges using XlsIO.
- The named range "CellName" is linked to the cell `C3`.

## API Reference

### `IWorksheet.Names`

- **Method**: `Add`
  - **Parameters**: 
    - `name`: string
  - **Returns**: `IName`
  - **Description**: Adds a named range to the worksheet.

### `IName`

- **Property**: `RefersToRange`
  - **Type**: `Range`
  - **Description**: Sets or gets the range to which the named range refers.

### `Console.WriteLine`

- **Usage**: Displays the value of a named range.

## Cross References

See also:
- [Creating Named Ranges Programmatically](#creating-named-ranges-programmatically)
- [XlsIO Documentation](#xlso-documentation)

<!-- tags: [XlsIO, named ranges, C#, VB.NET, Microsoft Office, Syncfusion Winforms] keywords: [XlsIO, named ranges, cell names, dynamic ranges, programmatically adding ranges, C#, VB.NET, Microsoft Office, sheet-level ranges] -->
```