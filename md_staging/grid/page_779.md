```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_779.jpeg
document_name: grid
page_number: 779
page_id: grid#page_779
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:48Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Properties Window

The image depicts the properties window for the `gridGroupingControl1` control in Syncfusion's Windows Forms Grid. Here’s an overview of the visible properties and their settings:

### TopLevelGroupOptions
- **CaptionSummaryRow**: Not explicitly defined in the visible properties.
- **CaptionText**: `{TableName}: {RecordCount} Items`
- **IsExpandedInitialValue**: `True`
- **RepaintCaptionWhenItems**: `True`
- **ShowAddNewRecordAfter**: `False`
- **ShowAddNewRecordBefore**: `True`
- **ShowCaption**: `True`
- **ShowCaptionPlusMinus**: `False`
- **ShowCaptionSummaryCells**: `False`
- **ShowColumnHeaders**: `True`
- **ShowEmptyGroups**: `False`
- **ShowFilterBar**: `True`

### Additional Options
- The `ShowFilterBar` property is highlighted, indicating its significance.
- The description for `ShowFilterBar` states: "Indicates whether FilterBar is visible."

### Toolbar/Dropdown Options
- **Preview and Edit**: Available for interaction.
- **Copy Schema**, **Paste Schema**, **Save Schema**.
- **Choose Schema**.
- **Copy Look and Feel**, **Paste Look and Feel**, **Save Look and Feel**.
- **Choose Look and Feel**.

### Figure Caption
**Figure 311: Setting ShowFilterBar Property**

This figure illustrates how to set the `ShowFilterBar` property in the Syncfusion Windows Forms Grid control.

## API Reference

### Namespace
- Syncfusion.Windows.Forms.Grid.Grouping

### Properties
- **ShowFilterBar**: A boolean property indicating whether the FilterBar is visible.  
  - **Value**: `True` in the current configuration.

### Methods/Events (Not directly visible in the image)
The figure only shows property settings, so specific methods or events are not displayed. However, typical methods/events for Grid controls include:
- `AddNewRecord`
- `FilterChanges`
- `Rebind`

## Code Examples

### Example in C#
```csharp
gridGroupingControl1.TopLevelGroupOptions.ShowFilterBar = true;
```

### Example Description
This example demonstrates setting the `ShowFilterBar` property to `true` in the `gridGroupingControl1` instance.

## Cross References
- See related sections in the document for more details on configuring Grid properties and functionalities.

### RAG Annotations
<!-- tags: [DockingManager, groupingControl, grid, properties, design-time, runtime, filterbar, windows forms] keywords: [gridGroupingControl1, ShowFilterBar, Syncfusion.Windows.Forms.Grid.Grouping, TopLevelGroupOptions, FilterBar, CaptionText, Design-Time Configuration, Runtime Visualization] -->
```