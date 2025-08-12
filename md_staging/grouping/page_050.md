```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: grouping
page_number: 050
page_id: grouping#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:41Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates how to configure and use the Grouping Engine to perform essential grouping operations in a dataset.

## Content

### Setting the Data Source
The following code snippet initializes a Grouping Engine and sets its data source using the `SetSourceList` method. It then iterates through the records of the Table, printing each object to the console.

```vb
' Set its datasource.
    groupingEngine.SetSourceList(list)

    ' Display the data before sorting.
    Dim rec As Record
    For Each rec In groupingEngine.Table.Records
        Dim obj As MyObject = CType(rec.GetData(), MyObject)
        If Not (obj Is Nothing) Then
            Console.WriteLine(obj)
        End If
    Next rec

    ' Pause
    Console.ReadLine()
```

### Sorting a Column
The next part of the snippet sorts the data based on Column "A" using the `SortedColumns.Add` method. After sorting, it displays the filtered records in the sorted order.

```vb
' Sort column A.
    groupingEngine.TableDescriptor.SortedColumns.Add("A")

    ' Display the data after sorting.
    For Each rec In groupingEngine.Table.FilteredRecords
        Dim obj As MyObject = CType(rec.GetData(), MyObject)
        If Not (obj Is Nothing) Then
            Console.WriteLine(obj)
        End If
    Next rec

    ' Pause
    Console.ReadLine()
```

This example illustrates the process of setting up a data source, performing sorting, and displaying the dataset at both before and after sorting stages.

## API Reference
- **GroupingEngine**: The main class that manages grouping operations.
  - **SetSourceList**: Method to set the data source for the Grouping Engine.
    - **Parameters**:
      - `list`: Collection of objects to set as the data source.
  - **TableDescriptor**: Property to access the TableDescriptor object.
    - **SortedColumns**: Collection property to add sorted columns.
      - **Add**: Method to add a column name to the sorted columns list.

## Code Examples

The provided snippet demonstrates the complete setup and usage of the Grouping Engine, including setting the data source, sorting, and displaying the data.

<!-- tags: [syncfusion, winforms, grouping, datahandling, tabledescriptor, group, sort] keywords: [groupingengine, sortedcolumns, filtering, records, display, sort, pause, console, data, source, table, descriptor, add] -->
```