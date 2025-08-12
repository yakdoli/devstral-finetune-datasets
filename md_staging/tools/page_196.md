```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_196.jpeg
document_name: tools
page_number: 196
page_id: tools#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:24:24Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Provides guidance on managing docked controls and their transitions to MDI child forms.
- Explains the `PersistState` mechanism and how to handle docking state serialization.
- Details the steps to convert docked controls to MDI children.

## Content

### See Also
- [ProvidePersistedID Event, How to avoid flickering while loading dock state?](ProvidePersistedID Event, How to avoid flickering while loading dock state?)
- [How to serialize or deserialize the docking state for a docked control on loading the application?]( How to serialize or deserialize the docking state for a docked control on loading the application?)

**Note:** The `PersistState` property mechanism assumes that the `DockingManager` is hosted on a form and captures the docking layout on the host form's closing event. When `DockingManager` is hosted on a `UserControl`, `LoadDockState` and `SaveDockState` methods have to be called explicitly, on the Load and Closed events of the form that hosts the `UserControl`.

#### 3.4.3.7.3 MDI Child Transition

A docked control can be converted to an MDI child form and vice versa, using the code below.

1. Add the required syncfusion assembly references.
2. Declare and initialize the `DockingManager` and other controls.
3. Set the properties required and add the controls to the form. The `IsMdiContainer` property of the form should be set to true.
4. Call the `SetAsMDIChild` method. This method will set the specified docked control as an MDI child.

| Methods               | Description                                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|
| `SetAsMDIChild`      | Sets the control specified in `Ctrl` parameter as MDI child when `bsetMDI` is set to true. The parameters are:<br><br>`Ctrl` - Indicates the docked control.<br>`bsetMDI` - Represents a Boolean value indicating true or false. |
| `SetAsMDIChild(Overloaded)` | Sets the specified docked control as MDI child with the new size provided using the `Layout` parameter.<br><br>`Ctrl` - Indicates the docked control.<br>`bsetMDI` - Represents a Boolean value indicating true or false. |

## Code Examples

To implement the above, the following methods can be utilized:

### Example: Setting a Docked Control as an MDI Child

```csharp
using Syncfusion.Windows.Forms.Docking;

public void ConvertDockedControlToMDIChild(Control ctrl, DockingManager dockingManager)
{
    // Initialize the docking manager
    dockingManager.DockForm = this;

    // Add the docked control
    dockingManager.Add(ctrl);

    // Set the control as an MDI child
    dockingManager.SetAsMDIChild(ctrl, true);
}
```

## Cross References

See also:
- [ProvidePersistedID Event, How to avoid flickering while loading dock state?](ProvidePersistedID Event, How to avoid flickering while loading dock state?)
- [How to serialize or deserialize the docking state for a docked control on loading the application?]( How to serialize or deserialize the docking state for a docked control on loading the application?)

<!-- tags: [Syncfusion, Windows Forms, DockingManager, MDI Child,тки징lleruttonlogging To tongokStatetagit表示性停止機種行人英語用語，] keywords: [Docking, MDI, persistence, serialization, deserialization, docked control, MDI child form] -->
```