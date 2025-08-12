```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_193.jpeg
document_name: tools
page_number: 193
page_id: tools#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:23:46Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

To persist docking information in a database, we need to serialize the state into a memory stream. After which the stream is written into the database. The field to where the dock state is saved is binary.

## Storing State

[C#]
```csharp
// Saving dock state to memory stream
MemoryStream ms = new MemoryStream();
AppStateSerializer aser = new
AppStateSerializer(SerializeMode.BinaryFmtStream, ms);
this.dockingManager1.SaveDockState(aser);
aser.PersistNow();
// Code to store the memory stream into database. Depends upon the database.
```

[VB.NET]
```vb.net
' Saving dock state to memory stream
Dim ms As MemoryStream = New MemoryStream()
Dim aser As AppStateSerializer = New
AppStateSerializer(SerializeMode.BinaryFmtStream, ms)
Me.dockingManager1.SaveDockState(aser)
aser.PersistNow()
' Code to store the memory stream into database. Depends upon the database.
```

## Retrieving State

[C#]
```csharp
// Code to retrieve data(stream) from database
MemoryStream ms = new MemoryStream(val);
ms.Position = 0;
AppStateSerializer aser = new
AppStateSerializer(SerializeMode.BinaryFmtStream, ms);
this.dockingManager1.LoadDockState(aser);
```

[VB.NET]
```vb.net
' Code to retrieve data(stream) from database
Dim ms As MemoryStream = New MemoryStream(value)
ms.Position = 0
Dim aser As AppStateSerializer = New
AppStateSerializer(SerializeMode.BinaryFmtStream, ms)
```

## API Reference

- `AppStateSerializer(SerializeMode.BinaryFmtStream, ms)`: Creates an instance of AppStateSerializer to serialize the docking state.
- `SaveDockState(aser)`: Saves the current docking state to the given AppStateSerializer.
- `LoadDockState(aser)`: Loads the docking state from the given AppStateSerializer.

## Code Examples

### C# Example: Saving Dock State
```csharp
MemoryStream ms = new MemoryStream();
AppStateSerializer aser = new AppStateSerializer(SerializeMode.BinaryFmtStream, ms);
this.dockingManager1.SaveDockState(aser);
aser.PersistNow();
```

### VB.NET Example: Saving Dock State
```vb.net
Dim ms As MemoryStream = New MemoryStream()
Dim aser As AppStateSerializer = New AppStateSerializer(SerializeMode.BinaryFmtStream, ms)
Me.dockingManager1.SaveDockState(aser)
aser.PersistNow()
```

### C# Example: Loading Dock State
```csharp
MemoryStream ms = new MemoryStream(val);
ms.Position = 0;
AppStateSerializer aser = new AppStateSerializer(SerializeMode.BinaryFmtStream, ms);
this.dockingManager1.LoadDockState(aser);
```

### VB.NET Example: Loading Dock State
```vb.net
Dim ms As MemoryStream = New MemoryStream(value)
ms.Position = 0
Dim aser As AppStateSerializer = New AppStateSerializer(SerializeMode.BinaryFmtStream, ms)
```

<!-- tags: [Syncfusion Winforms, Windows Forms, Docking, AppStateSerializer] keywords: [docking state, memory stream, serialization, database, AppStateSerializer, SerializeMode, BinaryFmtStream] -->
```