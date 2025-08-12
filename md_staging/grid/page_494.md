```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_494.jpeg
document_name: grid
page_number: 494
page_id: grid#page_494
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:06Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates handling print preview and printing for a `gridControl` using Syncfusion's GridPrintDocument.
- Provides two example methods: `PrintPreview_Click` and `Print_Click`.

## Content

### Print Preview and Print Handling
Here are the code examples for handling print preview and printing in C# using Syncfusion's GridPrintDocument.

```csharp
// PrintPreview button handler.
private void PrintPreview_Click(object sender, System.EventArgs e)
{
    if (this.gridControl1 != null)
    {
        try
        {
            // Uses the default printer.
            GridPrintDocument pd = new GridPrintDocument(this.gridControl1, true);
            PrintPreviewDialog dlg = new PrintPreviewDialog();
            dlg.Document = pd;
            dlg.ShowDialog();
        }
        catch (Exception ex)
        {
            MessageBox.Show("An error occurred attempting to preview the grid - " + ex.Message);
        }
    }
}

private void Print_Click(object sender, System.EventArgs e)
{
    if (this.gridControl1 != null)
    {
        try
        {
            GridPrintDocument pd = new GridPrintDocument(this.gridControl1, true);
            PrintDialog dlg = new PrintDialog();
            dlg.Document = pd;
            if (dlg.ShowDialog() == DialogResult.OK)
                pd.Print();
        }
        catch (Exception ex)
        {
            MessageBox.Show("An error occurred attempting to print the grid - " + ex.Message);
        }
    }
}
```

### Explanation of Code
- **`PrintPreview_Click`**:
  - This method is triggered when the user clicks the print preview button.
  - It creates a `GridPrintDocument` object for the `gridControl1`, indicating the use of a printer.
  - A `PrintPreviewDialog` is displayed, allowing the user to preview the printed output.
  
- **`Print_Click`**:
  - This method is triggered when the user clicks the print button.
  - It also creates a `GridPrintDocument` object for the `gridControl1`.
  - A `PrintDialog` is displayed to allow the user to configure and initiate the printing process.
  - If the user confirms the print action, the `Print` method of the `GridPrintDocument` is called to execute the printing.

### Using VB.NET
The next section will continue with examples of how to implement similar functionalities using VB.NET.

## API Reference
- `GridPrintDocument`: Represents the print document for the grid.
- `PrintPreviewDialog`: Provides a dialog box for previewing the print output.
- `PrintDialog`: Provides a dialog box for configuring and executing print jobs.
- `DialogResult.OK`: Enum value indicating the user has confirmed the action.

## Code Examples
The examples in this section demonstrate how to handle print preview and printing functionality for a grid control.

## References
- Syncfusion.grid.winframework.printing
- System.Windows.Forms.PrintDocument, PrintPreviewDialog, PrintDialog

<!-- tags: [syncfusion-sdk, windowsforms, grid, printing, preview] keywords: [gridControl, GridPrintDocument, PrintPreviewDialog, PrintDialog, print, preview, C#] -->
```
