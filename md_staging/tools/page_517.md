```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_517.jpeg
document_name: tools
page_number: 517
page_id: tools#page_517
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:14Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
pcc.HidePopup(Syncfusion.Windows.Forms.PopupCloseType.Done);
}
```

### [VB.NET]

```vb
Private Sub colorUIControl_ColorSelected(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Ensures that the PopupControlContainer is closed after the selection of a color.
    Private cuicontrol As Syncfusion.Windows.Forms.ColorUIControl = CType(If(TypeOf sender Is Syncfusion.Windows.Forms.ColorUIControl, sender, Nothing), Syncfusion.Windows.Forms.ColorUIControl)
    Private pcc As Syncfusion.Windows.Forms.PopupControlContainer = CType(If(TypeOf cuicontrol.Parent Is Syncfusion.Windows.Forms.PopupControlContainer, cuicontrol.Parent, Nothing), Syncfusion.Windows.Forms.PopupControlContainer)
    pcc.HidePopup(Syncfusion.Windows.Forms.PopupCloseType.Done)
End Sub
```

#### See Also

- [How to add a ColorUI Control to a Popup Menu?](https://www.syncfusion.com/)

## 3.5.4.3 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

### 3.5.4.3.1 How to add a ColorUI Control to a Popup Menu

To add ColorUIControl to a PopupMenu, we need to use PopupMenu, PopupControlContainer. Follow the below steps to add a ColorUIControl to a popup menu.

1. Drag and drop a ColorUIControl, a PopupMenu control, a PopupControlContainer control, a label control, and a Panel control onto the form. Place the ColorUIControl inside the PopupControlContainer and the label inside the panel control.
2. 
3. Right click PopupMenu and select 'Add Default ParentBarIItem' from the verbs.

---

```html
<!-- tags: [syncfusion-sdk, winforms, colorui, popupmenu, popupcontrolcontainer] keywords: [syncfusion, colorui control, popup menu, popup control container, frequently asked questions] -->
```