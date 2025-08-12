```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_987.jpeg
document_name: grid
page_number: 987
page_id: grid#page_987
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section discusses the navigation bar and navigation bar tooltips enabled for the Grid Grouping Control.
- Explains how printing and print previews are supported in the Grid Grouping control using .NET Framework classes and a derived `GridPrintDocument`.
- Provides code examples for launching a Print Preview dialog box.

## Content

### Navigation Bar and Navigation Bar Tooltip

![Figure: Navigation Bar and Navigation Bar ToolTip enabled for the Grid Grouping Control](#)

**Figure 382: Navigation Bar and Navigation Bar ToolTip enabled for the Grid Grouping Control**

### 4.3.4.12 Print and Print Preview

Grid Grouping control supports printing and printing previews through the .NET Framework classes `System.Windows.Forms.PrintPreviewDialog` and `System.Windows.Forms.PrintDialog`. A derived `GridPrintDocument` which represents the print document is passed to these classes. This `GridPrintDocument` implements the printing logic that is needed to print multipage grids.

#### Code for Print Preview Dialog Box

**C#**

```csharp
GridPrintDocument pd = new GridPrintDocument(this.gridGroupingControl1.TableControl, true);
PrintPreviewDialog ppv = new PrintPreviewDialog();
ppv.Document = pd;
ppv.DefaultPageSettings.Landscape = true;
ppv.ShowDialog();
```

**VB.NET**

```vb
Dim pd As New GridPrintDocument(Me.gridGroupingControl1.TableControl, True)
Dim ppv As New PrintPreviewDialog()
ppv.Document = pd
```

## API Reference

### GridPrintDocument
- Implements the logic for printing multipage grids.
- Constructor: `GridPrintDocument(TableControl, bool)`
  - Parameters:
    - `TableControl`: The table control to be printed.
    - `bool`: A boolean flag, typically for formatting or settings.

### PrintPreviewDialog
- Used to display a preview dialog for the print document.
- Property: `Document`
  - Sets the `GridPrintDocument` instance for the dialog.
- Method: `ShowDialog()`
  - Displays the print preview dialog box.

### PrintDocument
- Ultimately responsible for the printing process.
- Property: `DefaultPageSettings`
  - Can be used to set default settings such as landscape orientation.

## Code Examples ( Provided in the section above )

## Page-level Navigation/TOC
- **4.3.4.12 Print and Print Preview**
  - Code for Print Preview Dialog Box (C# & VB.NET)

## Cross References
- Refer to the main description for Grid Grouping Control for more details on its functionality.
- Check related sections for additional information on printing and document handling.

<!-- tags: [grid, windows forms, printing, print preview, dialog box, grid grouping control, navigation bar, tooltip, multipage grids] keywords: [navigation bar, print preview, GridPrintDocument, PrintPreviewDialog, PrintDialog, Grid Grouping Control, navigation tooltips] -->
```