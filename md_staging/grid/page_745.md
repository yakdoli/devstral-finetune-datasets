```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_745.jpeg
document_name: grid
page_number: 745
page_id: grid#page_745
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The Grid Grouping control allows you to display summaries for each group. Summaries let you derive additional information from your data like averages, maximums, summations, count, and so on.

For instance, you can get the number of records or maximum value, and so on. They display the calculation results in separate display rows. The calculation of summary values is very fast with only O(log2 n) operations (n being the number of records in the table), because of the highly optimized balanced tree structures used in the grouping engine.

The grouping grid provides the following built-in summary types.

- Int32Aggregate, DoubleAggregate (Count, Min, Max, Sum)
- StringAggregate (MaxLength, Count)
- Count
- DistinctCount (Count, Values array)
- Vector (Values)
- DoubleVector (statistical methods: Median, Min, Max, 25% Quartile, 75% Quartile)
- Custom (Custom Summaries)

The engine supports summaries that operate on vectors such as Distinct Count, Median, 25% and 75% Quartile. Users may also easily add custom summaries.

## SummaryRows Collection

The TableDescriptor.SummaryRows manages a collection of summary rows for the grid table. This collection implements an abstracted view to summaries which lets users define where to display the summary in the grid. Behind the scenes, the GridEngine adds many more hidden summaries to the Summaries collection. Examples for such hidden summaries are: maximum width for contents of a cell, filter bar choices, and display entries of a ForeignKeyKeyWords relation. You can have summaries for the individual columns (SummaryColumns) which can then be combined into a single Summary Row for display.

It is the SummaryDescriptorCollection that manages the summaries for a given table containing one entry for each summary. Each SummaryDescriptor in this collection has a MappingName that identifies a FieldDescriptor for which summaries should be calculated for, and a SummaryType property that defines the type of calculations to be performed. Possible options for SummaryType are: Count, BooleanAggregate, ByteAggregate, CharAggregate, DistinctCount, DoubleAggregate, Int32Aggregate, MaxLength, StringAggregate, Vector, DoubleVector, and Custom. By default, a SummaryDescriptor ignores the records that do not satisfy a filter criteria. This behavior can be changed with the IgnoreRecordFilterCriteria flag.

## Summaries Through Designer

### WinForms-specific conventions
- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Treat control names, namespaces, and types exactly (e.g., Syncfusion.Windows.Forms.Tools.TabControlAdv, Syncfusion.Windows.Forms.Grid).
- Distinguish design-time vs runtime features; preserve property grids, designer steps, and menu paths as regular text or ordered lists.
- When API elements are listed (Properties/Methods/Events/Enums), keep their exact order and names, including parentheses for methods and event handler signatures if visible.

### RAG Annotations
<!-- tags: grid, group, summarization, summaryrows, summarydescriptor, winforms, syncfusion -->
<!-- keywords: grid control, summaryRows, summaryRowsCollection, TableDescriptor, SummaryType, SummaryDescriptor, SummaryColumns, Custom Summaries, DoubleAggregate, Int32Aggregate, StringAggregate, DistinctCount, Vector, DoubleVector, SummaryColumn -->
```
