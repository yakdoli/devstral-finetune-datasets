```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: PivotGrid
page_number: 039
page_id: PivotGrid#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:07Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Content

### Printing Overview

Here are some code examples for configuring print settings and handling print previews in a `PivotGrid` control:

#### C#

```csharp
pd.DefaultPageSettings.Margins = new
System.Drawing.Printing.Margins(25, 25, 25, 25);
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

#### VB

```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)

Try

Dim pd As New PivotGridPrintDocumentAdv(Me.pivotGridControl1)

pd.DefaultPageSettings.Margins = New
System.Drawing.Printing.Margins(25, 25, 25, 25)
Dim previewDialog As New PrintPreviewDialog()
previewDialog.Document = pd
previewDialog.Show()

Catch ex As Exception
MessageBox.Show("Error while print preview" & ex.ToString())

End Try

End Sub
```

#### Headers and Footers

Headers and footers can also be added by using the `DrawGridPrintHeader` and `DrawGridPrintFooter` events. The following code illustrates how to add the header and footer:

#### C#

```csharp
pd.DrawGridPrintHeader += new
GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintHeader);
```

## API Reference

### Methods and Events

- `DefaultPageSettings.Margins`: Configures page margins for printing.
- `PrintPreviewDialog`: A dialog for previewing the printed content.
- `PivotGridPrintDocumentAdv`: A document class for handling PivotGrid printing.
- `DrawGridPrintHeader`: Event to draw a custom header for printed content.
- `DrawGridPrintFooter`: Event to draw a custom footer for printed content.

## Code Examples

The provided examples demonstrate how to set up print settings, handle errors in the print preview process, and customize headers and footers for printed output.

---

<!-- tags: [syncfusion, windowsforms, pivotgrid, printing, header, footer, exceptions] keywords: [margins, printpreviewdialog, drawgridprintheader, drawgridprintfooter, errors, customization] -->
```