```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_264.jpeg
document_name: edit
page_number: 264
page_id: edit#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:27Z
fidelity: lossless
-->

## ReadOnlyChanged Event

### Overview
- The ReadOnlyChanged event is triggered when the ReadOnly property of the Edit Control is altered. It specifies whether the Edit Control is in read-only mode.
- The event handler takes an argument of type `EventArgs`.

### Content

#### Event Handler Example in C#

```csharp
// Handle the ReadOnlyChanged event.
this.editControl.ReadOnlyChanged += new
EventHandler(editControl1_ReadOnlyChanged);

// Set the ReadOnly property to True.
this.editControl.ReadOnly = true;

private void editControl1_ReadOnlyChanged(object sender, EventArgs e)
{
    Console.WriteLine(" ReadOnlyChanged event is raised ");
}
```

#### Event Handler Example in VB.NET

```vb.net
' Handle the ReadOnlyChanged event.
Me.editControl.ReadOnlyChanged += New
EventHandler(editControl1_ReadOnlyChanged)

' Set the ReadOnly property to True.
Me.editControl.ReadOnly = True

Private Sub editControl1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ReadOnlyChanged event is raised ")
End Sub
```

## RegisteringDefaultKeyBindings Event

### Overview
- This event is related to configuring key bindings and is discussed in the Keystroke - Action Combinations Binding topic.

### Content
- The event `RegisteringDefaultKeyBindings` deals with assigning default key bindings to actions within the control.

## API Reference

### Events
- **ReadOnlyChanged**
  - **Description**: Triggered when the ReadOnly property is changed.
  - **Parameters**: `EventArgs`
  - **Usage**: Attach this event to handle changes to the ReadOnly state of the control.

- **RegisteringDefaultKeyBindings**
  - **Description**: Discusses configuration options for default key bindings to actions, usually tied to input handling within the control.

## Code Examples

### Example: Handling the ReadOnlyChanged Event in C#

The following example illustrates how to attach and handle the ReadOnlyChanged event in a C# application:

```csharp
public class MyEditControl : Control
{
    public MyEditControl()
    {
        this.editControl.ReadOnlyChanged += new
        EventHandler(editControl1_ReadOnlyChanged);
    }

    private void editControl1_ReadOnlyChanged(object sender, EventArgs e)
    {
        Console.WriteLine(" ReadOnlyChanged event is raised ");
    }
}
```

### Example: Handling the ReadOnlyChanged Event in VB.NET

The following example illustrates how to attach and handle the ReadOnlyChanged event in a VB.NET application:

```vb.net
Public Class MyEditControl
    Inherits Control

    Public Sub New()
        Me.editControl.ReadOnlyChanged += New
        EventHandler(editControl1_ReadOnlyChanged)
    End Sub

    Private Sub editControl1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
        Console.WriteLine(" ReadOnlyChanged event is raised ")
    End Sub
End Class
```

## Page-level Navigation/TOC

- [4.14.17 ReadOnlyChanged Event](#read-only-changed-event)
- [4.14.18 RegisteringDefaultKeyBindings Event](#registering-default-key-bindings-event)

<!-- tags: [product, module, control, api, version?] keywords: [ReadOnlyChanged, RegisteringDefaultKeyBindings, Edit Control, Key Bindings, EventHandler, Action Combinations, C#, VB.NET] -->
```