```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_493.jpeg
document_name: grid
page_number: 493
page_id: grid#page_493
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:05Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

- Add a handler for `CurrentCellDeactivated` to refresh the old row to remove its bold font.
- Add a handler for `CurrentCellActivated` to refresh the new current row to add its bold font.
- Add a handler for `PrepareViewStyleInfo` to conditionally change the bold style of the font if the requested cell is on the current row.

To see a full working sample, check the HighlightCurrent sample that ships with Essential Grid. Notice that the work is done just by making the grid refresh (redraw) a row. During this refresh, the `PrepareViewStyleInfo` is selected and the style is modified to be bold if the row is current. This means that no bold style information is saved anywhere. The `GridStyleInfo` object is just temporarily modified immediately before it is used in the drawing.

## 4.1.4.20 Print Preview and Printing

Essential Grid directly supports printing and print previews through the .NET Framework classes `Systems.Windows.Forms.PrintPreviewDialog` and `Systems.Windows.Forms.PrintDialog`. A derived `PrintDocument`, `GridPrintDocument`, is passed to these classes. This `GridPrintDocument` implements the printing logic that is needed to print multi-page grids.

Following code example illustrates how to enable print previewing.

1. Using C#
```csharp
// Load the Essential Grid document or grid data here.

// Create a PrintPreviewDialog instance
PrintPreviewDialog printPreviewDialog = new PrintPreviewDialog();
printPreviewDialog.Document = new GridPrintDocument();

// Show the Print Preview Dialog
printPreviewDialog.ShowDialog();
```
## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

<!-- tags: Windows Forms, Grid, PrintPreview, PrintDialog, GridPrintDocument, Multi-page printing, GridStyleInfo, CurrentCellActivated, CurrentCellDeactivated, PrepareViewStyleInfo, HighlightCurrent sample -->
``` 
```