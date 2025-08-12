```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: grouping
page_number: 044
page_id: grouping#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:14Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates filtering and accessing grouped data directly in the engine.
- Example code for C# and VB.NET to apply filters and iterate through filtered records.

## Content

### Code Example in C#

```csharp
rfd = new RecordFilterDescriptor("[D] LIKE 'd1' OR [B] = 2");
groupingEngine.TableDescriptor.RecordFilters.Add(rfd);

// Access the data directly from the Engine.
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

### Code Example in VB.NET

```vb
groupingEngine.TableDescriptor.RecordFilters.Clear()

rfd = New RecordFilterDescriptor("[D] LIKE 'd1' OR [B] = 2")
groupingEngine.TableDescriptor.RecordFilters.Add(rfd)

' Access the data directly from the Engine.
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()
```

## API Reference

### Methods/Properties
- `RecordFilterDescriptor(string filterExpression)`
  - Creates a new record filter descriptor with the specified filter expression.

- `TableDescriptor.RecordFilters`
  - Collection of record filter descriptors applied to the table.

- `Record.GetData()`
  - Retrieves the data object associated with the record.

- `FilteredRecords`
  - Collection of records that satisfy the current filter criteria.

## Code Examples

The examples demonstrate how to:
- Define a filter expression using `RecordFilterDescriptor`.
- Apply the filter to a `groupingEngine`.
- Iterate through the filtered records and access their data.
- Pause the program to view the output.

## Cross References

- See also:
  - [Using Filters in Grouping Engine](#)
  - [Accessing Data in Grouping](#)

<!-- tags: [WinForms, Grouping, Filter, Engine] keywords: [grouping, filter, record, engine, data access] -->
```