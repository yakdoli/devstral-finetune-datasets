```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_286.jpeg
document_name: edit
page_number: 286
page_id: edit#page_286
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:04Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
}
}

private void RemoveShortcutInEditControl(MenuItem miParent)
{
    // Remove F5 shortcut.
    if (miParent.Shortcut == Shortcut.F5)
        miParent.Shortcut = Shortcut.None;

    // Parse through the children recursively.
    foreach (MenuItem mi in miParent.MenuItems)
    {
        this.RemoveShortcutInEditControl(mi);
    }
}
```

```vb
[VB.NET]

Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim cm As ContextMenu = Me.editControl1.ContextMenu
    Dim mi As MenuItem
    For Each mi In cm.MenuItems
        Me.RemoveShortcutInEditControl(mi)
    Next
End Sub

Private Sub RemoveShortcutInEditControl(ByVal miParent As MenuItem)
    ' Remove F5 shortcut.
    If miParent.Shortcut = Shortcut.F5 Then
        miParent.Shortcut = Shortcut.None
    End If

    ' Parse through the children recursively.
    Dim mi As MenuItem
    For Each mi In miParent.MenuItems
        Me.RemoveShortcutInEditControl(mi)
    Next
End Sub
```

## 5.7 How To Dynamically Add Configuration Settings At Runtime

<!-- tags: [winforms, edit control, menu items, shortcuts, f5] keywords: [edit control, menuitems, shortcut, f5, recursive, configuration settings, runtime] -->
```