```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: XlsIO
page_number: 194
page_id: XlsIO#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:05Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Demonstrates how to hide and unhide specific rows and columns in XlsIO using methods such as ShowRow, ShowColumn, and ShowRange.

### Hiding and Unhiding Rows in XlsIO

- **Introduction**: XlsIO provides functionality to hide/unhide rows and columns using ShowRow, ShowColumn, and ShowRange methods.
- **Purpose**: This section explains how to use these methods effectively with code examples.

## Content

### Key Concepts

- **Hiding Rows and Columns**: 
  - Rows and columns can be hidden programmatically using the ShowRow and ShowColumn methods.
  - Boolean flag determines whether to show (true) or hide (false) a specific row or column.

### Code Examples

```csharp
[C#]

// Hiding the First Column and Second Row.
sheet.ShowColumn( 1, false );
sheet.ShowRow( 2, false );

// Hiding the Fifth Column and Fifth Row.
sheet.ShowColumn( 5, false );
sheet.ShowRow( 5, false );

// Unhiding the Fifth Column and Second Row.
sheet.ShowColumn( 5, true );
sheet.ShowRow( 2, true );

IRange range = sheet[1, 4];
//Hiding the first to third row and first to third column
sheet.ShowRange(range, false);

IRange firstRange = ws[1, 1,3,3];
IRange secondRange = ws[5, 5, 7, 7];
RangesCollection rangeCollection = new RangesCollection(app, ws);
rangeCollection.Add(firstRange);
rangeCollection.Add(secondRange);
//Hiding the collection of ranges
ws.ShowRange(rangeCollection, false);
```

### Explanation

- **Hiding Individual Rows/Columns**:
  - The `ShowColumn` and `ShowRow` methods are used to hide or show specific columns or rows based on their index and a boolean flag.
  
- **Hiding Ranges**:
  - The `ShowRange` method allows you to hide or show a specific range of cells defined by their coordinates.
  
- **Hiding Multiple Ranges**:
  - You can create a `RangesCollection` to group multiple ranges and hide or show them all at once.

## API Reference

### Methods

- **ShowColumn**: Hides or shows a specific column in a worksheet.
  - **Parameters**:
    - `columnIndex`: The index of the column to be hidden/shown.
    - `isVisible`: A boolean flag indicating whether to show (true) or hide (false) the column.
  
- **ShowRow**: Hides or shows a specific row in a worksheet.
  - **Parameters**:
    - `rowIndex`: The index of the row to be hidden/shown.
    - `isVisible`: A boolean flag indicating whether to show (true) or hide (false) the row.
  
- **ShowRange**: Hides or shows a specific range of cells in a worksheet.
  - **Parameters**:
    - `range`: The range of cells to be hidden/shown.
    - `isVisible`: A boolean flag indicating whether to show (true) or hide (false) the range.

## Code Examples (Continued)

The examples demonstrate how to use these methods to hide/unhide specific parts of a worksheet programmatically.

<!-- tags: [xlsio, hide, unhiding, rows, columns, showrow, showcolumn, showrange, ranges, syncfusion] keywords: [hide column, unhide row, range collection, boolean flag, worksheet manipulation] -->
```