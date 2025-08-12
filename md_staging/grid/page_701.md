```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_701.jpeg
document_name: grid
page_number: 701
page_id: grid#page_701
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:48Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Dim val As Object = e.Value
unboundValues(key) = val
End If
End If
End Sub
```

## Content

### Customizing Unbound Cells

5. **Customize the unbound cells by handling the QueryCellStyleInfo event.**

#### C#

```csharp
this.gridGroupingControl.QueryCellStyleInfo += new Syncfusion.Windows.Forms.Grid.Grouping.GridTableCellStyleInfoEventHandler(this.gridGroupingControl_QueryCellStyleInfo);

private void gridGroupingControl_QueryCellStyleInfo(object sender, GridTableCellStyleInfoEventArgs e)
{
    if (e.TableCellIdentity.ColIndex == 3 && e.TableCellIdentity.RowIndex > 2)
    {
        if (e.TableCellIdentity.RowIndex % 4 == 0)
            e.Style.CellValue = false;
        else
            e.Style.CellValue = true;
    }
}
```

#### VB.NET

```vb
Private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As Object, ByVal e As GridTableCellStyleInfoEventArgs) Handles gridGroupingControl1.QueryCellStyleInfo
    If e.TableCellIdentity.ColIndex = 3 AndAlso e.TableCellIdentity.RowIndex > 2 Then
        If e.TableCellIdentity.RowIndex Mod 4 = 0 Then
            e.Style.CellValue = False
        Else
            e.Style.CellValue = True
        End If
    End If
End Sub
```

### Running the Sample

6. **Run the sample. Here is a sample screenshot.**

---

\_  
© 2013 Syncfusion. All rights reserved.  
701 | Page

<!-- tags: [grid, windows-forms, unbound-cells, querycellstyleinfo-event] keywords: [customization, unbound cells, cell styling, essential grid, sample screenshot] -->
```