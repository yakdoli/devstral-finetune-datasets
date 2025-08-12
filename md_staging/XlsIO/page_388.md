```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_388.jpeg
document_name: XlsIO
page_number: 388
page_id: XlsIO#page_388
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:20Z
fidelity: lossless
-->

## Overview
- Ungrouping by columns and rows using the `ExcelGroupBy` enumeration in C# and VB.NET.
- Grouping actions performed on specific ranges within the Excel sheet.

## Content

### Ungrouping by Columns in C#

```csharp
// Ungroup by columns
sheet.Range["C1:F1"].Ungroup(ExcelGroupBy.ByColumns);
```

### Grouping and Ungrouping in VB.NET

```vbnet
[VB.NET]

' Grouping by Rows.
sheet.Range( "A1:A3" ).Group(ExcelGroupBy.ByRows, True)
sheet.Range( "A4:A6" ).Group(ExcelGroupBy.ByRows)

' Grouping by Columns.
sheet.Range( "A1:B1" ).Group(ExcelGroupBy.ByColumns, True)
sheet.Range( "C1:F1" ).Group(ExcelGroupBy.ByColumns)

' Ungroup by Rows
sheet.Range( "A1:A3" ).Ungroup(ExcelGroupBy.ByRows)

' Ungroup by columns
sheet.Range( "C1:F1" ).Ungroup(ExcelGroupBy.ByColumns)
```

## API Reference

### Methods
#### Ungroup
- **Description**: Ungroups the specified range in the Excel sheet by rows or columns.
- **Parameters**:
  - `ExcelGroupBy mode`: Specifies whether to ungroup by rows or columns.
- **Usage**:
  ```csharp
  sheet.Range["C1:F1"].Ungroup(ExcelGroupBy.ByColumns);
  ```

## Code Examples

### Complete Example

#### C#
```csharp
// Example: Ungroup rows and columns
// Set up ranges and ungroup them accordingly
sheet.Range["C1:F1"].Ungroup(ExcelGroupBy.ByColumns);
```

#### VB.NET
```vbnet
' Example: Group and Ungroup rows and columns
' Set up ranges and perform grouping and ungrouping
sheet.Range( "A1:A3" ).Group(ExcelGroupBy.ByRows, True)
sheet.Range( "A4:A6" ).Group(ExcelGroupBy.ByRows)
sheet.Range( "C1:F1" ).Ungroup(ExcelGroupBy.ByColumns)
```

## Cross References
See also: ExcelGroupBy, Range classes, and related methods for grouping and ungrouping functionality.

<!-- tags: [xlsio, grouping, ungrouping, excel, spreadsheet] keywords: [groupbycolumns, ungroupbyrows, vbdotnet, .net, syncfusion sdk] -->
```