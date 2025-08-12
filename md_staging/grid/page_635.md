```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_635.jpeg
document_name: grid
page_number: 635
page_id: grid#page_635
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The example also shows more optimized calculation of summaries. By default the engine uses binary trees and caches values in them. When changes to a field in a record are detected that affects a summary, then the nodes in the binary tree are marked dirty. This is a 2×O(log n) operation that is needed to mark nodes dirty and later again recalculate the summaries. The ManualTotalSummary sample demonstrates this by using a different approach. If you do not care about more complicated summaries such as minimum, maximum, distinct count, or median and if you know the delta of each value change, then you can keep a total value cached in the parent group and manually apply that delta to this parent group's summary value. Now you have a linear O(1) operation instead of the more costly binary tree updates. With that change, the sample can now deal nicely with 1,000 updates in 100 ms and 2 summary columns being changed with each update.

## GridListChangedInsertRemoveBehavior Enum

Definitions the values for the properties InsertRemoveBehavior and SortPositionChangedBehavior.

### InvalidateVisible

It will keep the engine in synchronization with ListChanged notifications and then invalidate rows on screen, below the affected row.

### InvalidateAll

It will simply set TableDirty = true, and the engine won't try to keep anything in synchronization at that time.

### ScrollWithImmediateUpdate

It will keep the engine in synchronization and use ScrollWindow, to scroll, window contents or adjust the top row index if changes occurred before the current visible row.

**Note:** For Complete Code for this example, refer the following Browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Performance\Manual Total Summary Demo
```

### Implementation

- The implementation uses a custom summary class named ManualTotalSummary. This is a manual summary class which can be updated immediately using the difference between old and new value in a ListChanged event. The Total property calculates the summaries for groups and table manually by looping through each group and record and summing up the values of the changed field. It provides faster updates on summaries by applying a delta between the old and new value when a record is changed.
```

```html
<!-- tags: [Syncfusion, Winforms, Essential Grid, Summary Calculation, Binary Trees, Manual Total Summary, InsertRemoveBehavior, SortPositionChangedBehavior, GridListChangedInsertRemoveBehaviorEnum, InvalidateVisible, InvalidateAll, ScrollWithImmediateUpdate] keywords: [optimized summary calculation, ManualTotalSummary, summary updates, O(1) operation, binary tree updates, ListChanged notifications, table dirty flag, synchronization in grid] -->
```