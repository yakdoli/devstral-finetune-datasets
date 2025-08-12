```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_615.jpeg
document_name: grid
page_number: 615
page_id: grid#page_615
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes techniques to reduce unnecessary redrawing of grid elements.
- Explains properties that control painting behavior based on list changes.

## Content

### Optimizing Repainting Behavior
- Changing certain properties can prevent the entire grid display from being invalidated when only a single record needs to be redrawn.
- By setting properties to `ListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate`, you can instruct the engine to only repaint the affected area instead of the entire screen.
- The engine uses the `ScrollWindow` API to shift records up or down and repaint only the record that was changed.
- This optimization is impactful for larger grids with costly painting operations.

### InvalidateAllWhenListChanged
- A setting that specifies whether the grid should simply call `Invalidate` when a `ListChanged` event is handled.
- Alternately, it can determine the area affected by the change and call `InvalidateRange`.
- Although determining the exact position of a record before marking it as dirty can be computationally expensive, it might be more efficient in scenarios with frequent updates.
- The group caption bar also requires updating when records change.

```markdown
#### Performance Considerations
- Properties such as `InsertRemoveBehavior`, `SortPositionChangedBehavior`, and `UpdateDisplayFrequency` can significantly speed up operations when `InvalidateAllWhenListChanged` is set to `false`.
```

### RaiseSourceListChangedEventsOnEngineOnly
- Property that determines how events are raised when the engine handles the `ListChanged` event.
- If set to `true`, events will only be raised on the `Engine` object.
- If set to `false`, events will also be raised on inner objects, potentially causing additional performance overhead.
- This property only has an effect if `UseOldListChangedHandler` is set to `false`.

### SortPositionChangedBehavior / SortPositionChangedBehaviorWithEndEdit
#### Overview
- Properties that control how the display updates when the sort position of a record changes.
- By default, the entire display is invalidated and repainted, even if only one record needs to be redrawn.
- This approach can degrade performance, especially for larger grids.

#### Optimization
- By setting these properties to `ListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate`, you can avoid repainting the entire screen.
- This ensures only the record that was actually changed is redrawn.

## API Reference

### Properties
- `InvalidateAllWhenListChanged`: Controls whether to invalidate the entire grid or determine the affected area.
- `RaiseSourceListChangedEventsOnEngineOnly`: Determines the scope of event raising.
- `SortPositionChangedBehavior`: Manages display updates for sort position changes.

### Methods
- `ScrollWindow`: API used to shift records and repaint only the changes.
- `InvalidateRange`: Method to mark and repaint specific areas of the grid.

## Code Examples

```csharp
// Example of setting InvalidateAllWhenListChanged
grid.InvalidateAllWhenListChanged = false;

// Example of setting RaiseSourceListChangedEventsOnEngineOnly
grid.RaiseSourceListChangedEventsOnEngineOnly = true;

// Example of setting SortPositionChangedBehavior
grid.SortPositionChangedBehavior = Enum.ListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate;
```

## Cross References
- [Report control for Windows Forms](report-control-for-windows-forms)
- [DataGrid for Windows Forms](datagrid-for-windows-forms)

## RAG Annotations
<!-- tags: [syncfusion, winforms, grid, Optimizing grids, repaint optimization, performance enhancement] keywords: [InvalidateRange, ScrollWindow, ListChangedInsertRemoveBehavior, SortPositionChangedBehavior, InvalidateAllWhenListChanged, RaiseSourceListChangedEventsOnEngineOnly] -->
```