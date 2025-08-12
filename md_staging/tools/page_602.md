```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_602.jpeg
document_name: tools
page_number: 602
page_id: tools#page_602
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Handling Focus in Custom Pop-up Controls

The `CustomPopupControlContainer` class inherits from `Syncfusion.Windows.Forms.PopupControlContainer`. It ensures that the derived control receives focus when the pop-up is displayed.

```vb
Public Class CustomPopupControlContainer Inherits Syncfusion.Windows.Forms.PopupControlContainer

    Public Sub New()
        End Sub

    Public Sub New(ByVal container As IContainer) : Me()
        container.Add(Me)
    End Sub

    ' Sets focus to the derived control.
    Protected Overrides Sub OnPopup(ByVal args As EventArgs)
        MyBase.OnPopup(args)
        Me.Focus()
    End Sub

End Class
```

### Explaining the Parent-Child Relationship

Here, the specification of the parent-child relationship between the `ComboBoxBase`'s pop-up and the `PopupControlContainer` is explained using coding examples.

#### C# Example

```csharp
[C#]

private void comboBoxBasel_DropDown(object sender, System.EventArgs e)
{
    /* Setup the relationship between the ComboBoxBase's dropdown and its
       parent PopupControlContainer, so that the pop-up will not close when
       the ComboBoxBase’s dropdown is shown */
    
    this.comboBoxBasel.PopupContainer.PopupParent = this.popupControlContainer1;
    this.popupControlContainer1.CurrentPopupChild = this.comboBoxBasel.PopupContainer;
}
```

#### VB.NET Example

```vb
[VB.NET]

Private Sub comboBoxBasel_DropDown(ByVal sender As Object, ByVal e As System.EventArgs)

    ' Setup the relationship between the ComboBoxBase's dropdown and its
    ' parent PopupControlContainer, so that the pop-up will not close when
    ' the ComboBoxBase’s dropdown is shown
    
    Me.comboBoxBasel.PopupContainer.PopupParent = Me.popupControlContainer1
    Me.popupControlContainer1.CurrentPopupChild = 
End Sub
```

## Code Examples

### C# Example

The following C# code snippet demonstrates how to set up the necessary relationship to prevent the pop-up from closing when the `ComboBoxBase`'s dropdown is shown:

```csharp
private void comboBoxBasel_DropDown(object sender, System.EventArgs e)
{
    this.comboBoxBasel.PopupContainer.PopupParent = this.popupControlContainer1;
    this.popupControlContainer1.CurrentPopupChild = this.comboBoxBasel.PopupContainer;
}
```

### VB.NET Example

The corresponding VB.NET example achieves the same functionality:

```vb
Private Sub comboBoxBasel_DropDown(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.comboBoxBasel.PopupContainer.PopupParent = Me.popupControlContainer1
    Me.popupControlContainer1.CurrentPopupChild = Me.comboBoxBasel.PopupContainer
End Sub
```

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, ComboBox, Popup, Focus, Parent-Child Relationship] keywords: [CustomPopupControlContainer, ComboBoxBase, PopupControlContainer, focus, pop-up, dropdown, parent-child relationship] -->
```
