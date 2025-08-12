```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_451.jpeg
document_name: tools
page_number: 451
page_id: tools#page_451
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The appearance of diagonal columns can be customized using the below code.

## Code Examples

### C#

```csharp
private void monthCalendarAdv1_DateCellQueryInfo(object sender, Syncfusion.Windows.Forms.Tools.DateCellQueryInfoEventArgs e)
{
    if (e.RowIndex == e.ColIndex)
    {
        // Creates an instance of GridStyleInfo.
        Syncfusion.Windows.Forms.Grid.GridStyleInfo gsi = e.Style;

        // Changes backcolor.
        gsi.BackColor = Color.Green;

        monthCalendarAdv1.SetInfo(e.RowIndex, e.ColIndex, gsi);
    }
}
```

### VB.NET

```vb
Private Sub monthCalendarAdv1_DateCellQueryInfo(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.DateCellQueryInfoEventArgs)

    ' Creates an instance of GridStyleInfo.
    If e.RowIndex = e.ColIndex Then
        Dim gsi As Syncfusion.Windows.Forms.Grid.GridStyleInfo = e.Style

        ' Changes backcolor.
        gsi.BackColor = Color.Green

        monthCalendarAdv1.SetInfo(e.RowIndex, e.ColIndex, gsi)
    End If

End Sub
```

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Type**: GridStyleInfo
- **Method**: SetInfo

### Parameters
- `RowIndex`: The row index of the cell to be customized.
- `ColIndex`: The column index of the cell to be customized.
- `GridStyleInfo`: The style information for the cell.

### Returns
None. This method directly modifies the grid style information for the specified cell.

### Exceptions
- Throws an exception if the `RowIndex` or `ColIndex` is out of range.

### See also
- [GridStyleInfo](https://docs.syncfusion.com/windowsforms/griddesktop/)
- [MonthCalendarAdv](https://docs.syncfusion.com/windowsforms/monthcalendaradv)

<!-- tags: [product, module, control, api, version?] keywords: [diagonal columns, custom appearance, GridStyleInfo, MonthCalendarAdv, SetInfo] -->
```