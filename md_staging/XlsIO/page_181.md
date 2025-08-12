```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_181.jpeg
document_name: XlsIO
page_number: 181
page_id: XlsIO#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:39Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### 4.1.3.3 Formats

**Overview**
- This section explains various formatting features in Excel cells using simple APIs provided by XlsIO. It covers cell resizing, visibility control, sheet organization, and cell protection.

**Details**
Excel cells have various formats that can be applied to customize the cells as per the users' needs. These formats include sizing up of the cell, showing or hiding cells, protecting the cells, and organizing the sheet that contains the cell.

XlsIO provides support for such formatting with simple APIs. This section explains the support for the following formats:

- **Cell Size** - This section explains various methods that are used to resize cells.
- **Visibility** - This section explains various options that control the cell's visibility.
- **Sheet Organization** - This section explains various manipulations for sheets that contain cells.
- **Protection** - This section explains how a cell and sheet can be protected from editing.

### 4.1.3.3.1 Changing Cell Size

## API Reference

### C#
```csharp
// Deleting Rows.
sheet.DeleteRow(startRow, NoOfRows);

// Deleting Columns.
sheet.DeleteColumn(startColumn, NoOfColumn);
```

### VB.NET
```vb
' Deleting Rows.
sheet.DeleteRow(startRow, NoOfRows)

' Deleting Columns.
sheet.DeleteColumn(startColumn, NoOfColumn)
```

**Notes:**
- **Efficiency Note**: Deletion by using the above methods is more efficient than looping.
- **Indexing Note**: Row/Column index of these methods are "one based".

## Code Examples

### C#
```csharp
// Example of deleting rows and columns
sheet.DeleteRow(2, 5); // Deletes 5 rows starting from row 2
sheet.DeleteColumn(3, 2); // Deletes 2 columns starting from column 3
```

### VB.NET
```vb
' Example of deleting rows and columns
sheet.DeleteRow(2, 5) ' Deletes 5 rows starting from row 2
sheet.DeleteColumn(3, 2) ' Deletes 2 columns starting from column 3
```

## Cross References
- Refer to the sections on **Visibility**, **Sheet Organization**, and **Protection** for more detailed information.

<!-- tags: [xlsio, excel, formatting, cell size, visibility, sheet organization, protection] keywords: [xlsio, cell formatting, resize, hide, protect, delete rows, delete columns] -->
```