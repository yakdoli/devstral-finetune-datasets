```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_225.jpeg
document_name: tools
page_number: 225
page_id: tools#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:45:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the `NewDockStateEndLoad` event in VB.NET.
- Explains the `DockVisibilityChanged` event related to dock control visibility changes.
- Provides details about event handling and event data for `DockVisibilityChanged`.

## Content

### Code Example: NewDockStateEndLoad Event in VB.NET

```vb
[VB.NET]

'The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.
Private Sub dockingManager1_NewDockStateEndLoad(ByVal sender As Object, ByVal e As System.EventArgs)
    Console.WriteLine("NewDockstateEndLoad Event occurred")
    'This will show until you click on the OK button.
    'So The new state will be loaded after finishing this statement.
    MessageBox.Show("This is NewDockStateEndLoad Event Message Box")
End Sub
```

#### Dock Visibility State
- **3.4.3.8.6 Dock Visibility State**
- This section covers events related to dock visibility changes.

##### 3.4.3.8.6.1 DockVisibilityChanged Event
- Occurs when a control's DockVisibility state has been altered.
- Triggered when the user clicks on the close button, causing the visibility change.
- Can also use `dockingManager.GetDockVisibility(control)` to ascertain the current DockVisibility status.

### Event Data
- The event handler receives an argument of type `DockVisibilityChangedEventArgs`.
- Provides detailed information about the control undergoing the visibility change.

| Member | Description |
| --- | --- |
| Control | Gets the control undergoing the visibility change. |

## API Reference
- **DockVisibilityChangedEventArgs**
  - **Control**: Provides the control that is undergoing a visibility state change.

## Code Examples
- Example of handling the `DockVisibilityChanged` event:
  ```vb
Sub control_DockVisibilityChanged(sender As Object, e As DockVisibilityChangedEventArgs)
    Dim dockedControl As DockWindow = e.Control
    ' Handle the visibility change here
End Sub
```

## Cross References
- Refer to additional documentation for more details on other events and properties related to dock layouts.

<!-- tags: [Syncfusion Winforms, Docking, Visibility, Events] keywords: [DockVisibilityChanged, NewDockStateEndLoad, DockWindow, DockVisibilityStateChanged, Event Handling, Syncfusion] -->
```