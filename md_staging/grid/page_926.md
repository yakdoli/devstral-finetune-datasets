```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_926.jpeg
document_name: grid
page_number: 926
page_id: grid#page_926
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

```csharp
e.Style.Font.Bold = true;
}
}
// Code for Row and Column.
else if (radioButton5.Checked)
{
    // Highlight the current row and column with SystemColors.Highlight and Bold font.
    if (e.RowIndex > grid.Model.Rows.HeaderCount && e.ColIndex > grid.Model.Cols.HeaderCount
        && (cc.RowIndex == e.RowIndex || cc.ColIndex == e.ColIndex))
    {
        e.Style.Interior = new BrushInfo(SystemColors.Highlight);
        e.Style.Font.Bold = true;
    }
}
```

### VB.NET

#### Handler for View Style Info
```vb
AddHandler gridGroupingControl1.TableControl.PrepareViewStyleInfo, AddressOf TableControl_PrepareViewStyleInfo

Private Sub TableControl_PrepareViewStyleInfo(ByVal sender As Object, ByVal e As GridPrepareViewStyleInfoEventArgs)
    Dim cc As GridCurrentCell = gridGroupingControl1.TableControl.CurrentCell
    Dim grid As GridControlBase = Me.gridGroupingControl1.TableControl.CurrentCell.Grid

    ' Code for RowOnly.
    If radioButton3.Checked Then

        ' Highlight the current row with SystemColors.Highlight and Bold font.
        If e.RowIndex > grid.Model.Rows.HeaderCount And e.ColIndex > grid.Model.Cols.HeaderCount AndAlso
            cc.HasCurrentCellAt(e.RowIndex) Then
            e.Style.Interior = New BrushInfo(SystemColors.Highlight)
            e.Style.TextColor = SystemColors.HighlightText
            e.Style.Font.Bold = True
        End If
    End If

    ' Code for CellOnly.
    ElseIf radioButton2.Checked Then
```

## API Reference

- `grid.Model.Rows.HeaderCount`
- `grid.Model.Cols.HeaderText`
- `grid.Model.Cols.CharIndex`
- `grid.HasCurrentCellAt(e.RowIndex)`
- `e.Style.Interior`
- `e.Style.Font.Bold`
- `e.Style.TextColor`

## Code Examples

### C#

```csharp
e.Style.Font.Bold = true;
}
}
// Code for Row and Column.
else if (radioButton5.Checked)
{
    // Highlight the current row and column with SystemColors.Highlight and Bold font.
    if (e.RowIndex > grid.Model.Rows.HeaderCount && e.ColIndex > grid.Model.Cols.HeaderCount
        && (cc.RowIndex == e.RowIndex || cc.ColIndex == e.ColIndex))
    {
        e.Style.Interior = new BrushInfo(SystemColors.Highlight);
        e.Style.Font.Bold = true;
    }
}
```

### VB.NET

#### Handler for View Style Info
```vb
AddHandler gridGroupingControl1.TableControl.PrepareViewStyleInfo, AddressOf TableControl_PrepareViewStyleInfo

Private Sub TableControl_PrepareViewStyleInfo(ByVal sender As Object, ByVal e As GridPrepareViewStyleInfoEventArgs)
    Dim cc As GridCurrentCell = gridGroupingControl1.TableControl.CurrentCell
    Dim grid As GridControlBase = Me.gridGroupingControl1.TableControl.CurrentCell.Grid

    ' Code for RowOnly.
    If radioButton3.Checked Then

        ' Highlight the current row with SystemColors.Highlight and Bold font.
        If e.RowIndex > grid.Model.Rows.HeaderCount And e.ColIndex > grid.Model.Cols.HeaderCount AndAlso
            cc.HasCurrentCellAt(e.RowIndex) Then
            e.Style.Interior = New BrushInfo(SystemColors.Highlight)
            e.Style.TextColor = SystemColors.HighlightText
            e.Style.Font.Bold = True
        End If
    End If

    ' Code for CellOnly.
    ElseIf radioButton2.Checked Then
```

<!-- tags: [Essential Grid, Windows Forms, Row Column Highlighting, GridControlBase, GridPrepareViewStyleInfoEventArgs, Style Properties] keywords: [HighlightFont, RowIndex, ColIndex, SystemColors.Highlight, Bold Font, Visual Studio, C#, VB.NET] -->
```