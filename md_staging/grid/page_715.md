```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_715.jpeg
document_name: grid
page_number: 715
page_id: grid#page_715
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
e.Style.TextColor = Color.White;
e.Style.Themed = false;
}
// Setting color to the remaining part.
else
e.Style.BackColor = Color.YellowGreen;
}
```

### VB.NET

```vb
Private Sub ParentTable_PrepareViewStyleInfo(ByVal sender As Object,
ByVal e As GridPrepareViewStyleInfoEventArgs)

    ' Setting color to the text displaying the table name.
    If e.ColIndex = 2 AndAlso e.RowIndex = 2 Then
        e.Style.Text = "ParentTable"
        e.Style.Font.Bold = True
        e.Style.BackColor = Color.YellowGreen
        e.Style.TextColor = Color.Blue
        e.Style.CellType = "Static"
        e.Style.HorizontalAlignment = GridHorizontalAlignment.Left
        e.Style.Enabled = False

    ' Setting color to the drop area.
    ElseIf e.Style.Text.StartsWith("Drag a") Then
        e.Style.Text = "Drag and Drop Parent Table Column headers"
        e.Style.BackColor = Color.White

    ' Setting color to the dropped columns.
    ElseIf e.Style.Text.StartsWith("Par") Then
        e.Style.BackColor = Color.Tomato
        e.Style.Themed = False

    ' Setting color to the remaining part.
    Else
        e.Style.BackColor = Color.YellowGreen
    End If
End Sub

Private Sub ChildTable_PrepareViewStyleInfo(ByVal sender As Object,
ByVal e As GridPrepareViewStyleInfoEventArgs)

    ' Setting color to the text displaying the table name.
    If e.ColIndex = 2 AndAlso e.RowIndex = 2 Then
        e.Style.Text = "ChildTable "
        e.Style.Font.Bold = True
```

<!-- tags: [Windows Forms, Essential Grid, Color, Interactions, Documentation] keywords: [ParentTable, ChildTable, GridPrepareViewStyleInfoEventArgs, TableStyling, DragDrop, ColorStyling, TableHeaders, MultiLangDocumentation] -->
```