<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_634.jpeg
document_name: tools
page_number: 634
page_id: tools#page_634
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Resizing the Popup

### Overview
- Drag and drop the ParentControl (e.g., RichTextBox and PopupControlContainer) onto the form.
- In the MouseUp event of RichTextBox, show the Popup using the `ShowPopup()` method.
- Make the Popup resizable by handling the `BeforePopup` event of PopupControlContainer and use the following code snippet.

### WinForms-specific Conventions
- Use `FormBorderStyle.SizableToolWindow` to make the pop-up resizable.
- Ensure the pop-up host's client size is set, especially since the pop-up's Dock style is set to `DockStyle.Fill`.
- Set the pop-up container to `DockStyle.Fill` to allow it to fill the entire pop-up host when resized.

### Code Examples

#### C#
```csharp
private void popupControlContainer1_BeforePopup(object sender, 
System.ComponentModel.CancelEventArgs e)
{
    // Make the pop-up host's border style re-sizable.
    this.popupControlContainer1.PopupHostFormBorderStyle = FormBorderStyle.SizableToolWindow;
    this.popupControlContainer1.PopupHost.BackColor = this.BackColor;

    // Necessary to set the host's client size every time, especially since the pop-up's Dock style is set to DockStyle.Fill.
    if(this.popupControlContainer1.PopupHost.Size.Width < 160)
        this.popupControlContainer1.PopupHost.Size = new Size(160, 176);

    // So that the pop-up container will fill the entire pop-up host when resized.
    this.popupControlContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
}
```

#### VB.NET
```vb
Private Sub popupControlContainer1_BeforePopup(ByVal sender As Object, 
ByVal e As System.ComponentModel.CancelEventArgs)

    ' Make the pop-up host's border style re-sizable.
    Me.popupControlContainer1.PopupHostFormBorderStyle = FormBorderStyle.SizableToolWindow
    Me.popupControlContainer1.PopupHost.BackColor = Me.BackColor

    ' Necessary to set the host's client size every time, especially since the pop-up's Dock style is set to DockStyle.Fill.
    If Me.popupControlContainer1.PopupHost.Size.Width < 160 Then
        Me.popupControlContainer1.PopupHost.Size = New Size(160, 176)
    End If

    ' So that the pop-up container will fill the entire pop-up host
End Sub
```

### Cross References
- Refer to the section on handling events and custom containers for more information on integrating the `PopupControlContainer`.

### RAG Annotations
<!-- tags: [winforms, popup, resizable, pop-up container, dockstyle, cancelargs] keywords: [resizing, showpopup, borderstyle, toolwindow, formstyle, backcolor, client size] -->