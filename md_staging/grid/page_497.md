```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_497.jpeg
document_name: grid
page_number: 497
page_id: grid#page_497
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Highlights the打印功能 of the GridPrintDocumentAdv class in the Syncfusion Windows Forms Grid.
- Demonstrates the setup and display of a print preview dialog for a grid control.
- Provides an example of configuring margins, header and footer heights, and scaling columns to fit the page.

## Content

### Advanced Printing Functionality Setup
The following code snippet demonstrates how to configure advanced printing options using the `GridPrintDocumentAdv` class.

```vb
Dim pd As Syncfusion.GridHelperClasses.GridPrintDocumentAdv = New Syncfusion.GridHelperClasses.GridPrintDocumentAdv(Me.gridControl1)
pd.DefaultPageSettings.Margins = New System.Drawing.Printing.Margins(25, 25, 25, 25)
pd.HeaderHeight = 70
pd.FooterHeight = 50
pd.ScaleColumnsToFitPage = True

Dim previewDialog As PrintPreviewDialog = New PrintPreviewDialog()
previewDialog.Document = pd
previewDialog.Show()
```

### Demonstration of Advanced Printing Functionality
The screenshot below illustrates the advanced printing functionality provided by the GridPrintDocumentAdv class.

**Figure 191: Print Grid**
The image shows a grid with the following features:
- A table containing customer orders, including columns such as OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, and ShipName.
- Grid Printing Options panel below the grid allowing the user to choose various printing settings.
- A "Print Preview" button for viewing the layout before printing.
- Options to show header and footer, and to scale columns to fit the page.

## Page Layout
The page layout includes:
- Code snippet for setting up the print document.
- Explanation and demonstration of the GridPrintDocumentAdv class functionalities.
- An illustrative screenshot showcasing the grid in a print preview mode.

<!-- tags: [Syncfusion, Windows Forms, Grid, Printing, Advanced Printing, PrintPreviewDialog, GridPrintDocumentAdv] keywords: [GridPrintDocumentAdv, PrintPreviewDialog, Syncfusion.Windows.Forms.Grid, margins, header height, footer height, scale columns] -->
```