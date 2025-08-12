```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_634.jpeg
document_name: grid
page_number: 634
page_id: grid#page_634
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:21Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

The example demonstrates an optimization that handles the case where changes to a record affect only single cells in the grid. The sample updates two columns (and summaries) in one thousand records in a timer event every 50 milliseconds while keeping CPU usage low. In this scenario, the engine detects that changes to the Freight or Employee field do not impact any counters in the engine's object. It checks if the record is visible in the current view, and if that is the case, it saves the record and field information for painting. The painting of the cell is delayed until `gridGroupingControl.Update` is called or until the time specified with `GridGroupingControl.UpdateDisplayFrequency` has elapsed.

### Handling Display Updates

In this example, you can also observe the throttling of display updates. The `UpdateDisplayFrequency` is initially set to 0, which means that the `timer_Tick` method in the form calls `grid.Update` to force pending updates. However, you can specify any amount of milliseconds in the Property Grid for this property to watch the grid react slower or faster to changes while the `ListChanged` events continue to come in at the same pace.

### Sorting Records

If you click on the Freight column to sort records by the values of this field, the strategy employed by the Grid Grouping control to update the internal structure and the display must change. Now, every change to the Freight column can potentially affect the sort position of a record. The moment you click on the column header and sort by that field, the engine will single out that field for more detailed inspection when a `ListChanged` event is received.

### Handling Updates to Specific Fields

If a change is detected to the Freight field in a `DataRow`, the engine will check the new value against the value of the previous record and the next record. If the new value is greater or equal to the previous record's value and smaller or equal to the next record's value, no further action is required other than repainting the cell. However, if the new value does not fit in between these records, the sort position of the records needs to be recalculated. The binary tree structures within the engine allow for quick removal and reinsertion of the record at the correct sort position. The engine will raise `SourceListRecordChanging` and `SourceListRecordChanged` events to indicate that the records' sort position is about to change and has changed.

### Updating the Display with Sort Position Changes

Updating the display with changes in the sort position of a record is significantly more demanding than simply repainting a cell. One or multiple records may need to be shifted up or down. The easiest way to handle this is to invalidate the whole display and repaint all rows. This is how the Grid Grouping control handles this case by default. You can change this default behavior by specifying how the grid should update the display using the `InsertRemoveBehavior` and `SortPositionChangeBehavior` properties.

### Optimizing Display Updates

By setting these properties to `ListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate`, you can instruct the engine not to repaint the whole screen. Instead, the engine will determine the area affected by a sort position change and use the `ScrollWindow` API to shift records up and down, only repainting the one record that was really changed. This approach can have a big impact if you have a large grid and repainting the whole display is expensive. It can increase the speed by the number of rows that are visible, as only one row needs to be repainted instead of repainting all rows.

---

<!-- tags: [GridView, GridGroupingControl, UI Optimization, Updating, Sorting] keywords: [grid, update, display frequency, Freight column, ListChanged, SortPosition, record painting, ScrollWindow, UI performance] -->
```