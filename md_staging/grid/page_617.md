```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_617.jpeg
document_name: grid
page_number: 617
page_id: grid#page_617
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- The list describes the optimizations provided by the grid, defined by the EngineOptimizations enumeration.
- By default, optimizations are turned off, but can be enabled when specified criteria are met.
- Key optimizations include None, DisableCounters, VirtualMode, PassThroughSort, and RecordsAsDisplayElements.

## Content

### EngineOptimizations Enumeration

- Specifies the values for the AllowedOptimizations property.

#### None

- **Description**: All optimizations are disabled.

#### DisableCounters

- **Description**: When the engine detects that a table lacks RecordFilters, GroupedColumns, or nested relations, counter logic is disabled for the RecordsDetails collection.
- The RecordsDetails collection will not have counters since it is in sync with actual records, e.g., all records in the data source are shown in the TopLevelGroup.
- Sorting support remains unaffected.

#### VirtualMode

- **Description**: If all criteria for this optimization are met and no SortedColumns are set, the RecordsDetails collection does not need to be initialized.
- Creates records on demand and discards them via garbage collection when no references exist.
- Reduces memory footprint to an absolute minimum, enabling the loading and display of millions of records in a table.
- The PrimaryKey collection is supported but initialized on demand when accessing the Table.PrimaryKeyRecords collection, where all records will be enumerated.

#### PassThroughSort

- **Description**: When all criteria for optimization are met and SortedColumns are set, the engine normally sorts records by looping through them.
- If the data source is an IBindingList and IBindingList.SupportsSort returns true, sorting is performed using IBindingList.Sort, with records accessed via VirtualMode.
- This approach is usually faster than the engine's built-in sorting but loses CurrentRecord and SelectedRecords information.
- Inserting and removing records becomes slower if the underlying data source is a DataView.
- PassThroughSort is ignored if the criteria for the optimization are not met.
- A Pass-through sort mechanism can be forced by implementing the IGroupingList interface, allowing sorting on the DataView directly.
- It is recommended to use the engine's own Sort mechanism and only rely on PassThroughSort in Virtual mode scenarios.

#### RecordsAsDisplayElements

- **Description**: [Further details on this optimization are not provided in the current text.]

## Remarks

- This section describes various optimizations that can be applied to improve performance and reduce memory usage in the Essential Grid for Windows Forms.
- The optimal selection of these optimizations depends on the specific use case and data characteristics.

```csharp
// Example usage of PassThroughSort
if (grid.EngineOptimizations.HasFlag(EngineOptimizations.PassThroughSort))
{
    grid.AllowPassThroughSort = true;
}
```

### Cross References

- For more details on performance tuning, see the section on "Best Practices for Optimizing Grid Performance."
- For information on implementing IGroupingList, refer to the "Integration with Data Sources" chapter.

<!-- tags: [grid, engineoptimizations, performance, memorymanagement] keywords: [virtualmode, passthroughsort, disablecounters, recordsasdisplayelements] -->
```