<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_631.jpeg
document_name: tools
page_number: 631
page_id: tools#page_631
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to implement a custom `PopupControlContainer` for handling pop-up behavior in combination with a `ComboBoxBase` control.
- Illustrates specifying the parent-child relationship between the `ComboBoxBase` pop-up and the `PopupControlContainer`.

## Content

### Custom PopupControlContainer Implementation
- A class inheriting from `Syncfusion.Windows.Forms.PopupControlContainer` is created to manage the pop-up behavior.
- On the `OnPopup` event, the container is focused to ensure that the pop-up remains open and does not close unintentionally.

```vbnet
Inherits Syncfusion.Windows.Forms.PopupControlContainer
Public Sub New()
End Sub

Public Sub New(ByVal container As IContainer) : Me()
    container.Add(Me)
End Sub

Protected Overrides Sub OnPopup(ByVal args As EventArgs)
    MyBase.OnPopup(args)
    Me.Focus()
End Sub
End Class
```

### Setting Parent-Child Relationship
- It is necessary to specify the relationship between the `ComboBoxBase`'s pop-up and the `PopupControlContainer`.
- This is achieved by handling the `ComboBoxBase`'s dropdown event, as shown below.

#### C#
```csharp
private void comboBoxBase1_DropDown(object sender, System.EventArgs e)
{
    /* Setup the relationship between the ComboBoxBase's dropdown
       and its parent PopupControlContainer, so that the pop-up will
       not close when the ComboBoxBase's dropdown is shown */
    
    this.comboBoxBase1.PopupContainer.PopupParent =
        this.popupControlContainer1;
    this.popupControlContainer1.CurrentPopupChild =
        this.comboBoxBase1.PopupContainer;
}
```

#### VB.NET
```vbnet
Private Sub comboBoxBase1_DropDown(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Setup the relationship between the ComboBoxBase's dropdown
    ' and its parent PopupControlContainer, so that the pop-up will
    ' not close when the ComboBoxBase's dropdown is shown
    Me.comboBoxBase1.PopupContainer.PopupParent =
        Me.popupControlContainer1
    Me.popupControlContainer1.CurrentPopupChild =
        Me.comboBoxBase1.PopupContainer
End Sub
```

## Cross References
- Refer to documentation on `ComboBoxBase` and `PopupControlContainer` for additional details on their usage and properties.

<!-- tags: [syncfusion winforms, comboboxbase, popupcontrolcontainer] keywords: [dropdown event, parent-child relationship, focus, popup parent, pop-up behavior, custom container] -->