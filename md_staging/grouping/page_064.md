```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: grouping
page_number: 064
page_id: grouping#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:25Z
fidelity: lossless
-->

# Essential Grouping

```csharp
using Syncfusion.Grouping;

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its datasource.
groupingEngine.SetSourceList(list);
```

```vb
Imports Syncfusion.Grouping

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

' Set its datasource.
groupingEngine.SetSourceList(list)
```

## 5.6 How to Clear a Filter?

To clear all filters, call the `groupingEngine.TableDescriptor.RecordFilters.Clear` method.

### Clear All Filters

```csharp
// Removes all the filters associated with the table.
this.gridGroupingControl.TableDescriptor.RecordFilters.Clear();
```

```vb
' Removes all the filters associated with the table.
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
```

### Remove Specific Filter by Name

```csharp
// Removes the Filter associated by sending the argument as RecordFilterDescriptor.name
this.gridGroupingControl.TableDescriptor.RecordFilters.Remove(RecordFilterDescriptor.Name);
```

### Remove RecordFilter by Index

```csharp
// Removes the RecordFilter associated by mentioning as index.
this.gridGroupingControl1.TableDescriptor.RecordFilters.RemoveAt();
```

```vb
' Removes the Filter associated by sending the argument as
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Remove(RecordFilterDescriptor.Name);
```

### Remove Specific Filter by Name (Vb.Net)

```vb
' Removes the Filter associated by sending the argument as
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Remove(RecordFilterDescriptor.Name);
```
```