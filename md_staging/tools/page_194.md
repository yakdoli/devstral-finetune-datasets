```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: tools
page_number: 194
page_id: tools#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:24:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Me.dockingManager1.LoadDockState(aser)
```

## Serialization with Binary Format

To serialize in **Binary Format**, use the following code.

### C#

```csharp
// To Save
AppStateSerializer serializer = new AppStateSerializer(SerializeMode.BinaryFile, "myfile");
this.dockingManager1.SaveDockState(serializer);
serializer.PersistNow();

// To Load
AppStateSerializer serializer = new AppStateSerializer(SerializeMode.BinaryFile, "myfile");
this.dockingManager1.LoadDockState(serializer);
```

### VB.NET

```vb
' To Save
Dim serializer As New AppStateSerializer(SerializeMode.BinaryFile, "myfile")
Me.dockingManager1.SaveDockState(serializer)
serializer.PersistNow()

' To Load
Dim serializer As New AppStateSerializer(SerializeMode.BinaryFile, "myfile")
Me.dockingManager1.LoadDockState(serializer)
```

## Serialization with Isolated Storage

To serialize in **Isolated Storage** medium, use the following code.

### C#

```csharp
// To Save
AppStateSerializer serializer = new AppStateSerializer(SerializeMode.IsolatedStorage, "myfile");
this.dockingManager1.SaveDockState(serializer);
serializer.PersistNow();

// To Load
AppStateSerializer serializer = new AppStateSerializer(SerializeMode.IsolatedStorage, "myfile");
this.dockingManager1.LoadDockState(serializer);
```

## Footer

© 2013 Syncfusion. All rights reserved.
```