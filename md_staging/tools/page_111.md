```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_111.jpeg
document_name: tools
page_number: 111
page_id: tools#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:28:39Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb.net
'}'}'}}
```

### [VB.NET]

```vb.net
' Handler for the CommandBar.CommandBarStateChanged event.
Private Sub cbFonts_CommandBarStateChanged(ByVal sender As Object, ByVal e As System.EventArgs)
    ' The Fonts CommandBar client dimensions may have been changed by the redocking.
    ' Size the panel containing the Fonts toolbar to fit the new CommandBar panel dimensions.
    If ((Me.commandBarFonts.DockState = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) OrElse
        (Me.commandBarFonts.DockState = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right)) AndAlso
        (Me.pnlFontsTB.Width > Me.commandBarFonts.Width) Then
            Me.pnlFontsTB.Size = Me.pnlFonts.Size
    Else
        ' The CommandBar has been moved out of a left / right dock position.
        If Me.pnlFontsTB.Height > Me.commandBarFonts.Height Then
            Me.pnlFontsTB.Size = Me.szFontToolbarPanel
        End If
    End If
End Sub
```

### 3.3.3.10.4 CommandBarUserClosed Event

This event is raised when a floating CommandBar is hidden by the user, i.e., when the user presses the close button of the CommandBar that exists in the float state.

The event handler receives an argument of type EventArgs containing data related to this event.

### [C#]

```csharp
// Set the CommandBar control to its Floating state.
this.commandBar1.DisableDocking = true;

// Handle the CommandBarUserClosed event.
this.commandBar1.CommandBarUserClosed += new EventHandler(commandBar1_CommandBarUserClosed);

private void commandBar1_CommandBarUserClosed(object sender, EventArgs e)
{
}
```
```