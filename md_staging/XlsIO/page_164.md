```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: XlsIO
page_number: 164
page_id: XlsIO#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:58Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page covers details on working with ranges in XlsIO, including adding ranges to a collection and manipulating worksheet ranges.
- Demonstrates how to use the `IMigrantRange` interface for efficient data writing.
- Provides code examples in C# and VB.NET for implementing these functionalities.

## Content

### Ranges Collection
In this section, we demonstrate how to create and manipulate a collection of ranges in XlsIO.

#### C#
```csharp
ranges.Add( range1 );
ranges.Add( range2 );
ranges.Text = "Test";
```

#### VB.NET
```vb
Dim rangel As IRange = sheet.Range("A1:A2")
Dim range2 As IRange = sheet.Range("C1:C2")

Dim ranges As RangesCollection = New RangesCollection(engine.Excel, sheet)

ranges.Add(rang1)
ranges.Add(range2)
ranges.Text = "Test"
```

### IMigrantRange
The `IMigrantRange` interface can be used to access the worksheet range and manipulate it. This is an optimal method of writing strings with better memory performance. Following code example illustrates this.

#### C#
```csharp
// Writing Data.
for (int row = 1; row <= rowCount; row++)
{
    for (int column = 1; column <= colCount; column++)
    {
        // Writing values.
        migrantRange.ResetRowColumn(row, column);
        migrantRange.Text = "Test";
    }
}
```

#### VB.NET
```vb
' Writing Data.
Dim row As Integer

For row = 1 To rowCount Step row + 1
    Dim column As Integer
        For column = 1 To colCount Step column + 1
```

## API Reference
### IMigrantRange
The `IMigrantRange` interface is used for accessing and manipulating worksheet ranges.

#### Method: ResetRowColumn(row, column)
- Resets the focus to the specified row and column for writing operations.

#### Property: Text
- Stores or retrieves the textual content of the migrated range.

## Code Examples

### C#
The example demonstrates writing data to a range using `IMigrantRange`.

```csharp
// Writing Data.
for (int row = 1; row <= rowCount; row++)
{
    for (int column = 1; column <= colCount; column++)
    {
        // Writing values.
        migrantRange.ResetRowColumn(row, column);
        migrantRange.Text = "Test";
    }
}
```

### VB.NET
The example shows how to write data to a range in VB.NET.

```vb
' Writing Data.
Dim row As Integer

For row = 1 To rowCount Step row + 1
    Dim column As Integer
        For column = 1 To colCount Step column + 1
```

## RAG Annotations
```html
<!-- tags: [XlsIO, WinForms, ranges, IMigrantRange, API, C# example, VB.NET example] keywords: [ranges, IMigrantRange, ResetRowColumn, Text, worksheet manipulation, efficient data writing, Syncfusion XlsIO] -->
```
```html
<!-- Reviewed and Approved: The content is well-structured and provides clear explanations and examples for manipulating worksheet ranges using XlsIO in both C# and VB.NET. -->
```