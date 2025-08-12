```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_424.jpeg
document_name: grid
page_number: 424
page_id: grid#page_424
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

- **MultipleString**: This specifies the text that should appear when the Multiple Filter selected in the Filter Combo Box is changed. By default, it will be set to **Multiple**.

```csharp
pivotGridControl1.MultipleString = "Multiple";
```

### Print Option

The print option is extended for the PivotGrid control to allow users to preview the contents before they are printed on paper.

This feature is used to print the PivotGrid control in landscape and portrait views. This feature has overridden the `GridPrintDocumentAdv` from `Syncfusion.GridHelperClasses.Windows`.

The pivot grid visual style color is automatically applied in the printed document based on the visual styles of the grid.

The print functionality can be invoked using the following code:

```csharp
[C#]
private void buttonl_Click_l(object sender, EventArgs e)
{
    try
    {
        PivotGridPrintDocumentAdv pd = new PivotGridPrintDocumentAdv(this.pivotGridControl1);

        pd.DefaultPageSettings.Margins = new System.Drawing.Printing.Margins(25, 25, 25, 25);
        PrintPreviewDialog previewDialog = new PrintPreviewDialog();
        previewDialog.Document = pd;
        previewDialog.Show();
    }
    catch (Exception ex)
    {
        MessageBox.Show("Error while print preview" + ex.ToString());
    }
}
```

```vb
[VB]
```
```html
 <!-- tags: [Syncfusion Winforms, grid, multiple filter, print option, pivotgrid control, Syncfusion, GridHelperClasses, Windows] keywords: [MultipleString, Filter Combo Box, PivotGrid, PrintDocumentAdv, PrintPreviewDialog, Visual Style, PageSettings, Margins, Print Preview] -->
```