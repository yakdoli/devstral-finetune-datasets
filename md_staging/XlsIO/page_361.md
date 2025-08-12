```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_361.jpeg
document_name: XlsIO
page_number: 361
page_id: XlsIO#page_361
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:29Z
fidelity: lossless
-->

# Essential XlsIO

![Sorting by Font Color](image.png)

## Overview
1. Demonstrates sorting data in Excel using font color as a criterion.
2. Provides sample code in both C# and VB for implementing font color sorting.
3. Explains the steps involved in creating a data sorter and specifying sorting criteria.

## Content

This section explains the process of sorting Excel data based on font color, as depicted in the image.

### Sorting by Font Color

The steps for sorting by font color are illustrated in the following code samples:

#### C#

```csharp
// Creates the data sorter
IDataSort sorter = book.CreateDataSorter();

// Range to sort
sorter.SortRange = range;

// Creates the sort field with the column index, sort based on and order by attribute
ISortField sortField = sorter.SortFields.Add(2, SortOn.FontColor, OrderBy.OnTop);

// Specifies the color to sort the data
sortField.Color = Color.Red;

// Sort based on the sort Field attribute
sorter.Sort();
```

#### VB

```vb
' Creates the Data sorter
Dim sorter As IDataSort = book.CreateDataSorter()

' Specifies the sort range
sorter.SortRange = range

Dim field As ISortField
' Adds the sort field with column index, sort based on and order by attribute
field = sorter.SortFields.Add(2, SortOn.FontColor, OrderBy.OnTop)
```

<!-- 
This section covers the essential techniques for sorting Excel data by font color using Syncfusion's XlsIO library. The provided code demonstrates how to set up and execute the sorting process effectively.
 -->

## See also
- [Syncfusion XlsIO Documentation](https://help.syncfusion.com/xlsio/)
- [Excel Data Operations](https://help.syncfusion.com/xlsio/excel-data-operations)

<!-- tags: [Syncfusion, Winforms, XlsIO, ExcelSorting, FontColor] keywords: [sorting by font color, Excel, C#, VB, data sorting, range sorting, attribute-based sorting] -->
```
