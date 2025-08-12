```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_065.jpeg
document_name: grouping
page_number: 065
page_id: grouping#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:58Z
fidelity: lossless
-->

## Essential Grouping

```csharp
RecordFilterDescriptor.name
Me.gridGroupingControl1.TableDescriptor.RecordFilters.Remove() ' Removes the RecordFilter associated by mentioning as index.
Me.gridGroupingControl1.TableDescriptor.RecordFilters.RemoveAt()
```

**Note:** To remove a particular filter, use the `groupingEngine.TableDescriptor.RecordFilters.Remove` or `groupingEngine.TableDescriptor.RecordFilters.RemoveAt`. To use `Remove`, you will need a reference to the `RecordFilterDescriptor` object that you want to delete or your `RecordFilterDescriptor` object would have to be named (setting the `RecordFilterDescriptor.Name` property or by passing a name string into its overloaded constructor).

### 5.7 How to Clear a Grouping?

To clear all grouping, call the `groupingEngine.TableDescriptor.GroupedColumns.Clear` method.

**[C#]**
```csharp
// Removes the grouping of all the grouped columns.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();

// Removes grouping of the column mentioned as an argument.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove(Name);

// Removes grouping of the column mentioned as column index.
this.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt(index);
```

**[VB.NET]**
```vb
' Removes the grouping of all the grouped columns.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()

' Removes grouping of the column mentioned as an argument.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove()

' Removes grouping of the column mentioned as column index.
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt()
```

```html
<!-- tags: [Syncfusion, Winforms, Grouping, RecordFilter, GroupedColumns, Remove, RemoveAt, Clear] keywords: [grouping, recordfilter, groupedcolumns, remove, removeat, clear, Winforms, Syncfusion] -->
```