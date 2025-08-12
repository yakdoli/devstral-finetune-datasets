```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_224.jpeg
document_name: tools
page_number: 224
page_id: tools#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:43:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The page discusses the `NewDockStateBeginLoad` and `NewDockStateEndLoad` events in the context of docked controls in WinForms applications.
- Explains the behavior of these events during the loading of a new dock state.
- Provides code examples in C# and VB.NET for handling these events.

## Content

### Handling `NewDockStateBeginLoad` Event

The `NewDockStateBeginLoad` event occurs just before a new dock state is loaded.

#### C#
```csharp
// The NewDockStateBeginLoad event occurs just before a new dock state is loaded.
private void dockingManager1_NewDockStateBeginLoad(object sender, System.EventArgs e)
{
    Console.WriteLine("NewDockStateBeginLoad Event occurred");
    // This will show until you click on the OK button.
    // So The new state will be loaded after finishing this statement.
    MessageBox.Show("This is NewDockStateBeginLoad Event Message Box");
}
```

#### VB.NET
```vb
Private Sub dockingManager1_NewDockStateBeginLoad(ByVal sender As Object, ByVal e As System.EventArgs)
    Console.WriteLine("NewDockStateBeginLoad Event occurred")
    ' This will show until you click on the OK button.
    ' So The new state will be loaded after finishing this statement.
    MessageBox.Show("This is NewDockStateBeginLoad Event Message Box")
End Sub
```

### Handling `NewDockStateEndLoad` Event

The `NewDockStateEndLoad` event occurs immediately after a new dock state has been loaded.

#### Description
- **Member**: Control
- **Description**: Gets the docked control for which a new dock state has been loaded.

#### Code Example

##### C#
```csharp
// The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.
private void dockingManager1_NewDockStateEndLoad(object sender, System.EventArgs e)
{
    Console.WriteLine("NewDockstateEndLoad Event occurred");
    // This will show until you click on the OK button.
    // So The new state will be loaded after finishing this statement.
    MessageBox.Show("This is NewDockStateEndLoad Event Message Box");
}
```

## API Reference

- **Control**: Gets the docked control for which a new dock state has been loaded.

## Code Examples

The page includes code snippets for handling the `NewDockStateBeginLoad` and `NewDockStateEndLoad` events in both C# and VB.NET.

<!-- tags: [WinForms, DockManager, DockStateEvents, Version: 11.4.0.26] keywords: [NewDockStateBeginLoad, NewDockStateEndLoad, DockedControls, Syncfusion, EventHandling, C#, VB.NET, MessageDialog, ConsoleOutput] -->
```