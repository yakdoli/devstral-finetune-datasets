```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_425.jpeg
document_name: grid
page_number: 425
page_id: grid#page_425
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Private Sub button1_Click_1(ByVal sender As Object, ByVal e As EventArgs)
    Try
        Dim pd As New PivotGridPrintDocumentAdv(Me.pivotGridControl1)
        pd.DefaultPageSettings.Margins = New System.Drawing.Printing.Margins(25, 25, 25, 25)
        Dim previewDialog As New PrintPreviewDialog()
        previewDialog.Document = pd
        previewDialog.Show()
    Catch ex As Exception
        MessageBox.Show("Error while print preview" & ex.ToString())
    End Try
End Sub
```

## Overview

- The following screen shots illustrate the print feature of the PivotGrid control.
- Headers and footers can also be added by using the `DrawGridPrintHeader` and `DrawGridPrintFooter` events.
- The following code illustrates how to add the header and footer.

### Headers and Footers

In C#:

```csharp
pd.DrawGridPrintHeader += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintHeader);
pd.DrawGridPrintFooter += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintFooter);
```

In VB:

```vb
AddHandler pd.DrawGridPrintHeader, AddressOf pd_DrawGridPrintHeader
AddHandler pd.DrawGridPrintFooter, AddressOf pd_DrawGridPrintFooter
```

## Code Examples

### Adding Headers and Footers

#### C# Example

```csharp
pd.DrawGridPrintHeader += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintHeader);
pd.DrawGridPrintFooter += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintFooter);
```

#### VB Example

```vb
AddHandler pd.DrawGridPrintHeader, AddressOf pd_DrawGridPrintHeader
AddHandler pd.DrawGridPrintFooter, AddressOf pd_DrawGridPrintFooter
```

## Output

The following image shows the printed output of the pivot grid:

---

<!-- tags: [pivotgrid, print, header, footer, printpreviewdialog, gridprintdocumentadv, drawgridprintfooter, drawgridprintfooterhandler] -->
```