```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_107.jpeg
document_name: tools
page_number: 107
page_id: tools#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:25:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
' Add items to the ParentBarItem.
Me.parentBarItem1.Items.AddRange(New Syncfusion.Windows.Forms.Tools.XPMenus.BarItem() {Me.barItem1, Me.barItem2, Me.barItem3})
Me.barItem1.Text = "Windows Forms Samples"
Me.barItem2.Text = "ASP.NET Samples"
Me.barItem3.Text = "WPF Samples"
' Handle the CommandBarDropDownClicked event.
AddHandler Me.commandBar1.CommandBarDropDownClicked, AddressOf commandBar1_CommandBarDropDownClicked
Private Sub commandBar1_CommandBarDropDownClicked(ByVal sender As Object, ByVal e As EventArgs)
    ' The below line will be displayed in the output window at runtime.
    Console.WriteLine(" CommandBarDropDownClicked event is raised ")
End Sub
```

## CommandBarStateChanging Event

This event is raised when a CommandBar's dock / float state is about to change.

The event handler receives an argument of type `CommandBarStateChangingEventArgs` containing data related to this event. The following `CommandBarStateChangingEventArgs` members provide information specific to this event.

| Members       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Cancel        | Gets / sets a value indicating whether the event should be canceled.      |
| NewDockState  | Gets / sets the CommandBar's new position.                                 |

### [C#]

```csharp
// Handler for the CommandBar.CommandBarStateChanging event.
private void cbFonts_CommandBarStateChanging(object obj, Syncfusion.Windows.Forms.Tools.CommandBarStateChangingEventArgs arg)
{
    // If the fonts CommandBar is being docked to a vertical dock position, ie., left or right,
    // then hide the two combo boxes and set the commandbar maxlength to be equal to
    // the length of the fonts toolbar.
    // NOTE - The CommandBar's dockstate will be set to CommandBarDockState.None when the CommandBar
    // is in an indeterminate state. This happens only during loading and deserialization.
}
```

<!-- tags: [product, module, control, api, version] keywords: [CommandBar, CommandBarDropDownClicked, CommandBarStateChanging, C#, VB, Syncfusion.Windows.Forms.Tools, EventHandling] -->
```