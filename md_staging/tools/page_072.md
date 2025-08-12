```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: tools
page_number: 072
page_id: tools#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles top.Click, right.Click, left.Click, bottom.Click, float_btn.Click
    Dim btn As Button = sender
    ' Dock to the Top
    If btn Is Me.top Then
        Me.commandBar1.DockState = CommandBarDockState.Top
    End If
    ' Dock to the Bottom
    If btn Is Me.bottom Then
        Me.commandBar1.DockState = CommandBarDockState.Bottom
    End If
    ' Dock to the Right
    If btn Is Me.right Then
        Me.commandBar1.DockState = CommandBarDockState.Right
    End If
    ' Dock to the Left
    If btn Is Me.left Then
        Me.commandBar1.DockState = CommandBarDockState.Left
    End If
    ' Dock as Floating
    If btn Is Me.float_btn Then
        Me.commandBar1.DockState = CommandBarDockState.Float
    End If
End Sub
```

## Output

The following figure shows the CommandBar docked to the right border of the Form.

![CommandBar Sample Image](https://via.placeholder.com/300x200?text=CommandBar+Sample+Image)

<!-- tags: essential-tools, windows-forms, commandbar, docking, syncfusion-sdk, windowsforms, 11.4.0.26 keywords: essentialtools, windowsforms, commandbar, docking, winforms, syncfusion, 11.4.0.26 -->
```