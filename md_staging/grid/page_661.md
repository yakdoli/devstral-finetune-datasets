```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_661.jpeg
document_name: grid
page_number: 661
page_id: grid#page_661
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
// The color of these cells depends on value of cell 1. If engines ListChanged handler
// detects a change to column 1, it should also automatically repaint the dependant columns.
for (int i = 2; i <= 20; i++) {
    gridGroupingControl1.TableDescriptor.Fields[i.ToString()].ReferencedFields = "1";
}
```

### VB.NET
```vb
Private colors As Color() = New Color() {Color.FromArgb(&H85, &HBF, &H75), Color.FromArgb(&HB4, &HE7, &HF2), Color.FromArgb(&HFF, &HBF, &H34), Color.FromArgb(&H82, &H2E, &H1B), Color.FromArgb(&H3A, &H86, &H7E)}

Private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As Object, ByVal e As GridTableCellStyleInfoEventArgs)
    Dim style As GridTableCellStyleInfo = CType(e.Style, GridTableCellStyleInfo)
    If e.TableCellIdentity.TableCellType = GridTableCellType.RecordFieldCell OrElse e.TableCellIdentity.TableCellType = GridTableCellType.AlternateRecordFieldCell Then
        If e.TableCellIdentity.Column.FieldDescriptor.FieldPropertyType Is GetType(String) Then
            Return
        End If

        ' Get the value from column 1 and color all cells in record based on this value.
        Dim r As Record = e.Style.TableCellIdentity.DisplayElement.GetRecord()
        Dim value As Object = r.GetValue("1")
        Dim v As Integer = Convert.ToInt32(value) Mod colors.Length
        e.Style.BackColor = colors(v)
    End If
End Sub
```

## Copyright Notice
© 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, grid, Essential Grid, ListChanged handler, QueryCellStyleInfo, field descriptors] keywords: [color based on cell value, record field cell, alternate record field cell, repaint, dependant columns] -->
```