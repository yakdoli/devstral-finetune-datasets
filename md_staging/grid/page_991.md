```html
<!-- source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_991.jpeg
document_name: grid
page_number: 991
page_id: grid#page_991
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## C#

```csharp
Syncfusion.GridHelperClasses.GridPrintDocumentAdv pd = new
Syncfusion.GridHelperClasses.GridPrintDocumentAdv(this.gridGroupingControl.TableControl);
pd.DefaultPageSettings.Margins = new
System.Drawing.Printing.Margins(25, 25, 25, 25);

// Set header and footer height.
pd.HeaderHeight = 70;
pd.FooterHeight = 50;

// Scale columns to fit page.
pd.ScaleColumnsToFitPage = true;

// Handle the following events to draw the header/footer.
pd.DrawGridPrintHeader += new
Syncfusion.GridHelperClasses.GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintHeader);
pd.DrawGridPrintFooter += new
Syncfusion.GridHelperClasses.GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintFooter);
pd = new
GridPrintDocument(this.gridGroupingControl.TableControl);
PrintDialog printDialog = new PrintDialog();
printDialog.Document = pd;
pd.DefaultPageSettings.Landscape = true;
if (printDialog.ShowDialog() == DialogResult.OK)
pd.Print();
```

## VB.NET

```vb
Dim pd As Syncfusion.GridHelperClasses.GridPrintDocumentAdv = New
Syncfusion.GridHelperClasses.GridPrintDocumentAdv(Me.gridGroupingControl.TableControl)
pd.DefaultPageSettings.Margins = New
System.Drawing.Printing.Margins(25, 25, 25, 25)

' Set header and footer height.
pd.HeaderHeight = 70
pd.FooterHeight = 50

' Scale columns to fit page.
pd.ScaleColumnsToFitPage = True

' Handle the following events to draw the header/footer.
AddHandler pd.DrawGridPrintHeader, AddressOf pd_DrawGridPrintHeader
AddHandler pd.DrawGridPrintFooter, AddressOf pd_DrawGridPrintFooter
```

<!-- tags: [Syncfusion Winforms, Grid, Print, Header, Footer] keywords: [C#, VB.NET, GridPrintDocumentAdv, DrawGridPrintHeader, DrawGridPrintFooter, PrintDialog] -->
```