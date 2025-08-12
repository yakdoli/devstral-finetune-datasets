```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_624.jpeg
document_name: tools
page_number: 624
page_id: tools#page_624
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:44Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
gc.AlphaBlendSelectionColor = Color.Transparent

Private Sub gc_PrepareViewStyleInfo(ByVal sender As Object, ByVal e As GridPrepareViewStyleInfoEventArgs)
    Dim cc As GridCurrentCell = Me.gc.CurrentCell
    If e.RowIndex = cc.RowIndex Then
        e.Style.BackColor = SystemColors.Highlight
        e.Style.TextColor = SystemColors.HighlightText
    End If
End Sub
```

## 3.5.6 Container Control

The control used to populate with child controls is referred to as a Container control. This section discusses the following Container controls.

### 3.5.6.1 PopupControlContainer

A `PopupControlContainer` is a panel-derived control that allows users to populate it with child controls in code or during design time and then insert it in code with a call to `PopupControlContainer.ShowPopup`. It also provides various options with respect to its border alignment with a popup-parent.

The `PopupControlContainer` was implemented to support creating custom control-rich popups and show them beside a popup-parent, such as a `context` menu.

![Figure 383: PopupControlContainer During Design-Time](image.png)

## Page-level Navigation/TOC (if applicable)

<!-- tags: [Windows Forms, Grid, ContainerControl, PopupControlContainer, ContextMenu, Design-Time Configuration] keywords: [PopupControlContainer, Design-Time, Grid, Windows Forms, Container Control, Control Rich Popups, Border Alignment, Context Menu] -->
``` 
