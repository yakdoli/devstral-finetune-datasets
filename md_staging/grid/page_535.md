```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_535.jpeg
document_name: grid
page_number: 535
page_id: grid#page_535
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:53Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
}
}
else
{
    this.zoomWindow.Visible = false;
    MessageBox.Show("Not a record cell");
}
}
```

### [VB.NET]

```vb
Private zoomWindow As System.Windows.Forms.PictureBox

' Code to show zoom window.
Private Sub gridControl1_CellClick(ByVal sender As Object, ByVal e As GridCellClickEventArgs)
    If e.RowIndex > 0 AndAlso e.ColIndex > 0 Then
        If checkBox1.Checked Then
            If (Not zoomWindow.Visible) Then
                Me.zoomWindow.Visible = True
            End If
            Dim p1 As Point = New Point(0, 0)
            Dim s As Size = New Size(Me.gridControl1.ColWidths(e.ColIndex) + 10, Me.gridControl1.RowHeights(e.RowIndex) + 5)
            s.Width += 50
            s.Height += 30
            Dim rect As Rectangle = New Rectangle(p1, s)
            zoomWindow.Size = s

            Dim bmp As Bitmap = New Bitmap(s.Width, s.Height)
            Dim g As Graphics = Graphics.FromImage(bmp)
            Dim style As GridStyleInfo = gridControl1(e.RowIndex, e.ColIndex)
            Dim size As Single = style.Font.Size
            style.Font.Size = 15.5F
            gridControl1.DrawSingleCell(g, e.RowIndex, e.ColIndex, rect, style, True, True)
            g.Dispose()

            Me.zoomWindow.Image = bmp
            Me.zoomWindow.BorderStyle = BorderStyle.FixedSingle
            Me.zoomWindow.Visible = True
            Dim pt As Point = Me.gridControl1.ViewLayout.RowColToPoint(e.RowIndex, e.ColIndex, GridCellSizeKind.VisibleSize)
            pt.Y += 60
        End If
    End If
End Sub
```

## Cross References

See also: grid, zoomWindow, gridControl1, CellClick, MessageBox, CheckBox, DrawSingleCell, GridStyleInfo, Graphics, Bitmap, Size, Rectangle, Point.
```