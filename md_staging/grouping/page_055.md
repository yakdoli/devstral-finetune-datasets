```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: grouping
page_number: 055
page_id: grouping#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:55Z
fidelity: lossless
-->

## Essential Grouping

### Overview

- Demonstrates the process of grouping objects in a `Grouping.Engine`.
- Explains setting up data sources, defining custom sorting, and displaying the grouped data.

### Content

```vb
' Create an arraylist of random MyObjects.
Dim list As New ArrayList()
Dim r As New Random()

Dim i As Integer
For i = 0 To 9
    list.Add(New MyObject(r.Next(20)))
Next i

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

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

' Custom sort column A.
' Get an IComparer object to handle the custom sorting.
Dim comparer As New AComparer()
groupingEngine.TableDescriptor.SortedColumns.Add("A")
groupingEngine.TableDescriptor.SortedColumns("A").Comparer = comparer

' Display the data before sorting.
Dim rec As Record
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
```

### WinForms-specific conventions

- The sample demonstrates the use of `Grouping.Engine` in VB.NET for organizing and sorting data.
- It leverages the `ArrayList` to store objects, and the `Random` class to simulate data generation.
- Custom sorting is implemented by setting an `IComparer` object for the specific column.

### Copyright Notice

© 2013 Syncfusion. All rights reserved.

---

<!-- tags: [product, module, control, api, version?] keywords: [grouping, Grouping.Engine, ArrayList, Random, IComparer, sorting] -->
```