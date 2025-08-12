```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_112.jpeg
document_name: tools
page_number: 112
page_id: tools#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:28:28Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Content

#### CommandBarUserClosed Event

```csharp
// This event is fired when the Floating CommandBar is closed. The
// below line will be displayed in the output window at runtime.
MessageBox.Show("CommandBarUserClosed Event is raised ");
}
```

**[VB.NET]**

```vb
' Set the CommandBar control to its Floating state.
Me.commandBar1.DisableDocking = True

' Handle the CommandBarUserClosed event.
AddHandler Me.commandBar1.CommandBarUserClosed, AddressOf _
    commandBar1_CommandBarUserClosed

Private Sub commandBar1_CommandBarUserClosed(ByVal sender As Object, _
    ByVal e As EventArgs)
    ' This event is fired when the Floating CommandBar is closed. The
    ' below line will be displayed in the output window at runtime.
    MessageBox.Show("CommandBarUserClosed Event is raised ")
End Sub
```

##### 3.3.3.10.5 CommandBarWrapping Event

This event is raised when the CommandBar is resized with either the **DockModeWrapping** or the **FloatModeWrapping** properties set to 'True'. This event can be handled to suggest suitable wrap size hints for the CommandBar.

The event handler receives an argument of type **CommandBarWrappingEventArgs** containing data related to this event. The following **CommandBarWrappingEventArgs** members provide information specific to this event.

| Members               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| ClientSize            | Gets/Sets the current/proposed size of CommandBar's client control.      |
| CommandBarResizeType  | Returns the type of resizing taking place.                              |

**[C#]**

```csharp
private void commandBarAlign_CommandBarWrapping(object obj,
    Syncfusion.Windows.Forms.Tools.CommandBarWrappingEventArgs arg)
{
    // Apply the wrapping algorithm only when the CommandBar is floating.
    if (this.commandBarAlign.DockState ==
```

## API Reference (if applicable)
- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `CommandBarWrappingEventArgs`
  - **Members**:
    - `ClientSize`: Gets/Sets the current/proposed size of CommandBar's client control.
    - `CommandBarResizeType`: Returns the type of resizing taking place.

## Code Examples (multi-language supported)
- **C# Example**:
  ```csharp
  private void commandBarAlign_CommandBarWrapping(object obj,
      Syncfusion.Windows.Forms.Tools.CommandBarWrappingEventArgs arg)
  {
      // Apply the wrapping algorithm only when the CommandBar is floating.
      if (this.commandBarAlign.DockState ==
  ```

## Related Links
- [Tooltip](Tooltip.md)
- [Setting Intellisense](Setting%20Intellisense.md)
- [Set up Style](Set%20up%20Style.md)
- [Validation in CommandBar](Validation%20in%20CommandBar.md)

<!-- tags: [Syncfusion Winforms, CommandBar, DockModeWrapping, FloatModeWrapping, CommandBarWrappingEventArgs] keywords: [CommandBar, resizing, wrappingAlgorithm, CommandBarWrapping, CommandBarResizeType] -->
```