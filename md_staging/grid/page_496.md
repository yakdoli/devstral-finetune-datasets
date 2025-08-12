```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_496.jpeg
document_name: grid
page_number: 496
page_id: grid#page_496
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:17Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Grid Helper Features

The following are the features of the **Grid Helper** that supports print preview and printing:

- Advanced printing
- Page layout
- Print Column To Fit

### Advanced Printing

Multiple grids can be printed across various pages using the helper class **GridPrintDocumentAdv**. This is achieved by drawing the full size grid to a large bitmap and then scaling this bitmap to fit the output page.

- The Print Preview can be enabled by using **GridPrintDocumentAdv** class or by clicking the Print Preview button under the **Grid Printing Options** in the UI.
- Columns can be specified to fit in a single page using the **ScaleColumnsToFitPage** property or selecting the **Scale Columns To Fit** check box on under the **Grid Printing Options** in the UI.
- Headers and footers can be added by using the **DrawGridPrintHeader** and **DrawGridPrintFooter** events or by selecting the **Show Header and Footer** check box under the **Grid Printing Options** in the UI.

#### Following code example illustrates Advanced Printing in Grid.

1. **Using C#**

```csharp
[C#]

Syncfusion.GridHelperClasses.GridPrintDocumentAdv pd = new 
Syncfusion.GridHelperClasses.GridPrintDocumentAdv(this.gridControl1);
pd.DefaultPageSettings.Margins = new 
System.Drawing.Printing.Margins(25, 25, 25, 25);
pd.HeaderHeight = 70;
pd.FooterHeight = 50;

pd.ScaleColumnsToFitPage = true;

PrintPreviewDialog previewDialog = new PrintPreviewDialog();
previewDialog.Document = pd;
previewDialog.Show();
```

2. **Using VB.NET**

```vb
[VB.NET]
```

<!-- tags: [print, grid_helper, page_layout, advanced_printing, grid_printing_options, grid_printdocumentadv] keywords: [print preview, scale_columns_to_fit_page, drawgridprintheader, drawgridprintfooter, show_header_and_footer, grid control] -->
```