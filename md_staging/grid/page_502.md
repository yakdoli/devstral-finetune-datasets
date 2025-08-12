```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_502.jpeg
document_name: grid
page_number: 502
page_id: grid#page_502
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
printDialog.ShowDialog();
```

```vb
[VB]

Dim ctrls As New List(Of Control)()
Dim gridsToPrint As New List(Of Control)()
For Each cd As Control In Me.Controls
    If TypeOf cd Is Control Then
        gridsToPrint.Add(CType(cd, Control))
    End If
Next cd
Dim pd As New MultiGridPrintDocument(gridsToPrint)
pd.GridPrintOption = MultiGridPrintDocument.GridPrintOptions.MultipleGridPrint
pd.ShowHeaderFooterOnAllPages = True
Dim printDialog As New PrintPreviewDialog()
printDialog.Document = pd
printDialog.ShowDialog()
```

## Overview
- Demonstrates advanced printing functionality provided by the `MultiGridPrintDocument` class.
- Provides a complete VB implementation for printing multiple grids.

## Content

The following screen shot illustrates the advanced printing functionality provided by the `MultipleGridPrintDocument` class:

![Advanced Printing Functionality](#)

The screenshot shows a two-grid configuration where:
- **Grid 1** contains columns such as `OrderID`, `CustomerID`, `EmployeeID`, and `OrderDate`.
- **Grid 2** contains columns like `Contact Name`, `Company Name`, and others.
- The grid printing options are visible at the bottom, including settings for MultiGridPrint, Show Header and Footer, and Print Preview.

### Printing Controls
- **MultiGridPrint**: A checkbox option to enable printing of multiple grids together.
- **PrintGridInNewPage**: Option to print each grid on a new page.
- **DefaultGridPrint**: An alternative setting for default grid printing.
- **ScaleColumnToFit**: Adjusts column widths for optimal printing.
- **Show Header and Footer**: Displays headers and footers on all pages.
- **Print Preview**: Displays the layout before printing.
- **Print Options**: Selects MultiGridPrint or CustomizePrintPage for specific requirements.

### Footer
© 2013 Syncfusion. All rights reserved.  
Page 502

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: MultiGridPrintDocument
- **Methods and Properties**:
  - `GridPrintOption`: Specifies the printing options.
  - `ShowHeaderFooterOnAllPages`: Boolean property to display headers and footers.
  - `Document`: Sets the content to be printed.

## Code Examples

### VB Example
```vb
Dim ctrls As New List(Of Control)()
Dim gridsToPrint As New List(Of Control)()
For Each cd As Control In Me.Controls
    If TypeOf cd Is Control Then
        gridsToPrint.Add(CType(cd, Control))
    End If
Next cd
Dim pd As New MultiGridPrintDocument(gridsToPrint)
pd.GridPrintOption = MultiGridPrintDocument.GridPrintOptions.MultipleGridPrint
pd.ShowHeaderFooterOnAllPages = True
Dim printDialog As New PrintPreviewDialog()
printDialog.Document = pd
printDialog.ShowDialog()
```

## Cross References
- Refer to the main documentation for additional details on grid printing features and customization options.

<!-- tags: [winforms, essential grid, printing, multi-grid] keywords: [MultiGridPrintDocument, GridPrintOption, Syncfusion.Windows.Forms.Grid, advanced printing functionality, ShowHeaderFooterOnAllPages] -->
```