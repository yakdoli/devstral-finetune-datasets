```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_616.jpeg
document_name: grid
page_number: 616
page_id: grid#page_616
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:18Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Key Properties and Behaviors

#### UpdateDisplayFrequency
- This property allows you to specify the number of milliseconds to wait between display updates when the new ListChanged event handler logic is used.
- It has no effect if UseOldListChangedHandler = true.
- Special values:
  - `0`: Only manually update the display by calling `grid.Update()`.
  - `1`: Update the display immediately after each change.

#### UseDefaultsForFasterDrawing
- Setting this to `true` enables faster GDI Draw Text, Solid Borders, and more efficient calculation of the optimal width of a column.
- Initializes recommended settings that improve handling of ListChanged events and scrolling through the grid.
- Affected settings include:
  - `TableOptions.ColumnsMaxLengthStrategy`
  - `TableOptions.GridLineBorder`
  - `TableOptions.DrawTextWithGdiInterop`
  - `TableOptions.VerticalPixelScroll`
  - `Appearance.AnyRecordFieldCell.WrapText`
  - `Appearance.AnyRecordFieldCell.Trimming`

#### UseOldListChangedHandler
- With version 4.4, the engine changed the internal handling of the ListChanged event to fix performance issues with earlier code.
- This property allows you to revert to the old behavior if you notice compatibility issues.
- Default value: `false`.

#### BlinkTime
- Grid Grouping control supports highlighting cells for a short period after a change is detected.
- The BlinkTime property specifies the duration in milliseconds for cell highlighting.
- Enable or disable this feature for individual columns by toggling `GridColumnDescriptor.AllowBlink`.

### Related Topics

#### Memory Performance - Engine Optimizations
- This section discusses various optimizations provided by the GroupingEngine to improve memory performance.
- Triggering these optimizations selectively reduces the memory footprint.
- Engine optimizations can be enabled by setting `AllowOptimizations` to a value other than `None`.
- To optimize memory usage, the `CounterLogic` property must be assigned a proper value.

## AllowOptimizations

---

```html
<!-- tags: [Essential Grid, Windows Forms, Display Frequency, ListChanged, Engine Optimizations, Memory Performance, UseDefaultsForFasterDrawing, UseOldListChangedHandler, BlinkTime, CounterLogic] keywords: [Syncfusion Winforms, version 11.4.0.26, GroupingEngine, Display updates, GDI Draw Text, ListChanged event, Memory footprint, optimizations] -->
```