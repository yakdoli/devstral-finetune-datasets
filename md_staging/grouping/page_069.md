```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: grouping
page_number: 069
page_id: grouping#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:02:10Z
fidelity: lossless
-->

# Essential Grouping

```csharp
Console.WriteLine("c1-group {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)
```

## 5.12 How to Sort a Collection?

To sort your data, add the name of the property that you want to sort to the Engine.TableDescriptor.SortedColumns collection.

### Sorting in C#

```csharp
// Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A");
```

### Sorting in VB.NET

```vb
' Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A")
```

## API Reference

- **Namespace:** Engine.TableDescriptor
- **Property:** SortedColumns

### Parameters

- **Column Name:** The name of the property you want to sort by.

### Returns

- **Type:** void

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Grid;

// Example of sorting a column in C#
GridEngine groupingEngine = new GridEngine();
groupingEngine.TableDescriptor.SortedColumns.Add("A");
```

### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Grid

' Example of sorting a column in VB.NET
Dim groupingEngine As GridEngine = New GridEngine()
groupingEngine.TableDescriptor.SortedColumns.Add("A")
```

### Explanation

- The `SortedColumns.Add` method is used to add the name of the column you want to sort to the SortedColumns collection.
- This method ensures that the data is sorted based on the specified column's property.

## See also

- [Grouping and Sorting Data](#)
- [Engine.TableDescriptor Reference](#)

<!-- tags: [grouping, sorting, columns, engine.tabledescriptor, csharp, vb.net, version: 11.4.0.26] keywords: [sort, collection, property, add, column, engine, tabledescriptor, sortedcolumns] -->
```