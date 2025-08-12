```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_195.jpeg
document_name: tools
page_number: 195
page_id: tools#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:26:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes methods to save and load docked control states in a WinForms application.
- Explains how to use serializer objects to manage application state persistence.
- Highlights the use of `LoadDesignerDockState()` and `GetSerializedControls()` methods for restoring and inspecting serialized control states.

## Content

### Saving and Loading Dock State

#### [VB.NET]
```vb
' To Save
Dim serializer As New AppStateSerializer(SerializeMode.IsolatedStorage, "myfile")
Me.dockingManager1.SaveDockState(serializer)
serializer.PersistNow()

' To Load
Dim serializer As New AppStateSerializer(SerializeMode.IsolatedStorage, "myfile")
Me.dockingManager1.LoadDockState(serializer)
```

#### C#
```csharp
this.dockingManager1.LoadDesignerDockState();
```

#### [VB.NET]
```vb
Me.dockingManager1.LoadDesignerDockState()
```

### LoadDesignerDockState()
- The dock state that is set through Visual Designer can be restored by calling the `LoadDesignerDockState` method.

### GetSerializedControls
- Calling the `GetSerializedControls` method will return the serialized control collection enumerator in the specified serializer. This can be done through code as follows.

#### [C#]
```csharp
this.dockingManager1.GetSerializedControls(serializer);
Console.Write("Serialized controls :" + this.dockingManager1.GetSerializedControls(serializer));
```

#### [VB.NET]
```vb
Me.dockingManager1.GetSerializedControls(serializer)
Console.Write("Serialized controls :" + Me.dockingManager1.GetSerializedControls(serializer))
```

## Parameters

| Parameter    | Description                                  |
|--------------|----------------------------------------------|
| Serializer   | An instance of AppStateSerializer class.     |

### Related Functionality
- The `AppStateSerializer` class is used to manage serialization modes and file persistence for application states.
- Methods like `PersistNow()` ensure that changes are immediately saved to the specified storage mode.

<!-- tags: [Syncfusion, WinForms, DockManager, DesignerDockState, SerializedControls, AppStateSerializer] keywords: [docking controls, load designer state, serialize controls, application state management, isolated storage] -->
```