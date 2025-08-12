```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_307.jpeg
document_name: tools
page_number: 307
page_id: tools#page_307
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:14Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Persisting data in XML files using Syncfusion's AppStateSerializer.
- Saving and loading AutoComplete data in XML format.
- Persisting data into a memory stream using AppStateSerializer.

## Content

### Persisting in XML file

To save and load the AutoComplete data in a XML,

#### [C#]

```csharp
using Syncfusion.Runtime.Serialization;

// To Save
AppStateSerializer aser = new AppStateSerializer(SerializeMode.XMLFile, @"C:\info.xml");
this.autoCompletel.SaveCurrentState(aser);

// To Load
AppStateSerializer aser = new AppStateSerializer(SerializeMode.XMLFile, @"C:\info.xml");
this.autoCompletel.LoadCurrentState(aser);
```

#### [VB.NET]

```vb
Imports Syncfusion.Runtime.Serialization

' To Save
Private aser As AppStateSerializer = New AppStateSerializer(SerializeMode.XMLFile, "C:\info.xml")
Me.autoCompletel.SaveCurrentState(aser)

' To Load
Private aser As AppStateSerializer = New AppStateSerializer(SerializeMode.XMLFile, "C:\info.xml")
Me.autoCompletel.LoadCurrentState(aser)
End Sub
```

### Persisting in Memory Stream

To serialize the data into a memory stream,

#### Storing State

##### [C#]

```csharp
MemoryStream ms = new MemoryStream();
AppStateSerializer aser = new AppStateSerializer(SerializeMode.BinaryFmtStream, ms);
```

## API Reference
- **Namespace**: `Syncfusion.Runtime.Serialization`
- **Class**: `AppStateSerializer`
- **Methods**:
  - **SaveCurrentState(AppStateSerializer serializer)**: Saves the current state of the control to the specified serializer.
  - **LoadCurrentState(AppStateSerializer serializer)**: Loads the state of the control from the specified serializer.

## Code Examples (multi-language supported)
- The examples demonstrate saving and loading state using both XML files and memory streams, showcasing the flexibility of `AppStateSerializer`.

## Page-level Navigation/TOC (if applicable)
- [Persisting in XML file]
- [Persisting in Memory Stream]

## Cross References
See also:
- [Syncfusion's Serialization Documentation](https://www.syncfusion.com/documentation/windows-forms/serialization)
- [AutoComplete Control Reference](https://www.syncfusion.com/documentation/windows-forms/autocomplete)

<!-- tags: [syncfusion, windowsforms, autoserialize, memorystream, xmlserialization, apistate] keywords: [autocomplete, appstateserializer, serialization, memorystream, xmlfile] -->
```