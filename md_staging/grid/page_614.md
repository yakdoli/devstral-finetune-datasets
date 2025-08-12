```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_614.jpeg
document_name: grid
page_number: 614
page_id: grid#page_614
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

This offline rendering of the grid ensures that all the required data is loaded into the memory and all grid data are initialized. Default value is true.

## Content

### BindToCurrencyManager

When you assign a `DataTable` to the grid grouping control, it will get access to the Default View of that Data Table through the Currency Manager that would listen to the updates to the underlying data table. The benefit of using `CurrencyManager` is that all the form elements would be kept in synchronization.

Using `CurrencyManager` may cause performance issues in certain scenarios. In such cases, you can bypass this `CurrencyManager` and access the list directly without ever involving the `CurrencyManager` by setting this property to false (which is true by default). This will in turn detach the grid from the `CurrencyManager` and hence the Grid Engine does not register the list with Windows Forms `CurrencyManager` and it will solely rely on listening to `ListChanged` events.

### CacheRecordValues

If you have custom collections, you can choose to have the engine to cache record values with this property. When set to true, the engine will cache copies of the old values from a record in the record object. You can get these values with the `Record.GetOldValue` method. With custom collections, the engine can also determine exactly which values in a record were changed when the engine receives the `ListChanged` event and previous values were cached.

### CounterLogic

It specifies the `CounterLogic` to be used within the engine. `GroupingEngine` maintains the counters for the `VisibleColumns`, `FilteredRecords`, `YAmount`, `HiddenRecords`, and the like. These counters occupy a countable portion of the grid tree in memory. On every list change, all these counters need to be refreshed too along with the data records.

Invalidating all the counters is not required at all times. For instance, if you have a larger data source and you don't want support for groups and filtered records, then there is no need to maintain the counters such as `FilteredRecords` and the like. Keeping all the counters in memory will greatly increase the memory consumption which is not necessary in this case and this will give a big degradation on grid performance.

To handle such scenarios, Grid Grouping control provides options to skip allocating these counters. By setting this property, you can reduce the memory footprint by selectively disabling the counters which are not required in your application. `EngineCounters` enum defines the values for this property which will be discussed in the next chapter.

### InsertRemoveBehavior / InsertRemoveBehaviorWithEndEdit

These properties determine how the grid should react when a record is inserted or deleted. One or multiple records need to be shifted up and down. By default, the whole

## Page-level Navigation/TOC (if applicable)
- List of properties discussed in this section:
  - BindToCurrencyManager
  - CacheRecordValues
  - CounterLogic
  - InsertRemoveBehavior / InsertRemoveBehaviorWithEndEdit

## Cross References
- EngineCounters enum will be discussed in the next chapter.

<!-- tags: [grid, windows forms, syncfusion, bindtoCurrencyManager, cacherecordvalues, counterlogic, insertremovebehavior, insertremovebehaviorwendedit] keywords: [currency manager, performance issues, list changed, old values, visiblecolumns, filtered records, y amount, hidden records, memory consumption, memory footprint, selective disabling] -->
```