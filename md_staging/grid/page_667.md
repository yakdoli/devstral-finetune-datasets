```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_667.jpeg
document_name: grid
page_number: 667
page_id: grid#page_667
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:33Z
fidelity: lossless
-->

## Overview
- This page focuses on the performance aspects of the grid grouping control in Syncfusion.
- It provides a sample to check the performance impact of various options that can affect the speed of the grid.
- Key options discussed include Sort and Categorize, CalculateMaximumColumnWidth, CustomSorting, and MultiThreading.
- The code sample is available at: `<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Performance\Grouping Performance Demo`.

## Content

### 4.3.4.1.4 Grouping Performance
This section focuses a sample that lets you check the performance of the grid grouping control by toggling various options that can affect the speed of the grid. The different options include Sort and Categorize the records, Calculating MaximumColumnWidth, CustomSorting and MultiThreading (in case if a multiprocessor system is available).

#### Options Used
- **Sort and Categorize**
  - This option enables grouping and sorting by assigning a group and sort order.

- **UseDataViewSort**
  - Uses the class `GroupingSortList` to wrap the `DataView` with `IBindingList`. It also implements `IGroupingList` interface. This allows performing the sort on the data view directly instead of relying on the grouping engine to perform sort.

- **CalculateMaximumColumnWidth**
  - When enabled, the maximum number of characters found in record field cells is calculated for columns. This will be used in re sizing the columns to optimal width. Affects `TableDescriptor.AllowCalculateMaxColumnWidth` property.

- **MultiThreading**
  - When set to true, this option will allow multithreading. It allows you to calculate the count in a separate thread when all records are categorized. Affects `Table.AllowThreading` property. Enable this only on true multiprocessor machines otherwise systems calculating counts in separate thread will slow categorization down.

### Notes
- For code, refer to the following Browser sample:
  `<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Performance\Grouping Performance Demo`

## Cross References
- See also: High Frequency Updates in Grid Grouping Control (Figure 268)

<!-- tags: [Syncfusion, GridGrouping, Performance, Options, Sort, Categorize, MultiThreading, MultiProcessor] keywords: [grid grouping, performance, sort, categorize, maximum column width, multithreading, multiprocessor] -->
```