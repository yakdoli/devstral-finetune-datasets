```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_042.jpeg
document_name: grouping
page_number: 042
page_id: grouping#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:15Z
fidelity: lossless
-->

## Essential Grouping

### Content
#### Filtering Records

```csharp
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

// Filter on [D] = d1
RecordFilterDescriptor rfd = new RecordFilterDescriptor("[D] LIKE 'd1'");
groupingEngine.TableDescriptor.RecordFilters.Add(rfd);

// Display the data after filtering.
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

#### [VB.NET]

```vb
' Display the data before filtering.
Dim rec As Record
    For Each rec In groupingEngine.Table.FilteredRecords
Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()

' Filter on [D] = d1
Dim rfd As New RecordFilterDescriptor("[D] LIKE 'd1'")
```

### API Reference

- **RecordFilterDescriptor**: Represents a descriptor for filtering records based on specific criteria.
  - **Constructor**: `RecordFilterDescriptor(string filterExpression)`
    - **filterExpression**: A string that defines the filtering criteria. (e.g., "[D] LIKE 'd1'").
  
### Code Examples

The provided code demonstrates how to:
1. Loop through filtered records and display relevant data.
2. Apply a filter condition to a table.
3. Display the filtered data.

### Cross References

See also:
- [Filtering Data in WinForms Grid](#filtering-data-in-winforms-grid)

## RAG Annotations
<!-- tags: Essential Grouping, filtering, WinForms, Grid, RecordFilterDescriptor keywords: Essential Grouping, filtering, WinForms, Grid, RecordFilterDescriptor -->
```