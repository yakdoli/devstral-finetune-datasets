```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: tools
page_number: 117
page_id: tools#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:31:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
ElseIf (arg.CommandBarResizeType = Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Bottom) OrElse
    (arg.CommandBarResizeType = Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Top) Then
    Dim nfactor As Integer = CInt(Math.Floor(CSng(szcurrent.Height) / CSng(szbtn.Height)))
    Dim ffactor As Single = CSng(szcurrent.Height) / CSng(szbtn.Height)

    If szcurrent.Height > szmaxwrap.Height Then
        arg.ClientSize = szmaxwrap
    ElseIf (nfactor > 1) AndAlso (nfactor = ffactor) Then
        ' The toolbar width is estimated to be equal to the button width + the
        ' number of button columns required.
        Dim nnewwidth As Integer = CInt(Math.Ceiling(CSng(nbtncount) / CSng(nfactor))) * szbtn.Width

        Dim sznew As Size = Size.Empty
        If nnewwidth > szmaxwrap.Width Then
            ' Assign the new width to the toolbar parent panel and get the
            ' corresponding
            ' toolbar height.
            sznew.Width = nnewwidth
            ToolBar.Parent.Width = sznew.Width
            sznew.Height = ToolBar.Height
            ToolBar.Parent.Width = sztemp.Width
        Else
            sznew = szmaxwrap
        End If

        ' Set the CommandBar's client size to be equal to this new size.
        arg.ClientSize = sznew
    ElseIf ffactor <= 1 Then
        arg.ClientSize = szminwrap
    Else
        arg.ClientSize = Toolbar.Size
    End If
End If
End Sub
```

## 3.3.4 Frequently Asked Questions

This section will help you become more familiar in using the CommandBar control.

<!-- tags: [Syncfusion Winforms, CommandBar, version] keywords: [EssentialTools, CommandBarResizeType, ButtonColumns, CommandBar, ClientSize, Toolbar, ControlBar] -->
```