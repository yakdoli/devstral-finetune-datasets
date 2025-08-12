```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_637.jpeg
document_name: tools
page_number: 637
page_id: tools#page_637
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Handles the data transfer between a PopUp control and Windows Forms controls.
- Implements the CloseUp event for the PopUp.
- Demonstrates hiding the PopUp on Button_Click.

## Content

### Handling Data Transfer using CloseUp Event

The `CloseUp` event is used to implement the data transfer from the PopUp to the control on the form.

#### C#

```csharp
private void popupControlContainer1_CloseUp(object sender, Syncfusion.Windows.Forms.PopupClosedEventArgs e)
{
    if (e.PopupCloseType == Syncfusion.Windows.Forms.PopupCloseType.Done)
    {
        this.richTextBox1.Text = this.textBox1.Text;
    }
    // Set focus back to textbox.
    if (e.PopupCloseType == Syncfusion.Windows.Forms.PopupCloseType.Done ||
        e.PopupCloseType == Syncfusion.Windows.Forms.PopupCloseType.Canceled)
        this.richTextBox1.Focus();
}
```

#### VB.NET

```vbnet
Private Sub popupControlContainer1_CloseUp(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.PopupClosedEventArgs)
    If e.PopupCloseType = Syncfusion.Windows.Forms.PopupCloseType.Done Then
        Me.richTextBox1.Text = Me.textBox1.Text
    End If
    ' Set focus back to textbox.
    If e.PopupCloseType = Syncfusion.Windows.Forms.PopupCloseType.Done OrElse e.PopupCloseType = Syncfusion.Windows.Forms.PopupCloseType.Canceled Then
        Me.richTextBox1.Focus()
    End If
End Sub
```

### Hiding the PopUp on Button Click

To hide the PopUp on button click, use the following snippet.

#### C#

```csharp
this.popupControlContainer1.HidePopup(Syncfusion.Windows.Forms.PopupCloseType.Done);
```

#### VB.NET

```vbnet
Me.popupControlContainer1.HidePopup(Syncfusion.Windows.Forms.PopupCloseType.Done)
```

## API Reference

This section covers the API elements used for handling the PopUp control.

### Methods
- `HidePopup(PopupCloseType)`
  - Hides the PopUp with the specified close type.

### Events
- `CloseUp(object, PopupClosedEventArgs)`
  - Triggered when the PopUp is closed, allowing for data transfer and focus handling.

### Properties
- `PopupCloseType`
  - Enumerates the possible types of PopUp closure (Done, Canceled).

## Code Examples

The above examples demonstrate how to handle the PopUp's `CloseUp` event and hide it programmatically in both C# and VB.NET.

### See also:
- [Syncfusion Windows Forms Documentation](https://help.syncfusion.com/windowsforms/)
- [PopUp Control](https://help.syncfusion.com/windowsforms/popups)
- [Event Handling in Windows Forms](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/event-handling-in-windows-forms-overview#design-time-event-handling)

## Page-level Navigation/TOC (if applicable)

This document focuses on using the PopUp control in Windows Forms to transfer data between controls and manage the PopUp's state using the `CloseUp` event and related methods.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, PopUp Control, Event Handling, CloseUp, HidePopup, C#, VB.NET] keywords: [Windows Forms, data transfer, popUp, close type, focus, hide popUp, event handling] -->
```
