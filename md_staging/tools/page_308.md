```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_308.jpeg
document_name: tools
page_number: 308
page_id: tools#page_308
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
this.autoCompletel.SaveCurrentState(aser);
aser.PersistNow();
```

[VB.NET]

```vb
Dim ms As MemoryStream = New MemoryStream()
Private aser As AppStateSerializer = New AppStateSerializer(SerializeMode.BinaryFmtStream, ms)
Me.autoCompletel.SaveCurrentState(aser)
aser.PersistNow()
```

## Retrieving State

### C#
```csharp
// Code to retrieve data(stream) from database
MemoryStream ms = new MemoryStream(val);
ms.Position = 0;
AppStateSerializer aser = new AppStateSerializer(SerializeMode.BinaryFmtStream, ms);
this.autoCompletel.LoadCurrentState(aser);
```

[VB.NET]

```vb
' Code to retrieve data(stream) from database
Dim ms As MemoryStream = New MemoryStream(value)
ms.Position = 0
Dim aser As AppStateSerializer = New AppStateSerializer(SerializeMode.BinaryFmtStream, ms)
this.autoCompletel.LoadCurrentState(aser);
```

### To serialize in Binary Format, use the below code.

#### C#
```csharp
// To Save
AppStateSerializer aser = new AppStateSerializer(SerializeMode.BinaryFile, "myfile");
this.autoCompletel.SaveCurrentState(aser);
aser.PersistNow();

// To Load
AppStateSerializer aser = new AppStateSerializer(SerializeMode.BinaryFile, "myfile");
```

<!-- tags: [WinForms, Serialization, AppStateSerializer, Binary Format] keywords: [autoComplete, state retrieval, binary serialization, memory stream, database, LoadCurrentState, PersistNow] -->
```