```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_890.jpeg
document_name: grid
page_number: 890
page_id: grid#page_890
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:11Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Grid Properties

| Property          | Description                                                             |
|-------------------|---------------------------------------------------------------------------|
| ShowTreeLines     | Indicates whether the PlusMinus cells are shown connected with lines.     |
| SummaryRowHeight  | Height in pixels of the summary rows. The value -1 is a special setting to indicate that the summary row height should always be the same as the RecordRowHeight. |
| TreeLineBorder    | Controls the style of the line that is used to draw the tree lines.      |

### Preview and Property Settings

In the Preview, try various property settings to see their effect on the display. Below is a sample of what you might see. The properties changed here are CaptionRowHeight, ColumnHeaderRowHeight, GridLineBorder, GridVisualStyles, ListBoxSelectionMode, SelectionBackColor, SelectionTextColor, and ShowTreeLines.

## API Reference

- **CaptionRowHeight**: Sets the height of the caption row in pixels.
- **ColumnHeaderRowHeight**: Sets the height of the column header row in pixels.
- **GridLineBorder**: Controls the style of the grid lines.
- **GridVisualStyles**: Defines the visual appearance of the grid.
- **ListBoxSelectionMode**: Specifies the selection mode for list boxes.
- **SelectionBackColor**: Sets the background color of the selected cells.
- **SelectionTextColor**: Sets the text color of the selected cells.
- **ShowTreeLines**: Indicates whether the tree lines are displayed.

## Code Examples

```csharp
// Example: Changing the SummaryRowHeight property
grid1.SummaryRowHeight = 20;

// Example: Setting the TreeLineBorder style
grid1.TreeLineBorder = System.Drawing.Drawing2D.DashStyle.Dash;
```

<!-- tags: [grid, windows forms, essential grid, properties, visual styles, selection mode, tree lines, summary row height] keywords: [caption row height, column header row height, grid line border, selection back color, selection text color, show tree lines] -->
```