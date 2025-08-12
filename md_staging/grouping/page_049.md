```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: grouping
page_number: 049
page_id: grouping#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:58Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates setting up a data source for grouping.
- Displays data before and after sorting.
- Sorts a specific column and displays the sorted result.
- Includes both C# and VB.NET examples for creating and using the GroupingEngine.

## Content

### Setting Up the Data Source and Displaying Records

#### C#
```csharp
// Set its datasource.
groupingEngine.SetSourceList(list);

// Display the data before sorting.
foreach (Record rec in groupingEngine.Table.Records)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();

// Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A");

// Display the data after sorting.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}

// Pause
Console.ReadLine();
```

#### VB.NET
```vb
' Create an arraylist of random MyObjects.
Dim list As New ArrayList()
Dim r As New Random()

Dim i As Integer
For i = 0 To 9
    list.Add(New MyObject(r.Next(5)))
Next i

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()
```

### Key Features
- **Data Source**: Defines the source list for grouping.
- **Sorting**: Sorts the table by a specific column.
- **Display**: Shows the data before and after sorting.
- **Paused Execution**: Allows the user to view the output at different stages.

### Summary
This example showcases how to use the Syncfusion GroupingEngine to sort a table and display the records before and after the sorting operation. Both C# and VB.NET implementations are provided, demonstrating the integration of the GroupingEngine in WinForms applications.

### Cross References
- Refer to [Grouping Overview] for more details on grouping functionality.

### API Reference
- **GroupingEngine**: The main class for managing and manipulating grouped data.
  - **SetSourceList(list)**: Sets the source list for the grouping.
  - **Table.Records**: Gets the unfiltered records.
  - **Table.FilteredRecords**: Gets the records after applying filters and sorting.
  - **TableDescriptor.SortedColumns.Add(columnName)**: Adds a column to the sorted columns list.

### Code Examples
- The provided C# and VB.NET code snippets demonstrate how to:
  1. Set the data source for grouping.
  2. Display the records before sorting.
  3. Sort a specific column.
  4. Display the sorted records.

<!-- tags: [grouping, data_source, sorting, GroupingEngine, WinForms] keywords: [syncfusion, grouping engine, data display, table sorting, csharp, vb.net] -->
```
