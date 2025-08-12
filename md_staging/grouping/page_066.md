```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: grouping
page_number: 066
page_id: grouping#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:49Z
fidelity: lossless
-->

# Essential Grouping

**Note:** To remove a particular grouping, use `groupingEngine.TableDescriptor.GroupedColumns.Remove` or `groupingEngine.TableDescriptor.SortedColumns.RemoveAt`.

## How to Clear a Sort?

To clear all sorts, call the `groupingEngine.TableDescriptor.SortedColumns.Clear` method.

**C#**

```csharp
// Removes all the sorting associated with the table.
this.gridGroupingControl.TableDescriptor.SortedColumns.Clear();

// Removes the sorting of the column mentioned as argument.
this.gridGroupingControl.TableDescriptor.SortedColumns.Remove(Name of the column);

// Removes the sorting of the column mentioned as column index.
this.gridGroupingControl.TableDescriptor.SortedColumns.RemoveAt(index);
```

**VB.NET**

```vb
' Removes all the sorting associated.
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Clear()

' Removes the sorting of the column mentioned as argument.
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Remove()

' Removes the sorting of the column mentioned as column index.
Me.gridGroupingControl1.TableDescriptor.SortedColumns.RemoveAt()
```

**Note:** To remove a particular sort, use `groupingEngine.TableDescriptor.SortedColumns.Remove` or `groupingEngine.TableDescriptor.SortedColumns.RemoveAt`.

## How to Filter a Collection?

To add a filter condition, add a `RecordFilterDescriptor` to the `Engine.TableDescriptor.RecordFilters` collection. The constructor on the `RecordFilterDescription` takes an expression, `[D] LIKE 'd1'`. This expression will be `True` only for those items in the list where the string property `D` has the value `d1`. Here are some other valid expressions where `B` is an integer property:

- `[D] LIKE 'd1'`
- `[B] > 30`

<!-- tags: [Syncfusion, Winforms, grouping, filter, sort, control, api, TableDescriptor] keywords: [filter condition, RecordFilterDescriptor, RecordFilters, groupingEngine, sortedColumns, groupedColumns] -->
```