```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: XlsIO
page_number: 180
page_id: XlsIO#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:57Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Right-clicking a cell provides a context menu for editing and managing rows and columns.
- Rows and columns can be deleted using specific methods offered by the `IWorksheet` interface.
- Deleting rows and columns dynamically rearranges the remaining content in the worksheet.

## Content

### Context Menu
![Figure: Context menu on right-clicking the cell](#)

Figure 60: **Context menu on right-clicking the cell**

#### Overview of Context Menu Functionality
- **Delete**: Selecting this option moves the below rows one step up when deleting a row. Deleting a column moves the columns to the right, shifting them one step to the left.

#### Using XlsIO for Row and Column Deletion

XlsIO provides methods to delete rows and columns programmatically. The `IWorksheet.DeleteRow` method is used to remove a specified row, while the `IWorksheet.DeleteColumn` method handles column deletion. Below are code examples demonstrating how to perform these actions.

#### Code Examples

##### C#
```csharp
// Deleting Row.
sheet.DeleteRow(3);

// Deleting Column.
sheet.DeleteColumn(2);
```

##### VB.NET
```vb
' Deleting Rows.
sheet.DeleteRow(3)

' Deleting Columns.
sheet.DeleteColumn(2)
```

#### Deleting Multiple Rows
You can also delete multiple rows by specifying the range or using the appropriate method parameters. This functionality allows for efficient management of large datasets within the worksheet.

## API Reference
- **Methods**
  - `IWorksheet.DeleteRow(rowIndex)`: Deletes the specified row and shifts subsequent rows up.
  - `IWorksheet.DeleteColumn(columnIndex)`: Deletes the specified column and shifts adjacent columns to the left.

## Code Examples (multi-language supported)
The examples provided demonstrate the direct use of the deletion methods in both C# and VB.NET.

## Page-level Navigation/TOC (if applicable)
- **Context Menu**
- **Using XlsIO for Row and Column Deletion**
- **Deleting Multiple Rows**
- **API Reference**

## Cross References
See other sections or examples for additional contexts where row and column deletion might be integrated with other worksheet operations.

### RAG Annotations
The functional context and code snippets provide a clear understanding of how to manipulate worksheets programmatically by deleting rows and columns.

<!-- tags: [Syncfusion, XlsIO, Worksheet, RowDeletion, ColumnDeletion] keywords: [IWorksheet, DeleteRow, DeleteColumn, Excel, Programming, C#, VB.NET, Syncfusion Winforms] -->
```
