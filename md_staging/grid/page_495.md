```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_495.jpeg
document_name: grid
page_number: 495
page_id: grid#page_495
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:24Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Example: Handling Print Preview and Print

The following VB.NET code demonstrates how to handle print preview and print functionalities for an Essential Grid control.

#### Print Preview Handler

```vb
Private Sub PrintPreview_Click(ByVal sender As Object, ByVal e As EventArgs)
    If (Not (gridControl1) Is Nothing) Then
        Try
            Dim pd As GridPrintDocument
            pd = New GridPrintDocument(gridControl1, True)

            ' Uses the default printer.
            Dim dlg As PrintPreviewDialog
            dlg = New PrintPreviewDialog()
            dlg.Document = pd
            dlg.ShowDialog()
        Catch ex As Exception
            MessageBox.Show("An error occurred attempting to preview the grid - " + ex.Message)
        End Try
    End If
End Sub
```

#### Print Handler

```vb
Private Sub Print_Click(ByVal sender As Object, ByVal e As EventArgs)
    If (Not (gridControl1) Is Nothing) Then
        Try
            Dim pd As GridPrintDocument
            pd = New GridPrintDocument(gridControl1, True)

            ' Uses the default printer.
            Dim dlg As PrintDialog
            dlg = New PrintDialog()
            dlg.Document = pd
            If dlg.ShowDialog() = DialogResult.OK Then
                pd.Print()
            End If
        Catch ex As Exception
            MessageBox.Show("An error occurred attempting to print the grid - " + ex.Message)
        End Try
    End If
End Sub
```

---

## Page-level Navigation/TOC (if applicable)

- **Print Preview Handler**
- **Print Handler**

---

## Cross References

See also:
- Related documentation on Essential Grid for Windows Forms.
- Details on `GridPrintDocument` and printing functionalities.

---

<!-- tags: [windows-forms, essential-grid, printing] keywords: [print-preview, print-dialog, grid-control] -->
```