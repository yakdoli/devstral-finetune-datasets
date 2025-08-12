```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_309.jpeg
document_name: tools
page_number: 309
page_id: tools#page_309
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
this.autoComplete1.LoadCurrentState(aser);
```

## Serialization in Binary File

### Save

```vbnet
' To Save
Private aser As AppStateSerializer = New AppStateSerializer(SerializeMode.BinaryFile, "myfile")
Me.autoComplete1.SaveCurrentState(aser)
aser.PersistNow()
```

### Load

```vbnet
' To Load
Private aser As AppStateSerializer = New AppStateSerializer(SerializeMode.BinaryFile, "myfile")
Me.autoComplete1.LoadCurrentState(aser)
```

## Serialization in Isolated Storage

To serialize in **Isolated Storage** medium, use the below code.

### C#

```csharp
// To Save
AppStateSerializer aser = new AppStateSerializer(SerializeMode.IsolatedStorage, "myfile");
this.autoComplete1.SaveCurrentState(aser);
aser.PersistNow();

// To Load
AppStateSerializer serializer = new AppStateSerializer(SerializeMode.IsolatedStorage, "myfile");
this.autoComplete1.LoadCurrentState(aser);
```

### VB.NET

```vbnet
' To Save
Private aser As AppStateSerializer = New AppStateSerializer(SerializeMode.IsolatedStorage, "myfile")
Me.autoComplete1.SaveCurrentState(aser)
aser.PersistNow()

' To Load
Private serializer As AppStateSerializer = New AppStateSerializer(SerializeMode.IsolatedStorage, "myfile")
Me.autoComplete1.LoadCurrentState(aser)
```
```html
<!-- tags: [windows forms, serialization, essential tools, binary file, isolated storage, app states, syncfusion, version 11.4.0.26] keywords: [Save, Load, AppStateSerializer, SerializeMode, BinaryFile, IsolatedStorage, myfile, PersistNow, autoComplete1] -->
```