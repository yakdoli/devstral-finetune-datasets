```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_162.jpeg
document_name: XlsIO
page_number: 162
page_id: XlsIO#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:14Z
fidelity: lossless
-->

# Range Manipulation

The IRange interface represents a single cell or a group of cells in a worksheet. XlsIO has several useful methods for manipulating the data and formatting it in the ranges. This section discusses the topics listed below.

## Overview

- Accessing a Range
- IMigrant Range
- Copying/Moving a Range
- Clearing a Range
- Getting Used Range

### Accessing a Range

Range of cells can be accessed through the IRange interface. Following code example illustrates this.

```csharp
// Get cell range.
IRange this[string name] { get; }

// Gets/sets cell by row and index.
IRange this[int row, int column] { get; }

// Get cell range.
IRange this[string name, bool IsR1C1Notation] { get; }

// Get cells range.
IRange this[int row, int column, int lastRow, int lastColumn] { get; }
```

### Note: Here row and column indexes in the range are "one based". Following code example explains various ways of accessing cells.

```csharp
// Method 1 to Access a Range.
sheet.Range["A7"].Text = "Accessing a Range (Method 1)";

// Method 2 to Access a Range.
sheet.Range[9, 1].Text = "Accessing a Range (Method 2)";
```

## API Reference

The `IRange` interface provides methods for accessing, copying, moving, clearing, and getting the used range of cells in a worksheet.

## Code Examples

### Accessing a Range

Here's an example of accessing a range using different methods:

```csharp
// Method 1: Using cell name
IRange range1 = sheet["A7"];

// Method 2: Using row and column indices
IRange range2 = sheet[9, 1];

// Method 3: Using cell name with R1C1 notation
IRange range3 = sheet["A7", true];

// Method 4: Using a range of cells
IRange range4 = sheet[1, 1, 10, 10];
```

## Cross References

See also:
- IMigrant Range
- Copying/Moving a Range
- Clearing a Range
- Getting Used Range

<!-- tags: [xlsio, iRange, range-manipulation, syncfusion-winforms, version: 11.4.0.26] keywords: [accessing, copying, moving, clearing, used-range, cell-range, iRange, xlsio, worksheet, data-manipulation] -->
```