```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: tools
page_number: 192
page_id: tools#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:21:50Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Save Dock State

The `SaveDockState` method can be used to save the state of the docked control. Here are examples in both C# and VB.NET:

#### C#

```csharp
this.dockingManager1.SaveDockState();
this.dockingManager1.SaveDockState(serializer);
this.dockingManager1.SaveDockState(serializer, this.listBox1);
```

#### VB.NET

```vb
Me.dockingManager1.SaveDockState()
Me.dockingManager1.SaveDockState(serializer)
Me.dockingManager1.SaveDockState(serializer, this.listBox1)
```

### Persisting Dock state in XML file

When the `DockingManager`'s `PersistState` property is set, it will save the dock state into the default persistence medium, 'IsolatedStorage'. To store the dock state in some other medium like XML, you can follow these steps:

#### C#

```csharp
using Syncfusion.Runtime.Serialization;
// Persist the dock state into XML File named Dock1.xml. Use this line in the constructor of Control which hosts the dockinglayout
public form1()
{
    AppStateSerializer.InitializeSingleton(SerializeMode.XMLFile, "Dock1");
}
```

#### VB.NET

```vb
Imports Syncfusion.Runtime.Serialization
' Persist the dock state into XML File named Dock1.xml. Use this line in the constructor of Control which hosts the dockinglayout
Private Sub New()
    AppStateSerializer.InitializeSingleton(SerializeMode.XMLFile, "Dock1")
End Sub
```

### Persisting Dock State in Memory Stream

This section explains how to persist the dock state in a memory stream. Instructions for both C# and VB.NET are provided below.

#### C#

```csharp
using Syncfusion.Runtime.Serialization;
// Persist the dock state in a memory stream. Use this line in the appropriate method or event handler
MemoryStream stream = new MemoryStream();
dockingManager1.SaveDockState(stream);
```

#### VB.NET

```vb
Imports Syncfusion.Runtime.Serialization
' Persist the dock state in a memory stream. Use this line in the appropriate method or event handler
Dim stream As New MemoryStream()
dockingManager1.SaveDockState(stream)
```

### Summary

This section covers the methods to save and persist the dock state in different mediums, such as XML files and memory streams, using the `DockingManager` in Syncfusion WinForms. These examples are provided in both C# and VB.NET syntax.

## RAG Annotations

The contents of this page cover the following topics:
- Saving the state of docked controls
- Persisting dock state using different methods
- Usage examples in C# and VB.NET

This page is part of the Syncfusion WinForms documentation, specifically focusing on docking functionality. It is useful for developers working on Windows Forms applications looking to implement persistence features for their docking controls.

<!-- tags: [Docking, Windows Forms, Persistence, XML, Memory Stream] keywords: [DockingManager, PersistState, SaveDockState, XMLFile, Memory Stream] -->
```