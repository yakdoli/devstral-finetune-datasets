```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_362.jpeg
document_name: XlsIO
page_number: 362
page_id: XlsIO#page_362
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:52Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
' ' Sorts the data based on this color
field.Color = Color.Red

' ' Sorts the data with the sort field attribute.
sorter.Sort()
```

## 4.5.3.4 Sorting by Cell Color

With this feature, MS Excel moves the cell text and color to the specified location (bottom or top) of the sorting range.

![Sorting by Cell Color](image.png)

This is explained in the following code samples:

### C#

```csharp
// Creates the data sorter
IDataSort sorter = book.CreateDataSorter();

// Range to sort
sorter.SortRange = range;

// Creates the sort field with the column index, sort based on and order by attribute
ISortField sortField = sorter.SortFields.Add(2, SortOn.CellColor, OrderBy.OnTop);

// Specifies the color to sort the data
sortField.Color = Color.Red;

// Sort based on the sort field attribute
```

### Figure:
![Sorting by Cell Color](image.png)

## Summary
- Explains how to sort data in Excel based on cell color using both MS Excel and code samples.
- Demonstrates the sorting process with detailed explanations and a C# code example.

<!-- tags: [xlsio, sorting, cell color, winforms, .net, csharp, excel, data manipulation] keywords: [sorting, cellcolor, excel, dat-sorter, code-sample, winforms, csharp, ms-excel] -->
```