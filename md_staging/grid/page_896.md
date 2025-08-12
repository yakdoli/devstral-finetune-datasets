```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_896.jpeg
document_name: grid
page_number: 896
page_id: grid#page_896
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:43Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to configure and use the `ShowStackedHeaders` property in the Essential Grid for Windows Forms.
- Highlights the functionality of stacked headers in the grouping grid.
- Demonstrates the result of setting the `ShowStackedHeaders` property to `True`.

## Content

### Grid Properties Configuration

The following image depicts the configuration of properties for the `gridGroupingControl1` in the Syncfusion Windows Forms Grid Grouping component:

```markdown
- **SummaryRows**
- **TableOptions**
- **TopLevelGroupOptions**
  - **CaptionSummaryRow**
    - **CaptionText**: `{TableName}: {RecordCount};`
    - **IsExpandedInitialValue**: `True`
    - **RepaintCaptionWhenItemsChange**: `True`
    - **ShowAddNewRecordAfterDetails**: `False`
    - **ShowAddNewRecordBeforeDetails**: `True`
    - **ShowCaption**: `True`
    - **ShowCaptionPlusMinus**: `False`
    - **ShowCaptionSummaryCells**: `False`
    - **ShowColumnHeaders**: `True`
    - **ShowEmptyGroups**: `False`
    - **ShowFilterBar**: `False`
    - **ShowGroupFooter**: `False`
    - **ShowGroupHeader**: `False`
    - **ShowGroupIndentAsCovered**: `False`
    - **ShowGroupPreview**: `False`
    - **ShowGroupSummaryWhenColumnFiltered**: `False`
    - **ShowStackedHeaders**: `True`
    - **ShowSummaries**: `True`
    - **SummaryRowPlacement**: `AfterDetails`
    - **WeakReferenceChangedList`: `(Collection)`
```

#### Key Property: ShowStackedHeaders

The `ShowStackedHeaders` property is set to `True`. This configuration allows the grouping grid to have stacked header rows, where the column headers can be manipulated by drag-and-drop actions. The screenshot also demonstrates the effect of rearranging the stacked headers on the visibility and order of the columns.

**Figure 354: Setting ShowStackedHeaders property to True**

### Output

Here are the screenshots showing the Grouping Grid with two Stacked Header Rows. It illustrates the effect of doing Drag / Drop on StackedHeaders. You could notice that the order of the Visible columns gets affected automatically while rearranging the StackedHeaders.

- **Description**: The images show the impact of rearranging stacked headers, highlighting how the order of visible columns is dynamically updated during header manipulation.
- **Functionality**: The drag-and-drop feature allows for easy reordering and rearrangement of headers, providing flexibility in data presentation.

## API Reference

### Properties

- **ShowStackedHeaders**
  - **Type**: Boolean
  - **Description**: Indicates whether the column headers are visible in stacked format.
  - **Default**: `False`
  
### Methods/Events
No additional methods or events are demonstrated in the current context.

## Code Examples

This section likely requires a code example illustrating how to programmatically set the `ShowStackedHeaders` property to `True` and interact with stacked headers, but such code is not explicitly included in the provided screenshot or text.

## Page-level Navigation/TOC (if applicable)
None

## Cross References
- Refer to **Syncfusion.Windows.Forms.Grid.Grouping.G** for more information on grid grouping options and properties.

### RAG Annotations
<!-- tags: [WinForms, Grid, Grouping, StackedHeaders, DragDrop, EssentialGrid] keywords: [ShowStackedHeaders, gridGroupingControl1, SummaryRows, CaptionSummaryRow, ColumnHeaders, DragAndDrop] -->
```
