```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_499.jpeg
document_name: grid
page_number: 499
page_id: grid#page_499
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:36Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to print an entire grid to fit a single page using the `GridPrintDocument` class.
- Demonstrates the Print To Fit functionality with code examples in C# and VB.NET.

## Content

### Print To Fit

An entire grid can be printed on a single page by deriving the `GridPrintDocument` class to handle the printing of the entire grid on a single page. The class achieves this by drawing the full-size grid to a large bitmap and then scaling the same to fit the output page. The following code example illustrates this.

#### C# Code Example

```csharp
GridPrintToFitDocument pd = new GridPrintToFitDocument(this.gridControl1, true);
PrintDialog dlg = new PrintDialog();
dlg.Document = pd;
if (dlg.ShowDialog() == DialogResult.OK)
    pd.Print();
```

#### VB.NET Code Example

```vb.net
Dim dlg As PrintDialog = New PrintDialog()
dlg.Document = pd
If dlg.ShowDialog() = DialogResult.OK Then
    pd.Print()
End If
```

Following screen shot illustrates the Grid's **Print To Fit** feature.

## API Reference

### GridPrintToFitDocument
- **Constructor**: `GridPrintToFitDocument(GridControl, Boolean)`
  - Parameters:
    - `GridControl`: The grid control to be printed.
    - `Boolean`: A flag indicating whether to fit the grid to a single page.

## Code Examples

### Print To Fit

The examples above demonstrate how to use the `GridPrintToFitDocument` class to print the grid to fit a single page. The class handles the scaling and drawing of the grid to ensure it fits on the printed page without distortion.

## Cross References

- **Show Page Layout Check Box**: The functionality mentioned above can also be achieved on UI by selecting the Show Page Layout check box on the UI, which allows the user to view the page layout.

<!-- tags: [Essential Grid, Windows Forms, Print, Print To Fit, GridPrintDocument] keywords: [Print, Scale, Bitmap, GridControl, Show Page Layout, UI, Page Layout] -->
```