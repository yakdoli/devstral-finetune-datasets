```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_619.jpeg
document_name: grid
page_number: 619
page_id: grid#page_619
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Counts visible elements, filtered records, and YAmount. Medium memory footprint.

## Optimizations and Their Application

**Note:** *Allowing certain optimizations does not mean that the optimization is necessarily used. Optimizations will only be used when applicable. Take for example the optimization. If you allow this optimization the engine will check schema settings when loading the table. If there are no SortedColumns, RecordFilters, GroupedColumns, and no nested relations for a table, then virtual mode can be used and no records need to be loaded into memory. If the user later sorts by one column, the virtual mode cannot be used any more. Records will need to be iterated through and sorted and tree structures will be built that allow quick access to records and IndexOf operations. When initializing the table the engine will check if criteria for DisableCounters optimization are met.*

### Example

This example illustrates the Virtual Mode and WithoutCounter optimizations having a VirtualList as the data source. The VirtualList is just a `CustomCollection` that implements `IList` and `ITypedList` interfaces. The list is populated with 100K items and the same is bound to the grid grouping control. The example also displays a Log Window where you could track the different optimizations applied at different instances. It also displays the time elapsed for populating the grid grouping control.

#### Optimization Application

All the optimizations are enabled by setting AllowedOptimizations to All. As said earlier, the optimizations specified will not be applied at all times. They will only be used when applicable, that is, when the criteria for those optimizations are met. This example best illustrates this process. On every property change, the log window displays the list of optimizations applied to the grid at that instance. When you run the sample, you could be able to track the optimizations applied in different engine states like with/without grouping, with/without sorting, etc.

## Example Structure

**Note:** For more details, refer the following Browser Sample:

- `<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Performance\Engine Optimization Demo`

### Implementation

Follow the steps below to experiment different engine optimizations.

1. Create a class (`VirtualItem`) that represents the record structure. It's data members form the record fields.

```csharp
public class VirtualItem
{
    int index;
}
```
```


<!-- tags: [Winforms, Grid, Engine Optimization, Virtual Mode, DisableCounters, CustomCollection] keywords: [VirtualMode, WithoutCounter, SortedColumns, RecordFilters, GroupedColumns, Nested Relations, Grid Grouping, Log Window, AllowedOptimizations, VirtualItem, IndexOf] -->
```