```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: tools
page_number: 252
page_id: tools#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to prevent the closing of docked windows using the `DockVisibilityChanging` event.
- Demonstrates how to prevent tabbed docking using the `DockAllow` event.
- Provides details on handling docking events and manipulating dock visibility.

## Content

### 3.4.4.1.10 How to prevent closing of docked window?

This can be done in the `DockVisibilityChanging` event. When the end user tries to change the docking control visibility, this event will be handled. The members of this event are as follows:

| **Members** | **Description** |
|-------------|------------------|
| **Cancel**  | This property gets / sets the value indicating whether the event should be canceled. |
| **Control** | Gets the control which is undergoing the transfer. |

#### Code Examples

**[C#]**

```csharp
private void dockingManager1_DockVisibilityChanging(object sender, Syncfusion.Windows.Forms.Tools.DockVisibilityChangingEventArgs arg)
{
    arg.Cancel = true;
}
```

**[VB.NET]**

```vb
Private Sub dockingManager1_DockVisibilityChanging(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockVisibilityChangingEventArgs) Handles dockingManager1.DockVisibilityChanging
    arg.Cancel = True
End Sub
```

Additionally, the dock visibility of a control can be retrieved using the `GetDockVisibility` method by passing the control as the parameter. Also, `DockVisibility` can be set for the controls using the `SetDockVisibility` method.

### 3.4.4.1.11 How to prevent tabbed docking?

The `DockAllow` event will be handled when a docking window is dragged over a potential dock target. In other words, whenever the user tries to dock a docked control to another docked control, this event will be raised. This lets you decide whether to allow tabbing or not. Giving `arg.Cancel` to `true` cancels the docking operation.

| **Members**      | **Description**                        |
|------------------|----------------------------------------|
| **DockStyle**    | Represents the docking style.         |
| **DragControl**  | Gets the control that is being dragged. |
| **TargetControl**| The dock target control.             |

## API Reference

### `DockVisibilityChangingEventArgs`
- **Cancel** - Sets or gets whether the event should be canceled.
- **Control** - Gets the control undergoing the transfer.

### `DockEventArgs`
- **DockStyle** - Represents the docking style.
- **DragControl** - Gets the control that is being dragged.
- **TargetControl** - Gets the dock target control.

## Code Examples (Continued)

The examples provided demonstrate how to handle the `DockVisibilityChanging` and `DockAllow` events in both C# and VB.NET, with code snippets to prevent closing of docked windows and tabbed docking.

## Cross References

- See also: Docking and Tabbing in Windows Forms, Dock Manager Events, and Dock Visibility Manipulation.

<!-- tags: [winforms, docking, tabbed docking, event handling] keywords: [dockvisibilitychanging, dockallow, args, cancel, control, dockstyle, dragcontrol, targetcontrol, getdockvisibility, setdockvisibility] -->
```