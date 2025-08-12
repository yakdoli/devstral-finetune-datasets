```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_642.jpeg
document_name: grid
page_number: 642
page_id: grid#page_642
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- A Grid Grouping control is setup with options to display the summary cells in caption.
- Enable the optimizations required.
- Use `InvalidateAll` option for `InsertRemoveBehavior` and `SortPositionChangedBehavior` properties when many records change sort position for a short time.
- Use `ScrollWithImmediateUpdate` if `ScrollWindow` should be called to minimize painting when sort position of limited number of records is changed.
- Grid Grouping control is detached from the Currency Manager and access the list directly to solely rely on `ListChanged` events.

## Content

### C# Code Example
```csharp
// Optimization code.
// 0 if Manual updates only from timer_tick.
this.gridGroupingControl.UpdateDisplayFrequency = 0;
this.gridGroupingControl.UseDefaultsForFasterDrawing = true;
this.gridGroupingControl.CounterLogic = EngineCounters.YAmount;
this.gridGroupingControl.AllowedOptimizations = EngineOptimizations.DisableCounters |
    EngineOptimizations.RecordsAsDisplayElements;
this.gridGroupingControl.CacheRecordValues = false;

this.gridGroupingControl.InsertRemoveBehavior =
    GridListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate;
this.gridGroupingControl.SortPositionChangedBehavior =
    GridListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate;

this.gridGroupingControl.BindToCurrencyManager = false;

// Enable Caption Summaries.
gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowCaptionSummaryCells = true;
gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowSummaries = true;
gridGroupingControl1.TableDescriptor.ChildGroupOptions.CaptionSummaryRow = "Caption";
```

### VB.NET Code Example
```vb
' Optimization code.
' 0 if Manual updates only from timer_tick.
Me.gridGroupingControl1.UpdateDisplayFrequency = 0
Me.gridGroupingControl1.UseDefaultsForFasterDrawing = True
Me.gridGroupingControl1.CounterLogic = EngineCounters.YAmount
Me.gridGroupingControl1.AllowedOptimizations = EngineOptimizations.DisableCounters Or
    EngineOptimizations.RecordsAsDisplayElements
Me.gridGroupingControl1.CacheRecordValues = False

Me.gridGroupingControl1.InsertRemoveBehavior =
```

## API Reference
- This section provides details about the settings and behaviors related to Grid Grouping in Windows Forms.

### Properties
- `UpdateDisplayFrequency`: Sets the frequency of display updates.
- `UseDefaultsForFasterDrawing`: Enables default settings for faster painting.
- `CounterLogic`: Defines the logic for calculating counters.
- `AllowedOptimizations`: Specifies the types of optimizations to apply.
- `CacheRecordValues`: Controls whether record values are cached.
- `InsertRemoveBehavior`: Determines the behavior when records are inserted or removed.
- `SortPositionChangedBehavior`: Defines the behavior when sort position changes.
- `BindToCurrencyManager`: Enables or disables binding to the Currency Manager.
- `ShowCaptionSummaryCells` and `ShowSummaries`: Enables or disables display of summary cells in captions.

## Code Examples (continued)
The provided code examples demonstrate how to configure a Grid Grouping control for optimal performance and display. These settings are crucial for managing large datasets effectively, ensuring smooth interaction, and displaying summary information accurately.

## Cross References
- For more detailed information on Grid Grouping properties and behaviors, refer to the官方Syncfusion documentation.

## RAG Annotations
<!-- tags: [grid grouping, windows forms, optimization, summary cells, caption, syncfusion] keywords: [update display frequency, insert remove behavior, sort position changed behavior, scroll with immediate update, currency manager, record values, display elements, captions] -->
```